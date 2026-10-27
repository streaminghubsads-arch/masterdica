---
name: yt-script
description: >-
  Escreva roteiros em português do Brasil para o MasterDica, incluindo
  aberturas, listas de filmes e séries, ganchos e revisão de ritmo.
---

# yt-script

Transforme a pauta aprovada em um roteiro falável, original e fiel aos fatos confirmados.

## Antes de escrever

1. Leia ~/.codex/youtube/voice.md, se estiver disponível. Na ausência, use o perfil editorial versionado em templates/voice.md; não invente maneirismos ou experiências pessoais do apresentador.
2. Confirme o formato, quantidade de itens, duração e público pretendidos. Se já estiverem no pedido, não pergunte de novo.
3. Confirme nomes oficiais em português do Brasil e fatos recentes em fontes confiáveis. Diferencie fatos, rumores e opiniões.
4. Não crie números, notas, datas, plataformas, citações, fontes, disponibilidade brasileira ou resultados de audiência sem evidência.

## Abertura

Para listas do MasterDica:

- Mire em 15–25 segundos, com um gancho direto e uma promessa que o vídeo cumpra.
- Use a assinatura “Eu sou o Alexandre Cardoso…” no contexto natural da abertura.
- Não use “Olá, pessoal” nem comece com explicação genérica do tema.
- Antecipe um item forte sem revelar o nome da obra.
- O primeiro item deve começar por volta de 0:20–0:25.
- Coloque o CTA principal após o segundo item; não interrompa o gancho com pedido de inscrição.

## Itens da lista

- Use cabeçalho no formato “NÚMERO X — [Nome da obra].”
- Abra cada item com uma pergunta ou situação concreta e revele o nome da obra dentro do parágrafo.
- Mire em 100–120 palavras e cerca de 40–50 segundos por item quando esse for o formato solicitado.
- Varie a construção entre itens. Não repita uma sinopse com palavras trocadas.
- Distribua obras fortes nas posições 1, 3 e 6 quando houver ao menos seis itens; adapte a distribuição quando a lista for menor.
- Termine cada bloco com uma frase curta que explique por que vale assistir.
- Não escreva transições para o item seguinte.
- Reserve indicação de trailer oficial de aproximadamente 15 segundos no fim do bloco quando a produção solicitar esse elemento e houver trailer apropriado.
- Não invente cenas. Sinalize onde entram imagens, cartelas ou trailer usando indicações curtas entre colchetes.

## Ritmo e formato de entrega

Entregue texto corrido para narração, com frases curtas e linguagem natural em PT-BR. Use os cabeçalhos numerados pedidos, sem subtítulos “Sinopse” ou “Comentário”. Estime duração a partir da quantidade de palavras e da velocidade informada; se ela não foi dada, identifique a estimativa como aproximada. Roteiros de listas devem manter o tamanho total solicitado pelo usuário.

## Avaliação auxiliar de ganchos

Quando houver várias aberturas, use hookscore.py para localizar diferenças de especificidade, interesse, consequência e concisão. Mostre no máximo as três melhores opções e explique que a pontuação é uma heurística, não uma previsão de retenção. Aplique julgamento editorial: um gancho pode funcionar sem pergunta ou pronome direto.

## Revisão final

Confira se a abertura corresponde ao título, se cada afirmação factual está sustentada, se os nomes estão em PT-BR e se os itens têm extensão compatível com o pedido. Nada é publicado por esta skill; deixe o roteiro pronto para revisão humana.