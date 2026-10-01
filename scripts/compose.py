#!/usr/bin/env python3
"""Batch 01: 1 carousel (6 slides) + 2 graphic posts, composed from Google Flow images.

1. Generate the 8 images in Google Flow with the prompts in instagram/batch-01/README.md.
2. Put them in instagram/batch-01/flow/ named by key (k1-cover.png, q2-clay.jpg, ...).
3. Run: python3 scripts/compose.py
   -> instagram/batch-01/final/*.png (1080x1350, 4:5)
   Missing images are drawn as labelled placeholders and the file is named *.preview.png.
"""
import base64
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH = ROOT / "instagram" / "batch-01"
FLOW_DIR = BATCH / "flow"
OUT_DIR = BATCH / "final"
HTML_DIR = BATCH / ".html"
FONTS = ROOT / "scripts" / "fonts"
sys.path.insert(0, str(ROOT / "instagram" / "data"))
import posts as D  # noqa: E402

MINT, CHAR, INK, SIGNAL = "#DDFFD4", "#2A2A2A", "#1B1D1B", "#7DFA6A"

P04 = next(p for p in D.POSTS if p["id"] == "P04")
P03 = next(p for p in D.POSTS if p["id"] == "P03")
P01 = next(p for p in D.POSTS if p["id"] == "P01")

# --------------------------------------------------------------------------- Flow images
FLOW = [
    {"key": "k1-cover", "used": "Karusel · slayd 1", "prompt": P04["shots"][0]["prompt"]},
    {"key": "k2-memarliq", "used": "Karusel · slayd 2", "prompt": P04["shots"][1]["prompt"]},
    {"key": "k3-interyer", "used": "Karusel · slayd 3", "prompt": P04["shots"][2]["prompt"]},
    {"key": "k4-animasiya", "used": "Karusel · slayd 4", "prompt": P04["shots"][3]["prompt"]},
    {"key": "k5-mehsul", "used": "Karusel · slayd 5", "prompt": P04["shots"][4]["prompt"]},
    {
        "key": "q1-studiya-gece",
        "used": "Qrafik post 1",
        "prompt": (
            "Portrait composition. Night, 3 a.m., a small design studio. Over-the-shoulder view from behind a "
            "young designer (face not visible) slumped in an office chair in front of a large monitor; the monitor "
            "shows a half-finished architectural interior render built from square tiles, the lower rows of tiles "
            "still grey and empty. Empty coffee cups, crumpled sketches and a white scale architectural model on the "
            "desk. Light sources: cold monitor glow and a faint pale-mint desk lamp. The upper 40% of the frame is "
            "dark and uncluttered (wall in shadow) to hold large text. " + D.LOOK_NIGHT
        ),
    },
    {
        "key": "q2-final",
        "used": "Qrafik post 2 · final yarı",
        "prompt": P03["ingredients"][0]["prompt"].replace("Portrait 9:16.", "Portrait composition."),
    },
    {
        "key": "q2-clay",
        "used": "Qrafik post 2 · clay yarı",
        "note": "q2-final şəklini istinad (ingredient) kimi əlavə et, sonra bu promptu yaz.",
        "prompt": P03["ingredients"][1]["prompt"],
    },
]

# --------------------------------------------------------------------------- slide content
FIELDS = [
    ("k2-memarliq", "MEMARLIQ", [("MODELLƏMƏ", ["Revit", "ArchiCAD", "SketchUp", "Rhino"]),
                                 ("RENDER / VİZUALİZASİYA", ["3ds Max", "Corona", "V-Ray", "Lumion", "Twinmotion", "Enscape", "D5"])]),
    ("k3-interyer", "İNTERYER", [("MODELLƏMƏ", ["3ds Max", "SketchUp"]),
                                 ("RENDER", ["Corona", "V-Ray", "D5 Render", "Enscape"])]),
    ("k4-animasiya", "ANİMASİYA / MOTION", [("PROQRAM", ["Blender", "Cinema 4D", "Maya", "Houdini", "Unreal Engine"]),
                                            ("RENDER MÜHƏRRİKİ", ["Cycles", "Redshift", "Octane", "Arnold", "Karma"])]),
    ("k5-mehsul", "MƏHSUL VİZUALI", [("PROQRAM", ["KeyShot", "Blender", "Cinema 4D", "3ds Max", "Rhino"]),
                                     ("RENDER", ["KeyShot", "Redshift", "Cycles", "V-Ray"])]),
]

CAPTIONS = {
    "karusel": (
        "Memar, interyer dizayneri, animator: hər kəsin öz proqram dəsti var. Bəs səninki hansıdır?\n\n"
        "Swipe et, öz sahəni tap 👉\n"
        "Max + Corona komandası? Blender sevərləri? C4D + Redshift?\n\n"
        "👇 Şərhə proqramını yaz. Ən çox yazılan proqram üçün növbəti postda render vaxtını qısaldan "
        "praktik bələdçi paylaşacağıq.\n\n"
        "Dəstəklənən proqramların tam siyahısı: link bioda.\n\n" + P04["hashtags"]
    ),
    "qrafik-1": P01["caption"] + "\n\n" + P01["hashtags"],
    "qrafik-2": P03["caption"] + "\n\n" + P03["hashtags"],
}


# --------------------------------------------------------------------------- helpers
def b64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()


def font_css():
    out = []
    for f in json.loads((FONTS / "fonts.json").read_text()):
        out.append(
            f"@font-face{{font-family:'{f['family']}';font-weight:100 900;font-display:block;"
            f"src:url(data:font/woff2;base64,{b64(FONTS / f['file'])}) format('woff2');"
            f"unicode-range:{f['range']};}}"
        )
    return "\n".join(out)


def find_image(key):
    for ext in ("png", "jpg", "jpeg", "webp"):
        p = FLOW_DIR / f"{key}.{ext}"
        if p.exists():
            mime = "jpeg" if ext in ("jpg", "jpeg") else ext
            return f"data:image/{mime};base64,{b64(p)}"
    return None


def bg(key, pos="center", light=False):
    src = find_image(key)
    if src:
        return f'<div class="bg"><img src="{src}" style="object-position:{pos}"></div>', True
    cls = "ph light" if light else "ph"
    return f'<div class="bg {cls}"><span>FLOW ŞƏKLİ<br>{key}</span></div>', False


def prog(n, total, ink=False):
    segs = "".join(f'<i class="{"on" if i < n else ""}"></i>' for i in range(total))
    return f'<div class="prog{" ink" if ink else ""}"><span>{n:02d} / {total:02d}</span><div class="segs">{segs}</div></div>'


def logo(style, ink=False):
    return f'<div class="logo{" ink" if ink else ""}" style="{style}"></div>'


def chips(items):
    return "".join(f'<span class="chip">{c}</span>' for c in items)


# --------------------------------------------------------------------------- slides
def slide_cover():
    b, ok = bg("k1-cover", "center 60%")
    return ok, f"""
{b}
<div class="scrim" style="background:linear-gradient(180deg,rgba(27,29,27,.92) 0%,rgba(27,29,27,.6) 36%,rgba(27,29,27,0) 60%,rgba(27,29,27,0) 78%,rgba(27,29,27,.75) 100%)"></div>
{prog(1, 6)}
<p class="kicker" style="top:118px">CYBER RENDER · PROQRAM XƏRİTƏSİ</p>
<h1 class="disp" style="position:absolute;left:72px;top:172px;font-size:128px;line-height:.98">SƏNİN<br>SAHƏN<br>HANSIDIR?</h1>
<div class="tag" style="position:absolute;left:72px;top:600px">PROQRAMINI TAP →</div>
<p class="kicker" style="bottom:86px;top:auto">SÜRÜŞDÜR →</p>
{logo("width:230px;right:72px;bottom:70px")}
"""


def slide_field(i, key, title, groups):
    b, ok = bg(key, "center 35%")
    rows = "".join(f'<div class="grp"><span class="gl">{lab}</span><div class="chips">{chips(items)}</div></div>'
                   for lab, items in groups)
    return ok, f"""
{b}
<div class="scrim" style="background:linear-gradient(180deg,rgba(27,29,27,.8) 0%,rgba(27,29,27,0) 20%)"></div>
{prog(i, 6)}
<div class="panel">
  <p class="lab">{i:02d} · SAHƏ</p>
  <div class="trow"><h2 class="disp" style="font-size:{96 if len(title) < 12 else 76}px;line-height:1">{title}</h2>{logo("position:static;width:150px;flex:none")}</div>
  {rows}
</div>
"""


def slide_cta():
    return True, f"""
<div class="bg" style="background:{MINT}"></div>
<div class="mark" style="width:1300px;right:-430px;top:470px"></div>
{prog(6, 6, ink=True)}
<p class="kicker ink" style="top:118px">06 · SƏNİN NÖVBƏN</p>
<h2 class="disp ink" style="position:absolute;left:72px;top:172px;font-size:112px;line-height:.98">SƏNİN<br>PROQRAMIN<br>HANSIDIR?</h2>
<p class="body ink" style="position:absolute;left:72px;top:560px;width:860px">Şərhə yaz. Ən çox yazılan proqram üçün növbəti postda render vaxtını qısaldan praktik bələdçi paylaşacağıq.</p>
<div class="tag dark" style="position:absolute;left:72px;top:820px">ŞƏRHƏ YAZ ↓</div>
<p class="kicker ink" style="bottom:92px;top:auto;max-width:560px;line-height:1.5">Dəstəklənən proqramların<br>tam siyahısı: link bioda</p>
{logo("width:240px;right:72px;bottom:72px", ink=True)}
"""


def post_night():
    b, ok = bg("q1-studiya-gece", "center 70%")
    return ok, f"""
{b}
<div class="scrim" style="background:linear-gradient(180deg,rgba(20,22,20,.93) 0%,rgba(20,22,20,.7) 40%,rgba(20,22,20,.15) 62%,rgba(20,22,20,0) 72%)"></div>
<p class="kicker" style="top:72px">CYBER RENDER</p>
{logo("width:150px;right:72px;top:58px")}
<p class="time">03:12</p>
<h1 class="disp" style="position:absolute;left:72px;top:398px;font-size:76px;line-height:1.02">RENDER HƏLƏ<br><span class="num">87%</span>-DƏDİR.</h1>
<div class="bar"><div class="fill"></div><span>87%</span></div>
<p class="kicker" style="top:676px;color:rgba(221,255,212,.7)">RENDERING · QALAN VAXT: ∞</p>
<div class="panel mint">
  <div class="trow"><h2 class="disp ink" style="font-size:84px;line-height:1">RENDER BİZDƏ.<br>SƏN YAT.</h2>{logo("position:static;width:170px;flex:none", ink=True)}</div>
  <div class="tag dark" style="margin-top:28px">DM: RENDER</div>
</div>
"""


def post_split():
    b, ok_final = bg("q2-final", "center")
    clay_src = find_image("q2-clay")
    ok = ok_final and bool(clay_src)
    clay = (f'<img src="{clay_src}" style="width:100%;height:100%;object-fit:cover">' if clay_src
            else '<div class="ph light" style="position:absolute;inset:0"><span style="transform:translateX(-200px)">FLOW ŞƏKLİ<br>q2-clay</span></div>')
    return ok, f"""
{b}
<div class="clay">{clay}<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(244,246,242,.6) 0%,rgba(244,246,242,0) 38%)"></div></div>
<svg class="diag" viewBox="0 0 1080 1350"><line x1="712.8" y1="0" x2="367.2" y2="1350" stroke="{MINT}" stroke-width="8"/></svg>
<h1 class="disp ink" style="position:absolute;left:72px;top:96px;font-size:84px;line-height:1">KLİENT BUNU<br>HEÇ VAXT<br>GÖRMÜR.</h1>
<div class="tag dark" style="position:absolute;left:72px;top:430px">SƏN: CLAY · TEST · DÜZƏLİŞ</div>
<div class="tag" style="position:absolute;right:72px;top:660px">KLİENT: YALNIZ BUNU</div>
<div class="panel">
  <div class="trow"><h2 class="disp" style="font-size:58px;line-height:1.05">ARADA QALAN RENDER<br>SAATLARINI BİZƏ VER.</h2>{logo("position:static;width:150px;flex:none")}</div>
  <div class="tag" style="margin-top:28px">DM: RENDER</div>
</div>
"""


CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:{INK}}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:Onest,sans-serif;color:{MINT}}}
.bg{{position:absolute;inset:0}}
.bg img{{width:100%;height:100%;object-fit:cover;display:block}}
.ph{{display:grid;place-items:center;background-color:#30342F;
  background-image:linear-gradient(rgba(221,255,212,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(221,255,212,.08) 2px,transparent 2px);
  background-size:54px 54px;font:500 30px/1.5 'JetBrains Mono';color:rgba(221,255,212,.6);text-align:center;letter-spacing:.1em}}
.ph.light{{background-color:#DADDD7;color:rgba(42,42,42,.55);
  background-image:linear-gradient(rgba(42,42,42,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(42,42,42,.08) 2px,transparent 2px)}}
.scrim{{position:absolute;inset:0}}
.disp{{font-family:Tektur,sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:.005em}}
.ink{{color:{CHAR}}}
.kicker{{position:absolute;left:72px;font:500 24px/1.2 'JetBrains Mono';letter-spacing:.14em;text-transform:uppercase}}
.body{{font:400 38px/1.4 Onest}}
.logo{{position:absolute;aspect-ratio:520/295;background:{MINT};
  -webkit-mask:url(data:image/png;base64,{{LOGO}}) center/contain no-repeat;mask:url(data:image/png;base64,{{LOGO}}) center/contain no-repeat}}
.logo.ink{{background:{CHAR}}}
.mark{{position:absolute;aspect-ratio:600/262;background:{CHAR};opacity:.07;
  -webkit-mask:url(data:image/png;base64,{{MARK}}) center/contain no-repeat;mask:url(data:image/png;base64,{{MARK}}) center/contain no-repeat}}
.num{{font-family:'JetBrains Mono';font-weight:700;letter-spacing:-.03em}}
.prog{{position:absolute;top:56px;left:72px;right:72px;display:flex;align-items:center;gap:20px;font:500 22px 'JetBrains Mono';letter-spacing:.1em}}
.prog .segs{{flex:1;display:flex;gap:8px}}
.prog .segs i{{flex:1;height:6px;background:rgba(221,255,212,.3)}}
.prog .segs i.on{{background:{MINT}}}
.prog.ink{{color:{CHAR}}}
.prog.ink .segs i{{background:rgba(42,42,42,.18)}}
.prog.ink .segs i.on{{background:{CHAR}}}
.tag{{display:inline-block;font:500 30px/1 'JetBrains Mono';letter-spacing:.08em;padding:20px 26px;background:{MINT};color:{CHAR};
  clip-path:polygon(14px 0,100% 0,100% calc(100% - 14px),calc(100% - 14px) 100%,0 100%,0 14px)}}
.tag.dark{{background:{CHAR};color:{MINT}}}
.panel{{position:absolute;left:0;right:0;bottom:0;background:{CHAR};padding:60px 72px 72px;
  clip-path:polygon(64px 0,100% 0,100% 100%,0 100%,0 64px)}}
.panel.mint{{background:{MINT}}}
.lab{{font:500 24px 'JetBrains Mono';letter-spacing:.14em;color:{SIGNAL};margin-bottom:14px}}
.trow{{display:flex;justify-content:space-between;align-items:flex-end;gap:24px}}
.grp{{margin-top:30px}}
.gl{{display:block;font:500 21px 'JetBrains Mono';letter-spacing:.14em;color:rgba(221,255,212,.55);margin-bottom:14px}}
.chips{{display:flex;flex-wrap:wrap;gap:12px}}
.chip{{font:500 28px/1 'JetBrains Mono';padding:14px 18px;background:rgba(221,255,212,.1);color:{MINT};
  clip-path:polygon(10px 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%,0 10px)}}
.time{{position:absolute;left:64px;top:128px;font:700 250px/1 'JetBrains Mono';letter-spacing:-.04em;color:{MINT}}}
.bar{{position:absolute;left:72px;right:72px;top:590px;height:62px;background:rgba(20,22,20,.85);outline:2px solid rgba(221,255,212,.35);outline-offset:-2px;
  clip-path:polygon(12px 0,100% 0,100% calc(100% - 12px),calc(100% - 12px) 100%,0 100%,0 12px)}}
.bar .fill{{position:absolute;left:8px;top:8px;bottom:8px;width:calc(87% - 16px);
  background:repeating-linear-gradient(90deg,{MINT} 0 52px,rgba(221,255,212,.55) 52px 56px)}}
.bar span{{position:absolute;right:20px;top:50%;transform:translateY(-50%);font:700 30px 'JetBrains Mono';color:{MINT}}}
.clay{{position:absolute;inset:0;clip-path:polygon(0 0,66% 0,34% 100%,0 100%)}}
.diag{{position:absolute;inset:0;width:100%;height:100%}}
"""

SLIDES = [
    ("karusel-01", slide_cover),
    *[(f"karusel-{i:02d}", (lambda i=i, f=f: slide_field(i, *f))) for i, f in enumerate(FIELDS, start=2)],
    ("karusel-06", slide_cta),
    ("qrafik-1", post_night),
    ("qrafik-2", post_split),
]


def build_readme():
    out = [
        "# Batch 01 · 1 karusel + 2 qrafik post",
        "",
        "> `scripts/compose.py` ilə yaradılır. Promptlar `instagram/data/posts.py`-dan gəlir.",
        "",
        "## Addımlar",
        "",
        "1. **Google Flow-da** aşağıdakı 8 şəkli yarat. Rejim: şəkil (Image). Ölçü: **portrait** (3:4 və ya 9:16, hansı varsa).",
        "   Hər prompt üçün 2–4 variant yarat, ən təmizini seç: yazı yoxdur, üz yoxdur, xətlər düzdür.",
        "2. Şəkilləri yüklə və **bu söhbətə göndər** (adı və ya sırası ilə: 1 → k1-cover, 2 → k2-memarliq ...).",
        "   Repo ilə işləyirsənsə, `instagram/batch-01/flow/` qovluğuna açar adı ilə qoy (məs. `k2-memarliq.png`).",
        "3. `python3 scripts/compose.py` hazır 1080×1350 PNG-ləri `instagram/batch-01/final/`-a yazır.",
        "   Şəkil çatışmırsa, yerində işarəli boş yer olur və fayl `*.preview.png` adlanır.",
        "",
        "## Flow promptları",
        "",
    ]
    for i, f in enumerate(FLOW, start=1):
        out += [f"### {i}. `{f['key']}` · {f['used']}"]
        if f.get("note"):
            out += [f"> {f['note']}", ""]
        out += ["```text", f["prompt"], "```", ""]
    out += [
        "## Postlar",
        "",
        "| Fayl | Nə |",
        "|---|---|",
        "| `karusel-01…06.png` | Karusel “Sahən hansıdır? Proqramını tap” (6 slayd) |",
        "| `qrafik-1.png` | “03:12. Render hələ 87%-dədir.” |",
        "| `qrafik-2.png` | “Klient bunu heç vaxt görmür.” (clay / final diaqonal) |",
        "",
        "## Caption-lar",
        "",
    ]
    for k, v in CAPTIONS.items():
        out += [f"### {k}", "```text", v, "```", ""]
    out += [
        "## Paylaşmazdan əvvəl",
        "",
        "- [ ] Fotoreal AI şəkillər üçün Instagram-da “AI info” etiketi (F8)",
        "- [ ] Karuseldəki proqram siyahısı sahədə **istifadə olunan** proqramlardır. Cyber Render-in dəstəklədiyi siyahı bioda olsun.",
        "- [ ] `Ə ə ğ ı ş ç ö ü` hərfləri final PNG-də düzgün görünür",
        "",
    ]
    return "\n".join(out)


def build_chrome_brief():
    """Task text to paste into Claude in Chrome, running in the user's own logged-in browser."""
    out = [
        "# Claude in Chrome üçün tapşırıq (Google Flow)",
        "",
        "Bu mətni Chrome-da Claude yan panelinə yapışdır. Əvvəlcə labs.google/flow-u aç və Google hesabına özün daxil ol.",
        "",
        "```text",
        "Google Flow-da (labs.google/flow) işləyirsən. Mən hesaba artıq daxil olmuşam.",
        "Tapşırıq: aşağıdakı 8 şəkli Flow-un şəkil yaratma rejimində yarat.",
        "",
        "Hər şəkil üçün:",
        "1. Ölçünü portrait seç (3:4 varsa onu, yoxdursa 9:16).",
        "2. Promptu dəyişmədən yapışdır və yarat.",
        "3. Variantlardan birini seç: şəkildə yazı/hərf yoxdur, insan üzü görünmür, şaquli xətlər düzdür, açıq nanə-yaşıl işıq var.",
        "4. Seçdiyini yüklə və faylı açar adı ilə adlandır (məs. k2-memarliq.png).",
        "",
        "Qaydalar:",
        "- Ödəniş, abunə, kredit alma və ya hesab ayarları pəncərəsi çıxsa, DAYAN və məndən soruş.",
        "- Heç nəyi paylaşma və dərc etmə. Yalnız yarat və yüklə.",
        "- q2-clay üçün əvvəlcə yaratdığın q2-final şəklini istinad (ingredient) kimi əlavə et.",
        "- Sonda hansı faylları yüklədiyini siyahı ilə yaz.",
        "",
    ]
    for i, f in enumerate(FLOW, start=1):
        out += [f"[{i}] {f['key']}" + (f"  ({f['note']})" if f.get("note") else ""), f["prompt"], ""]
    out += [
        "```",
        "",
        "Şəkillər hazır olanda onları Claude Code söhbətinə göndər. Final 1080×1350 postları oradan yığıram.",
        "",
    ]
    return "\n".join(out)


def main():
    for d in (FLOW_DIR, OUT_DIR, HTML_DIR):
        d.mkdir(parents=True, exist_ok=True)
    css = font_css() + (CSS.replace("{LOGO}", b64(ROOT / "instagram" / "assets" / "logo-mask.png"))
                        .replace("{MARK}", b64(ROOT / "instagram" / "assets" / "logo-mark-mask.png")))
    jobs = []
    for name, fn in SLIDES:
        ok, body = fn()
        out_name = f"{name}.png" if ok else f"{name}.preview.png"
        html = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="slide">{body}</div></body></html>'
        hp = HTML_DIR / f"{name}.html"
        hp.write_text(html, encoding="utf-8")
        # drop a stale counterpart (preview vs final) so final/ only holds the current state
        stale = OUT_DIR / (f"{name}.preview.png" if ok else f"{name}.png")
        stale.unlink(missing_ok=True)
        jobs.append({"html": str(hp), "png": str(OUT_DIR / out_name)})
    (BATCH / "README.md").write_text(build_readme(), encoding="utf-8")
    (BATCH / "CHROME-TAPSIRIQ.md").write_text(build_chrome_brief(), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "scripts" / "render.js")], input=json.dumps(jobs), text=True, check=True)
    for j in jobs:
        print(Path(j["png"]).name)


if __name__ == "__main__":
    main()
