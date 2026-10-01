# 04 · Google Flow ilə istehsal iş axını

Flow (flow.google) Google-un Veo video və şəkil modelləri ilə işləyən alətidir. Bu sənəd paketdəki postların Flow-da necə hazırlanacağını addım-addım göstərir.

> Flow-un interfeysi və rejim adları tez-tez dəyişir. Aşağıdakı adlar (Text to Video, Frames to Video, Ingredients to Video, Extend, Scenebuilder) yazıldığı vaxtkı versiyaya aiddir. Ad fərqlidirsə, eyni funksiyanı axtar.

---

## 0. Hazırlıq (bir dəfə)

1. Flow-da layihə aç: **"Cyber Render · IG · Oktyabr"**.
2. Bu iki bloku qeydlərində saxla, hər promptda lazım olacaq:
   - **Brend görünüşü bloku**: `02-rule-set.md`, F3 bölməsi. Paketdəki promptlara artıq əlavə olunub.
   - **Gil personaj kartının promptu**: `03-postlar.md`, P05.
3. Montaj üçün: **CapCut** (reels) və **Canva/Figma** (karusellər). Brend şriftlərini (Tektur, Onest, JetBrains Mono) quraşdır və **Ə ə** hərflərini yoxla.

## 1. Əvvəl "ingredient" kitabxanası

Təkrarlanan obyektlər əvvəlcə şəkil kimi yaradılır. Videolarda istinad olaraq işlədilir ki, kadrdan kadra dəyişməsin.

| Ingredient | Harada lazımdır | Prompt |
|---|---|---|
| Studiya otağı | P01 (A və B klipləri) | `03-postlar.md` → P01 |
| Gil maket (memarlıq) | P10 (B və C klipləri) | `03-postlar.md` → P10 |
| Gil personaj kartı | P05, P12 | `03-postlar.md` → P05 |
| Bakı mənzili: final + clay | P03 | `03-postlar.md` → P03 |

**Qayda:** hər ingredient üçün 4 variant yarat, ən təmizini saxla. Gil-in "üzü" görünürsə və ya forması fərqlidirsə, at (F5, F7).

## 2. Rejim seçimi

| Nə lazımdır | Flow rejimi | Paketdə nümunə |
|---|---|---|
| Sıfırdan atmosfer klipi | **Text to Video** | P06, P08, P11 |
| Eyni məkan və ya personaj ardıcıl görünsün | **Ingredients to Video** (istinad şəkilləri ilə) | P01, P10 |
| Başlanğıc və son kadr dəqiq olsun (clay → final) | **Frames to Video** | P03 |
| Klip 8 saniyədən uzun olsun | **Extend** / **Scenebuilder** | P06, P11 |
| Karusel şəkli | Şəkil yaratma (Image) | P02, P04, P05, P07, P09, P12 |

## 3. Bir klipin istehsalı (addım-addım)

1. **Ölçü:** reels üçün **9:16 (portrait)**.
2. **Promptu yapışdır.** Promptlar ingiliscədir (F1). Brend bloku artıq sonundadır.
3. **Əvvəl sürətli/ucuz model** (məsələn, Veo Fast). 2–4 variant yarat, promptu kilidlə (F6).
4. Yaxşı variant tapılanda **keyfiyyət modeli** ilə yenidən yarat.
5. Lazım olsa **Extend** ilə davam etdir, və ya **Scenebuilder**-də klipləri ardıcıl düz.
6. **Yüklə** (ən yüksək mövcud keyfiyyət, mümkünsə 1080p və ya upscale).

**Yoxlama:**
- [ ] Ekranlarda oxunan saxta yazı yoxdur (V10, V11)
- [ ] İnsan üzü yoxdur və ya təhrif olunmayıb (F7)
- [ ] Fizika düzgündür (əşyalar "əriyib axmır")
- [ ] Nanə imza işığı kadrdadır (V2)
- [ ] Səs qaralamadır, finalda lisenziyalı musiqi ilə əvəz olunur (V14)

## 4. Karusel şəkilləri

1. Flow-un şəkil rejimində **portrait** seç (3:4 və ya 9:16, hansı varsa).
2. Promptu yapışdır. Gil slaydlarında Gil kartını **istinad şəkli** kimi əlavə et.
3. Canva/Figma-da **1080×1350 (4:5)** kətana yerləşdir. Mətn üçün boş saxlanmış sahəyə başlıq qoy.
4. "Brend kartı" yazılan slaydlar Flow-suz, birbaşa şablonda hazırlanır.

## 5. Montaj (CapCut)

- Kətan **1080×1920**. Mətn təhlükəsiz zonada: aşağı 20% və sağ 15% boş (V7).
- **Hook mətni 0-cı saniyədə** görünür, animasiya gecikməsi yoxdur (M1).
- Mətn: Tektur, ağ və ya Mint, lazım olsa Charcoal lövhə üzərində.
- **Son kadr** (V15): Mint fon, loqo, bir cümlə, CTA. Şablonu bir dəfə hazırla, hər reel-də təkrar işlət.
- **Səs imzası** (V14): ventilyator → sükut → ding.
- Altyazı: Instagram-ın avtomatik altyazısı azərbaycancada səhv edə bilər. Mətni əl ilə ver.
- Export: 1080×1920, 30 fps, yüksək bitreyt.

## 6. Paylaşma

1. Fotoreal AI video və şəkil üçün Instagram-da **"AI info"** etiketini aç (F8).
2. Caption və heşteqlər `03-postlar.md`-dən.
3. Reel üçün örtük (cover) seç: hook mətni olan kadr, grid tonuna uyğun (D və ya M, bax `05-kontent-teqvimi.md`).
4. Açar söz avtomatlaşdırması (RENDER / STUDIO / KADR) qurulubsa, işlədiyini yoxla.
5. İlk 30 dəqiqədə şərhlərə cavab ver. Alqoritm erkən aktivliyi sevir.

## 7. Nəyi Flow-da etmirik

| İş | Səbəb | Əvəzinə |
|---|---|---|
| Loqo, yazı, rəqəm | AI hərfləri təhrif edir | CapCut/Canva overlay |
| 3ds Max/Blender interfeysi | AI interfeysi saxta görünür | Real ekran yazısı |
| "Klientimizin render-i" | Etik və brend riski (V9) | Real render, klient icazəsi ilə |
| Proqram loqoları | Əmtəə nişanı, təhrif | Mətnlə proqram adı |
| Tanınmış binalar və ya şəxslər | Hüquqi və etik risk | Orijinal arxitektura |
