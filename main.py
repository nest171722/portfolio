#git add , git commit (update) , git push UPLOAD ON GIT HUB
import streamlit as st
import random # นำเข้า library สำหรับสุ่มตัวเลขในเกม
import os

# 1. ตั้งค่าหน้าเว็บให้ดูกว้างขึ้นและมีไอคอน
st.set_page_config(page_title="Portfolio | Seththaphun Phruksananone ", page_icon="💻", layout="wide")
current_dir = os.path.dirname(__file__) 
image_path = os.path.join(current_dir, "por.jpg")
# --- ส่วนหัว (Header) ---
col1, col2 = st.columns([1, 2.5])
with col1:
    st.image("por.jpg", caption="Seththaphun Phruksananone", use_container_width=True)
with col2:
    st.title("Seththaphun phruksananone (Nest)")
    st.subheader("High school student / Python & C++ student ")
    st.write("""
    ผสมผสานทักษะงานบริหารเข้ากับความหลงใหลในเทคโนโลยีและการพัฒนาซอฟต์แวร์ 
    มีประสบการณ์ทั้งการจัดการระบบหลังบ้าน การพัฒนา Web Application และการสร้างระบบอัตโนมัติเพื่อลดขั้นตอนการทำงาน
    """)

st.divider()

# --- ใช้ Tabs แบ่งหน้าเนื้อหา (เพิ่มแท็บมินิเกม) ---
tab1, tab2, tab3, tab4 = st.tabs(["💼 ประสบการณ์การใช้โปรแกรม & การศึกษา", "🚀 โปรเจกต์ & ทักษะ", "🎮 มินิเกม", "📫 ติดต่องาน"])

# --- แท็บที่ 1: ประวัติ ---
with tab1:
    st.markdown("### 💼 ประสบการณ์การใช้โปรแกรม")
    st.write("- **2022 : ปัจจุบัน:** Code study, Front End")
    st.write("- ผู้ศึกษา python , C++")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🎓 การศึกษา")
    st.write("• **2022 :** python study, Cpp study")

# --- แท็บที่ 2: โปรเจกต์และทักษะ ---
with tab2:
    st.markdown("### 🛠️ ทักษะ (Skills)")
    st.write("**Programming & Software:** Python, C++ and Web application")
    st.write("**Interests:** music, game, programming, technology, and software development")

    st.markdown("### 🌟 ผลงานเด่น (Projects)")
    st.image("Hk.jpg", caption="", width = 400)
    st.image("IMG_7006.jpg", caption="", width = 400)
    st.image("IMG_7007.jpg", caption="", width = 400)
    st.image("IMG_7009.jpg", caption="", width = 400)
    st.image("IMG_7010.jpg", caption="", width = 400)
    st.image("IMG_7011.jpg", caption="", width = 400)
    st.image("IMG_7012.jpg", caption="", width = 400)
    st.image("IMG_7014.jpg", caption="", width = 400)
    st.image("IMG_7015.jpg", caption="", width = 400)
    st.image("dfgfdg.jpg", caption="", width = 400)
    st.image("dsads.jpg", caption="", width = 400)
    st.image("eda.jpg", caption="", width = 400)
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### 💰 WealthFlow Web App")
            st.write("พัฒนาเว็บไซต์สำหรับบันทึกรายรับ-รายจ่าย และติดตามพอร์ตการลงทุนส่วนตัว โดยใช้ React และเชื่อมต่อฐานข้อมูลด้วย Firebase เพื่อการจัดการการเงินอย่างเป็นระบบ")
    with col_p2:
        with st.container(border=True):
            st.markdown("#### 🤖 Data Automation System")
            st.write("สร้างระบบประมวลผลข้อมูลอัตโนมัติด้วย n8n (ตั้งค่า MQTT nodes) ร่วมกับ Scratch เพื่อดึงและบันทึกข้อมูลทางการเงินลงใน Google Sheets อัตโนมัติ")
            
    # เพิ่มโปรเจกต์ใหม่ที่นี่
    col_p3, col_p4 = st.columns(2)
    with col_p3:
        with st.container(border=True):
            st.markdown("#### ✈️ Travel Diary Web App")
            st.write("เว็บแอปพลิเคชันสำหรับบันทึกเรื่องราวและไดอารี่การท่องเที่ยว พัฒนาด้วย React ช่วยให้เก็บความทรงจำ สถานที่ และรูปภาพได้อย่างเป็นระเบียบ")
    with col_p4:
        with st.container(border=True):
            st.markdown("#### 🌳 Family Tree Web App")
            st.write("เว็บแอปพลิเคชันสร้างและแสดงแผนผังครอบครัว พัฒนาด้วย React เพื่อจัดการความสัมพันธ์และประวัติข้อมูลของสมาชิกในครอบครัวได้อย่างง่ายดายและสวยงาม")

    with tab3:
        st.markdown("### มินิเกม Python สำหรับคลายเครียด")
        st.write("ทดลองเล่นมินิเกมที่เขียนขึ้นด้วนภาษา phython และทำงานด้วย streamlit ได้เลยครับ")

        game_col1, game_col2 = st.columns(2)

        with game_col1:
            with st.container(border=True):
                st.markdown('#### เกมเป่ายิ่งชุบ ')
                choices = ['ค้อน','กรรไกร','กระดาษ']
                user_choices = st.radio('เลือกอาวุธ', choices, horizontal=True)

                if st.button('เป่ายิ้งฉุบ'):
                    bot_choices = random.choices(choices)

                    st.write(f"บอทเลือก : **{bot_choices}")

                    if user_choices == bot_choices:
                        st.info("เสมอ! ใจตรงกัน")
                    elif (user_choices == "ค้อน" and bot_choices == "กรรไกร") or (user_choices == "กรรไกร" and bot_choices == "กระดาษ") or (user_choices == "กระดาษ" and bot_choices == "ค้อน"):
                        st.success("You Win")
                    else:
                        st.error("You lose")
        with game_col2:
            with st.container(border=True):
                st.markdown("### เกมทายตัวเลข")

                if 'target_num' not in st.session_state:
                    st.session_state.target_num = random.randint(1, 50)
                    st.seesion_state.attempts = 0

                guess = st.number_input("ใส่ตัวเลขที่ทาย :", min_value=1, max_value=50, step=1)

                col_btn1, col_btn2 = st.columns([1, 1])
                with col_btn1:
                    if st.button("ทายตัวเลข"):
                        st.session_state.attempts += 1
                        if guess < st.session_state.target_num:
                            st.warning(f"ครั้งที่ {st.session_state.attempts}: น้อยไปครับ ")
                        elif guess > st.session_state.target_num:
                            st.warning(f"ครั้งที่ {st.session_state.attempts}: มากไปครับ ")
                        else:
                            st.success(f" ถูกต้อง! คำตอบคือ {st.session_state.target_num} (คุณทายไป {st.session_state.attempts})")
                            st.ballons()
                with col_btn2:
                    if st.button("เริ่มเกมใหม่"):
                        st.session_state.target_num = random.randint(1, 50)
                        st.session_state.attempts = 0
                        st.info("รีเซ็ตเกมเรียบร้อย! เริ่มทายใหม่ได้เลย")
with tab4:
    st.markdown("### ช่องทางการติดต่องาน")
    st.write("ยินดีรับโอกาศใหม่ๆ และการร่วมงานในโปรเจกต์ที่น่าสนใจ สามารถติดต่อพูดคุยกันได้ตามช่องทางด้านบล่างนี้เลยครับ")

    st.info("** Email:**Seththaphunnest@gmail.com**")
    st.write("")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("LinkedIn Profile","https://linkedin.com", use_container_width=True)
    with c2:
        st.link_button("Github Repository", "https://github.com", use_container_width=True)
    with c3:
        st.link_button("Portfolio ผลงานถ่ายภาพ", "https://instagram.com", use_container_width=True)

st.write("---")
st.caption("2026 Seththaphun phruksananone | Built with streamlit and phython")

                    