#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup Rich Menu 2 หน้า (หลัก 6 ปุ่ม + เลือกเพจ 1/2) ตั้งแต่ศูนย์.

ใช้:
    set LINE_CHANNEL_ACCESS_TOKEN=<long-lived token>
    set LINE_USER_ID=<U... แอดมิน>
    python scripts/make_richmenu.py

ทำ: สร้างภาพ 2 หน้า -> สร้างเมนู -> อัปโหลดภาพ -> ตั้ง alias
     (autopost-main/autopost-pages) -> ตั้งหน้าหลักเป็น Default -> ส่งข้อความทดสอบ
จด richMenuId ที่พิมพ์ท้ายไปอัปเดต docs/menus.md
"""
import json
import os
import sys
import urllib.request

TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN", "")
UID = os.environ.get("LINE_USER_ID", "")
if len(TOKEN) < 50:
    sys.exit("ตั้ง LINE_CHANNEL_ACCESS_TOKEN ก่อน (token ยาวๆ จาก LINE Developers)")
if not UID.startswith("U"):
    sys.exit("ตั้ง LINE_USER_ID ก่อน (ขึ้นต้นด้วย U)")

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
os.makedirs(ASSETS, exist_ok=True)
IMG_MAIN = os.path.join(ASSETS, "richmenu-main.png")
IMG_PAGES = os.path.join(ASSETS, "richmenu-pages.png")
ALIAS_MAIN, ALIAS_PAGES = "autopost-main", "autopost-pages"

from PIL import Image, ImageDraw, ImageFont  # pip install pillow

W, H = 2500, 1686
BG, GOLD, WHITE, GRAY = (11, 11, 13), (201, 162, 39), (245, 240, 225), (150, 145, 127)
FONT_B = os.environ.get("FONT_BOLD", r"C:\Windows\Fonts\tahomabd.ttf")
FONT_R = os.environ.get("FONT_REG", r"C:\Windows\Fonts\tahoma.ttf")


def center(d, cx, y, s, font, fill):
    bb = d.textbbox((0, 0), s, font=font)
    d.text((cx - (bb[2] - bb[0]) / 2, y), s, font=font, fill=fill)


def glyph(d, cx, y, ch, size=150):
    try:
        f = ImageFont.truetype(os.environ.get("FONT_EMOJI", r"C:\Windows\Fonts\seguiemj.ttf"), size)
        bb = d.textbbox((0, 0), ch, font=f)
        d.text((cx - (bb[2] - bb[0]) / 2, y), ch, font=f, fill=GOLD)
    except Exception as e:
        print("glyph skip", e)


fT, fD, fN = ImageFont.truetype(FONT_B, 72), ImageFont.truetype(FONT_R, 42), ImageFont.truetype(FONT_B, 40)

# ---------- หน้าหลัก ----------
cells = [
    ("1", "ต้องการโพสต์", "ดู draft พร้อมโพสต์", "✨"),
    ("2", "แก้ไขรูป", "ล้างรูป รับรูปใหม่", "🖼"),
    ("3", "แก้ไขข้อความ", "ล้างข้อความ รับใหม่", "✏"),
    ("4", "เลือกเพจ", "แตะเพื่อไปหน้าเลือกเพจ", "📄"),
    ("5", "โพสต์ใหม่", "ล้างทั้งหมด เริ่มใหม่", "🆕"),
    ("6", "โพสต์", "ยืนยันโพสต์ลงเพจ", "🚀"),
]
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
cw, ch = W // 3, H // 2
for i, (num, title, desc, g) in enumerate(cells):
    x0, y0 = (i % 3) * cw, (i // 3) * ch
    d.rectangle([x0 + 4, y0 + 4, x0 + cw - 5, y0 + ch - 5],
                fill=(17, 17, 20) if i % 2 == 0 else (22, 20, 14), outline=GOLD, width=6)
    d.ellipse([x0 + 40, y0 + 36, x0 + 130, y0 + 126], fill=GOLD)
    bb = d.textbbox((0, 0), num, font=fN)
    d.text((x0 + 85 - (bb[2] - bb[0]) / 2, y0 + 81 - (bb[3] - bb[1]) / 2 - bb[1]), num, font=fN, fill=(0, 0, 0))
    center(d, x0 + cw / 2, y0 + 200, title, fT, WHITE)
    center(d, x0 + cw / 2, y0 + 320, desc, fD, GRAY)
    glyph(d, x0 + cw / 2, y0 + 430, g)
img.save(IMG_MAIN)
print("IMG_MAIN_SAVED", IMG_MAIN)

# ---------- หน้าเลือกเพจ ----------
fT2, fD2 = ImageFont.truetype(FONT_B, 84), ImageFont.truetype(FONT_R, 46)
img2 = Image.new("RGB", (W, H), BG)
d2 = ImageDraw.Draw(img2)
for y0, num, title, desc, g in [
    (0, "1", "ก๊อดเองแม่ตั้งให้", "เพจหลัก · ความบันเทิง", "⭐"),
    (700, "2", "GETUP DEAL", "เพจดีลและโปรโมชั่น", "🛍"),
]:
    d2.rectangle([4, y0 + 4, W - 5, y0 + 700 - 5], fill=(17, 17, 20), outline=GOLD, width=6)
    d2.ellipse([80, y0 + 60, 190, y0 + 170], fill=GOLD)
    bb = d2.textbbox((0, 0), num, font=fN)
    d2.text((135 - (bb[2] - bb[0]) / 2, y0 + 115 - (bb[3] - bb[1]) / 2 - bb[1]), num, font=fN, fill=(0, 0, 0))
    center(d2, W / 2, y0 + 220, title, fT2, WHITE)
    center(d2, W / 2, y0 + 350, desc, fD2, GRAY)
    glyph(d2, W / 2, y0 + 450, g, 130)
d2.rectangle([4, 1404, W - 5, H - 5], fill=(30, 26, 12), outline=GOLD, width=6)
center(d2, W / 2, 1480, "« กลับเมนูหลัก", ImageFont.truetype(FONT_B, 64), GOLD)
img2.save(IMG_PAGES)
print("IMG_PAGES_SAVED", IMG_PAGES)


def call(base, path, method="GET", payload=None, ctype="application/json"):
    req = urllib.request.Request(base + path, method=method)
    req.add_header("Authorization", "Bearer " + TOKEN)
    body = None
    if isinstance(payload, dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req.add_header("Content-Type", ctype)
    elif isinstance(payload, bytes):
        body = payload
        if ctype:
            req.add_header("Content-Type", ctype)
    try:
        with urllib.request.urlopen(req, data=body, timeout=30) as r:
            try:
                return r.status, json.loads(r.read())
            except Exception:
                return r.status, {}
    except Exception as e:
        try:
            import urllib.error as E
            if isinstance(e, E.HTTPError):
                return e.code, {"_error": e.read().decode("utf-8", "replace")[:300]}
        except Exception:
            pass
        return -1, {"_error": str(e)[:300]}


menu_main = {"size": {"width": 2500, "height": 1686}, "selected": True,
             "name": "AutopostMain", "chatBarText": "เมนูโพสต์", "areas": [
    {"bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
     "action": {"type": "message", "label": "ต้องการโพสต์", "text": "✨ ต้องการโพสต์"}},
    {"bounds": {"x": 833, "y": 0, "width": 833, "height": 843},
     "action": {"type": "message", "label": "แก้ไขรูป", "text": "แก้ไขรูป"}},
    {"bounds": {"x": 1666, "y": 0, "width": 834, "height": 843},
     "action": {"type": "message", "label": "แก้ไขข้อความ", "text": "แก้ไขข้อความ"}},
    {"bounds": {"x": 0, "y": 843, "width": 833, "height": 843},
     "action": {"type": "richmenuswitch", "label": "เลือกเพจ", "richMenuAliasId": ALIAS_PAGES, "data": "to:pages"}},
    {"bounds": {"x": 833, "y": 843, "width": 833, "height": 843},
     "action": {"type": "message", "label": "โพสต์ใหม่", "text": "โพสต์ใหม่"}},
    {"bounds": {"x": 1666, "y": 843, "width": 834, "height": 843},
     "action": {"type": "message", "label": "โพสต์", "text": "โพสต์"}}]}
menu_pages = {"size": {"width": 2500, "height": 1686}, "selected": False,
              "name": "AutopostPages", "chatBarText": "เลือกเพจ", "areas": [
    {"bounds": {"x": 0, "y": 0, "width": 2500, "height": 700},
     "action": {"type": "message", "label": "1. ก๊อดเองแม่ตั้งให้", "text": "1"}},
    {"bounds": {"x": 0, "y": 700, "width": 2500, "height": 700},
     "action": {"type": "message", "label": "2. GETUP DEAL", "text": "2"}},
    {"bounds": {"x": 0, "y": 1400, "width": 2500, "height": 286},
     "action": {"type": "richmenuswitch", "label": "กลับเมนูหลัก", "richMenuAliasId": ALIAS_MAIN, "data": "to:main"}}]}

ids = {}
for key, menu in (("main", menu_main), ("pages", menu_pages)):
    st, res = call("https://api.line.me", "/v2/bot/richmenu", "POST", menu)
    print("CREATE", key, st, res if st != 200 else res.get("richMenuId"))
    if st != 200 or "richMenuId" not in res:
        sys.exit(1)
    ids[key] = res["richMenuId"]

for key, path in (("main", IMG_MAIN), ("pages", IMG_PAGES)):
    with open(path, "rb") as f:
        st, res = call("https://api-data.line.me", f"/v2/bot/richmenu/{ids[key]}/content", "POST", f.read(), "image/png")
    print("UPLOAD", key, st)
    if st != 200:
        sys.exit(1)

for alias, key in ((ALIAS_MAIN, "main"), (ALIAS_PAGES, "pages")):
    st, _ = call("https://api.line.me", f"/v2/bot/richmenu/alias/{alias}", "DELETE")
    st, res = call("https://api.line.me", "/v2/bot/richmenu/alias", "POST",
                   {"richMenuId": ids[key], "richMenuAliasId": alias})
    print("ALIAS", alias, st)

st, _ = call("https://api.line.me", f"/v2/bot/user/all/richmenu/{ids['main']}", "POST", b"", None)
print("SET_DEFAULT", st)

st, res = call("https://api.line.me", "/v2/bot/message/push", "POST",
               {"to": UID, "messages": [{"type": "text", "text": "ติดตั้ง Rich Menu เสร็จแล้ว เปิดดูเมนูได้เลย"}]})
print("TEST_PUSH", st)
print("MAIN_ID", ids["main"])
print("PAGES_ID", ids["pages"])
