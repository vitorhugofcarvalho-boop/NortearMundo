# Nortear Mundo — Design System

> Documento canônico do design system **oficial aprovado** da Nortear Mundo: paleta **"Pôr do Sol Tropical"** + tipografia **Newsreader / Figtree / Space Mono** (Opção 3 "Notícia Calorosa"). A estrutura (tokens, componentes, espaçamento, movimento) segue fiel à implementação do site (`fonts.css`, `colors_and_type.css`, `styles.css`, `index.html`, `content.json`); os **nomes dos tokens** foram preservados — só os valores (cor/fonte) evoluíram. Onde algo não está definido no código, está marcado como **(não definido no CSS)**.

> **✅ Status de implementação (re-sincronizado e no ar em 2026-06-19):** a identidade evoluída está aplicada e **deployada** (Vercel: `nortear-mundo.vercel.app`) em **todos os entregáveis** — landing do Radar de Milhas, lookbook (`identidade-visual/`), tokens do Figma (`identidade-visual/figma/nortear-tokens.json`) **e o CSS do site** (`colors_and_type.css`, `styles.css`, `fonts.css`). Fontes self-hosted: **Newsreader variável** (`newsreader-var` + `-var-i`, eixos `opsz`+`wght`) + Figtree + Space Mono; preloads do `<head>` e bloco inlined via `build_inline_css.py`. Os woff2 antigos (Playfair/DM Sans/DM Mono **e** as instâncias estáticas de Newsreader) já foram **removidos** de `/fonts`. Alguns valores `rgba()` nas descrições de componentes (§5–§6) ainda citam o literal antigo da âncora (`#0D3B6E` → `rgba(13,59,110)`) como exemplo textual; o mapeamento canônico vigente está em §2.8 e o CSS real já usa Marinho Maré `rgba(12,51,80)`.

---

## 1. Visão geral da marca

**Nortear Mundo** é uma agência de viagens fundada em 2021 por **Luna Carvalho** e **Caroline Lisboa**, potiguares (Rio Grande do Norte, Brasil), com atendimento 100% online para todo o Brasil.

**Posicionamento:** "A gente não vende pacote. A gente cuida do seu sonho do começo ao fim." — roteiros 100% personalizados, suporte humano 24h durante a viagem, preço justo e transparente, sem taxa de tabela.

**Sensação visual (mood extraído do CSS/conteúdo):**
- **Confiança + horizonte**: domina o azul profundo/médio (`--azul-nortear`, `--azul-profundo`), remetendo a céu/mar — território de viagem.
- **Acolhimento caloroso**: laranja (`--laranja-nortear`/`--laranja-ambar`) como contraponto humano e energético, usado em CTAs e destaques — nunca como cor de fundo dominante.
- **Editorial/elegante, não corporativo**: tipografia serifada (Newsreader — serif feita para leitura em tela) em grandes títulos, itálicos expressivos para tom de conversa/confidência, mono (Space Mono) para "etiquetas" técnicas (eyebrows, badges, preços) — efeito de "boarding pass"/diário de viagem.
- **Calmo, nunca agressivo**: raios generosos (nunca sharp), sombras suaves tingidas de azul (nunca cinza neutro), gradientes lentos e orgânicos (`nm-soft-shift`, `nm-radar-bg`), pulse discreto em CTAs.
- **Ritmo**: blocos grandes de respiro (`--space-9` a `--space-11`, padding de seção 96px), tudo com `padding: Xpx 10%` — gutter lateral consistente de 10% em qualquer largura.
- **Off-white quente, nunca branco puro nem preto puro**: `--branco-areia: #FCF7F0` (Areia Quente) como fundo padrão, `--grafite: #211A15` (Grafite Quente) como texto (CSS comenta explicitamente "NUNCA #000").

---

## 2. Cores

**Duas paletas mantidas como opções de trabalho** — os **nomes dos tokens são idênticos** nas duas, só mudam os valores resolvidos em `:root`. Alternar de paleta = trocar o bloco de valores (ver o diff direto em §2.8).

- **Paleta A — "Pôr do Sol Tropical" (ATUAL, em produção)** — §2.1. Direção oficial aprovada; é a que está no site (`colors_and_type.css`) e em todos os entregáveis.
- **Paleta B — "Horizonte" (ANTERIOR)** — §2.2. Paleta fiel original, de antes da evolução; mantida como alternativa válida pra trabalhar.

As outras paletas exploratórias (Primeira Classe, Bússola & Mapa) seguem só como **modes do Figma** (§2.7).

### 2.1 Paleta A — "Pôr do Sol Tropical" (ATUAL — em produção)

| Variável | HEX | Nome de marca | Uso |
|---|---|---|---|
| `--azul-nortear` | `#1A5FA8` | Azul Nortear | Cor dominante — confiança, horizonte (mantido) |
| `--azul-profundo` | `#0C3350` | Marinho Maré | Contraste e peso — âncora (headings, footer, seções escuras) |
| `--azul-ceu` | `#4A8FD4` | Azul Céu | Gradientes, hover (mantido) |
| `--azul-nevoa` | `#FBE9DD` | Rosa Aurora | Cards, inputs, separadores suaves — **apoio claro agora é quente** |
| `--laranja-nortear` | `#FB6A3C` | Coral Poente | Acento — CTAs, destaques |
| `--laranja-ambar` | `#F6A645` | Âmbar Dourado | Hover de CTAs, decorativo |
| `--laranja-suave` | `#FEEFE6` | Coral Suave | Fundo de copy-exemplo *(derivado — confirmar)* |
| `--branco-areia` | `#FCF7F0` | Areia Quente | Off-white — fundo padrão |
| `--cinza-claro` | `#F0EBE3` | Areia 2 | Cards alternados, divisores *(derivado quente — confirmar)* |
| `--cinza-medio` | `#C9C1B6` | Borda | Bordas, hairlines *(derivado quente — confirmar)* |
| `--cinza-baunilha` | `#7A6E64` | Madeira | Texto secundário |
| `--grafite` | `#211A15` | Grafite Quente | Texto principal (NUNCA #000) |

> *(derivado — confirmar)* = papéis auxiliares não definidos no BRAND-SPEC §B (que fixa os 8 papéis canônicos: primária, âncora, apoio claro, acento, acento 2, fundo, texto, texto suave). Valores propostos derivando da nova paleta (neutros levemente quentes, coral-suave como tint do Coral Poente). Validar antes do re-sync no site.

> **Regra de contraste (BRAND-SPEC):** Coral Poente `#FB6A3C` sobre fundo claro só em **botão ou texto ≥16px bold** — não usar coral para corpo de texto pequeno sobre claro.

### 2.2 Paleta B — "Horizonte" (ANTERIOR — alternativa)

Paleta fiel original, em uso antes da evolução para Pôr do Sol Tropical. Mesmos nomes de token da Paleta A — basta substituir os valores em `:root` para alternar. Caráter mais **frio e neutro** (apoio claro e off-white frios, laranja mais saturado/amarelado).

| Variável | HEX | Nome de marca | Uso |
|---|---|---|---|
| `--azul-nortear` | `#1A5FA8` | Azul Nortear | Cor dominante (igual à Paleta A) |
| `--azul-profundo` | `#0D3B6E` | Azul Profundo | Âncora — headings, footer, seções escuras |
| `--azul-ceu` | `#4A8FD4` | Azul Céu | Gradientes, hover (igual à Paleta A) |
| `--azul-nevoa` | `#EBF3FB` | Azul Névoa | Apoio claro **frio** — cards, inputs, separadores |
| `--laranja-nortear` | `#F47C20` | Laranja Nortear | Acento — CTAs, destaques |
| `--laranja-ambar` | `#FAA95A` | Âmbar | Hover de CTAs, decorativo |
| `--laranja-suave` | `#FEF0E3` | Laranja Suave | Fundo de copy-exemplo |
| `--branco-areia` | `#FAFAF8` | Branco Areia | Off-white **frio** — fundo padrão |
| `--cinza-claro` | `#F2F1EF` | Cinza Claro | Cards alternados, divisores |
| `--cinza-medio` | `#C8C4BE` | Cinza Médio | Bordas, hairlines |
| `--cinza-baunilha` | `#6B6560` | Cinza Baunilha | Texto secundário |
| `--grafite` | `#1C1916` | Grafite | Texto principal (NUNCA #000) |

> Status (`--sucesso`/`--erro`), WhatsApp `#25D366` e branco puro são **idênticos** nas duas paletas (§2.3, §2.6).

### 2.3 Status (uso restrito — apenas território ✓/✗)

| Variável | HEX | Uso |
|---|---|---|
| `--sucesso` | `#27AE60` | Sucesso (uso esparso) |
| `--erro` | `#C0392B` | Erros de formulário (`.nm-field-error`) |

### 2.4 Aliases semânticos

Os aliases resolvem para os valores da **paleta ativa** (abaixo, com os HEX da Paleta A em produção; sob a Paleta B resolvem para os valores de §2.2).

| Variável | Resolve para | Uso |
|---|---|---|
| `--bg` | `var(--branco-areia)` = `#FCF7F0` | Fundo padrão |
| `--bg-soft` | `var(--cinza-claro)` = `#F0EBE3` | Fundo de blocos alternados (`.nm-block-soft`) |
| `--bg-tint` | `var(--azul-nevoa)` = `#FBE9DD` | Fundo com tonalidade quente (Rosa Aurora) |
| `--bg-inverse` | `var(--azul-profundo)` = `#0C3350` | Fundo invertido (seções escuras) |
| `--fg` | `var(--grafite)` = `#211A15` | Texto principal |
| `--fg-muted` | `var(--cinza-baunilha)` = `#7A6E64` | Texto secundário |
| `--fg-on-dark` | `#FFFFFF` | Texto sobre fundo escuro |
| `--fg-on-dark-soft` | `rgba(255,255,255,0.65)` | Texto secundário sobre fundo escuro |
| `--fg-on-dark-faint` | `rgba(255,255,255,0.30)` | Texto terciário/decorativo sobre fundo escuro |
| `--accent` | `var(--laranja-nortear)` = `#FB6A3C` | Acento — CTAs, eyebrows |
| `--accent-hover` | `var(--laranja-ambar)` = `#F6A645` | Hover de acento |
| `--accent-soft` | `var(--laranja-suave)` = `#FEEFE6` | Fundo suave de acento |
| `--primary` | `var(--azul-nortear)` = `#1A5FA8` | Cor primária (links, dots de progresso) |
| `--primary-deep` | `var(--azul-profundo)` = `#0C3350` | Headings, fundos escuros, footer |
| `--primary-light` | `var(--azul-ceu)` = `#4A8FD4` | Hover/realces |
| `--primary-tint` | `var(--azul-nevoa)` = `#FBE9DD` | Fundos tintados (quente) |
| `--border` | `var(--cinza-claro)` = `#F0EBE3` | Bordas padrão |
| `--border-strong` | `var(--cinza-medio)` = `#C9C1B6` | Bordas de inputs, hairlines fortes |

### 2.5 Gradientes nomeados

| Variável | Valor |
|---|---|
| `--gradient-deep` | `linear-gradient(145deg, var(--azul-profundo) 0%, var(--azul-nortear) 60%, #2A7CC7 100%)` (resolve `#0C3350 → #1A5FA8 → #2A7CC7`) |
| `--gradient-warm` | `linear-gradient(135deg, var(--azul-profundo), var(--azul-nortear))` (resolve `#0C3350 → #1A5FA8`) |

### 2.6 Outras cores hardcoded relevantes (fora dos tokens)

| Cor | Onde aparece | Uso |
|---|---|---|
| `#25D366` | `.nm-btn-radar`, `.nm-fab` | Verde oficial do WhatsApp (reservado só para "entrar no grupo") |
| `#1EBE5A` | `.nm-btn-radar:hover` | Verde WhatsApp hover |
| `#E0531F` | `.nm-btn-primary:hover` | Coral escurecido no hover do CTA primário (era `#D96A10`) |
| `#1A6DB8` | gradiente `.nm-radar` (etapa 65%) | Azul intermediário do gradiente animado do radar |
| `#fff` / `#FFFFFF` | múltiplos | Branco puro — usado em cards, textos sobre fundo escuro |

### 2.7 Temas alternativos (modes do Figma)

A coleção de cor no Figma (`identidade-visual/figma/nortear-tokens.json`) traz "Pôr do Sol Tropical" como mode padrão + 3 modes alternativos (troca a marca inteira num clique). Os 4 papéis-chave:

| Mode | Primária | Âncora | Acento (CTA) | Fundo | Quando usar |
|---|---|---|---|---|---|
| **Pôr do Sol Tropical** ★ (= Paleta A) | `#1A5FA8` | `#0C3350` | `#FB6A3C` | `#FCF7F0` | Produção — direção oficial (no ar) |
| Horizonte (= Paleta B) | `#1A5FA8` | `#0D3B6E` | `#F47C20` | `#FAFAF8` | Alternativa — paleta fiel anterior (§2.2) |
| Primeira Classe (premium) | `#14324C` | `#0A1E33` | `#D9A557` (dourado) | `#F5EFE3` | Campanha premium/milhas |
| Bússola & Mapa (terroso) | `#2F5A4E` | `#1E3D35` | `#C25A36` | `#F4EFE4` | Campanha explorador/Nat Geo |

Espec completa de cada paleta: `identidade-visual/BRAND-SPEC.md` §"4 PALETAS".

### 2.8 Diff direto — Paleta A ↔ Paleta B

Os únicos tokens que mudam entre as duas paletas (o resto é idêntico). Para **alternar**, troque a coluna no `:root` de `colors_and_type.css`. **Paleta B (anterior) → Paleta A (atual):**

| Papel / token | Paleta B (Horizonte) | Paleta A (Pôr do Sol) |
|---|---|---|
| `--azul-profundo` (âncora) | `#0D3B6E` | `#0C3350` |
| `--laranja-nortear` (acento) | `#F47C20` | `#FB6A3C` |
| `--laranja-ambar` (acento 2) | `#FAA95A` | `#F6A645` |
| `--laranja-suave` | `#FEF0E3` | `#FEEFE6` |
| `--azul-nevoa` (apoio claro) | `#EBF3FB` | `#FBE9DD` |
| `--branco-areia` (fundo) | `#FAFAF8` | `#FCF7F0` |
| `--cinza-claro` | `#F2F1EF` | `#F0EBE3` |
| `--cinza-medio` | `#C8C4BE` | `#C9C1B6` |
| `--cinza-baunilha` (texto suave) | `#6B6560` | `#7A6E64` |
| `--grafite` (texto) | `#1C1916` | `#211A15` |
| hover do CTA | `#D96A10` | `#E0531F` |
| rgba de sombra (âncora) | `rgba(13,59,110,…)` | `rgba(12,51,80,…)` |
| `--azul-nortear`, `--azul-ceu` | `#1A5FA8` / `#4A8FD4` | inalterados |

---

## 3. Tipografia

### 3.1 Famílias (de `fonts.css` + `colors_and_type.css`)

Tipografia oficial: **Opção 3 "Notícia Calorosa" — Newsreader + Figtree + Space Mono** (escolha do cliente; ver `identidade-visual/TIPOGRAFIA-V2.md`). Trocou o Playfair Display por legibilidade em tela: o Playfair tem contraste de traço extremo (finos somem em tamanho médio/pequeno), enquanto **Newsreader** é serif desenhada para leitura em tela (Production Type) com itálicos expressivos que servem ao itálico de confidência da marca; **Figtree** é humanista geométrica de alta legibilidade; **Space Mono** mantém o efeito "boarding pass".

| Família | Token | Arquivos woff2 (a gerar no re-sync) | Pesos/estilos |
|---|---|---|---|
| **Newsreader** *(variável)* | `--font-display: 'Newsreader', Georgia, 'Times New Roman', serif` | `newsreader-var.woff2` (roman), `newsreader-var-i.woff2` (italic) | **Fonte variável**: eixos `opsz` 6–72 + `wght` 200–800, roman + italic |
| **Figtree** | `--font-body: 'Figtree', system-ui, -apple-system, BlinkMacSystemFont, sans-serif` | `figtree-400.woff2`, `figtree-500.woff2`, `figtree-600.woff2` | 400, 500, 600 (normal) |
| **Space Mono** | `--font-mono: 'Space Mono', ui-monospace, 'SFMono-Regular', Menlo, monospace` | `spacemono-400.woff2`, `spacemono-700.woff2` | 400, 700 (normal) |

Todas com `font-display: swap`, self-hosted, subset latin (`unicode-range: U+0000-00FF...`), **presentes em `/fonts`**: `newsreader-var.woff2` + `newsreader-var-i.woff2` (variáveis), `figtree-400/500/600/700`, `spacemono-400/700`. Preload no `<head>` apenas para as duas fontes do LCP: `newsreader-var.woff2` (display do hero) e `figtree-400.woff2`.

> **Por que variável (opsz):** Newsreader é uma fonte de *optical size*. A versão **variável** (`newsreader-var`) com `font-optical-sizing: auto` faz o desenho ganhar **contraste fino/grosso "display"** automaticamente nos tamanhos grandes (hero) e ficar mais robusto/legível no corpo — é o que casa o site com a página de tipografia (`identidade-visual/tipografia-opcoes.html`) e o Figma. As instâncias estáticas antigas (`newsreader-400/500/600/700`) travavam num único corte e foram removidas.
>
> **Nota de peso:** o hero (`.nm-display`) usa **Newsreader 600** com `font-optical-sizing: auto` (peso real interpolado da fonte variável — sem faux-bold). Newsreader vai até 800 real; 600 é o peso de display adotado. Títulos que no CSS antigo usavam Playfair 900/700 foram para **600** (`colors_and_type.css` e `styles.css`). Ver §3.5/§3.6.

### 3.2 Escala tipográfica (`--fs-*`)

| Token | Valor | px aprox. | Uso típico |
|---|---|---|---|
| `--fs-xs` | `0.72rem` | 11.5px | mono labels, metadados, eyebrows |
| `--fs-sm` | `0.825rem` | 13.2px | small body, captions |
| `--fs-base` | `0.95rem` | 15.2px | body padrão |
| `--fs-md` | `1.05rem` | 16.8px | body lead |
| `--fs-lg` | `1.25rem` | 20px | subtítulos pequenos |
| `--fs-xl` | `1.6rem` | 25.6px | — |
| `--fs-2xl` | `2.2rem` | 35.2px | — |
| `--fs-3xl` | `3rem` | 48px | — |
| `--fs-4xl` | `4rem` | 64px | — |
| `--fs-5xl` | `5.5rem` | 88px | capa / hero |

### 3.3 Line-heights (`--lh-*`)

| Token | Valor | Uso |
|---|---|---|
| `--lh-tight` | `1.05` | h1 |
| `--lh-snug` | `1.2` | h2 |
| `--lh-normal` | `1.45` | — |
| `--lh-relaxed` | `1.7` | Figtree body — sempre 1.7 |

### 3.4 Letter-spacing / tracking (`--ls-*`)

| Token | Valor | Uso |
|---|---|---|
| `--ls-tight` | `-0.02em` | h1 |
| `--ls-snug` | `-0.01em` | h2 |
| `--ls-normal` | `0` | — |
| `--ls-wide` | `0.04em` | — |
| `--ls-mono` | `0.12em` | Space Mono labels |
| `--ls-mono-wide` | `0.18em` | Eyebrows, capa-tag |

### 3.5 Hierarquia semântica (de `colors_and_type.css`)

| Elemento | Família | Peso | Tamanho | Line-height | Letter-spacing | Cor | Extras |
|---|---|---|---|---|---|---|---|
| `h1`/`.h1` | display (Newsreader) | 600 | `clamp(--fs-3xl, 6vw, --fs-5xl)` = `clamp(3rem, 6vw, 5.5rem)` | `--lh-tight` (1.05) | `--ls-tight` (-0.02em) | `--primary-deep` | `text-wrap: balance`, margin-bottom `--space-5` |
| `h2`/`.h2` | display | 600 | `clamp(--fs-xl, 3vw, --fs-2xl)` = `clamp(1.6rem, 3vw, 2.2rem)` | `--lh-snug` (1.2) | `--ls-snug` (-0.01em) | `--primary-deep` | `text-wrap: balance`, margin-bottom `--space-4` |
| `h3`/`.h3` | display | 600 | `--fs-lg` (1.25rem) | 1.3 | — | `--primary-deep` | margin-bottom `--space-3` |
| `h4`/`.h4` | body (Figtree) | 600 | `--fs-md` (1.05rem) | — | `0.01em` | `--primary-deep` | margin-bottom `--space-2` |
| `p` | body | — | `--fs-base` (herdado do `body`) | `--lh-relaxed` (1.7) | — | `--fg` | `max-width: var(--max-w-prose)` (62ch), `text-wrap: pretty` |
| `.eyebrow` / `.mono-label` | mono (Space Mono) | 400 | `--fs-xs` (0.72rem) | — | `--ls-mono-wide` (0.18em) | `--accent` | `text-transform: uppercase` |
| `.italic-display` | display | 400 italic | — | — | — | `--fg-on-dark-soft` | usado em taglines sobre fundo escuro |
| `code`/`kbd`/`pre`/`.mono` | mono | — | `0.9em` | — | — | — | — |

### 3.6 Classes específicas de componentes (de `styles.css`)

> A coluna **Família** usa os tokens abstratos `display`/`body`/`mono` — eles resolvem para **Newsreader / Figtree / Space Mono** (§3.1), então as classes abaixo seguem válidas. Os **pesos** mostrados na tabela são os herdados do CSS antigo (Playfair); o CSS já foi remapeado: **display 900 → Newsreader 600**, **display 700 → Newsreader 600**, **mono 500 → Space Mono 400**. Todo `italic` de display é **Newsreader italic 400**.

| Classe | Família | Peso/estilo | Tamanho | Outras props |
|---|---|---|---|---|
| `.nm-h2` | display | 700 | `clamp(1.7rem, 5.5vw, 3rem)` | line-height 1.05, letter-spacing -0.015em, cor `--primary-deep`; `.nm-h2 em` → 400 italic, cor `--primary` |
| `.nm-eyebrow` | mono | 500 | `11px` | letter-spacing 0.18em, uppercase, cor `--accent` |
| `.nm-lede` | body | — | `clamp(15px, 1.5vw, 17px)` (base 17px) | line-height 1.65, cor `--cinza-baunilha`, max-width 60ch |
| `.nm-display` (hero h1) | display | 900 | `clamp(2rem, 8.5vw, 5.5rem)` | line-height 0.98, letter-spacing -0.025em, cor `#fff` |
| `.nm-hero-sub` | display | 400 italic | `clamp(1.1rem, 1.8vw, 1.4rem)` | line-height 1.5, cor `rgba(255,255,255,.85)`, borda esquerda 3px `--accent` |
| `.nm-feature-title` | display | 700 | `clamp(17px, 1.7vw, 19px)` (base 19px) | line-height 1.25, cor `--primary-deep` |
| `.nm-feature-body` | body | — | `clamp(13.5px, 1.3vw, 14.5px)` | line-height 1.6, cor `--cinza-baunilha` |
| `.nm-step-num` | mono | 500 | `56px` | cor `--accent`, opacity 0.35 |
| `.nm-step-title` | display | 700 | `clamp(22px, 2.4vw, 26px)` | cor `--primary-deep` |
| `.nm-step-body` | body | — | `clamp(13.5px, 1.3vw, 14.5px)` | line-height 1.65, cor `--cinza-baunilha` |
| `.nm-roteiro-title` | display | 700 | `clamp(22px, 2.4vw, 26px)` | line-height 1.1, cor `--primary-deep` |
| `.nm-roteiro-sub` | display | 400 italic | `14px` | cor `--cinza-baunilha` |
| `.nm-roteiro-text` | body | — | `clamp(13.5px, 1.3vw, 14.5px)` | line-height 1.6, cor `--fg` |
| `.nm-price-prefix` | mono | — | `10px` | letter-spacing 0.12em, uppercase, cor `--accent` |
| `.nm-price-value` | display | 900 | `28px` | cor `--primary-deep` |
| `.nm-price-suffix` | body | — | `12px` | cor `--cinza-baunilha` |
| `.nm-bento-title` | display | 700 | `1.05rem` | cor `#fff` |
| `.nm-bento-text` | body | — | `12px` | line-height 1.5, cor `rgba(255,255,255,.82)` |
| `.nm-bento-modal-caption h3` | display | 700 | `1.45rem` | cor `#fff` |
| `.nm-quote-text` | display | 700 | `clamp(1.4rem, 2.4vw, 2rem)` | line-height 1.4, cor `#fff`; `em` → 400 italic, cor `--laranja-ambar` |
| `.nm-quote-cite-name` | mono | — | `11px` | letter-spacing 0.18em, uppercase, cor `--laranja-ambar` |
| `.nm-quote-cite-role` | body | italic | `14px` | cor `rgba(255,255,255,.65)` |
| `.nm-principle-text` | display | 700 | `clamp(1.7rem, 3.4vw, 2.6rem)` | line-height 1.35, cor `#fff`; `em` → italic, cor `--laranja-ambar`, weight 700 |
| `.nm-footer-mark` | display | 700 | `38px` | line-height 0.95, cor `#fff`, letter-spacing -0.02em |
| `.nm-footer-tag` | display | 400 italic | `18px` | line-height 1.4, cor `rgba(255,255,255,.7)` |
| `.nm-footer-col-h` | mono | 500 | `11px` | letter-spacing 0.18em, uppercase, cor `--laranja-ambar` |
| `.nm-footer-bot` | mono | — | `11px` | letter-spacing 0.06em, cor `rgba(255,255,255,.4)` |
| `.nm-about-sig` | display | 400 italic | `1.15rem` | cor `--primary` |
| `.nm-dif3-item p` | body | — | `14.5px` | line-height 1.68, cor `--fg-muted`; `strong` → display 700, cor `--primary-deep` |
| `.nm-timeline-title` | display | 700 | `clamp(1.2rem, 2.2vw, 1.5rem)` | cor `--primary-deep` |
| `.nm-timeline-body` | body | — | `15px` | line-height 1.72, cor `--fg` |
| `.nm-timeline-tag` | mono | — | `10px` | letter-spacing 0.14em, uppercase, cor `--accent` |
| `.nm-dep-card-quote` | display | italic | `.97rem` | line-height 1.65, cor `--fg` |
| `.nm-dep-card-name` | body | 600 | `.88rem` | cor `--fg` |
| `.nm-dep-card-dest` | mono | — | `10px` | letter-spacing 0.12em, uppercase, cor `--accent` |
| `.nm-radar-p` | body | — | `15.5px` | line-height 1.7, cor `rgba(255,255,255,.80)`, max-width 54ch |
| `.nm-form-step-h` | display | 700 | `clamp(1.2rem, 2.4vw, 1.5rem)` | cor `--primary-deep` |
| `.nm-field label` | mono | 500 | `10.5px` | letter-spacing 0.1em, uppercase, cor `--fg-muted` |
| `.nm-form-ok h3` | display | — | `1.6rem` | cor `--primary-deep` |
| `.nm-bento-badge` | body | 600 | `10px` | letter-spacing 0.08em, uppercase, cor `--laranja-ambar` |
| `.nm-roteiro-badge` | mono | 500 | `11px` | letter-spacing 0.12em, uppercase, cor `#fff` |

---

## 4. Espaçamento & layout

### 4.1 Escala de espaçamento (4pt baseline) — `--space-*`

| Token | Valor | px |
|---|---|---|
| `--space-0` | `0` | 0 |
| `--space-1` | `0.25rem` | 4 |
| `--space-2` | `0.5rem` | 8 |
| `--space-3` | `0.75rem` | 12 |
| `--space-4` | `1rem` | 16 |
| `--space-5` | `1.5rem` | 24 |
| `--space-6` | `2rem` | 32 |
| `--space-7` | `2.5rem` | 40 |
| `--space-8` | `3rem` | 48 |
| `--space-9` | `4rem` | 64 |
| `--space-10` | `5rem` | 80 |
| `--space-11` | `6rem` | 96 |

### 4.2 Larguras / containers — `--max-w-*`

| Token | Valor | Uso |
|---|---|---|
| `--max-w-prose` | `62ch` | largura máxima de `<p>` |
| `--max-w-content` | `1180px` | (não usado diretamente nas classes lidas — token disponível) |
| `--max-w-wide` | `1360px` | (não usado diretamente nas classes lidas — token disponível) |

### 4.3 Padrão de layout geral

- **Gutter lateral**: `padding: <vertical> 10%` em praticamente todas as seções (`.nm-header`, `.nm-hero`, `.nm-block`, `.nm-bento`, `.nm-dif3-*`, `.nm-radar`, `.nm-footer`) — 10% é a constante estrutural do site.
- **`.nm-block`**: `padding: 96px 10%`, `display: flex; flex-direction: column; align-items: center`.
- **`.nm-section-head`**: `width: 100%; margin: 0 0 56px; text-align: center`.
- **Grids flexíveis** (não CSS Grid, exceto bento):
  - `.nm-grid-4` (diferenciais antigos / features): `display: flex; flex-wrap: wrap; gap: 20px`, itens `flex: 1 1 240px`.
  - `.nm-grid-3` (roteiros legado): `display: flex; flex-wrap: wrap; gap: 24px`, itens `flex: 1 1 300px`.
  - `.nm-process`: `display: flex; flex-wrap: wrap; gap: 24px`, `.nm-step` `flex: 1 1 260px`.
- **Bento gallery** (`.nm-bento`): único `display: grid`, `grid-template-columns: repeat(4, 1fr)`, `grid-auto-rows: 60px`, `gap: 12px`, padding `0 10%`. Cards posicionados manualmente por `nth-child` (mosaico assimétrico 1+2+1 / 2+2).
- **`.nm-dif3-grid`**: `display: grid; grid-template-columns: 1fr minmax(200px,260px) 1fr`, gap `clamp(28px,4vw,64px)`.

### 4.4 Breakpoints reais (media queries usadas)

| Breakpoint | Direção | Principais ajustes |
|---|---|---|
| `1366px` | max-width | `.nm-block { padding-block: 88px }` (notebook — aperta ritmo vertical) |
| `1024px` | max-width | hero-sub menor, `.nm-block { padding-block: 80px }`, tipografia tablet (lede 17px, bodies 15-16px), `.nm-about-inner` vira coluna, `.nm-dif3-grid` vira 2 colunas |
| `1100px` | max-width | `.nm-step-connector` escondido, `.nm-grid-4/.nm-grid-3 > * { flex-basis: 44% }` (2-up), `.nm-block { padding-block: 80px }`, `.nm-hero { padding-top: 72px }` |
| `820px` | max-width | header com hamburguer (`.nm-nav-toggle` visível), nav some/expande, `.nm-about-inner` ajustes, bento 2 colunas, `.nm-radar-inner` vira coluna, `.nm-field-row` vira coluna |
| `640px` | max-width | hero centralizado, tudo 1-coluna, `.nm-block { padding-block: 60px }`, `.nm-quote-glyph` reduzido, footer empilha, bento 1 coluna |
| `420px` | max-width | `.nm-footer-cols > div { flex-basis: 100% }` |
| `641px` | min-width | exibe `.nm-dep-col-md` (2ª coluna de depoimentos) |
| `1024px` | min-width | exibe `.nm-dep-col-lg` (3ª coluna de depoimentos) |

**Filosofia responsiva**: o gutter lateral de 10% é mantido em **todas** as larguras — breakpoints só re-ajustam ritmo vertical (`padding-block`), wrapping de flex, e troca de nav para hamburguer. Tipografia é fluida via `clamp()` por padrão.

---

## 5. Raios, sombras e bordas

> **Nota de cor (§5–§6):** o CSS do site **já foi re-sincronizado** para "Pôr do Sol Tropical" — âncora Marinho Maré `#0C3350` → `rgba(12,51,80,…)` e acento Coral Poente `#FB6A3C` → `rgba(251,106,60,…)`. Alguns valores `rgba()` citados nas descrições de componentes abaixo ainda usam o **literal antigo** (`rgba(13,59,110)`/`rgba(244,124,32)`) apenas como texto histórico; a referência canônica é o mapa em §2.8. Os tokens de sombra em §5.2 já estão no valor novo.

### 5.1 Raios (`--radius-*`)

| Token | Valor | Uso típico |
|---|---|---|
| `--radius-xs` | `4px` | hex swatches, badges |
| `--radius-sm` | `8px` | inputs, copy callouts |
| `--radius-md` | `10px` | cards default |
| `--radius-lg` | `12px` | destaque, "principio-grande" |
| `--radius-xl` | `20px` | large overlays |
| `--radius-pill` | `999px` | pills/badges/circulares |

Valores observados em componentes específicos (hardcoded no `styles.css`, fora dos tokens): `.nm-roteiro` = `14px`, `.nm-bento-card` = `18px`, `.nm-bento-modal-img` = `16px`, `.nm-quote-block` = `16px`, `.nm-bento-modal-close` = `50%` (circular), `.nm-form-step-dot` = `50%`, `.nm-dif3-logo-wrap` = `24px`, `.nm-feature`/`.nm-step` = `12px`, `.nm-bento-thumb` = `10px`.

### 5.2 Sombras (`--shadow-*`) — tingidas de Marinho Maré, nunca cinza neutro

Valores no tema "Pôr do Sol Tropical" (âncora `#0C3350` → `rgba(12,51,80,…)`):

| Token | Valor |
|---|---|
| `--shadow-xs` | `0 1px 2px rgba(12, 51, 80, 0.06)` |
| `--shadow-sm` | `0 2px 8px rgba(12, 51, 80, 0.08)` |
| `--shadow-md` | `0 8px 24px rgba(12, 51, 80, 0.10), 0 2px 6px rgba(12, 51, 80, 0.05)` |
| `--shadow-lg` | `0 18px 48px rgba(12, 51, 80, 0.14), 0 4px 12px rgba(12, 51, 80, 0.06)` |
| `--shadow-focus` | `0 0 0 3px rgba(251, 106, 60, 0.30)` (Coral Poente — usado em `:focus` de inputs) |

Sombras hardcoded fora dos tokens:
- `.nm-dep-card`: `0 2px 12px rgba(0,0,0,.06)` (sombra neutra leve, única exceção)
- `.nm-fab`: `0 4px 18px rgba(37,211,102,.38)` (verde WhatsApp)
- `.nm-fab-top`: `0 4px 18px rgba(13,59,110,.38)`
- `.nm-bento-modal-img`: `0 32px 80px rgba(0,0,0,.55)`

### 5.3 Bordas

- `--border` = `var(--cinza-claro)` (`#F0EBE3`) — bordas suaves padrão.
- `--border-strong` = `var(--cinza-medio)` (`#C9C1B6`) — inputs, hairlines fortes, linha do timeline.
- Espessuras observadas: `1px` (cards, header), `1.5px` (botões ghost, inputs, radio options), `2px`/`2.5px`/`3px` (ícones SVG stroke-width, hero-sub border-left).
- `.nm-dif3-item` usa `border-bottom: 1px dashed var(--border-strong)`.

---

## 6. Componentes (`.nm-*`)

### 6.1 Botões — `.nm-btn`

Base (`.nm-btn`):
```css
display: inline-flex; align-items: center; gap: 10px;
font-family: var(--font-body); font-weight: 600; font-size: 14px;
padding: 12px 22px; border-radius: 8px; border: none; cursor: pointer;
transition: background 180ms var(--ease-out), box-shadow 180ms var(--ease-out), transform 180ms var(--ease-out);
text-decoration: none; white-space: nowrap;
```
Ícone interno (`.ico`) deslocado 3px à direita no hover (`transform: translateX(3px)`).

Variantes:

| Classe | Estado normal | Hover |
|---|---|---|
| `.nm-btn-primary` | fundo `--accent` (laranja), texto `#fff`, `box-shadow: --shadow-sm`. **Animação contínua**: `nm-cta-pulse 2.8s ease-in-out infinite` (pulso laranja, viés de saliência) | animação removida; fundo `#D96A10`; `box-shadow: --shadow-md, 0 6px 20px rgba(217,106,16,.35)`; `transform: translateY(-2px)` |
| `.nm-btn-ghost` | transparente, texto `--primary-deep`, borda `1.5px solid --primary-deep` | fundo `--azul-nevoa` |
| `.nm-btn-ghost-dark` | transparente, texto `#fff`, borda `1.5px solid rgba(255,255,255,.6)` (para uso sobre hero/fundo escuro) | fundo `rgba(255,255,255,.1)`, borda `#fff` |
| `.nm-btn-large` | `padding: 16px 28px; font-size: 16px` (modificador de tamanho) | — |
| `.nm-btn-radar` | fundo `#25D366` (WhatsApp green), texto `#fff`, `font-weight: 700`. Animação `nm-radar-pulse 2.8s` (pulso verde) | animação removida; fundo `#1EBE5A`; `box-shadow: 0 8px 28px rgba(37,211,102,.45)`; `translateY(-2px)` |

Keyframes:
```css
@keyframes nm-cta-pulse {
  0%,100% { box-shadow: var(--shadow-sm), 0 0 0 0 rgba(244,124,32,0.40); }
  55%     { box-shadow: var(--shadow-sm), 0 0 0 10px rgba(244,124,32,0); }
}
@keyframes nm-radar-pulse {
  0%,100% { box-shadow: var(--shadow-sm), 0 0 0 0 rgba(37,211,102,.50); }
  55%     { box-shadow: var(--shadow-sm), 0 0 0 12px rgba(37,211,102,0); }
}
```

Mobile (`max-width: 640px`): `.nm-btn { font-size: 15px; padding: 14px 22px }`.

### 6.2 Eyebrows & headings compartilhados

- `.nm-eyebrow` / `.nm-eyebrow-dark`: mono, 11px, 500, letter-spacing 0.18em, uppercase, cor `--accent`, `margin-bottom: 16px`.
- `.nm-h2`: ver §3.6. `.nm-h2 em` → itálico 400, cor `--primary`.
- `.nm-lede`: parágrafo de apoio sob o h2 de seção, cor `--cinza-baunilha`, max-width 60ch.
- `.nm-section-head`: container centralizado para eyebrow + h2 + lede de cada seção.

### 6.3 Header / Navegação — `.nm-header`

- `position: sticky; top: 0; z-index: 50`, `padding: 16px 10%`, fundo `--bg`, borda inferior `1px solid --border`.
- **Estado scrolled** (`.is-scrolled`, JS adiciona ao `scrollY > 60`): fundo `rgba(250,250,248,0.72)` + `backdrop-filter: blur(20px)` (frosted glass), `box-shadow: 0 2px 24px rgba(13,59,110,.10)`, borda transparente.
- `.nm-logo-svg`: `height: 44px`, cor `--primary-deep`.
- `.nm-nav`: flex, gap 36px, 14px/500.
- `.nm-nav a`: underline animado — `::after` com `transform: scaleX(0)→scaleX(1)` no hover, cor `--accent`, 220ms.
- `.nm-header-cta` / `.nm-nav-cta`: botão "Quero minha cotação" (`.nm-btn-primary`).
- **Mobile nav** (`.nm-nav-toggle`, ≤820px): hamburguer de 3 barras (`<span>`) que se transforma em X (`.is-open` → rotações ±45deg + opacity 0 na barra do meio). Nav vira painel absoluto abaixo do header, frosted (`blur(14px)`), `transform: translateY(-12px) → none` + opacity.

### 6.4 Hero — `.nm-hero`

- `min-height: clamp(620px, 88vh, 880px)`, `padding: 80px 10% 0`, texto branco, `overflow: hidden`.
- **Camadas em ordem**:
  1. `.nm-hero-poster` (`<img>` LCP, `object-fit: cover`, `filter: brightness(0.82) saturate(1.05)`) — carrega instantaneamente.
  2. `.nm-hero-bg` (`<video autoplay muted loop playsinline preload="none">`, mesmo filtro) — entra por cima quando carregado.
  3. `.nm-hero-overlay` — dois gradientes sobrepostos:
     - `linear-gradient(180deg, rgba(13,59,110,.35) 0%, rgba(13,59,110,.15) 40%, rgba(13,59,110,.85) 100%)`
     - `linear-gradient(90deg, rgba(13,59,110,.55) 0%, rgba(13,59,110,0) 60%)`
  4. `.nm-hero-inner` (conteúdo, `align-items: flex-start`, `padding-bottom: 80px`).
- `.nm-hero .nm-eyebrow`: cor `--laranja-ambar`.
- `.nm-display` (h1): ver §3.6.
- `.nm-hero-sub`: itálico, borda esquerda 3px `--accent`, `padding-left: 20px`; `em` interno vira normal/branco.
- `.nm-hero-cta`: flex gap 14px, wrap.
- `.nm-hero-foot`: rodapé de 3 benefícios com ícones, borda superior `1px solid rgba(255,255,255,.15)`, texto `13px` `rgba(255,255,255,.75)`; ícones cor `--laranja-ambar`.
- Mobile (≤640px): hero centralizado (`justify-content: center; text-align: center`), `.nm-hero-sub` perde borda esquerda e ganha borda superior 3px.

### 6.5 Blocos / seções genéricas

- `.nm-block`: `padding: 96px 10%`, flex column centrado.
- `.nm-block-light`: fundo `--bg`.
- `.nm-block-soft`: fundo `--cinza-claro`.

### 6.6 Seção "Sobre" — `.nm-about` (editorial assimétrico)

- Fundo: gradiente animado `linear-gradient(-20deg, var(--bg) 0%, var(--azul-nevoa) 55%, var(--bg) 100%)`, `background-size: 200% 200%`, animação `nm-soft-shift 22s ease-in-out infinite`.
- `.nm-about-inner`: flex, `gap: clamp(40px,7vw,96px)`, `align-items: center`, `padding: 96px 10%`.
- `.nm-about-photo-wrap`: `flex: 0 0 42%`, `max-width: 480px`.
- `.nm-about-photo`: `aspect-ratio: 3/4`, `object-fit: cover`, `border-radius: 16px`, **rotacionada `-2.5deg`** (assimetria deliberada), `box-shadow: --shadow-lg`. Hover: rotação volta a 0deg + `box-shadow: --shadow-lg, 0 0 0 4px var(--accent-soft)` (halo laranja).
- `.nm-about-photo-tag`: badge posicionado `bottom: -14px; right: -14px`, fundo `--accent`, mono 10px uppercase, `border-radius: 8px`.
- `.nm-about-content p`: `15.5px`, line-height 1.75; `em` → itálico cor `--primary`.
- `.nm-about-sigs`: assinaturas das fundadoras lado a lado, `.nm-about-sig` em Newsreader itálico `1.15rem` cor `--primary`, separadas por `·` (`.nm-about-sig-sep`, cor `--cinza-medio`).

Keyframe compartilhado:
```css
@keyframes nm-soft-shift {
  0%,100% { background-position: 0% 50%; }
  50%     { background-position: 100% 50%; }
}
```

### 6.7 Diferenciais — `.nm-diferenciais` (3 colunas + logo central)

- Fundo: gradiente animado `linear-gradient(160deg, var(--bg) 0%, var(--azul-nevoa) 45%, var(--bg) 100%)`, `nm-soft-shift 20s ease-in-out 1s infinite`.
- `.nm-dif3-grid`: CSS grid `1fr minmax(200px,260px) 1fr`, gap `clamp(28px,4vw,64px)`.
- `.nm-dif3-item`: linha com ícone de check + texto, `border-bottom: 1px dashed var(--border-strong)` (última sem borda). Coluna esquerda (`.nm-dif3-col-left`) inverte direção (`row-reverse`, `text-align: right`).
- `.nm-dif3-check`: círculo 28×28px, fundo `--accent-soft`, ícone cor `--accent`. Hover do item: fundo vira `--accent`, ícone `#fff`, `scale(1.12)`.
- **Centro — logo animada** (`.nm-dif3-center` / `.nm-dif3-logo-wrap`): cartão com `background: rgba(255,255,255,.72)`, `border-radius: 24px`, `backdrop-filter: blur(10px)`, `box-shadow: --shadow-md` (hover → `--shadow-lg`). Contém o SVG da logo (`viewBox="0 0 70.04 54.66"`, monograma "NORTEAR" em paths, `color: --primary-deep`).
  - **Animação de "letras surgindo"**: cada `path` da logo começa `opacity: 0`; quando `.nm-dif3-center.is-in` (scroll-reveal), cada `path` (filhos 2 a 12) anima `nm-logo-letter 0.65s` com delays escalonados de `0.06s` a `0.74s`:
    ```css
    @keyframes nm-logo-letter {
      0%   { opacity: 0; transform: translateY(5px) scale(0.92); }
      65%  { opacity: 1; transform: translateY(-1px) scale(1.01); }
      100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    ```
  - **Orbs flutuantes** (`.nm-dif3-orb-1`/`-2`): círculos com `radial-gradient` (laranja e azul translúcidos), animações `nm-dif-float1` (4.5s, sobe/desce -14px) e `nm-dif-float2` (5.5s, delay 1.2s, desce/sobe +18px).
- `.nm-dif3-cta`: botão sem animação de pulso (`animation: none !important`), `font-size: 13px; padding: 11px 20px`.

### 6.8 Processo — `.nm-process` / `.nm-step` (timeline horizontal)

- `.nm-step`: cartão branco, `border-radius: 12px`, `padding: 36px 32px`, borda `1px solid --border`.
- `.nm-step-num`: número grande mono (56px/500), cor `--accent`, `opacity: 0.35`.
- `.nm-step-title`: ver §3.6.
- `.nm-step-connector`: seta entre os cards (escondida ≤1100px quando o layout quebra para wrap).

### 6.9 Roteiros — cards legado (`.nm-roteiro`) e Bento Gallery (`.nm-bento`)

**Card legado `.nm-roteiro`** (grid `.nm-grid-3`):
- `border-radius: 14px`, `overflow: hidden`, borda `1px solid --border`. Hover: `box-shadow: --shadow-lg`, `translateY(-5px)`.
- `.nm-roteiro-photo`: altura 240px, `background-size: cover`; imagem interna escala `1.04x` no hover (400ms).
- `.nm-roteiro-badge`: pill posicionado `top:16px; left:16px`, fundo `rgba(13,59,110,.92)`, mono 11px uppercase, `border-radius: 999px`, `backdrop-filter: blur(8px)`.
- `.nm-roteiro-body`: padding 24px, flex column.
- `.nm-roteiro-foot`: preço + link, separado por `border-top: 1px solid --border`.
- `.nm-price-prefix`/`.nm-price-value`/`.nm-price-suffix`: "A PARTIR DE" (mono pequeno) + valor grande (Newsreader 600, 28px) + sufixo.
- `.nm-link-arrow`: link com seta que se afasta no hover (`gap: 6px → 12px`), cor `--accent → --accent-hover`.

**Bento Gallery `.nm-bento`** (seção "Roteiros recentes" — implementação ativa no HTML):
- CSS Grid `repeat(4, 1fr)`, `grid-auto-rows: 60px`, `gap: 12px`, `padding: 0 10%`.
- 5 cards (`.nm-bento-card`) com posicionamento manual via `nth-child`:
  - Card 1: col 1, row 1/span 3
  - Card 2: col 2/span 2, row 1/span 3 (maior, central)
  - Card 3: col 4, row 1/span 3
  - Card 4: col 1/span 2, row 4/span 2
  - Card 5: col 3/span 2, row 4/span 2
- Cada card: `border-radius: 18px`, `overflow: hidden`, fundo `--primary-deep` (placeholder antes da imagem carregar via lazy IntersectionObserver com `data-bg`).
- `.nm-bento-card-img`: `background-size: cover`, escala `1.055x` no hover (600ms).
- `::after` (overlay): `linear-gradient(to top, rgba(13,59,110,.88) 0%, rgba(13,59,110,.26) 55%, transparent 100%)`, `opacity: 0 → 1` no hover.
- `.nm-bento-card-info`: badge + título + texto, sobe com `translateY(10px) → none` + `opacity: 0 → 1` no hover (desktop). Em mobile/tablet (≤820px) sempre visível (`opacity: 1`).
- `.nm-bento-badge`: pill `rgba(0,0,0,.40)`, `backdrop-filter: blur(6px)`, texto `--laranja-ambar`.

**Responsivo do bento**:
- ≤820px: 2 colunas, `grid-auto-rows: 80px`, cards forçados a `grid-row: span 3`.
- ≤640px: 1 coluna, `grid-auto-rows: 180px`.

### 6.10 Modal do Bento — `.nm-bento-modal`

- Overlay fixo (`inset: 0; z-index: 900`), fundo `rgba(8,18,36,.84)`, `backdrop-filter: blur(16px)`. Transição `opacity 280ms` + `visibility` com delay.
- `.is-open` → `opacity: 1; visibility: visible`.
- `.nm-bento-modal-img`: `width: min(860px, 90vw)`, `aspect-ratio: 16/9`, `border-radius: 16px`, `box-shadow: 0 32px 80px rgba(0,0,0,.55)`. Entrada: `scale(0.94) translateY(16px) → none` (380ms).
- `.nm-bento-modal-caption`: gradiente `to top, rgba(0,0,0,.72), transparent`, título Newsreader 600 1.45rem + parágrafo `rgba(255,255,255,.82)`.
- `.nm-bento-modal-close`: botão circular 36×36px, `rgba(255,255,255,.15)`, hover `rgba(255,255,255,.30) scale(1.1)`.
- **Dock de thumbnails** (`.nm-bento-modal-dock`): faixa `rgba(255,255,255,.10)`, `backdrop-filter: blur(12px)`, `border-radius: 16px`.
  - `.nm-bento-thumb`: 44×44px, `border-radius: 10px`, rotação em "leque" via `transform: rotate(calc(var(--ti,0) * 7deg - 14deg))`.
  - `.is-active`: borda `rgba(255,255,255,.85)`, `translateY(-8px) scale(1.18) rotate(0deg)`.
  - Hover (não-ativo): `translateY(-10px) scale(1.12) rotate(0deg)`.
- Navegação por teclado (JS): `Escape` fecha, `ArrowRight`/`ArrowLeft` navegam entre roteiros.
- `prefers-reduced-motion: reduce`: todas as transições do bento/modal são removidas; `.nm-bento-card-info` fica sempre visível.

### 6.11 Testemunho destaque — `.nm-quote-block`

- Cartão de citação única, fundo `--primary-deep`, `border-radius: 16px`, `padding: 56px clamp(28px,6%,72px)`, texto branco.
- `.nm-quote-glyph`: aspas decorativas gigantes (`font-size: 220px`, Newsreader), cor do acento a ~18% (`rgba(251,106,60,0.18)` no tema novo; CSS atual `rgba(244,124,32,0.18)`), posicionadas `top:-28px; right:36px` (decorativo, `pointer-events: none`). Em mobile (≤640px) reduz para `140px`.
- `.nm-quote-text`: ver §3.6; `em` → itálico, cor `--laranja-ambar`.
- `.nm-quote-cite-name` (mono uppercase, `--laranja-ambar`) + `.nm-quote-cite-role` (itálico, `rgba(255,255,255,.65)`).

> Nota: este componente existe no CSS mas a seção de **depoimentos ativa no HTML** usa o sistema de colunas de scroll (§6.12), não este bloco único.

### 6.12 Depoimentos — `.nm-depoimentos` / `.nm-dep-*` (colunas de scroll infinito)

- Seção com fundo gradiente animado `linear-gradient(160deg, var(--bg-soft) 0%, var(--azul-nevoa) 45%, var(--bg-soft) 100%)`, `nm-soft-shift 26s ease-in-out 4s infinite`.
- `.nm-dep-columns`: flex, `gap: 20px`, `max-height: 720px`, `overflow: hidden`, com **fade mask** nas bordas verticais:
  ```css
  mask-image: linear-gradient(to bottom, transparent, black 18%, black 82%, transparent);
  ```
- Estrutura: 3 colunas (`.nm-dep-col`), cada uma com `.nm-dep-track` (flex column, cards duplicados para loop seamless).
  - Coluna 1: sempre visível.
  - Coluna 2 (`.nm-dep-col-md`): visível `min-width: 641px`.
  - Coluna 3 (`.nm-dep-col-lg`): visível `min-width: 1024px`.
- Cada track tem velocidade própria (parecem orgânicas):
  ```css
  @keyframes nm-dep-scroll { to { transform: translateY(-50%); } }
  .nm-dep-track-1 { animation: nm-dep-scroll 22s linear infinite; }
  .nm-dep-track-2 { animation: nm-dep-scroll 28s linear infinite; }
  .nm-dep-track-3 { animation: nm-dep-scroll 25s linear infinite; }
  ```
- Hover em qualquer coluna pausa a animação daquela track (`animation-play-state: paused`).
- `prefers-reduced-motion: reduce`: `animation: none`.
- **Card `.nm-dep-card`**: fundo `#fff`, `border-radius: 14px`, `padding: 26px 22px`, borda `1px solid --border`, `box-shadow: 0 2px 12px rgba(0,0,0,.06)` (única sombra neutra do sistema). Hover: `box-shadow: --shadow-md`, `translateY(-4px)`.
  - `.nm-dep-stars`: 5 ícones `#i-star` (fill), cor `--laranja-ambar`.
  - `.nm-dep-card-quote`: itálico Newsreader.
  - `.nm-dep-card-avatar`: círculo 42px, fundo `--primary-tint`, borda `2px solid --border` (placeholder sem foto).
  - `.nm-dep-card-name` + `.nm-dep-card-dest` (destino · data).

### 6.13 Radar de Milhas — `.nm-radar`

- Fundo gradiente animado de 4 paradas, 300% de tamanho:
  ```css
  background: linear-gradient(135deg, var(--azul-profundo) 0%, var(--azul-nortear) 40%, #1A6DB8 65%, var(--azul-profundo) 100%);
  background-size: 300% 300%;
  animation: nm-radar-bg 18s ease-in-out infinite;
  ```
- `::before`: glow radial laranja `radial-gradient(ellipse at 80% 50%, rgba(244,124,32,.18) 0%, transparent 60%)`.
- `.nm-radar-inner`: flex, `gap: clamp(28px,5vw,64px)`, `align-items: center`, `flex-wrap: wrap`.
- `.nm-radar-icon`: emoji ✈️ em `font-size: clamp(2.5rem,5vw,4rem)`.
- `.nm-radar-h2`: força `color: #fff`.
- `.nm-radar-p`: ver §3.6.
- CTA: `.nm-btn-radar` (verde WhatsApp, pulso — ver §6.1).
- ≤820px: `.nm-radar-inner` vira coluna, `.nm-btn-radar` ocupa 100% da largura.

### 6.14 Formulário multi-step — `.nm-cotacao` / `.nm-form-*`

- Seção com fundo gradiente animado `linear-gradient(145deg, var(--bg-tint) 0%, var(--bg-soft) 50%, var(--bg-tint) 100%)`, `nm-soft-shift 18s ease-in-out 2s infinite`.
- `.nm-form-wrap`: `max-width: 680px`, centralizado.
- **Barra de progresso** (`.nm-form-progress`, `role="progressbar"`):
  - `.nm-form-step-dot`: círculo 38px, fundo `--border`, texto `--fg-muted`.
    - `.active`: fundo `--primary`, texto `#fff`, halo `box-shadow: 0 0 0 6px var(--primary-tint)`.
    - `.done`: fundo `--accent`, texto `#fff`.
  - `.nm-form-step-line`: linha 2px `--border-strong`; `.done` → `--accent`.
  - `.nm-form-progress-labels`: labels mono 10px uppercase `--cinza-medio`; `.active` → `--primary`.
  - 3 etapas: ícones `#i-map` (Destino), `#i-compass` (A viagem), `#i-heart` (Contato).
- **Campos** (`.nm-field`):
  - `label`: mono 10.5px/500, uppercase, `--fg-muted`. `.nm-req` (asterisco) → `--accent`. `.nm-opt` → `--cinza-medio`, sem uppercase.
  - `input/select/textarea`: `padding: 13px 15px`, borda `1.5px solid --border-strong`, `border-radius: 9px`, fundo `#fff`, `font-size: 15px`.
  - `:focus`: borda `--primary`, `box-shadow: --shadow-focus` (halo laranja).
  - `.nm-field-error`: `12px`, cor `--erro`.
  - `.nm-field-row`: 2 campos lado a lado (`flex: 1` cada); ≤820px vira coluna.
- **Radio pills** (`.nm-radio-group`/`.nm-radio-opt`): `padding: 10px 16px`, borda `1.5px solid --border-strong`, `border-radius: 9px`; `:has(input:checked)` → borda `--primary`, fundo `--primary-tint`, texto `--primary-deep`.
- **Checkbox** (`.nm-check-opt`): `accent-color: --primary`.
- **Navegação**: `.nm-form-nav` (alinha à direita) / `.nm-form-nav-2` (space-between, Voltar + Continuar).
- **Estado de sucesso** (`.nm-form-ok`, injetado via JS após submit): ícone check em círculo (`.nm-form-ok-ico`, `--accent` sobre `--accent-soft`), `h3` + `p` centralizados.
- Etapas do formulário (conteúdo real):
  1. **"Pra onde você quer ir? 🗺️"** — destino (obrigatório), data prevista (opcional), duração.
  2. **"Como vai ser a viagem? 🧳"** — tipo (Casal/Família/Grupo/Solo, com emojis), número de pessoas, faixa de orçamento (select com 4 faixas + "prefiro não informar").
  3. **"Quase lá! Como a gente fala com você? 💬"** — nome (obrigatório), WhatsApp (obrigatório), e-mail (opcional), melhor horário (select), checkbox opt-in "Radar de Milhas". Submit → "Enviar cotação via WhatsApp" (ícone `#i-message-circle`).

### 6.15 Princípio (CTA grande) — `.nm-principle`

- Fundo `--primary-deep`, `padding: 120px 10%`, `text-align: center`.
- `.nm-principle-bg`: dois radial-gradients decorativos —
  ```css
  radial-gradient(ellipse at 20% 65%, rgba(244,124,32,.20) 0%, transparent 52%),
  radial-gradient(ellipse at 80% 25%, rgba(26,95,168,.28) 0%, transparent 50%)
  ```
- `.nm-principle-text`: ver §3.6; `em` → itálico, `--laranja-ambar`, peso 700.
- CTA primário ("Começa a sua agora").
- Entrada por scroll com **easing de mola** (`.nm-principle-stagger .reveal`): `transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1)`.
- ≤640px: `padding-block: 80px`.

### 6.16 Footer — `.nm-footer`

- Fundo `--primary-deep`, texto `rgba(255,255,255,.7)`, `padding: 80px 10% 32px`.
- `.nm-footer-top`: flex wrap, `gap: 64px`.
- `.nm-footer-brand` (`flex: 1 1 280px`): logo SVG invertida (`.nm-footer-logo-svg`, `filter: brightness(0) invert(1); opacity: 0.92; height: 48px`), `.nm-footer-tag` (itálico), `.nm-footer-social` (3 ícones circulares 40px, fundo `rgba(255,255,255,.08)`, hover → `--accent`).
- `.nm-footer-cols` (`flex: 2 1 420px`): 3 colunas (Navegar / Conversar / Onde estamos), cada `flex: 1 1 160px`. Títulos `.nm-footer-col-h` mono uppercase `--laranja-ambar`. Links com `padding: 6px 0`, hover → `#fff`.
- `.nm-footer-addr`: endereço com `<br>`.
- `.nm-footer-bot`: linha final, `border-top: 1px solid rgba(255,255,255,.1)`, mono 11px, `rgba(255,255,255,.4)`, `justify-content: space-between`. Conteúdo: copyright + "Feito com cuidado, no Nordeste 🌊".
- ≤640px: `padding-block: 56px 28px`, colunas reorganizam (`flex-basis: 40%` → `100%` em ≤420px), `.nm-footer-bot` vira coluna.

### 6.17 FABs (botões flutuantes)

- **`.nm-fab`** (WhatsApp): `position: fixed; bottom: 24px; right: 24px; z-index: 200`, círculo 58px, fundo `#25D366`, ícone `#i-message-circle`. Pulso contínuo:
  ```css
  @keyframes nm-fab-pulse {
    0%,100% { box-shadow: 0 4px 18px rgba(37,211,102,.38), 0 0 0 0 rgba(37,211,102,.32); }
    55%     { box-shadow: 0 4px 18px rgba(37,211,102,.38), 0 0 0 14px rgba(37,211,102,0); }
  }
  ```
  Hover: animação para, `scale(1.12) translateY(-2px)`.
- **`.nm-fab-top`** (voltar ao topo): `position: fixed; bottom: 24px; left: 24px; z-index: 200`, círculo 58px, fundo `--primary-deep`, ícone `#i-arrow-up`. Escondido por padrão (`opacity:0; visibility:hidden`), aparece (`.is-visible`) quando `window.scrollY > 500` (JS). Hover igual ao FAB do WhatsApp mas com sombra azul.
- Mobile (≤640px): ambos reduzem para 52px e `bottom/left/right: 16px`.

### 6.18 Toast — `.nm-toast`

- `position: fixed; bottom: 32px; right: 32px; z-index: 100`, fundo `--primary-deep`, texto branco, `border-radius: 12px`, `box-shadow: --shadow-lg`, `max-width: 340px`.
- Ícone cor `--laranja-ambar`.
- Entrada: `nm-toast-in 320ms var(--ease-out)`:
  ```css
  @keyframes nm-toast-in { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
  ```

---

## 7. Movimento & animações

### 7.1 Tokens de motion

| Token | Valor |
|---|---|
| `--ease-out` | `cubic-bezier(0.22, 1, 0.36, 1)` |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` |
| `--dur-fast` | `140ms` |
| `--dur-base` | `220ms` |
| `--dur-slow` | `420ms` |

### 7.2 Scroll-reveal (`.reveal`) — bidirecional via IntersectionObserver

```css
@media (prefers-reduced-motion: no-preference) {
  .reveal { opacity: 0; transform: translateY(28px); will-change: opacity, transform;
            transition: opacity 720ms var(--ease-out), transform 720ms var(--ease-out); }
  .reveal.is-in { opacity: 1; transform: none; }
  .reveal[data-delay="1"] { transition-delay: 80ms; }
  .reveal[data-delay="2"] { transition-delay: 160ms; }
  .reveal[data-delay="3"] { transition-delay: 240ms; }
}
```
- JS: `IntersectionObserver` com `rootMargin: "0px 0px -8% 0px"`, `threshold: 0.08`. Adiciona `.is-in` ao entrar; **remove `.is-in` ao sair por cima** (scroll-up reverte a animação) — comportamento bidirecional intencional. Sem suporte a `IntersectionObserver`: todos os `.reveal` recebem `.is-in` imediatamente.
- Usado em praticamente todas as seções (section heads, cards, steps, bento, form-wrap, etc.), com `data-delay="1|2|3"` para escalonar.

### 7.3 Hero — entrada e Ken Burns

```css
@media (prefers-reduced-motion: no-preference) {
  .nm-hero-inner > * { opacity: 0; animation: nm-rise 900ms var(--ease-out) forwards; }
  .nm-hero .nm-eyebrow { animation-delay: 150ms; }
  .nm-display  { opacity: 1; animation: nm-rise-tf 700ms var(--ease-out) both; } /* LCP-safe: só transform */
  .nm-hero-sub { animation-delay: 500ms; }
  .nm-hero-cta { animation-delay: 660ms; }
  .nm-hero-foot{ opacity: 0; animation: nm-rise 900ms var(--ease-out) 820ms forwards; }
}
@keyframes nm-rise    { from { opacity:0; transform: translateY(26px); } to { opacity:1; transform:none; } }
@keyframes nm-rise-tf { from { transform: translateY(22px); } to { transform: none; } }
```
- **Ken Burns** no vídeo de fundo:
  ```css
  @media (prefers-reduced-motion: no-preference) {
    .nm-hero-bg { animation: nm-kenburns 26s ease-in-out infinite alternate; }
  }
  @keyframes nm-kenburns { from { transform: scale(1.02); } to { transform: scale(1.10); } }
  ```

### 7.4 Backgrounds animados (gradiente "respirando")

```css
@keyframes nm-soft-shift {
  0%,100% { background-position: 0% 50%; }
  50%     { background-position: 100% 50%; }
}
@keyframes nm-radar-bg {
  0%,100% { background-position: 0% 50%; }
  50%     { background-position: 100% 50%; }
}
```
Usados (todos com `background-size: 200%`/`300%` + a animação acima, em durações diferentes para evitar sincronia):
- `.nm-about`: 22s
- `.nm-diferenciais`: 20s (delay 1s)
- `.nm-depoimentos`: 26s (delay 4s)
- `.nm-cotacao`: 18s (delay 2s)
- `.nm-radar`: `nm-radar-bg` 18s, `background-size: 300% 300%`

### 7.5 Pulsos de CTA

- `nm-cta-pulse` (laranja, 2.8s) — `.nm-btn-primary`.
- `nm-radar-pulse` (verde WhatsApp, 2.8s) — `.nm-btn-radar`.
- `nm-fab-pulse` (verde WhatsApp, 3s) — `.nm-fab`.
Todos param (`animation: none`) no `:hover`.

### 7.6 Outras animações nomeadas

| Keyframe | Onde | Descrição |
|---|---|---|
| `nm-toast-in` | `.nm-toast` | entrada deslizando de baixo, 320ms |
| `nm-logo-letter` | `.nm-dif3-logo-svg` | "letras" da logo aparecem com bounce sutil, 0.65s, escalonadas |
| `nm-dif-float1` / `nm-dif-float2` | `.nm-dif3-orb-1`/`-2` | flutuação vertical orgânica, 4.5s/5.5s |
| `nm-dep-scroll` | `.nm-dep-track-*` | scroll vertical infinito (`translateY(-50%)`), 22s/28s/25s |

### 7.7 Hover micro-interações (resumo)

- Botões: `translateY(-2px)` + sombra mais forte.
- Cards (`.nm-feature`, `.nm-roteiro`, `.nm-dep-card`): `translateY(-4px/-5px)` + `box-shadow` maior.
- Links com seta (`.nm-link-arrow`, `.nm-btn .ico`): seta desliza (`translateX`).
- Foto "Sobre": rotação `-2.5deg → 0deg` + halo laranja.
- `.nm-bento-card`: zoom da imagem (1.055x) + overlay escurece + info sobe.

### 7.8 Acessibilidade de movimento

- `@media (prefers-reduced-motion: reduce)`: desativa `.reveal`, hero rise/kenburns (via wrap em `no-preference`), bento/modal transitions, depoimentos scroll, e a animação de letras do logo (paths ficam `opacity: 1` direto).

---

## 8. Iconografia

Sprite SVG inline no `<body>` (`<svg style="display:none" aria-hidden="true">`), todos `viewBox="0 0 24 24"`, referenciados via `<use href="#i-...">` dentro de `<svg class="ico">`.

| ID do símbolo | Estilo | Uso no site |
|---|---|---|
| `#i-arrow-right` | stroke, 2 | CTAs ("Montar minha viagem", "Continuar", nav, links de roteiro/step) |
| `#i-camera` | stroke, 2 | Instagram (footer social) |
| `#i-compass` | stroke, 2 | Etapa 2 do formulário ("A viagem") |
| `#i-heart` | stroke, 2 | Benefício hero "Atendimento humano de verdade"; Etapa 3 do formulário |
| `#i-mail` | stroke, 2 | E-mail (footer social) |
| `#i-map` | stroke, 2 | Benefício hero "Roteiros 100% personalizados"; Etapa 1 do formulário |
| `#i-message-circle` | stroke, 2 | Benefício hero "Suporte 24h"; WhatsApp (FAB, footer, submit do form) |
| `#i-phone-call` | stroke, 2 | definido no sprite (não identificado em uso visível no HTML revisado) |
| `#i-star` | **fill**, sem stroke | Estrelas de avaliação (`.nm-dep-stars`, 5×) |
| `#i-arrow-up` | stroke, 2 | FAB "voltar ao topo" |
| `#i-check` | stroke, 2.5 | Checks dos diferenciais (`.nm-dif3-check`) |

Classe base `.ico`: `display: inline-block; flex: none; width: 16px; height: 16px; vertical-align: middle`. Tamanhos são sobrescritos por contexto (ex.: `.nm-fab .ico` = 26px, `.nm-feature-icon .ico` = 22px, dots do form = 13px).

**Ícone de fechar do modal** (`.nm-bento-modal-close`) é um SVG inline próprio (X, `stroke-width: 2.5`), não parte do sprite.

**Emojis usados como ícones decorativos** (fora do sprite): ✈️ (Radar de Milhas, hero CTA secundário), 🗺️/🧳/💬 (títulos das etapas do form), 💑/👨‍👩‍👧/👯/🧍 (tipos de viagem), 🌊 (footer).

---

## 9. Imagens & mídia

### 9.1 Assets em `/assets`

| Arquivo | Uso |
|---|---|
| `logo-nortear.svg` | Logo principal — header (`.nm-logo-svg`, 44px) e footer (`.nm-footer-logo-svg`, 48px, `filter: brightness(0) invert(1)` para versão branca) |
| `photo-tropical-sunset.webp` | Poster/LCP do hero (`<img class="nm-hero-poster">`, `fetchpriority="high"`, preload), também usado no bento (Maldivas, Caribe) |
| `photo-journeys-vertical.webp` | Bento — Lisboa & Porto (`background-position: center 18%`) e Japão (`center 72%`) |
| `photo-airport-gate.webp` | Bento — Itália |
| `photo-socias.webp` | Foto das fundadoras na seção "Sobre" (`.nm-about-photo`, `aspect-ratio: 3/4`, `object-fit: cover`, `width=480 height=640`) |
| `hero-drone-sea.mp4` | Vídeo de fundo do hero (`<video data-src="...">`, carregado via lazy-load JS, `loop muted playsinline`) |

### 9.2 Tratamento de imagens

- **Hero**: `<img class="nm-hero-poster">` (LCP, eager, `fetchpriority="high"`, `decoding="async"`, `width="1600" height="893"`) sob o `<video class="nm-hero-bg" preload="none" poster="...">`. Ambos com `filter: brightness(0.82) saturate(1.05)` e `object-fit: cover`.
- **Bento**: `background-size: cover; background-position: center` (ou posições customizadas via `style="background-position:..."` para enquadrar o foco da foto), carregadas via `data-bg` + IntersectionObserver (lazy).
- **Foto "Sobre"**: `aspect-ratio: 3/4`, `object-fit: cover`, `border-radius: 16px`, `loading="lazy"`, rotacionada -2.5deg.
- Regra global: `img, video, svg { max-width: 100% }`.

### 9.3 Fontes

Self-hosted em `/fonts`, todas `.woff2`, subset latin. **Newsreader é variável** (`newsreader-var.woff2` roman + `newsreader-var-i.woff2` italic, eixos `opsz`+`wght`); Figtree (400/500/600/700) e Space Mono (400/700) são estáticas. Preload apenas das duas fontes do LCP (`newsreader-var.woff2`, `figtree-400.woff2`). CSS é 100% inlined no `<head>` via `build_inline_css.py` (não editar o bloco `BUILD:CSS-INLINE-*` manualmente — rodar `python build_inline_css.py` após editar qualquer `.css`). *(Os estáticos antigos de Playfair/DM Sans/DM Mono e as instâncias estáticas de Newsreader foram removidos — só restam os arquivos acima.)*

---

## 10. Voz & tom de conteúdo

Extraído de `content.json` e do texto real do `index.html`.

### 10.1 Princípios de copy observados

1. **"A gente" em vez de "Nós" / "a empresa"** — tom coloquial, pessoal, brasileiro-nordestino. Ex.: *"A gente não vende pacote. A gente cuida do seu sonho do começo ao fim."*
2. **Reframe explícito "não X, mas Y"** — usado em headlines e diferenciais:
   - *"A gente não vende pacote ([prontos]). A gente cuida do seu sonho..."*
   - *"A primeira pergunta não é 'qual o orçamento' — é 'como você viaja?'"*
   - *"A gente compete em **presença**, não em **preço**."*
   - *"Pra inspirar — não pra escolher."* (roteiros)
3. **Itálico para confidência/intimidade** — frases-chave em `<em>`, estilizadas em Newsreader italic com cor de destaque (laranja `--laranja-ambar` sobre fundo escuro, `--primary` sobre fundo claro). Ex.: *"nunca pararam de **nortear o mundo**"*, *"A gente tá pronta."*, *"Nortear é **cuidar**... e começa a só **viver**."*
4. **Prova social hiper-específica** — depoimentos sempre com nome + destino + mês/ano (ex.: "Mariana & Thiago · Paris, França · Jun/25"), nunca genéricos.
5. **Benefício > feature, sempre amarrado a um medo real do viajante**: bagagem perdida, primeira viagem internacional com filhos, medo de gastar mais do que cabe no bolso, grupo de amigos brigando por logística, avó que quer viajar antes dos 80.
6. **Suporte 24h como pilar central**, repetido em hero, diferenciais, processo (etapa 3) e FAQ — sempre como "alguém do seu lado", não "central de atendimento".
7. **Identidade regional como ativo, não limitação**: "potiguares", "Nordeste, Brasil", "Feito com cuidado, no Nordeste 🌊" — mas com a ressalva de que atendem o Brasil inteiro, 100% online.
8. **Emojis funcionais, não decorativos aleatórios**: ✈️ (viagem/radar), 🗺️🧳💬 (etapas do formulário, mapeiam ao conteúdo de cada etapa), 💑👨‍👩‍👧👯🧍 (tipos de viagem no form), 🌊 (assinatura regional do footer).
9. **CTAs sempre orientados a ação pessoal**, nunca genéricos: "Montar minha viagem", "Falar com a gente", "Quero minha cotação", "Quero um roteiro só meu", "Começa a sua agora", "Entrar no Radar de Milhas".
10. **Transparência de preço como argumento de venda**: "Não existe preço de tabela porque não existe viagem de tabela" (FAQ); "Preço transparente e justo. Sem taxas escondidas, sem surpresa no cartão" (diferencial).
11. **Microcopy de confiança no formulário**: "Leva menos de 2 minutos. Nossa consultora entra em contato em até 2 horas via WhatsApp."

### 10.2 Eyebrows / labels (todos mono, uppercase, `--accent`)

- "Agência de viagem · desde 2021 · Nordeste, Brasil" (hero)
- "Quem vai cuidar de você" (sobre)
- "Por que a Nortear" (diferenciais)
- "Como a gente trabalha" (processo)
- "Roteiros recentes" (roteiros)
- "O que dizem por aí" (depoimentos)
- "Solicitar cotação" (formulário)
- "O nosso propósito" (princípio)

### 10.3 FAQ (presente em `content.json`, sem seção visível correspondente no HTML/CSS revisados — **não definido no CSS/HTML como componente**)

O `content.json` contém 6 perguntas/respostas (`faq[]`) cobrindo: como funciona o atendimento, se cobram pela cotação, quanto custa viajar, o que acontece em caso de imprevisto, se atendem fora do RN, e como começar. O tom segue os mesmos princípios do item 10.1 (reframe "não X, é Y", suporte 24h, preço sem tabela, "a gente é potiguar de coração, mas atende o Brasil inteiro"). Como não há marcação `.nm-faq`/accordion no CSS nem seção correspondente no `index.html` analisado, este conteúdo parece reservado para uso futuro (ex.: nova seção FAQ) — qualquer componente de FAQ a ser criado deve seguir os padrões de `.nm-dif3-item` (check + texto) ou um padrão de accordion ainda **não definido no CSS**.

### 10.4 Princípio-mestre da marca

> "Nortear é *cuidar*: a viagem começa quando você para de se preocupar e começa a só *viver*."

Esta frase (`principio.texto`) funciona como a tese central de toda a comunicação — todo outro texto da marca (diferenciais, processo, depoimentos) é uma prova ou ilustração dela.
