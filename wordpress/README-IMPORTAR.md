# Nortear Mundo — Importar no WordPress (Hello Elementor + Elementor Pro)

Página inteira montada como **template do Elementor** em `.JSON`, 100% editável no Elementor Pro.

## Pré-requisitos

- Tema **Hello Elementor** (ativo)
- **Elementor** + **Elementor Pro** (o Custom CSS da página e o vídeo de fundo do hero exigem o Pro)
- Acesso ao servidor (FTP/SFTP ou Gerenciador de Arquivos da hospedagem) para subir fontes e mídia

## Passo 1 — Subir as fontes e mídias (ANTES de importar)

O template aponta para caminhos fixos. Suba a pasta `uploads-nortear/` para dentro de
`/wp-content/uploads/` e **renomeie para `nortear`**. O resultado final deve ser exatamente:

```
/wp-content/uploads/nortear/
├── hero-drone-sea.mp4
├── photo-tropical-sunset.webp      (poster do vídeo + fallback)
├── photo-journeys-vertical.webp
├── photo-airport-gate.webp
└── fonts/
    ├── playfair-400.woff2
    ├── playfair-400i.woff2
    ├── playfair-700.woff2
    ├── playfair-900.woff2
    ├── dmsans-400.woff2
    ├── dmsans-500.woff2
    ├── dmsans-600.woff2
    ├── dmsans-700.woff2
    ├── dmmono-400.woff2
    └── dmmono-500.woff2
```

> Os caminhos `/wp-content/uploads/nortear/...` estão escritos dentro do JSON (fontes via
> `@font-face` no Custom CSS, vídeo do hero e poster). Se mudar o nome da pasta, o vídeo e as
> fontes quebram. Mantenha **`nortear`** exatamente assim (minúsculo).

## Passo 2 — Importar o template

1. No painel do WordPress: **Elementor → Modelos (Templates) → Importar Modelos**.
2. Selecione **`nortear-mundo-elementor.json`**.
3. O template aparece na biblioteca como **"Nortear Mundo — Home"**.

## Passo 3 — Criar a página

1. **Páginas → Adicionar nova** → dê o nome (ex.: "Home").
2. Em **Atributos da página → Modelo**, escolha **Elementor Full Width** (ou Canvas, se não quiser
   cabeçalho/rodapé do tema).
3. Clique em **Editar com Elementor**.
4. Na área de trabalho, clique no ícone de pasta (**Adicionar Modelo**) → aba **Meus Modelos** →
   insira **"Nortear Mundo — Home"**.
5. **Publicar.** Se for a home do site: **Configurações → Leitura → Página inicial estática → Home**.

## Passo 4 — Reapontar as mídias na biblioteca (recomendado)

O vídeo, o poster e as 3 fotos já carregam pelos caminhos fixos, mas para que fiquem **editáveis
pela interface** (trocar imagem com 1 clique), suba também essas mídias pela **Biblioteca de Mídia**
do WordPress e reselecione em cada widget:

- **Hero (seção 1):** editar a seção → aba **Estilo → Fundo → Vídeo**. Confirme o link do vídeo e a
  imagem de fallback/poster.
- **Roteiros (seção Roteiros):** os 3 cards usam widgets de **Imagem** — clique em cada um e
  reselecione pela biblioteca se quiser gerenciá-las pelo WP.

## O que já vem configurado

- **Animações de entrada por scroll** — cada bloco entra com fade/slide ao rolar (campo `_animation`
  nativo do Elementor; some/ajuste em **Avançado → Movimento** de cada elemento).
- **Vídeo do hero em loop**, com play no mobile e poster `.webp` enquanto carrega.
- **Botões de WhatsApp** já com o link `wa.me/5584994055713` e a mensagem automática
  *"Oi, vim pelo site e quero fazer uma cotação!"* (5 botões/CTAs).
- **Tipografia local** (Playfair Display, DM Sans, DM Mono) via `@font-face` no Custom CSS da página
  — zero requisição ao Google Fonts.
- **Layout fluido**: todas as seções em largura total com **10% de padding lateral** e tipografia
  responsiva (`clamp`) para desktop / notebook / tablet / mobile.

## Ajustes finos depois de importar

| Quero mudar… | Onde |
|---|---|
| Telefone/mensagem do WhatsApp | Cada botão → **Link** (`wa.me/...?text=...`) |
| Vídeo do hero | Seção Hero → **Estilo → Fundo → Vídeo** |
| Cores da marca | **Avançado → CSS Personalizado** da página, ou direto no widget |
| Textos | Clique no texto e edite inline |
| Fontes | Já locais; para trocar, suba o `.woff2` e ajuste o `@font-face` no Custom CSS |

## Observações de performance

- Mídia já otimizada: imagens em **WebP**, fontes em **WOFF2** (~307 KB no total).
- O vídeo (`hero-drone-sea.mp4`, **1,69 MB**) já foi recomprimido em H.264 CRF 26 — redução de
  **67%** sobre o original (5,12 MB) com perda imperceptível (SSIM 0,968 / PSNR 41 dB, ainda mais
  invisível atrás do overlay escuro). Carrega como fundo com poster, sem travar o First Contentful
  Paint.
- Recomendado ativar cache/CDN da hospedagem para os arquivos em `/uploads/nortear/`.
