@echo off
echo ================================================
echo   CYBORG NEXUS v3.5 - ตัวติดตั้ง Windows
echo ================================================
echo.

:: ตรวจสอบว่ามีการติดตั้ง Python หรือไม่
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ข้อผิดพลาด] Python ไม่ได้ติดตั้งหรือไม่อยู่ใน PATH
    echo กรุณาติดตั้ง Python 3.8+ จาก https://python.org
    echo.
    pause
    exit /b 1
)

echo [ข้อมูล] เวอร์ชัน Python:
python --version
echo.

:: ติดตั้งการพึ่งพา Python
echo [ข้อมูล] กำลังติดตั้งการพึ่งพา Python...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ข้อผิดพลาด] ไม่สามารถติดตั้งการพึ่งพา Python ได้
    pause
    exit /b 1
)
echo [สำเร็จ] ติดตั้งการพึ่งพา Python เสร็จสิ้น
echo.

:: ให้คำแนะนำการติดตั้ง TGPT
echo [ข้อมูล] ========================================================
echo [ข้อมูล] การติดตั้ง TGPT จำเป็นสำหรับการทำงานเต็มรูปแบบ
echo [ข้อมูล] ========================================================
echo.
echo [ตัวเลือก 1: การติดตั้ง TGPT อัตโนมัติ]
echo 1. ดาวน์โหลดตัวติดตั้ง TGPT จาก: https://github.com/aandrew-me/tgpt/releases
echo 2. ดาวน์โหลดรุ่น Windows ล่าสุด (tgpt-*-windows-amd64.zip)
echo 3. แตกไฟล์ที่ดาวน์โหลดมา
echo 4. คัดลอก tgpt.exe ไปยังโฟลเดอร์ที่อยู่ใน PATH (เช่น C:\Windows\)
echo 5. หรือเพิ่มโฟลเดอร์ที่แตกไฟล์เข้าไปในระบบ PATH
echo.
echo [ตัวเลือก 2: การตรวจสอบด้วยตนเอง]
echo หลังจากติดตั้ง TGPT ให้ตรวจสอบว่าทำงานได้โดยรัน:
echo   tgpt --version
echo.
echo [ทางเลือก: ใช้ผู้ให้บริการ AI อื่น]
echo หากคุณต้องการใช้ผู้ให้บริการ AI อื่นแทน TGPT คุณสามารถใช้:
echo - OpenAI (ต้องการคีย์ API)
echo - Google/Gemini (ต้องการคีย์ API)  
echo - Ollama (การติดตั้งในเครื่อง)
echo - Anthropic (ต้องการคีย์ API)
echo - Groq (ต้องการคีย์ API)
echo.
echo [ข้อมูล] ========================================================

:: ถามผู้ใช้ว่าต้องการดำเนินการต่อหรือไม่
set /p choice="คุณต้องการดำเนินการต่อหรือไม่? (y/n): "
if /i "%choice%" neq "y" (
    echo [ข้อมูล] การติดตั้งถูกยกเลิก กรุณาติดตั้ง TGPT ก่อน
    pause
    exit /b 0
)

echo.
echo [สำเร็จ] การติดตั้งเสร็จสมบูรณ์!
echo.
echo [ข้อมูล] หากต้องการรัน CYBORG NEXUS:
echo    python main.py
echo.
echo [ข้อมูล] เคล็ดลับการแก้ไขปัญหา:
echo - หากเห็นข้อความ "[WinError 193] %1 ไม่ใช่แอปพลิเคชัน Win32 ที่ถูกต้อง", 
echo   แสดงว่าคุณต้องติดตั้งเวอร์ชัน Windows ของ TGPT
echo - หากมีข้อผิดพลาดเกี่ยวกับคีย์ API ให้สร้างไฟล์ .env พร้อมคีย์ของคุณ
echo - ไฟล์ผลลัพธ์ทั้งหมดจะไปอยู่ในโฟลเดอร์ generated_outputs/
echo.
pause