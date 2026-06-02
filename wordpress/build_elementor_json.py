# -*- coding: utf-8 -*-
"""
Gera um template de PÁGINA do Elementor (.json) reproduzindo a landing
Nortear Mundo, para importar no WordPress (tema Hello Elementor + Elementor Pro).
Saída: nortear-mundo-elementor.json
"""
import json, secrets

# ---- paleta da marca ----
NAVY_DEEP="#0D3B6E"; NAVY="#1A5FA8"; ACCENT="#F47C20"; AMBER="#FAA95A"
SAND="#FAFAF8"; CARD_SOFT="#F2F1EF"; BORDER="#E7E5E1"; TEXT="#1C1916"
MUTED="#6B6560"; TINT="#EBF3FB"; WHITE="#FFFFFF"
PLAY="Playfair Display"; SANS="DM Sans"; MONO="DM Mono"

WA = {"url":"https://wa.me/5584994055713?text=Oi%2C%20vim%20pelo%20site%20e%20quero%20fazer%20uma%20cota%C3%A7%C3%A3o!",
      "is_external":"on","nofollow":"","custom_attributes":""}

def uid(): return secrets.token_hex(4)
def sz(size, unit="px"): return {"unit":unit,"size":size,"sizes":[]}
def dims(t,r,b,l,unit="px",linked=False):
    return {"unit":unit,"top":str(t),"right":str(r),"bottom":str(b),"left":str(l),"isLinked":linked}

def W(wtype, settings):
    return {"id":uid(),"settings":settings,"elements":[],"isInner":False,
            "widgetType":wtype,"elType":"widget"}
def COL(settings, elements, inner=False):
    return {"id":uid(),"settings":settings,"elements":elements,"isInner":inner,"elType":"column"}
def SEC(settings, elements, inner=False):
    return {"id":uid(),"settings":settings,"elements":elements,"isInner":inner,"elType":"section"}

def anim(name, delay=0):
    s={"_animation":name}
    if delay: s["_animation_delay"]=delay
    return s

def fa(value, lib="fa-solid"):
    return {"value":value,"library":lib}

# ---------- builders de widget ----------
def heading(title, *, size_d, size_t=None, size_m=None, weight="700", color=NAVY_DEEP,
            font=PLAY, lh=1.1, ls=-0.015, align=None, css=None, extra=None, tag="h2",
            animation=None, delay=0):
    s={"title":title,"header_size":tag,
       "title_color":color,
       "typography_typography":"custom","typography_font_family":font,
       "typography_font_weight":weight,
       "typography_font_size":sz(size_d),
       "typography_line_height":sz(lh,"em"),
       "typography_letter_spacing":sz(ls,"em")}
    if size_t is not None: s["typography_font_size_tablet"]=sz(size_t)
    if size_m is not None: s["typography_font_size_mobile"]=sz(size_m)
    if align:
        s["align"]=align; s["align_tablet"]=align.get("t") if isinstance(align,dict) else align
    if css: s["_css_classes"]=css
    if animation: s.update(anim(animation,delay))
    if extra: s.update(extra)
    return W("heading", s)

def text_editor(html, *, size_d=16, size_m=None, color=MUTED, font=SANS, lh=1.65,
                weight="400", align=None, animation=None, delay=0, extra=None):
    s={"editor":f"<p>{html}</p>",
       "text_color":color,
       "typography_typography":"custom","typography_font_family":font,
       "typography_font_weight":weight,"typography_font_size":sz(size_d),
       "typography_line_height":sz(lh,"em")}
    if size_m is not None: s["typography_font_size_mobile"]=sz(size_m)
    if align: s["align"]=align
    if animation: s.update(anim(animation,delay))
    if extra: s.update(extra)
    return W("text-editor", s)

def button(text, *, link=WA, bg=ACCENT, color=WHITE, align="left", size="md",
           ghost=False, animation=None, delay=0, css=None, full=False):
    s={"text":text,"link":dict(link),"align":align,"size":size,
       "typography_typography":"custom","typography_font_family":SANS,
       "typography_font_weight":"600","typography_font_size":sz(15),
       "border_radius":dims(8,8,8,8,linked=True),
       "text_padding":dims(14,26,14,26),
       "button_text_color":color}
    if ghost:
        s.update({"background_background":"classic","button_background_color":"rgba(0,0,0,0)",
                  "border_border":"solid","border_width":dims(1.5,1.5,1.5,1.5,linked=True),
                  "border_color":color,"button_text_color":color})
    else:
        s.update({"background_background":"classic","button_background_color":bg,
                  "button_box_shadow_box_shadow_type":"yes",
                  "button_box_shadow_box_shadow":{"horizontal":0,"vertical":4,"blur":14,"spread":0,
                                                  "color":"rgba(13,59,110,0.18)"}})
    if full:
        s["button_width_tablet"]="100%"
    if css: s["_css_classes"]=css
    if animation: s.update(anim(animation,delay))
    return W("button", s)

def icon_box(icon, title, body, *, animation=None, delay=0):
    return W("icon-box", {
        "selected_icon":icon,"title_text":title,"description_text":body,
        "position":"top","text_align":"left",
        "title_color":NAVY_DEEP,"description_color":MUTED,
        "title_typography_typography":"custom","title_typography_font_family":PLAY,
        "title_typography_font_weight":"700","title_typography_font_size":sz(19),
        "title_typography_line_height":sz(1.25,"em"),
        "description_typography_typography":"custom","description_typography_font_family":SANS,
        "description_typography_font_size":sz(14),"description_typography_line_height":sz(1.6,"em"),
        "primary_color":NAVY_DEEP,
        "icon_size":sz(24),
        "icon_padding":sz(12),
        "icon_space":sz(16),
        # card look
        "_background_background":"classic","_background_color":WHITE,
        "_border_border":"solid","_border_width":dims(1,1,1,1,linked=True),"_border_color":BORDER,
        "_border_radius":dims(12,12,12,12,linked=True),
        "_padding":dims(28,24,26,24),
        "_box_shadow_box_shadow_type":"yes",
        "_box_shadow_box_shadow":{"horizontal":0,"vertical":8,"blur":24,"spread":0,"color":"rgba(13,59,110,0.06)"},
        **(anim(animation,delay) if animation else {})
    })

def icon_list(items, *, color=WHITE, icon_color=AMBER, inline=False, size=14, space=12, align=None):
    lst=[{"text":t,"selected_icon":ic,"_id":uid()} for (t,ic) in items]
    s={"icon_list":lst,"view":"inline" if inline else "traditional",
       "icon_color":icon_color,"text_color":color,
       "icon_typography_typography":"custom","icon_typography_font_family":SANS,
       "icon_typography_font_size":sz(size),
       "space_between":sz(space),"icon_size":sz(18)}
    if align: s["align"]=align
    return W("icon-list", s)

def col(width, elements, *, pad=None, inline=None, valign=None, extra=None, inner=False):
    s={"_column_size":width,"_inline_size":width}
    if inline is not None: s["_inline_size"]=inline
    if pad: s["padding"]=pad
    if valign: s["content_position"]=valign
    if extra: s.update(extra)
    return COL(s, elements, inner=inner)

GUT = dims(0,10,0,10,unit="%")   # 10% lateral

def full_section(elements, *, vpad=(96,96), bg=None, bgcolor=None, title="",
                 extra=None, content_position=None):
    s={"layout":"full_width","padding":dims(vpad[0],0,vpad[1],0),
       "padding_mobile":dims(int(vpad[0]*0.62),0,int(vpad[1]*0.62),0),"_title":title}
    if bg=="classic": s.update({"background_background":"classic","background_color":bgcolor})
    if content_position: s["content_position"]=content_position
    if extra: s.update(extra)
    # single column with 10% gutter holds everything
    return SEC(s, [col(100, elements, pad=GUT)])

def inner_row(cols_elements, *, widths, gap="20", valign=None, structure=None):
    cols=[]
    for w,els in zip(widths, cols_elements):
        cols.append(col(w, els, valign=valign, inner=True))
    s={"gap":"custom","gap_columns_custom":sz(int(gap)),"gap_columns_custom_mobile":sz(16)}
    if structure: s["structure"]=structure
    return SEC(s, cols, inner=True)

content=[]

# ============================ 1. HERO ============================
hero_video_extra={
    "height":"min-height","custom_height":sz(720),"custom_height_mobile":sz(560),
    "content_position":"bottom",
    "background_background":"video",
    "background_video_link":"/wp-content/uploads/nortear/hero-drone-sea.mp4",
    "background_play_on_mobile":"yes","background_play_once":"",
    "background_image":{"url":"/wp-content/uploads/nortear/photo-tropical-sunset.webp","id":"","source":"library","alt":""},
    "background_overlay_background":"gradient",
    "background_overlay_color":"#0D3B6E","background_overlay_color_b":"#0D3B6E",
    "background_overlay_color_stop":sz(0,"%"),"background_overlay_color_b_stop":sz(100,"%"),
    "background_overlay_gradient_angle":sz(180,"deg"),
    "background_overlay_opacity":sz(0.62),
}
hero_inner=[
    heading("AGÊNCIA DE VIAGEM · DESDE 2021", size_d=11, weight="500", color=AMBER, font=MONO,
            lh=1, ls=0.18, tag="div", extra={"align":"left","align_mobile":"center"}),
    heading("Descubra o mundo com quem cuida de você.", size_d=64, size_t=48, size_m=34,
            weight="900", color=WHITE, lh=0.98, ls=-0.025, tag="h1",
            extra={"align":"left","align_mobile":"center"}, animation="fadeInUp", delay=100),
    text_editor("A gente não vende pacote. <i>A gente cuida do seu sonho do começo ao fim</i> — e fica do seu lado se a mala sumir no meio do caminho.",
                size_d=20, size_m=16, color="rgba(255,255,255,0.88)", font=PLAY, lh=1.5, weight="400",
                align="left", animation="fadeInUp", delay=250,
                extra={"align_mobile":"center","_css_classes":"nm-herosub"}),
]
hero_cta=inner_row([
    [button("Me conta seu destino", animation="fadeInUp", delay=400, full=True)],
    [button("Como a gente trabalha", link={"url":"#processo","is_external":"","nofollow":""},
            ghost=True, color=WHITE, animation="fadeInUp", delay=480, full=True)],
], widths=[50,50], gap="14")
hero_stats=icon_list([
    ("Suporte 24h durante a viagem", fa("far fa-comment-dots","fa-regular")),
    ("Roteiros 100% personalizados", fa("fas fa-map-marked-alt")),
    ("Atendimento humano de verdade", fa("fas fa-heart")),
], inline=True, color="rgba(255,255,255,0.85)", icon_color=AMBER, size=13, space=28)
hero_stats.get("settings")["_css_classes"]="nm-herofoot"
hero_stats.get("settings")["_padding"]={"unit":"px","top":"26","right":"0","bottom":"0","left":"0","isLinked":False}
hero_stats.get("settings")["_border_border"]="solid"
hero_stats.get("settings")["_border_width"]=dims(1,0,0,0)
hero_stats.get("settings")["_border_color"]="rgba(255,255,255,0.15)"

content.append(SEC({**{"layout":"full_width","padding":dims(80,0,40,0),"_title":"HERO"}, **hero_video_extra},
                   [col(100, hero_inner + [hero_cta, hero_stats], pad=GUT, valign="bottom")]))

# ===================== 2. DIFERENCIAIS =====================
head_diff=[
    heading("01 · POR QUE A NORTEAR", size_d=11, weight="500", color=ACCENT, font=MONO, lh=1, ls=0.18,
            tag="div", extra={"align":"center"}),
    heading('A gente compete em <span class="nm-accent">presença</span>, não em preço.',
            size_d=48, size_t=38, size_m=28, weight="700", lh=1.05, extra={"align":"center"},
            animation="fadeInUp"),
    text_editor("A maioria das agências some depois da venda. A gente fica — e essa diferença muda tudo na hora que o imprevisto chega.",
                size_d=17, color=MUTED, align="center",
                extra={"_padding":dims(8,0,0,0),"_css_classes":"nm-lede"}),
]
cards=[
    icon_box(fa("fas fa-headset"),"Suporte 24h durante a viagem",
             "Não é marketing — é estrutura. Enquanto você está viajando, tem alguém da Nortear pronto pra resolver: extravio, voo cancelado, dúvida de última hora.",
             animation="fadeInUp", delay=0),
    icon_box(fa("fas fa-map-marked-alt"),"Roteiros com curadoria real",
             "Nenhum roteiro é copiado do anterior. Cada viagem é planejada a partir da conversa com você — o que gosta, como viaja, o que não pode faltar.",
             animation="fadeInUp", delay=120),
    icon_box(fa("fas fa-compass"),"Assessoria antes da venda",
             "Você não entra num funil pra ser convertida. Entra numa conversa pra ser entendida. A gente orienta antes de oferecer qualquer coisa.",
             animation="fadeInUp", delay=240),
    icon_box(fa("fas fa-heart"),"Presença pós-viagem",
             "A relação não termina no embarque. A gente acompanha, pergunta, e constrói um histórico pra que a próxima viagem seja ainda mais precisa.",
             animation="fadeInUp", delay=360),
]
diff_row=inner_row([[c] for c in cards], widths=[25,25,25,25], gap="20", valign="stretch", structure="40")
sec_diff=full_section([head_diff_wrap:=SEC({"gap":"no","padding":dims(0,0,46,0)},[col(100,head_diff,inner=True)],inner=True), diff_row],
                      bg="classic", bgcolor=SAND, title="DIFERENCIAIS",
                      extra={"_element_id":"sobre"})
content.append(sec_diff)

# ===================== 3. PROCESSO =====================
head_proc=[
    heading("02 · COMO A GENTE TRABALHA", size_d=11, weight="500", color=ACCENT, font=MONO, lh=1, ls=0.18,
            tag="div", extra={"align":"center"}),
    heading('Três passos. <span class="nm-accent">Zero pacote pronto.</span>',
            size_d=44, size_t=34, size_m=26, weight="700", lh=1.05, extra={"align":"center"},
            animation="fadeInUp"),
]
def step(n,title,body,delay):
    return [
        heading(n, size_d=56, weight="500", color=ACCENT, font=MONO, lh=1, ls=0, tag="div",
                extra={"_css_classes":"nm-stepnum"}),
        heading(title, size_d=26, size_m=22, weight="700", lh=1.1, tag="h3"),
        text_editor(body, size_d=14, color=MUTED, lh=1.65),
    ]
steps=inner_row([
    step("01","A conversa",'A primeira pergunta não é "qual o orçamento" — é "como você viaja?". Antes de qualquer pacote, a gente entende quem é você.',0),
    step("02","O roteiro","Curadoria real de destino, ritmo, hospedagem e experiências. Você lê, comenta, ajusta. A gente reescreve até estar certo.",120),
    step("03","A viagem","Você embarca com a Nortear no bolso. Qualquer imprevisto, qualquer hora — tem alguém da equipe disponível pra resolver.",240),
], widths=[33,34,33], gap="24", valign="stretch", structure="30")
# card look + animação por coluna
for i,c in enumerate(steps["elements"]):
    c["settings"].update({"_background_background":"classic","_background_color":WHITE,
        "_border_border":"solid","_border_width":dims(1,1,1,1,linked=True),"_border_color":BORDER,
        "_border_radius":dims(12,12,12,12,linked=True),"padding":dims(36,32,36,32),
        **anim("fadeInUp", i*120)})
sec_proc=full_section([SEC({"gap":"no","padding":dims(0,0,46,0)},[col(100,head_proc,inner=True)],inner=True), steps],
                      bg="classic", bgcolor=CARD_SOFT, title="PROCESSO",
                      extra={"_element_id":"processo"})
content.append(sec_proc)

# ===================== 4. ROTEIROS =====================
head_rot=[
    heading("03 · ALGUNS ROTEIROS RECENTES", size_d=11, weight="500", color=ACCENT, font=MONO, lh=1, ls=0.18,
            tag="div", extra={"align":"center"}),
    heading('Pra inspirar — <span class="nm-accent">não pra escolher.</span>',
            size_d=44, size_t=34, size_m=26, weight="700", lh=1.05, extra={"align":"center"}, animation="fadeInUp"),
    text_editor("Esses são alguns roteiros que a gente montou esse ano. O seu vai ser único, mas dá pra ter ideia do nosso estilo.",
                size_d=17, color=MUTED, align="center", extra={"_padding":dims(8,0,0,0)}),
]
def roteiro(img, badge, title, sub, body, price, delay):
    return [
        W("image",{"image":{"url":img,"id":"","source":"library","alt":title},"image_size":"large",
                   "_border_radius":dims(0,0,0,0)}),
        heading(badge, size_d=11, weight="500", color=WHITE, font=MONO, lh=1, ls=0.12, tag="div",
                extra={"_css_classes":"nm-badge","_background_background":"classic",
                       "_background_color":NAVY_DEEP,"_padding":dims(6,12,6,12),
                       "_border_radius":dims(999,999,999,999)}),
        heading(title, size_d=26, size_m=22, weight="700", lh=1.1, tag="h3"),
        text_editor(sub, size_d=14, color=MUTED, font=PLAY, lh=1.4, weight="400"),
        text_editor(body, size_d=14, color=TEXT, lh=1.6),
        heading(f'<span style="font-family:DM Mono;font-size:10px;letter-spacing:.12em;color:{ACCENT}">A PARTIR DE R$</span> {price} <span style="font-size:12px;color:{MUTED};font-family:DM Sans">/ pessoa</span>',
                size_d=28, weight="900", color=NAVY_DEEP, lh=1, tag="div"),
        button("Quero esse roteiro", animation=None),
    ]
rot_cards=[
    roteiro("/wp-content/uploads/nortear/photo-journeys-vertical.webp","EUROPA · 10 DIAS","Lisboa & Porto",
            "com a curadoria de quem já dormiu lá","Bairros que ninguém indica, restaurantes que ninguém posta, e uma noite de fado fora do circuito turístico.","8.490",0),
    roteiro("/wp-content/uploads/nortear/photo-tropical-sunset.webp","TROPICAL · 7 DIAS","Maldivas em ritmo lento",
            "sem voos curtos, sem agenda apertada","Uma ilha, sete dias, um único deck pro pôr do sol. Pra quem entende que viajar também é ficar.","14.900",120),
    roteiro("/wp-content/uploads/nortear/photo-airport-gate.webp","AVENTURA · 5 DIAS","Itália do norte ao sul",
            "roteiro relâmpago, do jeito certo","Milão, Florença e Roma em cinco dias sem virar uma maratona — porque a gente sabe onde cortar.","11.200",240),
]
rot_row=inner_row(rot_cards, widths=[33,34,33], gap="24", valign="stretch", structure="30")
for i,c in enumerate(rot_row["elements"]):
    c["settings"].update({"_background_background":"classic","_background_color":WHITE,
        "_border_border":"solid","_border_width":dims(1,1,1,1,linked=True),"_border_color":BORDER,
        "_border_radius":dims(14,14,14,14,linked=True),"padding":dims(0,0,24,0),
        "_css_classes":"nm-card","space_between_widgets":14, **anim("fadeInUp", i*120)})
sec_rot=full_section([SEC({"gap":"no","padding":dims(0,0,46,0)},[col(100,head_rot,inner=True)],inner=True), rot_row],
                     bg="classic", bgcolor=SAND, title="ROTEIROS", extra={"_element_id":"roteiros"})
content.append(sec_rot)

# ===================== 5. DEPOIMENTO =====================
quote=[
    heading("04 · O QUE SIGNIFICA \"SUPORTE DE VERDADE\"", size_d=11, weight="500", color=ACCENT, font=MONO,
            lh=1, ls=0.18, tag="div", extra={"align":"center","_padding":dims(0,0,40,0)}),
    heading('A bagagem da Julia sumiu em Frankfurt. <span class="nm-accent">Eram 23h de uma sexta-feira.</span> Em 40 minutos a gente tinha acionado a companhia, garantido kit de emergência e deixado ela seguindo o roteiro sem precisar cancelar nada.',
            size_d=30, size_m=22, weight="700", color=WHITE, lh=1.4, tag="div", animation="fadeInUp"),
    heading("CASO REAL · OUTUBRO 2024", size_d=11, weight="500", color=AMBER, font=MONO, lh=1.4, ls=0.18,
            tag="div", extra={"_padding":dims(24,0,0,0)}),
    text_editor("Cliente Nortear · primeira viagem à Europa", size_d=14, color="rgba(255,255,255,0.65)",
                font=SANS, lh=1.4, extra={"_css_classes":"nm-i"}),
]
quote_card=SEC({"gap":"no","background_background":"classic","background_color":NAVY_DEEP,
                "border_radius":dims(16,16,16,16,linked=True),"padding":dims(56,64,56,64),
                "padding_mobile":dims(38,24,38,24)},
               [col(100,[quote[1],quote[2],quote[3]],inner=True)], inner=True)
sec_quote=full_section([SEC({"gap":"no","padding":dims(0,0,0,0)},[col(100,[quote[0]],inner=True)],inner=True), quote_card],
                       bg="classic", bgcolor=SAND, title="DEPOIMENTO")
content.append(sec_quote)

# ===================== 6. PRINCÍPIO =====================
principle=[
    heading("O NOSSO PRINCÍPIO", size_d=11, weight="500", color=AMBER, font=MONO, lh=1, ls=0.18, tag="div",
            extra={"align":"center"}),
    heading('Nortear é <span class="nm-accent">cuidar</span>: a viagem começa quando o cliente para de se preocupar e começa a só viver.',
            size_d=40, size_m=26, weight="700", color=WHITE, lh=1.35, tag="div",
            extra={"align":"center","_padding":dims(16,0,32,0)}, animation="fadeInUp"),
    button("Começa a sua agora", align="center", size="lg", animation="fadeInUp", delay=120),
]
sec_prin=SEC({"layout":"full_width","padding":dims(120,0,120,0),"padding_mobile":dims(80,0,80,0),
              "background_background":"gradient","background_color":NAVY_DEEP,"background_color_b":NAVY,
              "background_gradient_angle":sz(145,"deg"),"_title":"PRINCÍPIO"},
             [col(100, principle, pad=GUT)])
content.append(sec_prin)

# ===================== 7. RODAPÉ =====================
brand_col=[
    heading("Nortear<br>Mundo", size_d=38, weight="700", color=WHITE, lh=0.95, ls=-0.02, tag="div"),
    text_editor("A gente cuida do seu sonho do começo ao fim.", size_d=18, color="rgba(255,255,255,0.7)",
                font=PLAY, lh=1.4, weight="400", extra={"_css_classes":"nm-i","_padding":dims(12,0,18,0)}),
    icon_list([("",fa("fab fa-instagram","fa-brands")),("",fa("fab fa-whatsapp","fa-brands")),("",fa("fas fa-envelope"))],
              inline=True, color=WHITE, icon_color=WHITE, space=14),
]
def fcol(title, links):
    els=[heading(title, size_d=11, weight="500", color=AMBER, font=MONO, lh=1, ls=0.18, tag="div",
                 extra={"_padding":dims(0,0,12,0)})]
    for t in links:
        els.append(text_editor(t, size_d=14, color="rgba(255,255,255,0.7)", lh=1.8,
                               extra={"_padding":dims(2,0,2,0)}))
    return els
foot_links=inner_row([
    fcol("NAVEGAR",["Roteiros","Como funciona","Sobre a gente","Diário"]),
    fcol("CONVERSAR",["WhatsApp","Instagram · @nortearmundo","oi@nortearmundo.com.br"]),
    fcol("ONDE ESTAMOS",["São Paulo · Brasil","Atendimento 24h durante viagens"]),
], widths=[33,34,33], gap="32")
foot_top=inner_row([brand_col,[foot_links]], widths=[35,65], gap="64", structure="20")
foot_bot=heading("© 2025 Nortear Mundo · CNPJ 00.000.000/0001-00     ·     Feito com cuidado, em São Paulo",
                 size_d=11, weight="400", color="rgba(255,255,255,0.4)", font=MONO, lh=1.6, ls=0.06,
                 tag="div", extra={"align":"center","_padding":dims(40,0,0,0),
                 "_border_border":"solid","_border_width":dims(1,0,0,0),"_border_color":"rgba(255,255,255,0.1)"})
sec_foot=SEC({"layout":"full_width","padding":dims(80,0,32,0),"background_background":"classic",
              "background_color":NAVY_DEEP,"_title":"RODAPÉ","_element_id":"contato"},
             [col(100,[foot_top, foot_bot], pad=GUT)])
content.append(sec_foot)

# ============================ CSS DA PÁGINA ============================
FONT_BASE="/wp-content/uploads/nortear/fonts"
faces=[("Playfair Display","normal",400,"playfair-400.woff2"),
       ("Playfair Display","italic",400,"playfair-400i.woff2"),
       ("Playfair Display","normal",700,"playfair-700.woff2"),
       ("Playfair Display","normal",900,"playfair-900.woff2"),
       ("DM Sans","normal",400,"dmsans-400.woff2"),("DM Sans","normal",500,"dmsans-500.woff2"),
       ("DM Sans","normal",600,"dmsans-600.woff2"),("DM Sans","normal",700,"dmsans-700.woff2"),
       ("DM Mono","normal",400,"dmmono-400.woff2"),("DM Mono","normal",500,"dmmono-500.woff2")]
css_faces="\n".join(
    f"@font-face{{font-family:'{f}';font-style:{st};font-weight:{w};font-display:swap;src:url('{FONT_BASE}/{file}') format('woff2');}}"
    for f,st,w,file in faces)
custom_css = css_faces + """
.nm-accent{color:#F47C20;font-style:italic;font-weight:400;}
.nm-i, .nm-i p{font-style:italic;}
.nm-herosub{border-left:3px solid #F47C20;padding-left:20px;max-width:560px;}
.nm-stepnum{opacity:.35;}
.nm-badge{display:inline-block;text-transform:uppercase;position:absolute;top:16px;left:16px;z-index:2;}
.nm-card{position:relative;overflow:hidden;}
.nm-card .elementor-widget-image img{height:240px;object-fit:cover;width:100%;display:block;}
.nm-card .elementor-widget{padding-left:24px;padding-right:24px;}
.nm-card .elementor-widget-image{padding-left:0;padding-right:0;}
@media(max-width:767px){
  .nm-herosub{border-left:none;border-top:3px solid #F47C20;padding-left:0;padding-top:16px;text-align:center;max-width:none;}
  .nm-herofoot{justify-content:center;}
}
"""

page = {
  "content": content,
  "page_settings": {
    "background_background":"classic","background_color":SAND,
    "custom_css": custom_css.strip()
  },
  "version":"0.4",
  "title":"Nortear Mundo — Home",
  "type":"page"
}

out="nortear-mundo-elementor.json"
with open(out,"w",encoding="utf-8") as fh:
    json.dump(page, fh, ensure_ascii=False)
print("OK ->", out)
print("sections:", len(content))
# sanity: count widgets
def count(el,acc):
    if el.get("elType")=="widget": acc[0]+=1
    for c in el.get("elements",[]): count(c,acc)
acc=[0]
for s in content: count(s,acc)
print("widgets:", acc[0])
