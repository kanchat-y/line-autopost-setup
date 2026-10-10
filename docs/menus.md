# Rich Menu — ค่าปัจจุบัน (10 Oct 2026)

## เมนูที่ใช้งานจริง

| หน้า | richMenuId | name | chatBarText | Default |
|---|---|---|---|---|
| หลัก (6 ปุ่ม) | `richmenu-8d538df75d627fed1d5af428130b2232` | AutopostMainV3 | เมนูโพสต์ | ✅ |
| เลือกเพจ | `richmenu-9dc2e9b1a2f06ce5bf86871a747a1a7c` | AutopostPages12 | เลือกเพจ | — |

## Alias (ปุ่มสลับหน้าใช้ตัวนี้ ไม่ใช้ ID ตรง)

| alias | ชี้ไป |
|---|---|
| `autopost-main` | เมนูหลัก |
| `autopost-pages` | เมนูเลือกเพจ |

## โครงปุ่มหน้าหลัก (2500×1686, 3 คอลัมน์ × 2 แถว)

| ปุ่ม | action | ส่งข้อความ |
|---|---|---|
| 1. ต้องการโพสต์ | message | `✨ ต้องการโพสต์` |
| 2. แก้ไขรูป | message | `แก้ไขรูป` |
| 3. แก้ไขข้อความ | message | `แก้ไขข้อความ` |
| 4. เลือกเพจ | richmenuswitch → `autopost-pages` | (สลับหน้า ไม่ส่งข้อความ) |
| 5. โพสต์ใหม่ | message | `โพสต์ใหม่` |
| 6. โพสต์ | message | `โพสต์` |

## โครงปุ่มหน้าเลือกเพจ

| ปุ่ม | action | ส่งข้อความ |
|---|---|---|
| 1. ก๊อดเองแม่ตั้งให้ (บน) | message | `1` |
| 2. GETUP DEAL (กลาง) | message | `2` |
| « กลับเมนูหลัก (ล่าง) | richmenuswitch → `autopost-main` | (สลับหน้า) |

ภาพต้นฉบับ: `assets/richmenu-main.png`, `assets/richmenu-pages.png`
(ฟอนต์ Tahoma — รองรับไทย, ธีมดำทอง #0B0B0D / #C9A227)

## สร้างใหม่ / ย้ายเครื่อง
รัน `python scripts/make_richmenu.py` (ต้องตั้ง `LINE_CHANNEL_ACCESS_TOKEN`
กับ `LINE_USER_ID` ก่อน) — สคริปต์สร้างภาพ+เมนู+alias+default ให้ครบ
จด ID ใหม่มาอัปเดตไฟล์นี้ด้วย
