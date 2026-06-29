@echo off
echo กำลังเริ่มต้น CYBORG NEXUS v3.5...
echo.
python main.py
if errorlevel 1 (
    echo.
    echo โปรแกรมออกจากการทำงานด้วยข้อผิดพลาด.
    echo ตรวจสอบว่า:
    echo 1. การพึ่งพา Python ได้ติดตั้งแล้ว (pip install -r requirements.txt)
    echo 2. TGPT ได้ติดตั้งแล้วหรือคุณกำลังใช้ผู้ให้บริการทางเลือก
    echo 3. คีย์ API ได้ตั้งค่าในไฟล์ .env (หากใช้ผู้ให้บริการแบบชำระเงิน)
    echo.
    pause
)