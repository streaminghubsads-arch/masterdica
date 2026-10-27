# masterdica

Skills do YouTube Agent disponíveis para o Codex neste repositório em `.agents/skills/`.
Abra uma nova sessão do Codex neste projeto para descobrir as skills locais.

## Skills incluídas

| Skill | Uso |
|---|---|
| `yt-script` | Roteiros e avaliação de ganchos |
| `yt-package` | Títulos e thumbnails |
| `yt-viral` | Pesquisa de vídeos por desempenho relativo ao canal |
| `yt-retention` | Análise de exportações de retenção |
| `yt-edit` | Lista de cortes a partir de transcrições |
| `yt-plan` | Planejamento de publicações |
| `yt-comment` | Rascunhos de respostas a comentários |
| `yt-seo` | Descrições, tags e busca |
| `yt-chapters` | Capítulos com timestamps |
| `yt-shorts` | Seleção de trechos para Shorts |
| `yt-audit` | Auditoria de canal |

Exemplo no Codex: `Use $yt-script para preparar um roteiro sobre o tema que vou enviar.`

## Ferramentas locais

Requisito: Python 3 (validado com 3.12). Não há pacotes Python para instalar.
Execute na raiz do repositório:

```bash
python3 .agents/skills/yt-script/hookscore.py --hook "Why your first 30 seconds lose viewers"
python3 .agents/skills/yt-package/title.py --title "I tested 3 cameras" --thumb "ONE WINNER"
python3 .agents/skills/yt-edit/deadair.py transcript.srt
python3 .agents/skills/yt-chapters/chapters.py transcript.srt --target 8
python3 .agents/skills/yt-retention/retention.py retention.csv --duration 600
python3 .agents/skills/yt-viral/swipe.py collected.json --min 2.0
```

Use arquivos reais para análises reais; os scripts não buscam dados privados nem publicam vídeos.
Transcrição automática e coleta com `yt-dlp` são opcionais e não estão instaladas por este pacote.
As heurísticas de texto foram escritas em inglês; pontuações em português exigem interpretação.

## Perfil de voz

O modelo está em `templates/voice.md`. As skills originais procuram o perfil pessoal em
`~/.codex/youtube/voice.md`. Copie o modelo para esse caminho apenas se ainda não existir um perfil,
e preencha com sua voz e exemplos reais. Nenhum perfil pessoal foi criado nesta integração.

## Origem e licença

As 11 skills, os seis scripts e o modelo foram importados sem alterações do
[YouTube Agent de Jake Schincariol](https://github.com/Jakeschincariol/chatgpt-youtube-agent-skill).
Versão e licença MIT em [third_party/youtube-agent](third_party/youtube-agent/UPSTREAM.md).
