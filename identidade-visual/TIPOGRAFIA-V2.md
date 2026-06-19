# Tipografia v2 — Nortear Mundo (foco: LEGIBILIDADE em tela)

> Reabertura do sistema tipográfico. Motivo: o Playfair Display (display atual) é uma serif de
> **contraste de traço extremo** — bela em display grande, mas em tamanhos médios/pequenos e em
> telas comuns os traços finos "somem", prejudicando a legibilidade no site.
> Critério #1 destas opções = legibilidade em tela em TODOS os tamanhos. Mantemos a alma editorial
> (serif com calor) e a etiqueta mono "boarding pass" como DNA. Todas Google Fonts (grátis/performático).

## O problema do Playfair (a evidenciar no comparativo)
- Contraste fixo e alto: a partir de ~24px pra baixo os finos quebram em telas 1x; em corpo é frágil.
- Não tem eixo óptico → o mesmo desenho "fino" é usado em todo tamanho.

## 5 OPÇÕES

### Opção 1 — "Editorial Legível" · Fraunces + Inter + DM Mono ★ RECOMENDADA
- **Display:** Fraunces (pesos 500/600/900; SOFT/WONK baixos)
- **Corpo:** Inter (400/500/600)
- **Etiqueta:** DM Mono (mantém o boarding pass)
- **Por que é legível:** Fraunces tem **eixo óptico (opsz)** — em tamanhos menores os traços finos engrossam automaticamente, exatamente onde o Playfair falha. Inter é o benchmark de leitura em UI/tela (x-height alto, formas abertas). Mantém serif editorial + mono = evolução, não ruptura.
- **Afinidade:** Paleta B (Pôr do Sol), A.

### Opção 2 — "Calor de Leitura" · Lora + Source Sans 3 + IBM Plex Mono
- **Display:** Lora (500/600/700) — pode descer até subtítulos
- **Corpo:** Source Sans 3 (400/600)
- **Etiqueta:** IBM Plex Mono
- **Por que é legível:** Lora é serif de **contraste moderado** desenhada para tela, curvas "brushed" calorosas; funciona de display a corpo sem quebrar. Source Sans 3 = legibilidade impecável. A opção mais à prova de falhas em qualquer tamanho/densidade.
- **Afinidade:** todas; especialmente A/B.

### Opção 3 — "Notícia Calorosa" · Newsreader + Figtree + Space Mono
- **Display/Serif:** Newsreader (400/500/600 + itálicos)
- **Corpo:** Figtree (400/500/600)
- **Etiqueta:** Space Mono
- **Por que é legível:** Newsreader é serif feita para **leitura em tela** (Production Type); seus itálicos expressivos servem perfeitamente ao itálico de confidência da Nortear. Figtree é humanista geométrica, clara e amigável. Tom editorial-jornalístico contemporâneo.
- **Afinidade:** B/C.

### Opção 4 — "Grotesco Caloroso" · Bricolage Grotesque + Hanken Grotesk + Space Mono
- **Display:** Bricolage Grotesque (500/700/800)
- **Corpo:** Hanken Grotesk (400/500/600)
- **Etiqueta:** Space Mono
- **Por que é legível:** abandona a serif → **legibilidade máxima** e ar moderno. Bricolage tem personalidade (não é grotesca genérica); Hanken Grotesk é altamente legível em corpo. Mantém o mono pro toque técnico de viagem. Para quem quer romper com a serif e mirar público jovem (caçador de milhas).
- **Afinidade:** B/D.

### Opção 5 — "Sistema Coeso" · Source Serif 4 + Source Sans 3 + IBM Plex Mono
- **Display:** Source Serif 4 (500/600/700)
- **Corpo:** Source Sans 3 (400/600)
- **Etiqueta:** IBM Plex Mono
- **Por que é legível:** superfamília Adobe → harmonia automática serif↔sans e **legibilidade de referência** em tela. Source Serif 4 tem contraste contido (não quebra). Sóbrio, confiável, "sistema" — menos decisão, mais coerência.
- **Afinidade:** A/C.

## DECISÃO FINAL (escolha do cliente)
**Opção 3 — Newsreader + Figtree + Space Mono ("Notícia Calorosa").**
Newsreader é serif feita para **leitura em tela** (Production Type), com itálicos expressivos que
servem perfeitamente ao itálico de confidência da Nortear — resolve a fragilidade do Playfair sem
abrir mão da alma editorial. Figtree é humanista geométrica de alta legibilidade no corpo, e Space
Mono mantém o "boarding pass" nas etiquetas. É a **tipografia oficial** do design system Nortear
(`../Design.md` §3), a aplicar na landing do Radar de Milhas e no lookbook.

> **Histórico:** a recomendação original do art director foi a Opção 1 (Fraunces+Inter); por um
> período registrou-se a **Opção 2 (Lora + Source Sans 3 + IBM Plex Mono)** como escolha — o cliente
> revisou em 2026-06-19 e fechou na **Opção 3**. Esta é a decisão vigente; ignorar referências a Lora
> em versões anteriores dos entregáveis (a re-sincronizar).
