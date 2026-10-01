# 02 · Cyber Render Instagram rule set

Hər postdan əvvəl bu qaydalar yoxlanır. Qaydaların kodları (V = vizual, M = mətn, P = psixologiya, F = Flow) post kartlarında istinad kimi işlədilir.

---

## A. Brend DNT-si (bir baxışda)

- **Kimik:** dizaynerlər, memarlar, studiyalar və animatorlar üçün render gücü.
- **Ton:** *sakit güc.* Dəqiq, həmkar kimi, bir az zarafatcıl. Heç vaxt bağırmırıq, heç vaxt yalvarmırıq.
- **Əsas şüar:** *Sən təsəvvür et. Biz hesablayaq.*
- **Vizual imza:** nanə + kömür, kəsik künclər, qaranlıq səhnədə bir nanə işıq xətti.

## B. Rəng sistemi

| Token | HEX | Rol | Mənbə |
|---|---|---|---|
| **Mint** | `#DDFFD4` | Əsas fon, işıq imzası, açıq postlar | Loqo (dəqiq) |
| **Charcoal** | `#2A2A2A` | Əsas mətn, qaranlıq postlar, forma | Loqo (dəqiq) |
| Ink | `#1B1D1B` | Gecə səhnələri, ən qaranlıq fon | Törəmə |
| Mint 300 | `#B6EFA9` | İkinci dərəcəli forma, qrafik xətlər | Törəmə |
| Signal | `#7DFA6A` | Yalnız kiçik vurğu: progress xətti, nöqtə, ox. Kadrın 5%-indən az. | Törəmə |
| Fog | `#8C948A` | Kiçik yazılar, meta məlumat | Törəmə |

> "Törəmə" rənglər loqodan çıxarılmış təklifdir. Saytda başqa köməkçi rənglər varsa, onlar üstündür.

**V1. İki rəng intizamı.** Brend qrafikasında (overlay, kart, son kadr) Mint + Charcoal ən azı 80% olur. Başqa parlaq rəng qrafikaya girmir.

**V2. Render kadrlarında rəng.** Render vizualı təbii qalır: beton, palıd, şüşə, travertin. Amma **hər kadrda bir nanə element** olur (LED xətti, pəncərə işığı, parça, şüşə). Bu, "Cyber Render işığı"dır.

**V3. Grid ritmi.** Postlar növbə ilə **qaranlıq (D)** və **nanə (M)** örtüklə paylaşılır. 3 sütunlu gridin tək sayda sütunu olduğu üçün D-M-D-M növbəsi avtomatik şahmat taxtası yaradır (bax: `05-kontent-teqvimi.md`).

## C. Forma və tipoqrafiya

**V4. Kəsik künc.** Çərçivə, düymə, etiket, slayd kartı loqodakı kimi 30°/45° kəsik küncə və ya paraleloqram formasına malikdir. Yumru "pill" düymələr və yumşaq kölgələr yoxdur.

**V5. Şriftlər** (Azərbaycan hərfləri yoxlanıb: Ə ə ğ ı ş ç ö ü):

| Rol | Şrift | Qeyd |
|---|---|---|
| Başlıq | **Tektur** (SemiBold/Bold, böyük hərflə) | Künclər kəsikdir, loqonun dilinə yaxındır |
| Mətn | **Onest** (Regular/Medium) | Təmiz və oxunaqlıdır |
| Texniki etiket | **JetBrains Mono** | Rəqəmlər, proqram adları, "render log" stili |

> ⚠️ **Orbitron və Michroma loqoya bənzəyir, amma onlarda `Ə/ə` yoxdur.** Azərbaycanca başlıqda bu hərflər qırılır. İşlətmə.
> Saytda xüsusi brend şrifti varsa, əvvəl onun `Ə ə` hərflərini yoxla.

**V6. Ekranda mətn həcmi.** Bir kadrda ən çox 7 söz. Bir slaydda bir fikir. Başlıq ölçüsü 1080 px enində ən azı 64 px.

**V7. Təhlükəsiz zonalar.**
- Reels (1080×1920): mətn aşağıdakı 20%-ə və sağdakı 15%-ə düşmür, çünki Instagram düymələri orada olur.
- Feed/karusel (1080×1350, 4:5): əsas mətn mərkəzi 1080×1080 sahədə qalır, çünki grid önizləməsi kəsir.

## D. Vizual məzmun qaydaları

**V8. Render birinci.** Hər postun qəhrəmanı render keyfiyyətli vizualdır: interyer, eksteryer, məhsul, motion kadr. Görünüşü "Corona/V-Ray/Redshift-dən çıxıb" hissi verir.

**V9. AI vizual = atmosfer, real render = sübut.** Bu, ən vacib qaydadır.
- Flow-da yaradılan vizual **metafor və əhval** üçündür: render gecəsi, işıq, keçid.
- "Bu, bizim render-imizdir" və ya "klientimizin işidir" deyilən hər post **yalnız real render** ilə hazırlanır (klientin icazəsi ilə).
- Memarlar AI şəklini dərhal tanıyır. Render xidmətinin AI şəklini "öz işi" kimi göstərməsi brendi bir postla yıxa bilər.

**V10. Real UI yalnız real ekran yazısından.** Proqram interfeysi (3ds Max, Blender və s.), progress bar və bildiriş Flow-da yaradılmır, çünki AI interfeysi saxta görünür. Bunlar ya real ekran yazısıdır, ya da CapCut/Figma-da çəkilən sadə qrafikadır.

**V11. Mətn və loqo Flow-da yaradılmır.** Flow-dan "təmiz plan" alırıq: yazısız, loqosuz, mətn üçün boş yer saxlanmış kadr. Yazı və loqo montajda əlavə olunur. AI hərfləri və loqonu təhrif edir.

**V12. Proqram adları mətnlə yazılır.** "3ds Max · Corona · Blender" kimi mətn etiketləri olur. Rəsmi loqoları AI ilə çəkdirmirik. Rəsmi loqo lazımdırsa, istehsalçının brend qaydaları ilə rəsmi fayl götürülür.

**V13. Hərəkət qrammatikası.**
- Kamera "render kamerası" kimi hərəkət edir: yavaş dolly, orbit, crane. Bir klipdə bir hərəkət olur.
- **İmza keçidlər:** *Clay → Final*, *Noise → Clean*, *Bucket reveal* (kafel-kafel açılma), *Wireframe → Render*. Hər reel bunlardan birini işlədir.

**V14. Səs imzası.** *Ventilyator uğultusu → sükut → yumşaq "ding".* Bu, ağrıdan rahatlığa keçidin səsidir. Veo-nun yaratdığı səs qaralama sayılır. Final musiqi lisenziyalı olur.

**V15. Son kadr (end card).** Reel-in son 1.5 saniyəsi belə qurulur: Mint fon, loqo, bir cümlə, bir CTA. Loqo heç vaxt əvvəldə gəlmir.

## E. Mətn (copy) qaydaları

**M1. Hook ilk saniyədədir.** İlk kadrda hərəkət və mətn birlikdə olur. Hook növləri:
1. **Saat və an:** "03:12. Render hələ 87%-dədir."
2. **Riyaziyyat:** "1 kadr = 4 dəq. 1 dəqiqəlik animasiya = ?"
3. **Seqmenti çağırmaq:** "Corona-da işləyirsənsə, bunu yadda saxla."
4. **Gizli həqiqət:** "Klient yalnız sonu görür."
5. **Ziddiyyət:** "Bu noise sənin deyil."
6. **POV/meme:** "Render başlayanda vs. 3 saat sonra."

**M2. Həmkar kimi danış.** Müraciət "sən" formasındadır. Sahənin dili işlənir: render, sample, noise, denoiser, kadr, rakurs, klient, düzəliş, deadline. Korporativ dil yoxdur ("innovativ həllər təqdim edirik" yazılmır).

**M3. Bir post = bir emosiya = bir CTA.**

**M4. Caption strukturu:**
1. 1-ci sətir: hook, ən çox 125 simvol ("daha çox" düyməsindən əvvəl görünən hissə).
2. 2–4 qısa sətir: ağrı, sonra çıxış yolu.
3. 1 sətir: detal və ya sübut.
4. CTA.
5. 5–8 heşteq.

**M5. CTA pilləkəni** (təzyiq tədricən artır):

| Pillə | Nümunə | Nə vaxt |
|---|---|---|
| Yumşaq | "Yadda saxla", "Render-i bitməyən dostuna göndər" | Təhsil və meme postları |
| Orta | "Şərhə proqramını yaz", "Şərhə KADR yaz" | Etiraz yox, məlumat toplanır |
| Birbaşa | "DM-ə RENDER yaz", "Link bioda" | Ağrı və təklif postları |

**Açar söz sistemi:** `RENDER` (ümumi), `STUDIO` (studiyalar), `KADR` (animatorlar).
Şərh və ya DM açar sözü avtomatlaşdırılmış DM ilə cavablandırıla bilər (Chatplace, ManyChat və s.).

**M6. Rəqəmlər yalnız doğrudursa.** Arifmetika (1500 kadr × 4 dəq = 100 saat) həmişə olar. Sürət ("X dəfə sürətli"), qiymət, GPU sayı yalnız təsdiqlənmiş fakt kimi yazılır. Təsdiqlənməyənlər `[mötərizədə]` qalır.

**M7. Heşteqlər:** 5–8 ədəd, qarışıq:
- Niş: `#archviz #3dsmax #coronarender #vray #blender3d #cinema4d`
- Sahə: `#interiordesign #architecture #motiondesign`
- Yerli: `#memarlıq #interyerdizayn #baku #azerbaijan`
- Brend: `#cyberrender`

## F. Psixoloji tətiklər (etik çərçivədə)

Peşəkar auditoriyanı yalan iddia ilə "manipulyasiya" etmək bir dəfə işləyir, sonra brendi yandırır. Ona görə tətiklər **real ağrıya və real faydaya** dayanır.

| Kod | Tətik | Necə işlədirik | Post |
|---|---|---|---|
| **P1** | İtki qorxusu | Gecələri, saatları, yuxunu, klienti itirmək | P01, P08 |
| **P2** | Konkret riyaziyyat | Abstrakt "vaxt itir" yox, "100 saat" | P02, P11 |
| **P3** | Qrup kimliyi | "Bunu yalnız 3D adamı başa düşər" meme-ləri. Paylaşım gətirir. | P05 |
| **P4** | Kontrast | Gecə/səhər, clay/final, noise/clean | P01, P03, P06 |
| **P5** | Qarşılıqlılıq | Pulsuz faydalı bilik verilir, sonra xidmət xatırladılır | P07 |
| **P6** | Status və qürur | Klientin "vau"su, qalib təqdimat | P08, P10 |
| **P7** | Kiçik öhdəlik | Şərhə bir söz yazmaq, sonra DM, sonra sifariş | P02, P04, P11 |
| **P8** | Sağlam düşüncə (B2B) | Workstation-ın gizli xərcləri | P09 |
| **P9** | Təcililik | Yalnız **real** müddətli təklif olanda | `[təklif]` |

**Qadağan:** saxta rəy, saxta klient işi, saxta "son 3 yer", təsdiqlənməmiş sürət və qiymət iddiası, real şəxslərin və ya tanınmış binaların AI ilə "bizim işimiz" kimi göstərilməsi.

## G. Google Flow prompt qaydaları

**F1. Promptlar ingiliscədir.** Model ingiliscəni daha dəqiq başa düşür. Ekrandakı mətn və caption azərbaycancadır.

**F2. Prompt anatomiyası** (bu ardıcıllıqla):
`format → subyekt → hərəkət → məkan → kamera (növ, hərəkət, linza) → işıq → material və palitra → stil → səs → istisnalar`

**F3. Brend görünüşü bloku.** Hər promptun sonuna əlavə olunur:

```
Color palette: neutral natural materials (charcoal concrete, light oak, glass, travertine) with one soft pale-mint-green accent light (#DDFFD4) and deep charcoal shadows (#2A2A2A). High-end architectural visualization look, physically based global illumination, crisp detail, subtle film grain, calm and precise mood. No text, no letters, no logos, no watermarks, no user interface elements.
```

**F4. Bir klip = bir hərəkət = 8 saniyə.** Uzun reel 2–3 klipin birləşməsidir (Scenebuilder və ya CapCut).

**F5. Ardıcıllıq üçün "ingredient".** Təkrarlanan məkan və personaj (studiya otağı, "Gil" maskotu) əvvəl şəkil kimi yaradılır. Sonra *Ingredients to Video* və ya *Frames to Video* ilə istinad edilir.

**F6. Əvvəl ucuz, sonra keyfiyyət.** Prompt sürətli və ucuz model (Fast) ilə kilidlənir. Yalnız seçilmiş klip keyfiyyətli modellə yaradılır və böyüdülür.

**F7. İnsan üzü yoxdur.** İnsan arxadan, bulanıq və ya siluet kimi görünür. Bu, AI üz artefaktlarının qarşısını alır, izləyicinin də özünü yerinə qoymasını asanlaşdırır.

**F8. AI açıqlaması.** Fotoreal AI video paylaşanda Instagram-ın "AI info" etiketi qoyulur. Veo klipləri SynthID su nişanı daşıyır.

## H. Yoxlama siyahısı (paylaşmazdan əvvəl)

- [ ] İlk 1 saniyədə hook və hərəkət var
- [ ] Nanə imza işığı kadrdadır
- [ ] AI vizual "bizim işimiz" kimi təqdim olunmayıb (V9)
- [ ] Bütün rəqəmlər doğrudur və ya `[mötərizə]` ilə dəyişdirilib (M6)
- [ ] `Ə ə ğ ı ş ç ö ü` düzgün görünür
- [ ] Mətn təhlükəsiz zonadadır (V7)
- [ ] Bir CTA var və açar sözlə uyğundur (M5)
- [ ] Son kadrda loqo var, əvvəldə yoxdur (V15)
- [ ] Fotoreal AI üçün "AI info" etiketi qoyulub (F8)
