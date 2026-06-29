#!/bin/bash

echo "================================================"
echo "   CYBORG NEXUS v3.5 - ตัวติดตั้ง Linux/macOS"
echo "================================================"
echo

# ตรวจสอบว่ามีการติดตั้ง Python หรือไม่
if ! command -v python3 &> /dev/null; then
    echo "[ข้อผิดพลาด] Python 3 ไม่ได้ติดตั้งหรือไม่อยู่ใน PATH"
    echo "กรุณาติดตั้ง Python 3.8+ จาก https://python.org"
    echo "บน Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "บน CentOS/RHEL: sudo dnf install python3 python3-pip"
    echo "บน macOS: brew install python"
    exit 1
fi

echo "[ข้อมูล] เวอร์ชัน Python:"
python3 --version
echo

# ติดตั้งการพึ่งพา Python
echo "[ข้อมูล] กำลังติดตั้งการพึ่งพา Python..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ข้อผิดพลาด] ไม่สามารถติดตั้งการพึ่งพา Python ได้"
    exit 1
fi
echo "[สำเร็จ] ติดตั้งการพึ่งพา Python เสร็จสิ้น"
echo

# ให้คำแนะนำการติดตั้ง TGPT
echo "[ข้อมูล] ========================================================"
echo "[ข้อมูล] การติดตั้ง TGPT จำเป็นสำหรับการทำงานเต็มรูปแบบ"
echo "[ข้อมูล] ========================================================"
echo
echo "[ตัวเลือก 1: การติดตั้ง TGPT อัตโนมัติ (แนะนำ)]"
echo "curl -sSf https://raw.githubusercontent.com/aandrew-me/tgpt/master/install.sh | sh"
echo
echo "[ตัวเลือก 2: ผู้จัดการแพ็คเกจ]"
echo "Ubuntu/Debian: ไม่มีในคลังเริ่มต้น (ใช้ตัวเลือก 1)"
echo "Fedora: sudo dnf copr enable atim/tgpt && sudo dnf install tgpt"
echo "macOS: brew install tgpt"
echo
echo "[ตัวเลือก 3: การติดตั้งด้วยตนเอง]"
echo "1. ดาวน์โหลดจาก: https://github.com/aandrew-me/tgpt/releases"
echo "2. แตกไฟล์และย้ายไบนารี tgpt ไปยัง /usr/local/bin/ หรือ ~/bin/"
echo "3. ทำให้สามารถเรียกใช้ได้: chmod +x /usr/local/bin/tgpt"
echo
echo "[ทางเลือก: ใช้ผู้ให้บริการ AI อื่น]"
echo "หากคุณต้องการใช้ผู้ให้บริการ AI อื่นแทน TGPT คุณสามารถใช้:"
echo "- OpenAI (ต้องการคีย์ API)"
echo "- Google/Gemini (ต้องการคีย์ API)"  
echo "- Ollama (การติดตั้งในเครื่อง)"
echo "- Anthropic (ต้องการคีย์ API)"
echo "- Groq (ต้องการคีย์ API)"
echo
echo "[ข้อมูล] ========================================================"

# ถามผู้ใช้ว่าต้องการดำเนินการต่อหรือไม่
read -p "คุณต้องการดำเนินการต่อหรือไม่? (y/n): " choice
if [[ ! "$choice" =~ ^[Yy]$ ]]; then
    echo "[ข้อมูล] การติดตั้งถูกยกเลิก กรุณาติดตั้ง TGPT ก่อน"
    exit 0
fi

echo
echo "[สำเร็จ] การติดตั้งเสร็จสมบูรณ์!"
echo
echo "[ข้อมูล] หากต้องการรัน CYBORG NEXUS:"
echo "    python3 main.py"
echo
echo "[ข้อมูล] เคล็ดลับการแก้ไขปัญหา:"
echo "- หากคำสั่ง TGPT ล้มเหลว ให้ตรวจสอบว่าติดตั้งและอยู่ใน PATH แล้ว"
echo "- หากมีข้อผิดพลาดเกี่ยวกับคีย์ API ให้สร้างไฟล์ .env พร้อมคีย์ของคุณ:"
echo "  OPENAI_API_KEY=your_key_here"
echo "  GEMINI_API_KEY=your_key_here"
echo "- ไฟล์ผลลัพธ์ทั้งหมดจะไปอยู่ในโฟลเดอร์ generated_outputs/"
echo