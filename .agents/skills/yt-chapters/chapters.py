#!/usr/bin/env python3
"""Gera rascunhos de capítulos a partir de uma transcrição com timestamps.

Uso:
    python3 chapters.py transcricao.srt
    python3 chapters.py transcricao.srt --target 8 --json

Os títulos gerados são palavras-chave em português, não títulos editoriais prontos. Revise cada
capítulo contra o vídeo; a seleção automática de pausas pode não coincidir com as mudanças de tema.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "yt-edit"))
from deadair import load  # noqa: E402

WORD = re.compile(r"[a-zà-ÿ']{4,}", re.I)
STOP = set(
    "a à agora aí ainda algo algumas alguns alguém ali antes ao aos após aquela aquelas aquele "
    "aqueles aquilo as até com como contudo da das de dela dele demais depois desde desta deste "
    "disso do dos durante e ela elas ele eles em então entre era essa essas esse esses esta estas "
    "este estes eu foi foram for sua seu suas seus havia isso isto já mais mas me mesmo minha minhas "
    "muito na nas nem nesse nesta neste no nos nossa nossas nosso nossos o os ou outra outras outro "
    "outros para pela pelas pelo pelos perante por porque qual quando que quem se sem sendo ser sob "
    "sobre sua suas também te tem tendo ter teu teus toda todas todo todos tu um uma umas uns você "
    "vocês vai vão você vocês".split()
)


def keywords(text):
    return {word for word in WORD.findall(text.lower()) if word not in STOP}


def mmss(seconds):
    seconds = int(seconds)
    hours, minutes, remainder = seconds // 3600, (seconds % 3600) // 60, seconds % 60
    return f"{hours}:{minutes:02d}:{remainder:02d}" if hours else f"{minutes}:{remainder:02d}"


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    args = [arg for arg in args if arg != "--json"]
    target = int(args[args.index("--target") + 1]) if "--target" in args else 7
    files = [arg for arg in args if not arg.startswith("--") and not arg.isdigit()]
    if not files or not os.path.isfile(files[0]):
        print(__doc__)
        sys.exit(1)

    cues = load(files[0])
    if len(cues) < 6:
        print("Poucos trechos para sugerir capítulos.", file=sys.stderr)
        sys.exit(1)

    duration = cues[-1][1]
    candidates = []
    for index in range(1, len(cues)):
        gap = cues[index][0] - cues[index - 1][1]
        before = " ".join(cue[2] for cue in cues[max(0, index - 12):index])
        after = " ".join(cue[2] for cue in cues[index:index + 12])
        before_words, after_words = keywords(before), keywords(after)
        union = before_words | after_words
        shift = 1 - (len(before_words & after_words) / len(union)) if union else 0
        candidates.append((gap * 1.6 + shift * 3.2, cues[index][0]))

    candidates.sort(reverse=True)
    picked, minimum = [0.0], 10.0
    for _, timestamp in candidates:
        if len(picked) >= target:
            break
        if all(abs(timestamp - previous) >= minimum for previous in picked) and duration - timestamp >= minimum:
            picked.append(timestamp)
    picked.sort()

    chapters = []
    for index, timestamp in enumerate(picked):
        end = picked[index + 1] if index + 1 < len(picked) else duration
        text = " ".join(
            cue[2] for cue in cues if cue[0] >= timestamp and cue[1] <= end
        )
        counts = {}
        for word in keywords(text):
            counts[word] = text.lower().count(word)
        top_words = sorted(counts, key=lambda word: (-counts[word], word))[:3]
        label = " ".join(word.capitalize() for word in top_words) or "Revisar tema"
        chapters.append({
            "inicio_segundos": round(timestamp, 2),
            "timestamp": mmss(timestamp),
            "rascunho": label,
            "duracao_segundos": round(end - timestamp, 2),
        })

    valid = (
        len(chapters) >= 3
        and chapters[0]["inicio_segundos"] == 0
        and all(chapter["duracao_segundos"] >= minimum for chapter in chapters)
    )
    if as_json:
        print(json.dumps({"valido": valid, "capitulos": chapters}, ensure_ascii=False, indent=2))
        return

    print()
    for chapter in chapters:
        print(f"  {chapter['timestamp']} {chapter['rascunho']}")
    status = "válidos como rascunho" if valid else "inválidos: confira 3+ capítulos, início em 00:00 e intervalos de 10+ segundos"
    print(f"\n  {len(chapters)} capítulos — {status}")
    print("  Reescreva os rótulos como promessas curtas da seção e confira os tempos no vídeo.\n")


if __name__ == "__main__":
    main()
