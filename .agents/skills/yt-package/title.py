#!/usr/bin/env python3
"""Revisa títulos e pares de título/thumbnail com critérios editoriais do MasterDica.

Uso:
    python3 title.py --title "ELES ESTÃO PRESOS E PRECISAM SOBREVIVER" --thumb "SEM SAÍDA"
    python3 title.py titulos.txt
    python3 title.py --title "..." --json

A nota é uma heurística local, não uma previsão de CTR. Caixa alta e ausência de números não são
erros por si só. Revise a promessa junto do vídeo.
"""
import json
import os
import re
import sys

WORD = re.compile(r"[a-zà-ÿ0-9]+", re.I)
STOP = {
    "a", "à", "ao", "aos", "as", "com", "da", "das", "de", "do", "dos",
    "e", "em", "esta", "esse", "essa", "este", "o", "os", "ou", "para",
    "por", "que", "se", "um", "uma", "uns", "umas",
}
VAGUE = {
    "incrível", "imperdível", "sensacional", "perfeito", "épico",
    "surpreendente", "inacreditável",
}


def words(text):
    return WORD.findall(text.lower())


def check(title, thumb=None):
    title = title.strip()
    length = len(title)
    issues, good = [], []

    if 30 <= length <= 50:
        good.append("dentro da faixa de referência de 30–50 caracteres")
    elif length < 30:
        issues.append(("comprimento", "curto para a faixa preferida; confirme se o conflito está claro"))
    elif length <= 60:
        issues.append(("comprimento", "acima da faixa preferida de 30–50 caracteres"))
    elif length <= 100:
        issues.append(("comprimento", "longo; confira o corte em telas menores"))
    else:
        issues.append(("limite", "acima do limite de 100 caracteres"))

    if title.isupper():
        good.append("caixa alta aprovada pelo estilo do canal")
    if re.search(r"\d", title):
        good.append("inclui número, útil quando a seleção é numerada")

    vague = sorted({token for token in words(title) if token in VAGUE})
    if vague:
        issues.append(("vago", f"adjetivo(s) genérico(s): {', '.join(vague)}; procure um conflito concreto"))

    significant = [token for token in words(title) if token not in STOP]
    if not significant:
        issues.append(("assunto", "não foi possível identificar palavras centrais"))

    if thumb is not None:
        thumbnail_words = words(thumb)
        shared = (set(significant) & set(thumbnail_words)) - STOP
        if len(thumbnail_words) > 3:
            issues.append(("texto da thumb", f"{len(thumbnail_words)} palavras; prefira até três"))
        else:
            good.append("texto da thumbnail curto")
        if shared:
            good.append(
                "título e thumbnail compartilham termo(s) útil(eis): "
                + ", ".join(sorted(shared))
                + "; confirme que a thumbnail acrescenta outra ideia"
            )
        else:
            good.append("título e thumbnail usam palavras diferentes")

    score = max(0, min(100, 100 - 10 * len(issues) + 5 * len(good)))
    return {
        "titulo": title,
        "caracteres": length,
        "nota_auxiliar": score,
        "alertas": issues,
        "pontos_a_favor": good,
    }


def show(result):
    print(f"\n  {result['titulo']}")
    print(f"  {result['caracteres']} caracteres | nota auxiliar {result['nota_auxiliar']}/100")
    for kind, message in result["alertas"]:
        print(f"    Revisar — {kind}: {message}")
    for message in result["pontos_a_favor"]:
        print(f"    A favor — {message}")


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    args = [arg for arg in args if arg != "--json"]
    thumb = args[args.index("--thumb") + 1] if "--thumb" in args else None

    if "--title" in args:
        index = args.index("--title")
        if index + 1 >= len(args):
            print("Informe o texto após --title.", file=sys.stderr)
            sys.exit(2)
        rows = [check(args[index + 1], thumb)]
    elif args and os.path.isfile(args[0]):
        with open(args[0], encoding="utf-8") as f:
            rows = [check(line, thumb) for line in f if line.strip()]
    else:
        print(__doc__)
        sys.exit(1)

    rows.sort(key=lambda row: -row["nota_auxiliar"])
    if as_json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return
    for result in rows:
        show(result)
    print("\nA nota é um apoio à revisão, não uma previsão de desempenho.\n")


if __name__ == "__main__":
    main()
