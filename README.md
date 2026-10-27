# MasterDica — fluxo de produção para YouTube

Skills locais do Codex para apoiar a produção do canal MasterDica, da pesquisa à revisão de desempenho. O fluxo prepara materiais para decisão humana; não publica vídeos nem altera o canal.

## Fluxo recomendado

1. **Planejar a semana** — use yt-plan para organizar os vídeos de terça, quinta e sábado, publicados por volta de 11h–11h30. Priorize curadoria atemporal de filmes e séries e respeite a capacidade e o material já disponível.
2. **Pesquisar e escolher a pauta** — use yt-viral para estudar vídeos públicos de canais relevantes. Diferencie dados observados de hipóteses editoriais; Alexandre aprova a pauta antes do roteiro.
3. **Escrever o roteiro** — use yt-script com o título ou promessa aprovados. Aplique a estrutura e as regras de voz do perfil MasterDica.
4. **Preparar o pacote** — use yt-package para títulos e briefing de thumbnail; depois yt-seo para descrição, hashtags e tags.
5. **Preparar a edição** — use yt-edit para sugestões de corte e yt-chapters para rascunhos de capítulos. Confira tudo contra o vídeo antes de aplicar.
6. **Aproveitar e revisar** — use yt-shorts, yt-comment, yt-retention e yt-audit quando houver transcrição, comentários ou dados do YouTube Studio disponíveis.

Use templates/pacote-video.md para acompanhar cada vídeo. Nenhuma etapa autoriza publicação. Revise fatos, títulos, roteiro, thumbnail e descrição antes de usar.

## Skills incluídas

| Skill | Função |
|---|---|
| yt-plan | Plano semanal dos vídeos e etapas de produção |
| yt-viral | Pesquisa comparativa de vídeos públicos e fórmulas de título |
| yt-script | Roteiro, abertura e avaliação auxiliar de ganchos |
| yt-package | Títulos, texto e briefing de thumbnail |
| yt-seo | Descrição, hashtags, tags e consultas de busca |
| yt-chapters | Rascunho de capítulos a partir de transcrição |
| yt-edit | Lista de cortes sugeridos a partir de transcrição |
| yt-shorts | Seleção de trechos para Shorts |
| yt-comment | Triagem e rascunhos de resposta a comentários |
| yt-retention | Leitura de exportações de retenção |
| yt-audit | Auditoria editorial do canal |

## Configuração

Requisitos para os scripts locais: Python 3. Não há dependências adicionais neste repositório.

As skills procuram o perfil pessoal em ~/.codex/youtube/voice.md. O perfil editorial inicial do MasterDica está em templates/voice.md. Copie-o para o caminho acima no ambiente em que o Codex executa; mantenha a cópia pessoal fora do repositório. O perfil registra decisões editoriais já aprovadas, mas não substitui amostras de fala: acrescente trechos de três vídeos para calibrar ritmo e vocabulário quando estiverem disponíveis.

Inicie uma nova sessão do Codex na pasta do projeto para carregar as skills locais. Exemplos de pedido:

- “Use yt-plan para montar o plano de produção desta semana.”
- “Use yt-script para escrever o roteiro desta pauta seguindo o perfil MasterDica.”
- “Use yt-package para criar títulos e um briefing de thumbnail para este vídeo.”
- “Use yt-seo para montar a descrição e tags deste vídeo.”

## Ferramentas locais

Execute os comandos na raiz do repositório:

    python3 .agents/skills/yt-script/hookscore.py --hook "Você reconheceria esta série pelo primeiro episódio?"
    python3 .agents/skills/yt-package/title.py --title "ELES ESTÃO PRESOS E PRECISAM SOBREVIVER" --thumb "SEM SAÍDA"
    python3 .agents/skills/yt-edit/deadair.py transcricao.srt
    python3 .agents/skills/yt-chapters/chapters.py transcricao.srt --target 8
    python3 .agents/skills/yt-retention/retention.py exportacao-retencao.csv --duration 600
    python3 .agents/skills/yt-viral/swipe.py videos-publicos.json --min 2.0

Os scripts analisam arquivos fornecidos por você. Não coletam métricas privadas, não acessam credenciais e não publicam conteúdo. A coleta de vídeos para yt-viral é manual; yt-dlp não está incluído. Use somente dados que você tem autorização para analisar.

## Dados e privacidade

Não envie para o repositório público tokens, senhas, cookies, credenciais, dados pessoais de espectadores, transcrições brutas ou exportações privadas do YouTube Studio. Guarde materiais de trabalho em pastas locais ignoradas pelo Git, como local-data/ ou exports/. Compartilhe apenas exemplos já revisados e sem dados sensíveis.

## Como avaliar os resultados

As notas de hookscore.py e title.py são heurísticas editoriais, não previsões de CTR, retenção ou visualizações. Use-as para localizar algo que merece revisão; a decisão final considera promessa, clareza, contexto do vídeo e voz do canal.

## Origem e licença

As skills importadas e os scripts de origem estão identificados em third_party/youtube-agent/UPSTREAM.md. O conteúdo original é distribuído sob licença MIT; consulte third_party/youtube-agent/LICENSE. As adaptações específicas do MasterDica devem ser mantidas separadas e documentadas nos commits.