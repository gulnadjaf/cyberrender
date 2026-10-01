#!/usr/bin/env python3
"""Build the Cyber Render Instagram pack from instagram/data/posts.py.

Outputs:
  instagram/03-postlar.md         every post: hook, Flow prompts, overlays, caption
  instagram/05-kontent-teqvimi.md 4-week calendar, grid rhythm, stories
  instagram/board.html            interactive board with copy buttons (published as an Artifact)

Usage: python3 scripts/build.py
"""
import base64
import datetime as dt
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IG = ROOT / "instagram"
sys.path.insert(0, str(IG / "data"))
import posts as D  # noqa: E402

DAY_OFFSETS = [0, 2, 4]  # Mon, Wed, Fri
DAY_NAMES = ["Bazar ertəsi", "Çərşənbə axşamı", "Çərşənbə", "Cümə axşamı", "Cümə", "Şənbə", "Bazar"]
TRIGGERS = {
    "P1": "İtki qorxusu",
    "P2": "Konkret riyaziyyat",
    "P3": "Qrup kimliyi",
    "P4": "Kontrast",
    "P5": "Qarşılıqlılıq",
    "P6": "Status və qürur",
    "P7": "Kiçik öhdəlik",
    "P8": "Sağlam düşüncə",
    "P9": "Təcililik (yalnız real təklif)",
}
TONE = {"D": "Qaranlıq (Charcoal)", "M": "Nanə (Mint)"}


def post_date(order):
    start = dt.date.fromisoformat(D.START_DATE)
    week, slot = divmod(order - 1, 3)
    return start + dt.timedelta(days=7 * week + DAY_OFFSETS[slot])


def fmt_date(d):
    return f"{d.day:02d}.{d.month:02d}.{d.year}"


POSTS = sorted(D.POSTS, key=lambda p: p["order"])
assert [p["order"] for p in POSTS] == list(range(1, len(POSTS) + 1)), "orders must be 1..N"
assert all(post_date(p["order"]).weekday() in (0, 2, 4) for p in POSTS), "START_DATE must be a Monday"
assert all(a["tone"] != b["tone"] for a, b in zip(POSTS, POSTS[1:])), "tones must alternate (rule V3)"


# --------------------------------------------------------------------------- markdown
def build_posts_md():
    out = [
        "# 03 · Postlar: 12 hazır ssenari",
        "",
        "> Bu fayl `scripts/build.py` ilə `data/posts.py`-dan yaradılır. Dəyişikliyi `posts.py`-da et.",
        "> `[kvadrat mötərizə]` saytdan təsdiq lazımdır deməkdir. Qayda kodları (V, M, P, F): `02-rule-set.md`.",
        "> Flow promptları ingiliscədir və kopyalamağa hazırdır. Brend görünüşü bloku artıq daxildir.",
        "",
        "| # | Tarix | Post | Format | Seqment | Grid |",
        "|---|---|---|---|---|---|",
    ]
    for p in POSTS:
        out.append(
            f"| {p['order']:02d} | {fmt_date(post_date(p['order']))} | [{p['id']} · {p['title']}](#{p['id'].lower()}) "
            f"| {p['kind']} | {', '.join(p['segment'])} | {p['tone']} |"
        )
    out.append("")
    for p in POSTS:
        d = post_date(p["order"])
        out += [
            "---",
            "",
            f'<a id="{p["id"].lower()}"></a>',
            f"## {p['id']} · {p['title']}",
            "",
            f"**#{p['order']:02d} · {DAY_NAMES[d.weekday()]}, {fmt_date(d)}, {D.POST_TIME}** · {p['format']}  ",
            f"**Seqment:** {', '.join(p['segment'])} · **Sütun:** {p['pillar']} · **Grid örtüyü:** {TONE[p['tone']]}  ",
            "**Tətiklər:** " + ", ".join(f"{t} {TRIGGERS[t]}" for t in p["triggers"]),
            "",
            f"### Hook\n> **{p['hook']}**",
            "",
            f"**İdeya.** {p['idea']}",
            "",
        ]
        if p["ingredients"]:
            out.append("### 1) Əvvəl yarat: ingredientlər (Flow → şəkil)")
            for ing in p["ingredients"]:
                out += [f"**{ing['name']}**", "```text", ing["prompt"], "```"]
            out.append("")
        out.append("### 2) Kadrlar / slaydlar")
        for s in p["shots"]:
            out.append(f"**{s['label']}** · _{s['mode']}_")
            if s["prompt"]:
                out += ["```text", s["prompt"], "```"]
            overlay = s["overlay"].replace("\n", "  \n")
            out += [f"Ekran mətni:  \n{overlay}", ""]
        out += [
            "### 3) Caption",
            "```text",
            p["caption"] + "\n\n" + p["hashtags"],
            "```",
            f"**CTA:** {p['cta']}",
            "",
            "### 4) Montaj qeydləri",
        ]
        out += [f"- {e}" for e in p["edit"]]
        if p["verify"]:
            out += ["", "### ⚠️ Paylaşmazdan əvvəl təsdiq et"]
            out += [f"- [ ] {v}" for v in p["verify"]]
        out.append("")
    return "\n".join(out)


def build_calendar_md():
    out = [
        "# 05 · Kontent təqvimi (4 həftə) və grid planı",
        "",
        "> `scripts/build.py` ilə yaradılır.",
        f"> Saat: {D.POST_TIME} (Bakı) başlanğıc fərziyyəsidir. 2 həftədən sonra Instagram Insights-da auditoriyanın aktiv saatına görə düzəlt.",
        "",
        "## Təqvim",
        "",
        "| # | Gün | Tarix | Post | Format | Seqment | CTA | Grid |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for p in POSTS:
        d = post_date(p["order"])
        out.append(
            f"| {p['order']:02d} | {DAY_NAMES[d.weekday()]} | {fmt_date(d)} | {p['id']} · {p['title']} | "
            f"{p['kind']} | {', '.join(p['segment'])} | {p['cta']} | {p['tone']} |"
        )
    out += [
        "",
        "**Həftələrin məntiqi**",
        "1. **Həftə 1. Kimik?** Brend filmi, proqramlar (auditoriya özünü tapır), ilk ağrı postu.",
        "2. **Həftə 2. Faydalıyıq.** Təhsil karuseli, clay → final kontrastı, paylaşılan meme.",
        "3. **Həftə 3. Animatorlar və studiyalar.** Kadr riyaziyyatı, klientin gecə mesajı.",
        "4. **Həftə 4. Qərar.** Workstation məntiqi, keyfiyyət, 3 addımda sifariş (pin).",
        "",
        "## Grid ritmi (V3)",
        "",
        "Postlar növbə ilə **D** (qaranlıq) və **M** (nanə) örtüklə paylaşılır. Gridin 3 sütunu (tək say) olduğu üçün",
        "bu növbə avtomatik şahmat taxtası yaradır. Ay sonunda profil belə görünür (ən yeni post sol yuxarıda):",
        "",
        "```text",
    ]
    rev = list(reversed(POSTS))
    for i in range(0, len(rev), 3):
        row = rev[i:i + 3]
        out.append("  ".join(f"[{p['tone']} {p['id']}]" for p in row))
    out += [
        "```",
        "",
        "## Stories (hər həftə 3–5 story)",
        "",
        "| Növ | Nümunə |",
        "|---|---|",
    ]
    out += [f"| {k} | {v} |" for k, v in D.STORIES]
    out += [
        "",
        "## Ölçmə (hər həftənin sonunda)",
        "",
        "| Metrik | Nəyi göstərir | Hansı postlar |",
        "|---|---|---|",
        "| Saxlama (save) | Faydalılıq | P07, P02, P09 |",
        "| Paylaşma (share/send) | Qrup kimliyi, emosiya | P05, P01 |",
        "| Şərh, açar söz | Kiçik öhdəlik, lid | P04, P02, P11 |",
        "| DM (RENDER/STUDIO/KADR) | Satış niyyəti | P01, P03, P08, P09, P12 |",
        "| 3 saniyəlik izlənmə | Hook gücü | Bütün reels |",
        "",
        "Ən yaxşı nəticə verən hook növünü (M1) növbəti ayın postlarında iki dəfə çox işlət.",
        "",
    ]
    return "\n".join(out)


# --------------------------------------------------------------------------- html
def esc(s):
    return html.escape(s, quote=True)


def nl2br(s):
    return "<br>".join(esc(x) for x in s.split("\n"))


def copy_block(text, label="Kopyala"):
    return (
        f'<div class="code"><pre>{esc(text)}</pre>'
        f'<button type="button" class="copy" data-copy="{esc(text)}">{label}</button></div>'
    )


def render_post(p):
    d = post_date(p["order"])
    seg = "".join(f'<span class="chip">{esc(s)}</span>' for s in p["segment"])
    trig = "".join(f'<span class="chip trig" title="{esc(TRIGGERS[t])}">{t} · {esc(TRIGGERS[t])}</span>' for t in p["triggers"])
    parts = [
        f'<article class="post" id="{p["id"].lower()}" data-kind="{esc(p["kind"])}" data-seg="{esc("|".join(p["segment"]))}">',
        '<header class="post-head">',
        f'<div class="post-meta"><span class="ord">#{p["order"]:02d}</span>'
        f'<span class="date">{DAY_NAMES[d.weekday()]}, {fmt_date(d)} · {D.POST_TIME}</span>'
        f'<span class="tone tone-{p["tone"]}" title="{esc(TONE[p["tone"]])}">{p["tone"]}</span></div>',
        f'<p class="pid">{p["id"]} · {esc(p["title"])}</p>',
        f'<h3 class="hook">{esc(p["hook"])}</h3>',
        f'<p class="fmt">{esc(p["format"])}</p>',
        f'<div class="chips">{seg}<span class="chip pillar">{esc(p["pillar"])}</span></div>',
        "</header>",
        f'<p class="idea">{esc(p["idea"])}</p>',
        f'<div class="chips">{trig}</div>',
    ]
    if p["ingredients"]:
        parts.append('<details class="blk"><summary>Əvvəl yarat: ingredientlər <span class="n">'
                     f'{len(p["ingredients"])}</span></summary><div class="blk-body">')
        for ing in p["ingredients"]:
            parts.append(f'<div class="shot"><p class="shot-label">{esc(ing["name"])}</p>'
                         f'<span class="mode">Flow · Image</span>{copy_block(ing["prompt"])}</div>')
        parts.append("</div></details>")
    open_attr = " open" if p["order"] == 1 else ""
    parts.append(f'<details class="blk"{open_attr}><summary>Kadrlar və slaydlar <span class="n">'
                 f'{len(p["shots"])}</span></summary><div class="blk-body">')
    for s in p["shots"]:
        parts.append(f'<div class="shot"><p class="shot-label">{esc(s["label"])}</p>'
                     f'<span class="mode">{esc(s["mode"])}</span>')
        if s["prompt"]:
            parts.append(copy_block(s["prompt"]))
        parts.append(f'<div class="overlay"><span class="ov-tag">Ekran mətni</span><p>{nl2br(s["overlay"])}</p></div></div>')
    parts.append("</div></details>")
    cap = p["caption"] + "\n\n" + p["hashtags"]
    parts.append('<details class="blk"><summary>Caption və heşteqlər</summary><div class="blk-body">'
                 + copy_block(cap, "Caption-u kopyala") + "</div></details>")
    parts.append(f'<p class="cta"><span>CTA</span>{esc(p["cta"])}</p>')
    parts.append('<div class="notes"><p class="notes-h">Montaj</p><ul>'
                 + "".join(f"<li>{esc(e)}</li>" for e in p["edit"]) + "</ul></div>")
    if p["verify"]:
        parts.append('<div class="verify"><p class="notes-h">Təsdiq et</p><ul>'
                     + "".join(f"<li>{esc(v)}</li>" for v in p["verify"]) + "</ul></div>")
    parts.append("</article>")
    return "\n".join(parts)


def render_grid():
    tiles = []
    for p in reversed(POSTS):
        icon = "▶" if p["kind"] == "Reel" else "▦"
        tiles.append(
            f'<a class="tile tile-{p["tone"]}" href="#{p["id"].lower()}">'
            f'<span class="t-top"><span>{p["id"]}</span><span aria-label="{esc(p["kind"])}">{icon}</span></span>'
            f'<span class="t-hook">{esc(p["hook"])}</span>'
            f'<span class="t-bot">#{p["order"]:02d} · {fmt_date(post_date(p["order"]))[:5]}</span></a>'
        )
    return "\n".join(tiles)


def render_calendar_rows():
    rows = []
    for p in POSTS:
        d = post_date(p["order"])
        rows.append(
            f'<tr><td class="num">{p["order"]:02d}</td><td>{DAY_NAMES[d.weekday()]}<br><span class="sub">{fmt_date(d)}</span></td>'
            f'<td><a href="#{p["id"].lower()}">{p["id"]} · {esc(p["title"])}</a></td><td>{esc(p["kind"])}</td>'
            f'<td>{esc(", ".join(p["segment"]))}</td><td>{esc(p["cta"])}</td>'
            f'<td><span class="tone tone-{p["tone"]}">{p["tone"]}</span></td></tr>'
        )
    return "\n".join(rows)


def render_verify():
    site = [
        "Xidmətlərin dəqiq siyahısı (render farm, stansiya icarəsi, render xidməti, animasiya)",
        "Dəstəklənən proqram və render mühərrikləri",
        "Aparat: GPU/CPU modelləri və sayı (yalnız real rəqəmlər)",
        "Qiymət modeli (saat, kadr, paket, abunə)",
        "Sifariş prosesi: fayl necə göndərilir, nəticə necə qayıdır",
        "Hazırlanma müddəti və sürət iddiaları",
        "Aktiv təklif (pulsuz test render, ilk sifarişə endirim)",
        "Məxfilik və NDA siyasəti",
        "Saytın şrifti və köməkçi rəngləri",
        "Cyber Arena ilə əlaqə (brend hekayəsi üçün)",
    ]
    items = [("Sayt", s) for s in site]
    for p in POSTS:
        items += [(p["id"], v) for v in p["verify"]]
    out = []
    for i, (src, text) in enumerate(items):
        out.append(
            f'<li><input type="checkbox" id="v{i}" data-key="v{i}"><label for="v{i}">'
            f'<span class="src">{esc(src)}</span>{esc(text)}</label></li>'
        )
    return "\n".join(out)


def build_html():
    logo = base64.b64encode((IG / "assets" / "logo-mask.png").read_bytes()).decode()
    tpl = (ROOT / "scripts" / "board.template.html").read_text(encoding="utf-8")
    n_reel = sum(p["kind"] == "Reel" for p in POSTS)
    stories = "".join(f"<li><b>{esc(k)}</b> {esc(v)}</li>" for k, v in D.STORIES)
    repl = {
        "{{LOGO}}": logo,
        "{{N_POSTS}}": str(len(POSTS)),
        "{{N_REEL}}": str(n_reel),
        "{{N_CAROUSEL}}": str(len(POSTS) - n_reel),
        "{{START}}": fmt_date(post_date(1)),
        "{{END}}": fmt_date(post_date(len(POSTS))),
        "{{GRID}}": render_grid(),
        "{{POSTS}}": "\n".join(render_post(p) for p in POSTS),
        "{{CAL_ROWS}}": render_calendar_rows(),
        "{{STORIES}}": stories,
        "{{VERIFY}}": render_verify(),
        "{{LOOK}}": copy_block(D.LOOK, "Bloku kopyala"),
        "{{GIL}}": copy_block(D.GIL_REF, "Gil promptunu kopyala"),
        "{{TIME}}": D.POST_TIME,
    }
    for k, v in repl.items():
        tpl = tpl.replace(k, v)
    assert "{{" not in tpl, "unreplaced placeholder"
    return tpl


def main():
    (IG / "03-postlar.md").write_text(build_posts_md(), encoding="utf-8")
    (IG / "05-kontent-teqvimi.md").write_text(build_calendar_md(), encoding="utf-8")
    (IG / "board.html").write_text(build_html(), encoding="utf-8")
    print("built:", ", ".join(["03-postlar.md", "05-kontent-teqvimi.md", "board.html"]))


if __name__ == "__main__":
    main()
