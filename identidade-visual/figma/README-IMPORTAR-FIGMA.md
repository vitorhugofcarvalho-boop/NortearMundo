# Cadastrar o Design System Nortear no Figma

> O MCP do Figma bateu no limite de chamadas do plano **Starter** (cadastrar variáveis/estilos
> nativamente exige dezenas a centenas de chamadas — inviável nesse plano). A rota abaixo coloca
> **o design system inteiro dentro do Figma como variáveis e estilos reais**, via plugin gratuito,
> sem depender do MCP.

## O que este arquivo gera no Figma
- **1 coleção de variáveis de cor com 4 modes** (Horizonte · Pôr do Sol Tropical · Primeira Classe · Bússola & Mapa) — troca a marca inteira num clique.
- **Variáveis primitivas** (50 cores nomeadas) + **semânticas** (bg, surface, text, primary, accent, border, whatsapp, etc.) aliasadas aos primitivos.
- **Variáveis de espaçamento** (escala 4pt: 0→128), **raios** (xs→pill) e **tipografia** (famílias, pesos, tamanhos, entrelinhas, tracking).
- **9 estilos de texto** (display, h1, h2, h3, body-lg, body, caption, eyebrow, cta) em Newsreader / Figtree / Space Mono.
- **4 estilos de efeito** (sombras azuladas xs/sm/md/lg).

## Passo a passo (≈3 min)

1. No arquivo Figma **Nortear Mundo**, abra **Plugins → procure "Tokens Studio for Figma"** e instale (gratuito).
2. Abra o plugin. Na primeira vez ele pergunta o storage — escolha **Local document**.
3. No menu do plugin (canto superior) → **Tools → Import** (ou o ícone de import) → **Import from file / Paste** e cole/abra o conteúdo de `nortear-tokens.json`.
   - Se pedir, confirme substituir os sets vazios.
4. Vá em **Settings** e ative **"Base Font Size = 16"** (deixa os `rem`/px corretos) — opcional.
5. Aba **Themes** → você verá o grupo **Nortear** com os 4 temas. Clique no ⚙️/**"Manage themes"** e confirme os 4.
6. Clique em **"Export"** (ou o botão de exportar para Figma) → **Export to Figma → Variables + Styles**. Marque:
   - **Create variables** (gera a coleção com os 4 modes)
   - **Create styles** → **Text styles** e **Effect styles**.
7. Confirme. Pronto: abra o painel de **Variables** (ícone no canvas) e o painel de **Local styles** — o sistema está cadastrado.

## Conferir
- **Variables**: deve existir a coleção com modes `Horizonte / Pôr do Sol Tropical / Primeira Classe / Bússola & Mapa`. Troque o mode num frame e veja as cores mudarem.
- **Text styles**: `tipografia/display`, `tipografia/body`, etc. (verifique que as fontes **Newsreader**, **Figtree** e **Space Mono** estão instaladas na sua conta Figma — são gratuitas no Google Fonts; o Figma já as tem nativas). Newsreader display = peso 600 (Semibold); Space Mono só tem 400/700, então o eyebrow usa 400.
- **Effect styles**: `elevacao/md`, `elevacao/lg`, etc.

## Tema recomendado
Deixe **Pôr do Sol Tropical** como mode padrão dos frames de produção (é a direção escolhida:
azul-marca + Coral Poente + areia quente). Os outros 3 ficam disponíveis para teste/campanha.

## Quando fizer upgrade do plano Figma
Se assinar um plano com MCP liberado, me avise: eu construo nativamente também os **componentes**
(Botão, Eyebrow, Card, Campo de formulário, Selo Radar de Milhas) com variantes e bindings de
variável, montando a biblioteca completa por cima destes tokens — fechando o design system.
