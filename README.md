# LINE Autopost Setup — ก๊อดเองแม่ตั้งให้ (@308fvqux)

Repo นี้เก็บ**ทุกอย่างสำหรับติดตั้งระบบใหม่ตั้งแต่ศูนย์** (โค้ด webhook อยู่
[kanchat-y/line-fb-webhook](https://github.com/kanchat-y/line-fb-webhook)).

```
LINE OA (@308fvqux)
 ├─ Rich Menu 2 หน้า (assets/ + scripts/make_richmenu.py)
 │    ├─ หน้าหลัก 6 ปุ่ม: ต้องการโพสต์ / แก้ไขรูป / แก้ไขข้อความ /
 │    │                    เลือกเพจ / โพสต์ใหม่ / โพสต์
 │    └─ หน้าเลือกเพจ 2 ปุ่มใหญ่: ก๊อดเองแม่ตั้งให้ / GETUP DEAL
 └─ Webhook → Flask (line-fb-webhook บน Render)
        └─ Facebook Graph API v23.0 → 2 เพจ (ดู docs/env.md)
```

## เริ่มติดตั้ง (3 ขั้น)

### 1. Deploy Webhook
1. Fork/clone https://github.com/kanchat-y/line-fb-webhook
2. Render → New Web Service → Connect repo นั้น
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
3. ตั้ง Environment ตามตารางใน [docs/env.md](docs/env.md)
4. LINE Developers → Webhook URL = `https://<ชื่อ-service>.onrender.com/line-webhook`
   → Verify → เปิด Use webhook = On
5. กันหลับ (Render Free): cron-job.org / UptimeRobot ยิง `/ping` ทุก 10 นาที

### 2. สร้าง Rich Menu
```powershell
$env:LINE_CHANNEL_ACCESS_TOKEN = "<Channel Access Token>"
$env:LINE_USER_ID = "<User ID ของแอดมิน>"
python scripts/make_richmenu.py
```
สคริปต์จะ: สร้างภาพ 2 หน้า → สร้างเมนู → อัปโหลดภาพ → ตั้ง alias
(`autopost-main` / `autopost-pages`) → ตั้งหน้าหลักเป็น Default → ส่งข้อความทดสอบ
ค่า ID ปัจจุบันดูที่ [docs/menus.md](docs/menus.md)

### 3. ต่อ AI Agent (MCP)
ก๊อป `templates/opencode.json.template` เป็น `opencode.json` แล้วใส่ Token จริง
(ไฟล์นี้ต้อง**ไม่** commit ขึ้น git — มีตัวอย่างการกรอกในไฟล์)

## เอกสาร
- [docs/env.md](docs/env.md) — Env vars, ต่ออายุ Token 60 วัน, LINE/FB setup
- [docs/menus.md](docs/menus.md) — Rich Menu IDs, alias, โครงปุ่ม
- [docs/flows.md](docs/flows.md) — โฟลว์ 6 ปุ่ม + คำสั่งพิมพ์

## ทดสอบหลังติดตั้ง
1. เปิด LINE OA → เห็นเมนู 6 ปุ่ม
2. ส่งรูป + แคปชัน → ได้ Preview → กด `โพสต์` → ถามเพจ → โพสต์สำเร็จ + ลิงก์
3. ลองหลายรูป / วิดีโอ / ปุ่มล้าง / เปลี่ยนเพจ
