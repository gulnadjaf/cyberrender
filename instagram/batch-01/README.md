# Batch 01 · 1 karusel + 2 qrafik post

> `scripts/compose.py` ilə yaradılır. Promptlar `instagram/data/posts.py`-dan gəlir.

## Addımlar

1. **Google Flow-da** aşağıdakı 8 şəkli yarat. Rejim: şəkil (Image). Ölçü: **portrait** (3:4 və ya 9:16, hansı varsa).
   Hər prompt üçün 2–4 variant yarat, ən təmizini seç: yazı yoxdur, üz yoxdur, xətlər düzdür.
2. Şəkilləri yüklə və **bu söhbətə göndər** (adı və ya sırası ilə: 1 → k1-cover, 2 → k2-memarliq ...).
   Repo ilə işləyirsənsə, `instagram/batch-01/flow/` qovluğuna açar adı ilə qoy (məs. `k2-memarliq.png`).
3. `python3 scripts/compose.py` hazır 1080×1350 PNG-ləri `instagram/batch-01/final/`-a yazır.
   Şəkil çatışmırsa, yerində işarəli boş yer olur və fayl `*.preview.png` adlanır.

## Flow promptları

### 1. `k1-cover` · Karusel · slayd 1
```text
Portrait composition. Overhead flat-lay on a charcoal concrete surface, arranged in a precise grid: a white clay architectural model, interior material swatches (light oak, travertine, pale-mint velvet), a small product prototype in brushed metal, and a matte white clay character maquette mid-pose. Soft-box top light, one thin pale-mint light strip along the top edge of the frame, generous empty space in the upper third for a headline. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.
```

### 2. `k2-memarliq` · Karusel · slayd 2
```text
Portrait composition. Photorealistic architectural exterior visualization: a modern residential building with a charcoal basalt facade and vertical light-oak fins on a hillside above the Caspian Sea at blue hour, warm interior lights, a thin pale-mint LED line along the roof edge. Eye-level, two-point perspective, 24mm, vertical lines perfectly straight. Lower half of the frame darker to hold text. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.
```

### 3. `k3-interyer` · Karusel · slayd 3
```text
Portrait composition. Photorealistic interior visualization of a calm bedroom in a modern Baku apartment: charcoal limewash walls, pale-mint linen bedding, light oak floor and headboard, travertine bedside table, soft morning light through sheer curtains, a thin pale-mint LED cove light. Eye-level, 28mm, vertical lines straight, Corona Renderer look. Lower third kept simple for text. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.
```

### 4. `k4-animasiya` · Karusel · slayd 4
```text
Portrait composition. Abstract 3D motion-design still: glossy charcoal and frosted-glass geometric shapes with chamfered edges suspended mid-motion in a dark void, motion-blur trails, a single pale-mint emissive ring, studio lighting, Redshift-style render. Palette strictly deep charcoal (#2A2A2A) and pale mint green (#DDFFD4) with soft neutral highlights. Clean premium 3D render look, physically based lighting, crisp detail. No text, no letters, no logos, no watermarks.
```

### 5. `k5-mehsul` · Karusel · slayd 5
```text
Portrait composition. Product render: a minimalist wireless speaker in charcoal fabric and brushed aluminium on a pale-mint pedestal with a chamfered 45-degree edge, soft studio light, crisp reflections, seamless charcoal background. Palette strictly deep charcoal (#2A2A2A) and pale mint green (#DDFFD4) with soft neutral highlights. Clean premium 3D render look, physically based lighting, crisp detail. No text, no letters, no logos, no watermarks.
```

### 6. `q1-studiya-gece` · Qrafik post 1
```text
Portrait composition. Night, 3 a.m., a small design studio. Over-the-shoulder view from behind a young designer (face not visible) slumped in an office chair in front of a large monitor; the monitor shows a half-finished architectural interior render built from square tiles, the lower rows of tiles still grey and empty. Empty coffee cups, crumpled sketches and a white scale architectural model on the desk. Light sources: cold monitor glow and a faint pale-mint desk lamp. The upper 40% of the frame is dark and uncluttered (wall in shadow) to hold large text. Moody, tense, cinematic, shallow depth of field, subtle film grain; deep charcoal tones with one faint pale-mint (#DDFFD4) light. No readable text on any screen, no logos, no watermarks.
```

### 7. `q2-final` · Qrafik post 2 · final yarı
```text
Portrait composition. Photorealistic interior visualization of a minimalist living room in a modern Baku apartment at golden hour: charcoal microcement walls, a pale-mint-green velvet sofa, light oak floor, travertine coffee table, sculptural floor lamp, floor-to-ceiling window with a soft hazy view of the Caspian Sea, a thin linear pale-mint LED in the ceiling cove. Eye-level, 24mm, two-point perspective, vertical lines perfectly straight, Corona Renderer look, ultra detailed. No people. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.
```

### 8. `q2-clay` · Qrafik post 2 · clay yarı
> q2-final şəklini istinad (ingredient) kimi əlavə et, sonra bu promptu yaz.

```text
Turn this exact image into a clay render: identical camera, geometry, objects and composition; replace all materials with matte white clay, remove all textures and colors, soft ambient occlusion, neutral soft daylight. Keep every object in exactly the same position. No text.
```

## Postlar

| Fayl | Nə |
|---|---|
| `karusel-01…06.png` | Karusel “Sahən hansıdır? Proqramını tap” (6 slayd) |
| `qrafik-1.png` | “03:12. Render hələ 87%-dədir.” |
| `qrafik-2.png` | “Klient bunu heç vaxt görmür.” (clay / final diaqonal) |

## Caption-lar

### karusel
```text
Memar, interyer dizayneri, animator: hər kəsin öz proqram dəsti var. Bəs səninki hansıdır?

Swipe et, öz sahəni tap 👉
Max + Corona komandası? Blender sevərləri? C4D + Redshift?

👇 Şərhə proqramını yaz. Ən çox yazılan proqram üçün növbəti postda render vaxtını qısaldan praktik bələdçi paylaşacağıq.

Dəstəklənən proqramların tam siyahısı: link bioda.

#3dsmax #coronarender #vray #blender3d #cinema4d #archviz #interiordesign #cyberrender
```

### qrafik-1
```text
03:12. Render hələ 87%-dədir. Təqdimat isə saat 10:00-da. 😮‍💨

Bu gecəni hər dizayner, hər memar, hər animator ən azı bir dəfə yaşayıb. Ventilyator uğuldayır, sən ekrana baxıb dua edirsən ki, işıq sönməsin.

Başqa yol var. Səhnəni göndər, render-i biz hesablayaq. Sən isə yat.

👉 DM-ə “RENDER” yaz. Səhnənə baxıb vaxtı və qiyməti dəqiq deyək.

#archviz #3dsmax #coronarender #rendering #memarlıq #interyerdizayn #baku #cyberrender
```

### qrafik-2
```text
Klient yalnız son şəkli görür. Clay-i, testləri, gecə 2-dəki düzəlişi, 6 saatlıq final render-i görmür.

Amma sən görürsən. Hər saatını.

O saatları bizə ver. Sən dizayna qayıt.

👉 DM-ə “RENDER” yaz, ilk səhnəni birlikdə hesablayaq.

#archviz #coronarender #3dsmax #interiordesign #clayrender #3dvisualization #baku #cyberrender
```

## Paylaşmazdan əvvəl

- [ ] Fotoreal AI şəkillər üçün Instagram-da “AI info” etiketi (F8)
- [ ] Karuseldəki proqram siyahısı sahədə **istifadə olunan** proqramlardır. Cyber Render-in dəstəklədiyi siyahı bioda olsun.
- [ ] `Ə ə ğ ı ş ç ö ü` hərfləri final PNG-də düzgün görünür
