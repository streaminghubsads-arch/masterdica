#!/usr/bin/env python3
"""Avalia ganchos de vídeo em português brasileiro como apoio à revisão editorial.

Uso:
    python3 hookscore.py hooks.txt
    python3 hookscore.py --hook "Uma família desaparece e ninguém sabe por quê"
    python3 hookscore.py --json hooks.txt

A nota é uma heurística lexical. Não foi calibrada com resultados do MasterDica e não prevê
retenção, cliques ou visualizações. Leia o gancho em voz alta e julgue a promessa no contexto.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "hooks.json"), encoding="utf-8") as f:
    FORMULAS = json.load(f)["hooks"]

FILLER = {
    "basicamente", "literalmente", "realmente", "muito", "hoje", "vídeo",
    "canal", "pessoal", "inscreva", "inscrever", "começar", "vamos",
}
VAGUE = {
    "incrível", "insano", "absurdo", "chocante", "imperdível", "perfeito",
    "surpreendente", "sensacional", "melhor", "épico",
}
CONCRETE = re.compile(
    r"\b(?:\d[\d.,]*\s?(?:%|mil|milhão|milhões|h|min|s)?|"
    r"\d+\s?(?:segundos?|minutos?|horas?|dias?|semanas?|meses?|anos?))\b",
    re.I,
)
DIRECT = re.compile(r"\b(?:você|seu|sua|seus|suas|quem|já imaginou)\b", re.I)
STAKES = re.compile(
    r"\b(?:morrer|morte|perder|perdeu|sobreviver|preso|presa|perigo|ameaça|"
    r"fugir|desaparecer|desapareceu|segredo|vingança|crime|risco|sem saída)\b",
    re.I,
)
CURIOSITY = re.compile(
    r"\b(?:por que|como|o que|quem|qual|até|mas|ninguém|ninguém sabe|"
    r"antes|exceto|segredo|mistério|descobrir|revelar)\b",
    re.I,
)
WORD = re.compile(r"[a-zà-ÿ0-9]+", re.I)


def words(text):
    return WORD.findall(text.lower())


def specificity(text):
    tokens = words(text)
    if not tokens:
        return 0
    numbers = len(CONCRETE.findall(text))
    vague = sum(token in VAGUE for token in tokens)
    filler = sum(token in FILLER for token in tokens)
    return max(0, min(100, 46 + numbers * 18 - vague * 12 - filler * 5))


def address(text):
    tokens = words(text)
    opening = " ".join(tokens[:6])
    direct = bool(DIRECT.search(opening))
    count = len(DIRECT.findall(text))
    return max(0, min(100, 48 + count * 12 + (15 if direct else 0)))


def stakes(text):
    count = len(STAKES.findall(text))
    concrete = bool(CONCRETE.search(text))
    return max(0, min(100, 38 + count * 18 + (10 if concrete else 0)))


def curiosity(text):
    count = len(CURIOSITY.findall(text))
    question = 14 if text.strip().endswith("?") else 0
    resolved = -12 if re.search(r"\b(?:porque|portanto|ou seja)\b", text, re.I) else 0
    return max(0, min(100, 38 + count * 12 + question + resolved))


def concision(text):
    count = len(words(text))
    if count == 0:
        return 0
    # Faixa ampla: a abertura pode ocupar 15–25 segundos, e não uma frase isolada.
    if 8 <= count <= 38:
        return 100
    if count < 8:
        return max(35, 100 - (8 - count) * 10)
    return max(15, 100 - (count - 38) * 5)


PROPERTIES = [
    ("ESPECIFICIDADE", specificity),
    ("ENDEREÇAMENTO", address),
    ("CONSEQUÊNCIA", stakes),
    ("CURIOSIDADE", curiosity),
    ("CONCISÃO", concision),
]


def classify(text):
    best_name, best_hits = "Sem fórmula dominante", 0
    for formula in FORMULAS:
        hits = sum(bool(re.search(pattern, text, re.I)) for pattern in formula["match"])
        if hits > best_hits:
            best_name, best_hits = formula["name"], hits
    return best_name, best_hits


def score(text):
    parts = {name: fn(text) for name, fn in PROPERTIES}
    values = list(parts.values())
    verdict = round(0.6 * (sum(values) / len(values)) + 0.4 * min(values))
    name, hits = classify(text)
    return parts, verdict, name, hits


def band(value):
    return "forte como rascunho" if value >= 72 else "revisável" if value >= 55 else "rever"


FIX = {
    "ESPECIFICIDADE": "troque um adjetivo vago por um conflito, personagem ou detalhe confirmado",
    "ENDEREÇAMENTO": "avalie se uma pergunta direta ao espectador ajuda esta abertura",
    "CONSEQUÊNCIA": "mostre o que está em jogo, sem exagerar o que a obra promete",
    "CURIOSIDADE": "deixe uma pergunta aberta sem esconder informação essencial",
    "CONCISÃO": "leia em voz alta e corte o trecho que não reforça a promessa",
}


def report(text, parts, verdict, formula, hits):
    print(f"\n  {text.strip()}")
    for name, value in parts.items():
        print(f"    {name:<18} {value:3d}")
    print(f"    {'NOTA AUXILIAR':<18} {verdict:3d}  {band(verdict)}")
    suffix = f" ({hits} padrão(ões))" if hits else ""
    print(f"    fórmula provável: {formula}{suffix}")
    weakest = min(parts, key=parts.get)
    print(f"    ponto para revisar: {FIX[weakest]}")


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    args = [arg for arg in args if arg != "--json"]
    if "--hook" in args:
        index = args.index("--hook")
        if index + 1 >= len(args):
            print("Informe o texto após --hook.", file=sys.stderr)
            sys.exit(2)
        lines = [args[index + 1]]
    elif args and os.path.isfile(args[0]):
        with open(args[0], encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    else:
        print(__doc__)
        sys.exit(1)
    results = []
    for line in lines:
        parts, verdict, formula, hits = score(line)
        results.append({
            "gancho": line.strip(),
            "criterios": parts,
            "nota_auxiliar": verdict,
            "faixa": band(verdict),
            "formula_provavel": formula,
            "padroes_encontrados": hits,
        })
    results.sort(key=lambda row: -row["nota_auxiliar"])
    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    for row in results:
        report(
            row["gancho"], row["criterios"], row["nota_auxiliar"],
            row["formula_provavel"], row["padroes_encontrados"],
        )
    if len(results) > 1:
        print(f"\n  Melhor nota auxiliar: {results[0]['nota_auxiliar']} — revise no contexto.\n")


if __name__ == "__main__":
    main()
