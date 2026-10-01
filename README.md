# Cyber Render · Instagram kontent paketi

Dizaynerlər, memarlar, dizayn/memarlıq studiyaları və animatorlar üçün 4 həftəlik Instagram seriyası. Vizuallar **Google Flow** (Veo + şəkil modeli) ilə hazırlanır.

## Fayllar

| Fayl | Nə var |
|---|---|
| [`instagram/01-biznes-analizi.md`](instagram/01-biznes-analizi.md) | Brend, auditoriya, emosional xəritə, mövqe, təsdiq siyahısı |
| [`instagram/02-rule-set.md`](instagram/02-rule-set.md) | Vizual, mətn, psixologiya və Flow prompt qaydaları (V, M, P, F kodları) |
| [`instagram/03-postlar.md`](instagram/03-postlar.md) | 12 post: hook, Flow promptları, ekran mətni, caption, CTA, montaj |
| [`instagram/04-google-flow-is-axini.md`](instagram/04-google-flow-is-axini.md) | Flow-da addım-addım istehsal |
| [`instagram/05-kontent-teqvimi.md`](instagram/05-kontent-teqvimi.md) | 4 həftəlik təqvim, grid ritmi, stories, ölçmə |
| [`instagram/board.html`](instagram/board.html) | Kopyalama düymələri olan interaktiv board (eyni məzmun) |
| `instagram/assets/` | Loqo |

## Postları dəyişmək

`03-postlar.md`, `05-kontent-teqvimi.md` və `board.html` eyni mənbədən yaradılır: `instagram/data/posts.py`.

```bash
python3 scripts/build.py
```

## Paylaşmazdan əvvəl

`[kvadrat mötərizədə]` olan hər şey saytdan təsdiqlənməlidir: proqram siyahısı, qiymət, proses, sürət, təkliflər.
Paket yazılanda sayt və Instagram iş mühitindən açılmırdı. Tam siyahı `01-biznes-analizi.md`-nin sonundadır.
