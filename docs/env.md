# Environment & Token

## Env vars (Render → Environment)

| ตัวแปร | จำเป็น | คืออะไร |
|---|---|---|
| `LINE_CHANNEL_SECRET` | ✅ | LINE Developers → Basic settings → Channel secret |
| `LINE_CHANNEL_ACCESS_TOKEN` | ✅ | Messaging API → Channel access token (Long-lived, Issue) |
| `META_ACCESS_TOKEN` | ✅ | User Token 60 วันของเพจหลัก (ดูวิธีต่ออายุด้านล่าง) |
| `META_ACCESS_TOKEN_GETUPDEAL` | ถ้าใช้ 2 เพจ | User Token ของแอดมินเพจ GETUP DEAL |
| `GEMINI_API_KEY` | ไม่ | ใช้กับปุ่มช่วยเกลา (ตอนนี้ซ่อนไว้) |
| `RICHMENU_MAIN_ID` | ไม่ | มีค่า default ในโค้ดอยู่แล้ว (เมนูหน้าหลักปัจจุบัน) |
| `FORCE_PAGE_ID` | ไม่ | ถ้าตั้ง = ล็อคเพจเดียว ไม่ถามเลือกเพจ |

## เพจ
- `104158371681569` — ก๊อดเองแม่ตั้งให้ (ใช้ `META_ACCESS_TOKEN`)
- `788732444316483` — GETUP DEAL (ใช้ `META_ACCESS_TOKEN_GETUPDEAL`, page token แบบไม่หมดอายุ)

## LINE OA
- ชื่อ: ก๊อดเองแม่ตั้งให้, Basic ID: `@308fvqux`
- เปิด Messaging API + ตั้ง Webhook URL + Use webhook = On

## ต่ออายุ Token 60 วัน (Facebook)
1. Graph API Explorer (App `Post_Automation`) → Generate token 1 ชม. (`EAAG...`)
   ติ๊ก `pages_manage_posts`, `pages_read_engagement`, `pages_show_list`
2. แลกเป็น 60 วัน:
```
https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=<APP_ID>&client_secret=<APP_SECRET>&fb_exchange_token=<EAAG...>
```
3. ได้ `EAAY...` → อัปเดตที่ Render Environment + เครื่อง (`setx`)

## LINE Token
- Channel Access Token แบบ Long-lived ออกที่ Developers → Messaging API → Issue
- ถ้าหมดอายุ/รั่ว: กด Issue ใหม่ แล้วอัปเดต Render + `opencode.json`
