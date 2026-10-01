# -*- coding: utf-8 -*-
"""Cyber Render Instagram content pack: single source of truth.

Edit this file, then run `python3 scripts/build.py` to regenerate
instagram/03-postlar.md, instagram/05-kontent-teqvimi.md and instagram/board.html.

Placeholders in [square brackets] must be confirmed against the website before posting.
"""

# Brand look blocks appended to Google Flow prompts (rule F3).
LOOK = (
    "Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft "
    "pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural "
    "visualization look, physically based global illumination, crisp detail, subtle film grain, calm and "
    "precise mood. No text, no letters, no logos, no watermarks."
)
LOOK_NIGHT = (
    "Moody, tense, cinematic, shallow depth of field, subtle film grain; deep charcoal tones with one faint "
    "pale-mint (#DDFFD4) light. No readable text on any screen, no logos, no watermarks."
)
LOOK_ABSTRACT = (
    "Palette strictly deep charcoal (#2A2A2A) and pale mint green (#DDFFD4) with soft neutral highlights. "
    "Clean premium 3D render look, physically based lighting, crisp detail. No text, no letters, no logos, "
    "no watermarks."
)
LOOK_CLAY = (
    "3D clay render style: the matte white faceless clay character, soft ambient occlusion, clean studio "
    "lighting, deep charcoal (#2A2A2A) and pale mint (#DDFFD4) environment. Portrait composition. No text, "
    "no letters, no logos, no watermarks."
)

GIL_REF = (
    "Character reference sheet: 'Gil', a faceless matte white clay mannequin figure, smooth simplified human "
    "form exactly like an untextured 3D clay render, soft ambient occlusion, friendly proportions with a "
    "slightly large round head, no facial features at all, no clothing. Shown standing in a neutral pose, "
    "front view and three-quarter view side by side, on a plain pale-mint (#DDFFD4) background, soft even "
    "studio light. No text, no letters, no logos."
)

START_DATE = "2026-10-05"  # first Monday after the pack was written
POST_TIME = "20:00"       # Baku time; confirm with Instagram Insights after 2 weeks

POSTS = [
    # ------------------------------------------------------------------ 1
    {
        "id": "P10",
        "order": 1,
        "title": "Sən təsəvvür et. Biz hesablayaq.",
        "kind": "Reel",
        "format": "Reel · 3 klip + son kadr · ~26 san · 9:16",
        "segment": ["Hamısı"],
        "pillar": "Brend",
        "tone": "D",
        "triggers": ["P6"],
        "hook": "Hər layihə bir işıqla başlayır.",
        "idea": (
            "Yeni vizual kimliyin təqdimatı. Qaranlıqda nanə işıq xətti yanır, beton qalereyada ağ gil "
            "maket görünür, maket real materiallara çevrilir. Clay → Final keçidi brendin vədidir: "
            "ideyanı sən gətirirsən, ağır hesablamanı biz edirik."
        ),
        "ingredients": [
            {
                "name": "Gil maket (B və C klipləri üçün)",
                "prompt": (
                    "Portrait composition. A small matte white clay architectural model of a modern two-storey "
                    "house with a cantilevered roof stands on a raw charcoal concrete plinth inside a dark "
                    "brutalist gallery. A sharp geometric beam of pale-mint daylight falls on it from an angular "
                    "skylight. Product-photography framing, 50mm. " + LOOK
                ),
            }
        ],
        "shots": [
            {
                "label": "Klip A · 0–8 san",
                "mode": "Text to Video",
                "prompt": (
                    "Vertical 9:16. Extreme macro close-up in near darkness: a thin pale-mint-green LED light line "
                    "slowly ignites along the sharp chamfered 45-degree edge of a charcoal concrete slab, revealing "
                    "fine concrete pores and floating dust particles. Slow lateral camera slide from left to right, "
                    "100mm macro lens, very shallow depth of field. Audio: deep low electrical hum, a crisp soft "
                    "click as the light ignites, airy room tone. " + LOOK
                ),
                "overlay": "Hər layihə bir ideya ilə başlayır.",
            },
            {
                "label": "Klip B · 8–16 san",
                "mode": "Ingredients to Video (Gil maket)",
                "prompt": (
                    "Vertical 9:16. Interior of a minimalist brutalist gallery with raw charcoal concrete walls; a "
                    "single angular skylight cut at 45 degrees lets a sharp geometric beam of pale-mint daylight fall "
                    "across the polished concrete floor. In the beam stands the small matte white clay architectural "
                    "model on its concrete plinth. Slow crane-up camera move, 24mm lens, symmetrical composition. "
                    "Audio: reverberant quiet room tone, distant soft footsteps, a slowly swelling ambient synth pad. "
                    + LOOK
                ),
                "overlay": "Sonra gecələr gəlir: test, düzəliş, yenə render…",
            },
            {
                "label": "Klip C · 16–24 san",
                "mode": "Ingredients to Video (Gil maket)",
                "prompt": (
                    "Vertical 9:16. Close orbit around the small white clay architectural model on the concrete "
                    "plinth. As the camera orbits 90 degrees, the matte clay surfaces transform into real materials "
                    "sweeping across the model: clear glass, light oak cladding, dark charcoal stone. Tiny warm "
                    "lights switch on inside the rooms and one thin pale-mint light line glows under the roof. "
                    "Smooth, precise, satisfying. Audio: rising synth, a subtle digital shimmer as materials appear, "
                    "resolving on a clean warm chord. " + LOOK
                ),
                "overlay": "Sən təsəvvür et. Biz hesablayaq.",
            },
            {
                "label": "Son kadr · 24–26 san",
                "mode": "CapCut / Canva (Flow yox)",
                "prompt": "",
                "overlay": "Mint fon · loqo · “Render gücü: dizaynerlər, memarlar, animatorlar üçün” · Link bioda",
            },
        ],
        "caption": (
            "Hər layihə bir ideya ilə başlayır. Sonra gecələr gəlir.\n"
            "Test. Düzəliş. Yenə render. Yenə gözləmək.\n\n"
            "Biz həmin gecələri öz üzərimizə götürürük.\n"
            "Sən dizayn et, rakursu seç, işığı qur. Ağır hesablamanı Cyber Render etsin.\n\n"
            "Yeni görünüşümüz də bu fikirdən gəlir: qaranlıqda bir nanə işığı. Səhnən hazır olanda yanan işıq.\n\n"
            "👉 Necə işlədiyini görmək üçün profili izlə. Link bioda."
        ),
        "cta": "Profili izlə · Link bioda (yumşaq)",
        "hashtags": "#cyberrender #archviz #3dvisualization #memarlıq #interyerdizayn #baku #rendering",
        "edit": [
            "Musiqi: ambient/elektronik, lisenziyalı. Kəsiklər vuruşa düşür.",
            "A ilə B arasında 0.3 san qara kadr.",
            "Mətn Tektur ilə, kadrın yuxarı 1/3-ində (V7).",
        ],
        "verify": ["Son kadrdakı brend təsviri saytdakı ifadə ilə üst-üstə düşsün."],
    },
    # ------------------------------------------------------------------ 2
    {
        "id": "P04",
        "order": 2,
        "title": "Sahən hansıdır? Proqramını tap",
        "kind": "Karusel",
        "format": "Karusel · 7 slayd · 4:5 (1080×1350)",
        "segment": ["Hamısı"],
        "pillar": "Proqramlar",
        "tone": "M",
        "triggers": ["P3", "P7"],
        "hook": "Sənin sahən hansıdır? Proqramını tap →",
        "idea": (
            "Hər sahənin gündəlik proqram dəsti. Auditoriya özünü tapır, şərhə proqramını yazır "
            "(kiçik öhdəlik). Şərhlər bizə real tələbatı göstərir. Növbəti təhsil postunun (P07) mövzusu da "
            "buradan seçilir."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Slayd 1 · Hook",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Overhead flat-lay on a charcoal concrete surface, arranged in a precise "
                    "grid: a white clay architectural model, interior material swatches (light oak, travertine, "
                    "pale-mint velvet), a small product prototype in brushed metal, and a matte white clay character "
                    "maquette mid-pose. Soft-box top light, one thin pale-mint light strip along the top edge of the "
                    "frame, generous empty space in the upper third for a headline. " + LOOK
                ),
                "overlay": "SƏNİN SAHƏN HANSIDIR? Proqramını tap →",
            },
            {
                "label": "Slayd 2 · Memarlıq",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Photorealistic architectural exterior visualization: a modern residential "
                    "building with a charcoal basalt facade and vertical light-oak fins on a hillside above the "
                    "Caspian Sea at blue hour, warm interior lights, a thin pale-mint LED line along the roof edge. "
                    "Eye-level, two-point perspective, 24mm, vertical lines perfectly straight. Lower half of the "
                    "frame darker to hold text. " + LOOK
                ),
                "overlay": "MEMARLIQ\nRevit · ArchiCAD · SketchUp · Rhino\n→ 3ds Max · Corona · V-Ray · Lumion · Twinmotion · Enscape · D5",
            },
            {
                "label": "Slayd 3 · İnteryer",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Photorealistic interior visualization of a calm bedroom in a modern Baku "
                    "apartment: charcoal limewash walls, pale-mint linen bedding, light oak floor and headboard, "
                    "travertine bedside table, soft morning light through sheer curtains, a thin pale-mint LED cove "
                    "light. Eye-level, 28mm, vertical lines straight, Corona Renderer look. Lower third kept simple "
                    "for text. " + LOOK
                ),
                "overlay": "İNTERYER\n3ds Max · Corona · V-Ray · SketchUp · D5 Render · Enscape",
            },
            {
                "label": "Slayd 4 · Animasiya / motion",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Abstract 3D motion-design still: glossy charcoal and frosted-glass "
                    "geometric shapes with chamfered edges suspended mid-motion in a dark void, motion-blur trails, "
                    "a single pale-mint emissive ring, studio lighting, Redshift-style render. " + LOOK_ABSTRACT
                ),
                "overlay": "ANİMASİYA / MOTION\nBlender · Cinema 4D · Maya · Houdini · Unreal Engine\nCycles · Redshift · Octane · Arnold · Karma",
            },
            {
                "label": "Slayd 5 · Məhsul vizualı",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Product render: a minimalist wireless speaker in charcoal fabric and "
                    "brushed aluminium on a pale-mint pedestal with a chamfered 45-degree edge, soft studio light, "
                    "crisp reflections, seamless charcoal background. " + LOOK_ABSTRACT
                ),
                "overlay": "MƏHSUL VİZUALI\nKeyShot · Blender · Cinema 4D · 3ds Max",
            },
            {
                "label": "Slayd 6 · Biz nəyi dəstəkləyirik",
                "mode": "Brend kartı (Canva/Figma)",
                "prompt": "",
                "overlay": "CYBER RENDER-DƏ DƏSTƏKLƏNİR:\n[saytdakı tam siyahı, ✓ ilə]",
            },
            {
                "label": "Slayd 7 · CTA",
                "mode": "Brend kartı (Canva/Figma)",
                "prompt": "",
                "overlay": "Proqramını şərhə yaz 👇\nƏn çox yazılan proqram üçün növbəti postda render vaxtını qısaldan bələdçi.",
            },
        ],
        "caption": (
            "Memar, interyer dizayneri, animator: hər kəsin öz proqram dəsti var. Bəs səninki hansıdır?\n\n"
            "Swipe et, öz sahəni tap 👉\n"
            "Max + Corona komandası? Blender sevərləri? C4D + Redshift?\n\n"
            "👇 Şərhə proqramını yaz. Ən çox yazılan proqram üçün növbəti postda render vaxtını qısaldan "
            "praktik bələdçi paylaşacağıq.\n\n"
            "Dəstəklədiyimiz proqramların tam siyahısı: link bioda."
        ),
        "cta": "Şərhə proqramını yaz (orta)",
        "hashtags": "#3dsmax #coronarender #vray #blender3d #cinema4d #archviz #interiordesign #cyberrender",
        "edit": [
            "Slayd 2–5: proqram adları JetBrains Mono ilə, kəsik künclü etiketlərdə (V4, V12).",
            "Rəsmi proqram loqoları AI ilə çəkilmir (V12).",
        ],
        "verify": ["Slayd 6: dəstəklənən proqramların dəqiq siyahısı saytdan götürülsün."],
    },
    # ------------------------------------------------------------------ 3
    {
        "id": "P01",
        "order": 3,
        "title": "Render gecəsi",
        "kind": "Reel",
        "format": "Reel · 2 klip + son kadr · ~19 san · 9:16",
        "segment": ["Hamısı", "Frilanserlər"],
        "pillar": "Ağrı → Rahatlıq",
        "tone": "D",
        "triggers": ["P1", "P4"],
        "hook": "03:12. Render hələ 87%-dədir.",
        "idea": (
            "Hər 3D adamın yaşadığı gecə və onun tərsi. Gecə kompüter uğuldayır, tile-lar donub. Səhər "
            "kompüter sönülüdür, dizayner yatıb, hazır render planşetdədir. Səs imzası: ventilyator → sükut → ding."
        ),
        "ingredients": [
            {
                "name": "Studiya otağı (hər iki klip üçün)",
                "prompt": (
                    "Portrait composition. A small home design studio: a desk by a large window with a big monitor, "
                    "a desktop tower, a white scale architectural model, sketches and coffee cups; an office chair; a "
                    "grey sofa in the background. Low light from the monitor and a pale-mint desk lamp. Wide shot, "
                    "24mm. " + LOOK
                ),
            }
        ],
        "shots": [
            {
                "label": "Klip A · 0–8 san · gecə",
                "mode": "Ingredients to Video (studiya otağı)",
                "prompt": (
                    "Vertical 9:16. Night, 3 a.m., in this small design studio. Over-the-shoulder shot from behind a "
                    "young designer (face never visible) slumped in the chair, staring at a large monitor where a "
                    "half-finished architectural interior image is being rendered in square tiles that have frozen. "
                    "Empty coffee cups, crumpled sketches, the white scale model on the desk. Light sources: cold "
                    "monitor glow and a faint pale-mint desk lamp. Very slow push-in toward the screen. Audio: loud "
                    "strained computer fans whirring, a wall clock ticking, a tired exhale. " + LOOK_NIGHT
                ),
                "overlay": "0–3 san: “03:12. Render hələ 87%-dədir.”\n3–7 san: “Təqdimat saat 10:00-dadır.”",
            },
            {
                "label": "Klip B · 8–16 san · səhər",
                "mode": "Ingredients to Video (studiya otağı)",
                "prompt": (
                    "Vertical 9:16. The same design studio at sunrise. The desk is calm and tidy, the computer tower "
                    "is switched off and silent, soft pale-mint morning light pours through the window. In the "
                    "background, out of focus, the designer sleeps peacefully on the grey sofa under a blanket (face "
                    "not visible). On the desk a tablet lies face-up showing a finished, bright, photorealistic "
                    "living-room render. Slow lateral dolly from left to right toward the tablet. Audio: near "
                    "silence, birds outside, a single gentle notification chime. " + LOOK
                ),
                "overlay": "Kəsikdə: “Yaxud…”\n10–15 san: “Render bizdə. Sən yat.”",
            },
            {
                "label": "Son kadr · 16–19 san",
                "mode": "CapCut / Canva (Flow yox)",
                "prompt": "",
                "overlay": "Mint fon · loqo · “Render bizdə. Sən yat.” · DM: RENDER",
            },
        ],
        "caption": (
            "03:12. Render hələ 87%-dədir. Təqdimat isə saat 10:00-da. 😮‍💨\n\n"
            "Bu gecəni hər dizayner, hər memar, hər animator ən azı bir dəfə yaşayıb. Ventilyator uğuldayır, "
            "sən ekrana baxıb dua edirsən ki, işıq sönməsin.\n\n"
            "Başqa yol var. Səhnəni göndər, render-i biz hesablayaq. Sən isə yat.\n\n"
            "👉 DM-ə “RENDER” yaz. Səhnənə baxıb vaxtı və qiyməti dəqiq deyək."
        ),
        "cta": "DM: RENDER (birbaşa)",
        "hashtags": "#archviz #3dsmax #coronarender #rendering #memarlıq #interyerdizayn #baku #cyberrender",
        "edit": [
            "Klip A-nın üstünə CapCut-da sadə progress bar: 87%, yanıb-sönür (V10, AI interfeysi yox).",
            "Səs: A-da ventilyator, kəsikdə tam sükut (0.5 san), B-də ding (V14).",
        ],
        "verify": [],
    },
    # ------------------------------------------------------------------ 4
    {
        "id": "P07",
        "order": 4,
        "title": "Render vaxtını qısaldan 7 vərdiş",
        "kind": "Karusel",
        "format": "Karusel · 9 slayd · 4:5 (1080×1350)",
        "segment": ["İnteryer", "Memarlar"],
        "pillar": "Təhsil",
        "tone": "M",
        "triggers": ["P5"],
        "hook": "Render vaxtını qısaldan 7 vərdiş. Yadda saxla 🔖",
        "idea": (
            "Pulsuz, praktik bilik (qarşılıqlılıq). Saxlanan və komandaya göndərilən post növüdür. "
            "Sonuncu slayd yumşaq satışdır: final render-i ümumiyyətlə öz kompüterində etmə."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Slayd 1 · Hook",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Split image of the same minimalist living room: the left half rendered as "
                    "matte white clay, the right half fully photorealistic (charcoal microcement walls, pale-mint "
                    "velvet sofa, light oak floor, travertine table); the split is a clean diagonal line at 45 "
                    "degrees. Eye-level, 24mm, vertical lines straight. Empty space at the top for a headline. "
                    + LOOK
                ),
                "overlay": "RENDER VAXTINI QISALDAN 7 VƏRDİŞ\nCorona · V-Ray · Yadda saxla 🔖",
            },
            {"label": "Slayd 2", "mode": "Brend kartı", "prompt": "",
             "overlay": "01 · Testləri kiçik ölçüdə et.\nFinal rezolyusiya yalnız ən sonda."},
            {"label": "Slayd 3", "mode": "Brend kartı", "prompt": "",
             "overlay": "02 · Noise limit + denoiser.\nLimiti bir az yüksək saxla, qalanını denoiser təmizləsin. İncə teksturları yoxla: denoiser onları yuya bilər."},
            {"label": "Slayd 4", "mode": "Brend kartı", "prompt": "",
             "overlay": "03 · Region render.\nBütün kadrı yox, yalnız problemli hissəni yenidən hesabla."},
            {"label": "Slayd 5", "mode": "Brend kartı", "prompt": "",
             "overlay": "04 · Proxy və instancing.\nAğac, ot, stul təkrarlanırsa, səhnəni yükləmə: proxy işlət."},
            {"label": "Slayd 6", "mode": "Brend kartı", "prompt": "",
             "overlay": "05 · Teksturları ölç.\nKameradan uzaqdakı obyektə 8K tekstur lazım deyil."},
            {"label": "Slayd 7", "mode": "Brend kartı", "prompt": "",
             "overlay": "06 · Displacement seçici olsun.\nYalnız kameraya yaxın səthlərə."},
            {"label": "Slayd 8", "mode": "Brend kartı", "prompt": "",
             "overlay": "07 · İşığı interaktiv rejimdə qur (IPR / Interactive).\nFinal render-i bir dəfə burax."},
            {"label": "Slayd 9 · CTA", "mode": "Brend kartı (Charcoal)", "prompt": "",
             "overlay": "BONUS: final render-i ümumiyyətlə öz kompüterində etmə 😉\nCyber Render · DM: RENDER\nYadda saxla · komandana göndər"},
        ],
        "caption": (
            "Render vaxtını qısaldan 7 vərdiş. 🔖 Yadda saxla.\n"
            "Corona və V-Ray üçün yazılıb, amma prinsiplər demək olar ki, hər render mühərrikində işləyir.\n\n"
            "Vaxtın çoxunu render-in özü yox, düzgün qurulmamış səhnə aparır. Bu vərdişlər hər layihədə "
            "xeyli vaxt qazandırır.\n\n"
            "Hansını artıq edirsən? Şərhə nömrəsini yaz 👇\n\n"
            "Bonus: final render-i ümumiyyətlə öz kompüterində etmə. Bunun üçün biz varıq. DM: RENDER"
        ),
        "cta": "Yadda saxla + komandana göndər (yumşaq) · DM: RENDER",
        "hashtags": "#coronarender #vray #3dsmax #archviz #rendertips #interiordesign #3dvisualization #cyberrender",
        "edit": [
            "Slayd 2–8: Mint fon, Charcoal mətn, nömrə JetBrains Mono ilə kəsik künclü etiketdə.",
            "P04-ün şərhlərində Blender çoxluq təşkil etsə, eyni 7 prinsipi Cycles terminləri ilə yaz "
            "(adaptive sampling + denoiser, region render, instancing, texture size, IPR → viewport render).",
        ],
        "verify": ["Texniki ifadələri komandadakı 3D mütəxəssis bir dəfə oxusun."],
    },
    # ------------------------------------------------------------------ 5
    {
        "id": "P03",
        "order": 5,
        "title": "Klient bunu heç vaxt görmür",
        "kind": "Reel",
        "format": "Reel · 1 klip + son kadr · ~12 san · 9:16",
        "segment": ["İnteryer", "Memarlar"],
        "pillar": "Kontrast / Sübut",
        "tone": "D",
        "triggers": ["P4", "P1"],
        "hook": "Klient bunu heç vaxt görmür.",
        "idea": (
            "Clay-dən finala keçid. Klient yalnız son şəkli görür, arada qalan render saatlarını görmür. "
            "Ən güclü versiya: real layihədən real clay və final kadrlar (V9). AI versiyası konsept kimi "
            "işlədilir və “AI info” ilə işarələnir."
        ),
        "ingredients": [
            {
                "name": "Final kadr (son kadr kimi)",
                "prompt": (
                    "Portrait 9:16. Photorealistic interior visualization of a minimalist living room in a modern "
                    "Baku apartment at golden hour: charcoal microcement walls, a pale-mint-green velvet sofa, light "
                    "oak floor, travertine coffee table, sculptural floor lamp, floor-to-ceiling window with a soft "
                    "hazy view of the Caspian Sea, a thin linear pale-mint LED in the ceiling cove. Eye-level, 24mm, "
                    "two-point perspective, vertical lines perfectly straight, Corona Renderer look, ultra detailed. "
                    "No people. " + LOOK
                ),
            },
            {
                "name": "Clay kadr (final şəkli giriş kimi verib redaktə et)",
                "prompt": (
                    "Turn this exact image into a clay render: identical camera, geometry, objects and composition; "
                    "replace all materials with matte white clay, remove all textures and colors, soft ambient "
                    "occlusion, neutral soft daylight. Keep every object in exactly the same position. No text."
                ),
            },
        ],
        "shots": [
            {
                "label": "Klip · 0–8 san",
                "mode": "Frames to Video (ilk: clay, son: final)",
                "prompt": (
                    "Vertical 9:16. Slow forward dolly. The matte white clay interior gradually turns into the fully "
                    "textured photorealistic room: materials sweep across the surfaces from left to right like a "
                    "render pass being revealed, colors and reflections appear, the window light warms up, and the "
                    "pale-mint LED in the ceiling cove switches on last. Smooth, precise, satisfying. Audio: soft "
                    "digital whoosh, subtle rising synth tone, a crisp click when the light switches on."
                ),
                "overlay": "0–3 san (clay): “Klient bunu heç vaxt görmür.”\n4–7 san: “Yalnız sonu görür.”\n8–10 san: “Arada qalan render saatlarını isə heç kim görmür.”",
            },
            {
                "label": "Son kadr · 10–12 san",
                "mode": "CapCut / Canva (Flow yox)",
                "prompt": "",
                "overlay": "“O saatları bizə ver.” · loqo · DM: RENDER",
            },
        ],
        "caption": (
            "Klient yalnız son şəkli görür. Clay-i, testləri, gecə 2-dəki düzəlişi, 6 saatlıq final render-i görmür.\n\n"
            "Amma sən görürsən. Hər saatını.\n\n"
            "O saatları bizə ver. Sən dizayna qayıt.\n\n"
            "👉 DM-ə “RENDER” yaz, ilk səhnəni birlikdə hesablayaq."
        ),
        "cta": "DM: RENDER (birbaşa)",
        "hashtags": "#archviz #coronarender #3dsmax #interiordesign #clayrender #3dvisualization #baku #cyberrender",
        "edit": [
            "Real layihə varsa: 3ds Max-dan eyni kameradan clay və final render götür, Flow-da yalnız Frames to Video et.",
            "Fotoreal AI kadrdırsa, “AI info” etiketi qoy (F8).",
        ],
        "verify": ["Real klient işi işlədilsə, klientin yazılı icazəsi alınsın."],
    },
    # ------------------------------------------------------------------ 6
    {
        "id": "P05",
        "order": 6,
        "title": "Render gedərkən sən: 5 mərhələ",
        "kind": "Karusel",
        "format": "Karusel · 7 slayd · 4:5 · maskot “Gil”",
        "segment": ["Hamısı"],
        "pillar": "Meme / Qrup kimliyi",
        "tone": "M",
        "triggers": ["P3"],
        "hook": "Render gedərkən sən: 5 mərhələ",
        "idea": (
            "Maskot “Gil”: üzü olmayan ağ gil manekenidir, yəni clay render-in canlı versiyası. Hələ "
            "“render olunmamış” dizayneri təmsil edir. Meme formatı paylaşılır və etiketlənir. Gil sonrakı "
            "postlarda (P12) seriya personajı kimi qayıdır."
        ),
        "ingredients": [{"name": "Gil personaj kartı (bütün slaydlar üçün istinad)", "prompt": GIL_REF}],
        "shots": [
            {
                "label": "Slayd 1 · Hook",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "The faceless white clay mannequin character Gil from the reference sits at a charcoal desk seen "
                    "from behind, chin resting on one hand, facing a large glowing monitor (screen softly blurred), "
                    "in a dark room lit by a pale-mint desk lamp. Cinematic still, empty space at the top. " + LOOK_CLAY
                ),
                "overlay": "RENDER GEDƏRKƏN SƏN: 5 MƏRHƏLƏ",
            },
            {
                "label": "Slayd 2 · Mərhələ 1",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, leans back very relaxed in an office "
                    "chair with feet up on the charcoal desk, holding a coffee mug, monitor glowing softly in front. "
                    "Calm evening light. " + LOOK_CLAY
                ),
                "overlay": "1. “Cəmi 40 dəqiqə yazır.” 😌",
            },
            {
                "label": "Slayd 3 · Mərhələ 2",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, sits hunched extremely close to the "
                    "glowing monitor, head almost touching the screen, several empty coffee cups around, late night. "
                    + LOOK_CLAY
                ),
                "overlay": "2. “Bir az da gözləyim…”",
            },
            {
                "label": "Slayd 4 · Mərhələ 3",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, kneels on the floor with hands pressed "
                    "together as if praying in front of a desktop computer tower that glows pale mint, dramatic soft "
                    "light rays from the tower, dark room, humorous and theatrical. " + LOOK_CLAY
                ),
                "overlay": "3. Kompüterə dua 🙏",
            },
            {
                "label": "Slayd 5 · Mərhələ 4",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, stands frozen in a shocked pose with "
                    "both hands on its head in a completely dark room, lit only by a phone flashlight from below; the "
                    "monitor is black. Humorous, dramatic. " + LOOK_CLAY
                ),
                "overlay": "4. 99%. Və… işıq sönür.",
            },
            {
                "label": "Slayd 6 · Mərhələ 5",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, sleeps peacefully curled up on a "
                    "pale-mint beanbag in soft morning light; the computer on the desk behind is switched off. "
                    "Serene, cozy. " + LOOK_CLAY
                ),
                "overlay": "5. Cyber Render-i kəşf edir. 😴",
            },
            {
                "label": "Slayd 7 · CTA",
                "mode": "Brend kartı (Charcoal)",
                "prompt": "",
                "overlay": "Sən hansı mərhələdəsən? Şərhə 1–5 yaz 👇\nRender-i bitməyən dostunu etiketlə.",
            },
        ],
        "caption": (
            "Render gedərkən sən: 5 mərhələ. Hamımız keçmişik. 😅\n\n"
            "1. “Cəmi 40 dəqiqə yazır.”\n"
            "2. “Bir az da gözləyim…”\n"
            "3. Kompüterə dua\n"
            "4. 99%. Və işıq sönür.\n"
            "5. Cyber Render-i kəşf edir.\n\n"
            "Sən indi hansı mərhələdəsən? Şərhə nömrəni yaz 👇\n"
            "Render-i heç bitməyən dostunu da etiketlə."
        ),
        "cta": "Şərhə 1–5 yaz + dostunu etiketlə (yumşaq)",
        "hashtags": "#3dartist #archviz #rendering #3dsmax #blender3d #designerlife #memarlıq #cyberrender",
        "edit": [
            "Gil-in görünüşü hər slaydda eyni qalmalıdır. Uyğun gəlməyən variantı at, yenidən yarat (F5).",
            "Mətn kartın yuxarısında, ağ kəsik künclü lövhədə.",
        ],
        "verify": [],
    },
    # ------------------------------------------------------------------ 7
    {
        "id": "P11",
        "order": 7,
        "title": "1500 kadr. Bir-bir yox, eyni anda",
        "kind": "Reel",
        "format": "Reel · 2 klip + son kadr · ~19 san · 9:16",
        "segment": ["Animatorlar"],
        "pillar": "Güc / Riyaziyyat",
        "tone": "D",
        "triggers": ["P2", "P7"],
        "hook": "1 kadr. 4 dəqiqə. Daha 1499 kadr var…",
        "idea": (
            "Kadr-kadr gözləmək ilə bütün kadrların eyni anda hesablanması arasındakı fərq. Bu, paylanmış "
            "render metaforasıdır. Bir şüşə kadr yavaş-yavaş dolur, sonra kamera geri çəkilir və minlərlə "
            "kadr birdən yanır."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Klip A · 0–8 san",
                "mode": "Text to Video",
                "prompt": (
                    "Vertical 9:16. A single thin glass film frame floats in a dark charcoal void. Inside it, a "
                    "colorful stylized 3D animation still (an original small round robot character mid-jump with "
                    "motion blur) slowly fills in from top to bottom like an image being rendered, while a thin "
                    "pale-mint progress line crawls painfully slowly along the frame's bottom edge. Locked-off static "
                    "camera, centered. Audio: slow clock ticking, a single computer fan humming, a bored sigh. "
                    + LOOK_ABSTRACT
                ),
                "overlay": "0–3 san: “1 kadr. 4 dəqiqə.”\n4–8 san: “Daha 1499 kadr var…”",
            },
            {
                "label": "Klip B · 8–16 san",
                "mode": "Text to Video (və ya A-nın son kadrından Extend)",
                "prompt": (
                    "Vertical 9:16. The camera pulls back fast and rises to reveal thousands of identical thin glass "
                    "film frames arranged in a vast precise grid stretching to the horizon in the dark charcoal void. "
                    "In one sweeping wave, all frames light up at the same time in pale mint and fill with images "
                    "simultaneously. Epic scale, symmetrical, cinematic. Audio: a deep bass swell, a cascade of soft "
                    "digital clicks, then a bright uplifting synth hit. " + LOOK_ABSTRACT
                ),
                "overlay": "“Bəs hamısı eyni anda hesablansa?”",
            },
            {
                "label": "Son kadr · 16–19 san",
                "mode": "CapCut / Canva (Flow yox)",
                "prompt": "",
                "overlay": "Animatorlar üçün render gücü\nBlender · Cinema 4D · Maya · Houdini [dəstəyi yoxla]\nŞərhə KADR yaz",
            },
        ],
        "caption": (
            "1 kadr = 4 dəqiqə. 1 dəqiqəlik animasiya = 1500 kadr. Qalanını hesablamağa qorxursan? 😬\n\n"
            "Sənin kompüterində kadrlar bir-bir növbəyə düzülür. Render gücü çox olanda isə kadrlar paralel "
            "hesablanır və gözləmə kəskin qısalır. [paralel render təsdiqlənsin]\n\n"
            "👇 Şərhə “KADR” yaz. Layihənin kadr sayını və bir kadrın vaxtını DM-də göndər, real müddəti hesablayaq."
        ),
        "cta": "Şərhə KADR yaz → DM (orta)",
        "hashtags": "#blender3d #cinema4d #houdini #motiondesign #3danimation #redshift3d #animation #cyberrender",
        "edit": [
            "B klipinin ortasında (dalğa anı) musiqidə bass vuruşu olsun.",
            "Robot personajı orijinaldır. Tanınmış film və ya oyun personajına bənzəməməlidir.",
        ],
        "verify": ["Cyber Render-in kadrları paralel (bir neçə GPU/maşında) hesabladığı təsdiqlənsin.",
                   "Son kadrdakı proqram siyahısı saytla üst-üstə düşsün."],
    },
    # ------------------------------------------------------------------ 8
    {
        "id": "P02",
        "order": 8,
        "title": "Animasiyanın riyaziyyatı",
        "kind": "Karusel",
        "format": "Karusel · 7 slayd · 4:5 (1080×1350)",
        "segment": ["Animatorlar"],
        "pillar": "Riyaziyyat / Təhsil",
        "tone": "M",
        "triggers": ["P2", "P7"],
        "hook": "1 kadr = 4 dəq. Bəs 1 dəqiqəlik animasiya?",
        "idea": (
            "Animatorun qorxulu kalkulyatoru, addım-addım. Hər slayd bir hesab. Ən ağrılı nöqtə 5-ci "
            "slayddır: bir düzəliş yenidən 100 saat deməkdir. Hesablar yoxlanıb: 25 × 60 = 1500; "
            "1500 × 4 = 6000 dəq = 100 saat = 4 gün 4 saat."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Slayd 1 · Hook",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Abstract 3D still: hundreds of thin glass film frames floating in a long "
                    "spiral through a dark charcoal void, each holding a faint animation image, one frame in the "
                    "foreground glowing pale mint; deep perspective, volumetric light, Redshift-style render. Empty "
                    "upper third for a headline. " + LOOK_ABSTRACT
                ),
                "overlay": "1 KADR = 4 DƏQ.\nBƏS 1 DƏQİQƏLİK ANİMASİYA?",
            },
            {"label": "Slayd 2", "mode": "Brend kartı", "prompt": "",
             "overlay": "25 kadr × 60 saniyə\n= 1 500 kadr"},
            {"label": "Slayd 3", "mode": "Brend kartı", "prompt": "",
             "overlay": "1 500 × 4 dəq\n= 6 000 dəq\n= 100 saat"},
            {"label": "Slayd 4", "mode": "Brend kartı", "prompt": "",
             "overlay": "100 saat = 4 gün 4 saat.\nFasiləsiz. Bu müddətdə kompüterin sənin deyil."},
            {"label": "Slayd 5", "mode": "Brend kartı (Charcoal, vurğu)", "prompt": "",
             "overlay": "Klient bir düzəliş istədi?\nYenidən 100 saat. ⚠"},
            {"label": "Slayd 6", "mode": "Brend kartı", "prompt": "",
             "overlay": "Kadrlar paralel hesablananda növbə yoxdur.\n[Cyber Render-də paralel render: təsdiqlə]"},
            {"label": "Slayd 7 · CTA", "mode": "Brend kartı", "prompt": "",
             "overlay": "Kadr sayını və 1 kadrın vaxtını şərhə yaz.\nSənin üçün hesablayaq 👇"},
        ],
        "caption": (
            "1 kadr = 4 dəqiqə. Az görünür, elə deyil?\n\n"
            "25 fps × 60 saniyə = 1 500 kadr\n"
            "1 500 × 4 dəq = 6 000 dəqiqə = 100 saat\n"
            "100 saat = 4 gün 4 saat fasiləsiz render\n\n"
            "Klient bir düzəliş istəyəndə isə hamısı yenidən. 🙃\n\n"
            "Problem təkcə kompüterin gücündə deyil, kadrların bir-bir növbəyə düzülməsindədir. Kadrlar paralel "
            "hesablananda bu növbə yoxa çıxır.\n\n"
            "👇 Layihənin kadr sayını və bir kadrın render vaxtını şərhə yaz. Real müddəti hesablayıb cavab verək."
        ),
        "cta": "Şərhə rəqəmlərini yaz (orta)",
        "hashtags": "#3danimation #blender3d #cinema4d #motiondesign #animator #rendering #cyberrender",
        "edit": [
            "Rəqəmlər JetBrains Mono ilə, iri və mərkəzdə. Hər slayd bir sətir hesab.",
            "Slayd 5 tək Charcoal slayddır, qalanları Mint. Bu, vurğunu gücləndirir.",
        ],
        "verify": ["Slayd 6 və caption: paralel render iddiası təsdiqlənsin."],
    },
    # ------------------------------------------------------------------ 9
    {
        "id": "P08",
        "order": 9,
        "title": "Klient, 23:47",
        "kind": "Reel",
        "format": "Reel · 2 klip + son kadr · ~19 san · 9:16",
        "segment": ["Studiyalar", "Frilanserlər"],
        "pillar": "Ağrı → Status",
        "tone": "D",
        "triggers": ["P1", "P6"],
        "hook": "Klient, 23:47: “Sabah 10-a 5 rakurs hazır olar?”",
        "idea": (
            "Gecə gələn təcili mesajın stressi və səhərki sakit təqdimatın qüruru. Bildiriş interfeysi "
            "CapCut-da çəkilir (V10). Görüş otağındakı ekran metafordur, klient işi kimi təqdim olunmur (V9)."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Klip A · 0–8 san · gecə",
                "mode": "Text to Video",
                "prompt": (
                    "Vertical 9:16. Close-up of a smartphone lying face-up on a dark charcoal desk among architectural "
                    "drawings, a pencil and a scale ruler, late at night. The phone screen suddenly lights up and "
                    "vibrates with an incoming message (screen content blurred and unreadable). Cold mint-tinted "
                    "screen light spills over the paper. Locked-off camera, then a slow push-in. Audio: phone "
                    "vibration buzzing on wood, distant city night ambience, a tense low drone. " + LOOK_NIGHT
                ),
                "overlay": "CapCut bildirişi: “Klient · 23:47: Sabah 10-a 5 rakurs hazır olar?”\nSonra: “Sən: …yazır”",
            },
            {
                "label": "Klip B · 8–16 san · səhər",
                "mode": "Text to Video",
                "prompt": (
                    "Vertical 9:16. Bright modern meeting room in the morning with pale-mint walls and light oak "
                    "furniture. A large wall screen shows a photorealistic exterior visualization of a modern "
                    "residential building at dusk. Two people seen from behind and out of focus lean toward the "
                    "screen; one nods. Slow dolly toward the screen. Audio: quiet room tone, a soft impressed "
                    "murmur, a gentle positive synth note. " + LOOK
                ),
                "overlay": "“10:00. 5 rakurs. Sakit üz.”",
            },
            {
                "label": "Son kadr · 16–19 san",
                "mode": "CapCut / Canva (Flow yox)",
                "prompt": "",
                "overlay": "Studiyalar və frilanserlər üçün render gücü · DM: STUDIO",
            },
        ],
        "caption": (
            "Klient, 23:47: “Sabah saat 10-a 5 rakurs hazır olar?”\n\n"
            "Səndə iki seçim var:\n"
            "1) “Əlbəttə” yazıb bütün gecəni kompüterin yanında keçirmək.\n"
            "2) “Əlbəttə” yazıb render-i bizə göndərmək. ✅\n\n"
            "Səhər 10:00. Beş rakurs. Sakit üz. Klient isə sadəcə “vau” deyir.\n\n"
            "👉 Studiyalar və frilanserlər üçün: DM-ə “STUDIO” yaz, təcili sifarişlər üçün iş axınını birlikdə quraq."
        ),
        "cta": "DM: STUDIO (birbaşa)",
        "hashtags": "#archviz #architecture #interiordesign #designstudio #3dsmax #coronarender #baku #cyberrender",
        "edit": [
            "Bildiriş: iOS/Android üslubunda sadə, bulanıq fon üzərində ağ kart. Brend adı və loqo yoxdur.",
            "Səs: A-da vibrasiya, B-yə keçiddə sükut, sonra müsbət not (V14).",
        ],
        "verify": ["Gecə ərzində (təcili) hazırlanma imkanı təsdiqlənsin, əks halda “səhər” vurğusunu yumşalt."],
    },
    # ------------------------------------------------------------------ 10
    {
        "id": "P09",
        "order": 10,
        "title": "Workstation-ın gerçək qiyməti",
        "kind": "Karusel",
        "format": "Karusel · 8 slayd · 4:5 (1080×1350)",
        "segment": ["Studiyalar"],
        "pillar": "B2B məntiq",
        "tone": "M",
        "triggers": ["P8", "P1"],
        "hook": "Yeni workstation almadan əvvəl bunu oxu.",
        "idea": (
            "Studiya rəhbəri üçün sağlam düşüncə postu: aparatın görünməyən xərcləri. Rəqəm verilmir, "
            "suallar verilir. Oxucu öz rəqəmlərini hesablayır və nəticəyə özü gəlir."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Slayd 1 · Hook",
                "mode": "Image",
                "prompt": (
                    "Portrait composition. Product hero shot: a sleek dark charcoal workstation tower with a thin "
                    "pale-mint light strip, standing on a raw concrete plinth with a chamfered 45-degree edge in a "
                    "dark studio; dramatic rim light, crisp reflections, low angle, 50mm. Empty space at the top. "
                    + LOOK_ABSTRACT
                ),
                "overlay": "YENİ WORKSTATION ALMADAN ƏVVƏL BUNU OXU.",
            },
            {"label": "Slayd 2", "mode": "Brend kartı", "prompt": "",
             "overlay": "Qiymət etiketi yalnız başlanğıcdır."},
            {"label": "Slayd 3", "mode": "Brend kartı", "prompt": "",
             "overlay": "+ Elektrik.\nRender gecələri ayda neçə saatdır? Hesabla."},
            {"label": "Slayd 4", "mode": "Brend kartı", "prompt": "",
             "overlay": "+ İstilik və səs.\nRender gedən otaq sobaya, ofis server otağına çevrilir."},
            {"label": "Slayd 5", "mode": "Brend kartı", "prompt": "",
             "overlay": "+ Köhnəlmə.\nHər 2–3 ildən bir yeni GPU nəsli çıxır. Sənin maşının dəyəri isə düşür."},
            {"label": "Slayd 6", "mode": "Brend kartı (Charcoal, vurğu)", "prompt": "",
             "overlay": "+ Ən bahalısı:\nrender gedərkən dayanan dizayner. Onun saatı neçəyədir?"},
            {"label": "Slayd 7", "mode": "Brend kartı", "prompt": "",
             "overlay": "Alternativ: gücü yalnız lazım olanda götür.\nİnvestisiyanı aparata yox, layihələrə yönəlt."},
            {"label": "Slayd 8 · CTA", "mode": "Brend kartı", "prompt": "",
             "overlay": "Studiyanın aylıq render həcmini DM-ə yaz.\nSənə uyğun variantı rəqəmlərlə müqayisə edək.\nDM: STUDIO"},
        ],
        "caption": (
            "Yeni workstation almaq istəyirsən? Əvvəl gerçək qiymətini hesabla.\n\n"
            "Qiymət etiketi yalnız başlanğıcdır. Üstünə elektrik, istilik, səs, texniki xidmət və köhnəlmə "
            "gəlir. Ən bahalısı isə render gedərkən dayanan dizaynerin saatıdır.\n\n"
            "Bəzən daha ağıllı yol başqadır: render gücünü yalnız lazım olanda götürmək.\n\n"
            "👉 Studiyanın təxminən ayda nə qədər render etdiyini DM-ə yaz (“STUDIO”). Sənə uyğun variantı "
            "rəqəmlərlə müqayisə edək."
        ),
        "cta": "DM: STUDIO (birbaşa)",
        "hashtags": "#designstudio #architecturestudio #archviz #3dvisualization #workstation #rendering #baku #cyberrender",
        "edit": ["Slayd 3–6: “+” işarəsi Signal rəngində (V-qayda: 5%-dən az)."],
        "verify": ["DM-də müqayisə üçün real qiymət modeli hazır olsun (saat/kadr/paket)."],
    },
    # ------------------------------------------------------------------ 11
    {
        "id": "P06",
        "order": 11,
        "title": "Bu noise sənin deyil",
        "kind": "Reel",
        "format": "Reel · 1 klip + son kadr · ~14 san · 9:16",
        "segment": ["Memarlar", "Archviz"],
        "pillar": "Keyfiyyət",
        "tone": "D",
        "triggers": ["P4"],
        "hook": "Bu noise sənin deyil.",
        "idea": (
            "Keyfiyyət ilə vaxt arasındakı əbədi seçim. Videonun əvvəlində ağır noise var, kamera geri "
            "çəkildikcə şəkil “təmizlənir”. Noise effekti montajda verilir, ona görə tam idarə olunur."
        ),
        "ingredients": [],
        "shots": [
            {
                "label": "Klip · 0–8 san",
                "mode": "Text to Video",
                "prompt": (
                    "Vertical 9:16. Exterior of a modern two-storey villa on a hillside overlooking the Caspian Sea at "
                    "blue hour: charcoal basalt facade, floor-to-ceiling glass with warm interior light, a thin "
                    "pale-mint LED line under the cantilevered roof, an infinity pool reflecting the sky, olive trees "
                    "and dry grasses moving gently in the wind. Very slow aerial pull-back with a slight rise. Audio: "
                    "soft wind, distant waves, a low ambient synth pad. " + LOOK
                ),
                "overlay": "0–2 san: “Bu noise sənin deyil.”\n2–4 san: “Bu, vaxtın azlığıdır.”\n5–8 san: “Az sample = noise. Çox sample = saatlar.”",
            },
            {
                "label": "Davamı · 8–12 san",
                "mode": "Extend (eyni klip, yavaş davam)",
                "prompt": (
                    "Continue the same slow aerial pull-back, revealing more of the hillside and the calm sea at blue "
                    "hour. Same lighting and mood. Audio: wind and waves fading, synth pad resolving."
                ),
                "overlay": "“Keyfiyyət ilə vaxt arasında seçim etmə.”",
            },
            {
                "label": "Son kadr · 12–14 san",
                "mode": "CapCut / Canva (Flow yox)",
                "prompt": "",
                "overlay": "Final render-i bizə ver · DM: RENDER",
            },
        ],
        "caption": (
            "Bu noise sənin deyil. Bu, vaxtın azlığıdır.\n\n"
            "Az sample: noise, ləkələr, “denoiser bir təhər düzəldər” ümidi.\n"
            "Çox sample: təmiz şəkil, amma bütün gecə.\n\n"
            "Hər dizayner bu seçimi edib. Amma etməli deyil.\n\n"
            "👉 Final render-i bizə ver, keyfiyyətdən güzəşt etmədən al. DM: RENDER"
        ),
        "cta": "DM: RENDER (birbaşa)",
        "hashtags": "#archviz #exteriordesign #coronarender #vray #architecture #rendering #3dvisualization #cyberrender",
        "edit": [
            "CapCut: 0–3 san güclü grain/noise effekti, 3–5 san ərzində sıfıra endir.",
            "Daha güclü versiya: real 3ds Max kadrı (aşağı pass → yüksək pass) ekran yazısı kimi.",
        ],
        "verify": [],
    },
    # ------------------------------------------------------------------ 12
    {
        "id": "P12",
        "order": 12,
        "title": "Render-i göndərmək: 3 addım",
        "kind": "Karusel",
        "format": "Karusel · 5 slayd · 4:5 · maskot “Gil”",
        "segment": ["Hamısı"],
        "pillar": "Təklif / Konversiya",
        "tone": "M",
        "triggers": ["P7", "P9"],
        "hook": "Render-i göndərmək: 3 addım. Gözləmək: 0.",
        "idea": (
            "Ayın sonunda konversiya postu. Proses sadə görünür, ilk addımın qorxusu qalmır. Gil maskotu "
            "P05-dən qayıdır və seriya hissi yaradır. Addımlar saytdakı real prosesə görə doldurulur."
        ),
        "ingredients": [{"name": "Gil personaj kartı (P05-dəki ilə eyni)", "prompt": GIL_REF}],
        "shots": [
            {
                "label": "Slayd 1 · Hook",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, confidently pushes a glowing pale-mint "
                    "cube into a sharp chamfered hexagonal portal cut into a charcoal concrete wall; the portal glows "
                    "pale mint inside. Dynamic three-quarter view, empty space at the top. " + LOOK_CLAY
                ),
                "overlay": "RENDER-İ GÖNDƏRMƏK: 3 ADDIM.\nGÖZLƏMƏK: 0.",
            },
            {
                "label": "Slayd 2 · Hazırla",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, carefully packs a small glowing "
                    "pale-mint cube together with tiny material swatches into a charcoal box with chamfered corners, "
                    "on a clean work table. Neat, precise. " + LOOK_CLAY
                ),
                "overlay": "01 · HAZIRLA\nSəhnəni teksturlar və proxy-lərlə birlikdə arxivlə. [saytdakı tələblər]",
            },
            {
                "label": "Slayd 3 · Göndər",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, slides the charcoal box into the "
                    "glowing pale-mint chamfered portal in a charcoal concrete wall, light streaming out. "
                    + LOOK_CLAY
                ),
                "overlay": "02 · GÖNDƏR\n[yükləmə üsulu: sayt / forma / link]",
            },
            {
                "label": "Slayd 4 · Al",
                "mode": "Image + Gil istinadı",
                "prompt": (
                    "Gil, the faceless white clay mannequin from the reference, receives a large glowing framed "
                    "picture of a photorealistic interior coming out of the pale-mint portal, holding it up "
                    "proudly. " + LOOK_CLAY
                ),
                "overlay": "03 · AL\nHazır kadrlar sənə qayıdır. [çatdırılma üsulu və müddəti]",
            },
            {
                "label": "Slayd 5 · CTA",
                "mode": "Brend kartı (Charcoal)",
                "prompt": "",
                "overlay": "İlk səhnəni birlikdə göndərək.\nDM: RENDER · Link bioda\n[təklif varsa: məsələn, ilk test render pulsuz]",
            },
        ],
        "caption": (
            "Render-i göndərmək: 3 addım. Gözləmək: 0.\n\n"
            "01 Hazırla: səhnəni teksturlar və proxy-lərlə birlikdə arxivlə.\n"
            "02 Göndər: [yükləmə üsulu]\n"
            "03 Al: hazır kadrlar sənə qayıdır. [müddət]\n\n"
            "Bu vaxt sən növbəti layihəyə keçirsən. Kompüterin də sərbəstdir.\n\n"
            "👉 İlk dəfədir? DM-ə “RENDER” yaz, ilk səhnəni addım-addım birlikdə göndərək. Link bioda."
        ),
        "cta": "DM: RENDER · Link bioda (birbaşa)",
        "hashtags": "#cyberrender #rendering #archviz #3dsmax #blender3d #cinema4d #interiordesign #baku",
        "edit": ["Bu postu profildə pin et (yuxarıda saxla). Yeni gələnlər prosesi dərhal görsün."],
        "verify": ["Addımlar, yükləmə üsulu, müddət və təklif saytdakı real prosesə görə doldurulsun."],
    },
]

STORIES = [
    ("Sorğu", "“Ən uzun render-in nə qədər çəkib?” <1 saat · 1–5 saat · 5–12 saat · 12+ saat 😵"),
    ("Quiz", "“1500 kadr × 4 dəq neçə saatdır?” 25 · 50 · 100 ✅ · 200 (P02-yə körpü)"),
    ("Sual stikeri", "“Render-lə bağlı ən böyük problemin nədir?” Cavablar növbəti postların mövzusudur."),
    ("Slider", "“Bu gün render-in sənə nə qədər stress verdi?” 😐 → 😵"),
    ("Paylaşım", "Hər yeni postu story-də “Yeni post” stikeri ilə paylaş + açar söz xatırlatması."),
    ("Pərdə arxası", "Real ekran yazısı: render prosesi, aparat, komanda [real görüntü, AI yox]."),
]
