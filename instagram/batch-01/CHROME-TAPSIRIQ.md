# Claude in Chrome üçün tapşırıq (Google Flow)

Bu mətni Chrome-da Claude yan panelinə yapışdır. Əvvəlcə labs.google/flow-u aç və Google hesabına özün daxil ol.

```text
Google Flow-da (labs.google/flow) işləyirsən. Mən hesaba artıq daxil olmuşam.
Tapşırıq: aşağıdakı 8 şəkli Flow-un şəkil yaratma rejimində yarat.

Hər şəkil üçün:
1. Ölçünü portrait seç (3:4 varsa onu, yoxdursa 9:16).
2. Promptu dəyişmədən yapışdır və yarat.
3. Variantlardan birini seç: şəkildə yazı/hərf yoxdur, insan üzü görünmür, şaquli xətlər düzdür, açıq nanə-yaşıl işıq var.
4. Seçdiyini yüklə və faylı açar adı ilə adlandır (məs. k2-memarliq.png).

Qaydalar:
- Ödəniş, abunə, kredit alma və ya hesab ayarları pəncərəsi çıxsa, DAYAN və məndən soruş.
- Heç nəyi paylaşma və dərc etmə. Yalnız yarat və yüklə.
- q2-clay üçün əvvəlcə yaratdığın q2-final şəklini istinad (ingredient) kimi əlavə et.
- Sonda hansı faylları yüklədiyini siyahı ilə yaz.

[1] k1-cover
Portrait composition. Overhead flat-lay on a charcoal concrete surface, arranged in a precise grid: a white clay architectural model, interior material swatches (light oak, travertine, pale-mint velvet), a small product prototype in brushed metal, and a matte white clay character maquette mid-pose. Soft-box top light, one thin pale-mint light strip along the top edge of the frame, generous empty space in the upper third for a headline. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.

[2] k2-memarliq
Portrait composition. Photorealistic architectural exterior visualization: a modern residential building with a charcoal basalt facade and vertical light-oak fins on a hillside above the Caspian Sea at blue hour, warm interior lights, a thin pale-mint LED line along the roof edge. Eye-level, two-point perspective, 24mm, vertical lines perfectly straight. Lower half of the frame darker to hold text. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.

[3] k3-interyer
Portrait composition. Photorealistic interior visualization of a calm bedroom in a modern Baku apartment: charcoal limewash walls, pale-mint linen bedding, light oak floor and headboard, travertine bedside table, soft morning light through sheer curtains, a thin pale-mint LED cove light. Eye-level, 28mm, vertical lines straight, Corona Renderer look. Lower third kept simple for text. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.

[4] k4-animasiya
Portrait composition. Abstract 3D motion-design still: glossy charcoal and frosted-glass geometric shapes with chamfered edges suspended mid-motion in a dark void, motion-blur trails, a single pale-mint emissive ring, studio lighting, Redshift-style render. Palette strictly deep charcoal (#2A2A2A) and pale mint green (#DDFFD4) with soft neutral highlights. Clean premium 3D render look, physically based lighting, crisp detail. No text, no letters, no logos, no watermarks.

[5] k5-mehsul
Portrait composition. Product render: a minimalist wireless speaker in charcoal fabric and brushed aluminium on a pale-mint pedestal with a chamfered 45-degree edge, soft studio light, crisp reflections, seamless charcoal background. Palette strictly deep charcoal (#2A2A2A) and pale mint green (#DDFFD4) with soft neutral highlights. Clean premium 3D render look, physically based lighting, crisp detail. No text, no letters, no logos, no watermarks.

[6] q1-studiya-gece
Portrait composition. Night, 3 a.m., a small design studio. Over-the-shoulder view from behind a young designer (face not visible) slumped in an office chair in front of a large monitor; the monitor shows a half-finished architectural interior render built from square tiles, the lower rows of tiles still grey and empty. Empty coffee cups, crumpled sketches and a white scale architectural model on the desk. Light sources: cold monitor glow and a faint pale-mint desk lamp. The upper 40% of the frame is dark and uncluttered (wall in shadow) to hold large text. Moody, tense, cinematic, shallow depth of field, subtle film grain; deep charcoal tones with one faint pale-mint (#DDFFD4) light. No readable text on any screen, no logos, no watermarks.

[7] q2-final
Portrait composition. Photorealistic interior visualization of a minimalist living room in a modern Baku apartment at golden hour: charcoal microcement walls, a pale-mint-green velvet sofa, light oak floor, travertine coffee table, sculptural floor lamp, floor-to-ceiling window with a soft hazy view of the Caspian Sea, a thin linear pale-mint LED in the ceiling cove. Eye-level, 24mm, two-point perspective, vertical lines perfectly straight, Corona Renderer look, ultra detailed. No people. Color palette: natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks.

[8] q2-clay  (q2-final şəklini istinad (ingredient) kimi əlavə et, sonra bu promptu yaz.)
Turn this exact image into a clay render: identical camera, geometry, objects and composition; replace all materials with matte white clay, remove all textures and colors, soft ambient occlusion, neutral soft daylight. Keep every object in exactly the same position. No text.

```

Şəkillər hazır olanda onları Claude Code söhbətinə göndər. Final 1080×1350 postları oradan yığıram.
