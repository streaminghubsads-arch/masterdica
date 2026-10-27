---
name: yt-viral
description: >-
  Pesquise vídeos públicos de canais estrangeiros de filmes e séries,
  compare desempenho relativo ao canal e extraia oportunidades originais
  para a curadoria atemporal do MasterDica.
---

# yt-viral

Use referências de outros canais para descobrir temas e formatos que merecem investigação. Um vídeo com muitas visualizações é uma pista editorial, não prova de que o mesmo resultado se repetirá no MasterDica.

## Onde pesquisar

- Comece por Max Estrenos e amplie para canais relevantes da Espanha, México, América Latina e Estados Unidos.
- Priorize vídeos recentes e pautas evergreen de filmes e séries que tenham relação com suspense, ação, ficção científica, minisséries ou descoberta de catálogo.
- Use listagens e informações públicas. Não use sessões autenticadas, credenciais ou dados privados.
- Registre canal, título original, URL, visualizações observadas, duração e data de publicação quando disponíveis. Não invente campos ausentes.
- Para calcular múltiplos por canal, use pelo menos quatro vídeos comparáveis por canal. Compare com cautela: idade do vídeo, formato e tamanho do canal mudam a leitura.
- A coleta com o script é manual; yt-dlp não faz parte do repositório.

## Análise

O script swipe.py compara visualizações com a mediana dos vídeos fornecidos para cada canal. Não normalize por idade do vídeo e não compare diretamente múltiplos de canais diferentes como se fossem equivalentes. Informe quando o conjunto for pequeno, incompleto ou não comparável.

A classificação de fórmula usa correspondência aproximada com títulos em português em yt-script/hooks.json. Ela descreve padrões de texto encontrados, não demonstra por que um vídeo teve bom desempenho.

Para cada referência promissora, separe:

1. **Observação:** o que os dados públicos mostram.
2. **Hipótese:** qual mecanismo de tema ou embalagem pode ter ajudado.
3. **Adaptação:** como transformar a ideia em pauta original para o MasterDica, sem copiar roteiro, thumbnail ou identidade visual.
4. **Checagem editorial:** título oficial brasileiro, disponibilidade no Brasil, fatos confirmados e trailer oficial quando necessário.

## Entrega

Apresente até cinco referências com URL, canal, data e métricas disponíveis; identifique limites dos dados. Em seguida, sugira pautas originais adequadas ao calendário do MasterDica e explique em uma frase o encaixe de cada uma. Destaque uma prioridade, mas deixe a seleção final para Alexandre.

Não apresente estimativas como números observados, não invente causalidade e não recomende copiar conteúdo. Nada é publicado por esta skill.