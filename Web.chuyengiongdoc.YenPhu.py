import streamlit as st
import edge_tts
import asyncio
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Chuyển đổi Văn bản số - Xã Yên Phú", page_icon="📢")

st.title("📢 CÔNG CỤ CHUYỂN ĐỔI VĂN BẢN SỐ")
st.markdown("#### ỦY BAN NHÂN DÂN XÃ YÊN PHÚ - TUYÊN QUANG")
st.info("Hệ thống hỗ trợ tự động chuyển văn bản hành chính thành giọng nói.")

# --- PHẦN 1: CÔNG CỤ ĐỌC TRỰC TIẾP (MIỄN PHÍ) ---
st.markdown("---")
st.markdown("### 🎙️ BỘ ĐỌC TIÊU CHUẨN (MIỄN PHÍ, KHÔNG GIỚI HẠN)")

# Chia màn hình làm 2 cột
cot_trai, cot_phai = st.columns([1, 2])

with cot_trai:
    giong_doc = st.radio("Đồng chí chọn giọng đọc:", [
        "Hoài Nội (Nữ - Miền Bắc)", 
        "Nam Minh (Nam - Miền Bắc)", 
        "Hoài My (Nữ - Miền Nam)"
    ])
    
    # ÁNH XẠ MÃ GIỌNG CHÍNH XÁC THEO THƯ VIỆN MICROSOFT
    if "Hoài Nội" in giong_doc:
        ma_giong = "vi-VN-HoaiNoiNeural"
    elif "Nam Minh" in giong_doc:
        ma_giong = "vi-VN-NamMinhNeural"
    else:
        ma_giong = "vi-VN-HoaiMyNeural"

with cot_phai:
    van_ban = st.text_area("Nhập nội dung văn bản hành chính vào đây:", height=250, placeholder="Dán nội dung Thông báo, Kế hoạch...")

if st.button("▶️ BẮT ĐẦU CHUYỂN ĐỔI"):
    if van_ban.strip() == "":
        st.warning("Đồng chí chưa nhập nội dung văn bản!")
    else:
        with st.spinner('Hệ thống đang xử lý, đồng chí đợi vài giây...'):
            async def tao_am_thanh():
                # Sử dụng biến ma_giong đã được ánh xạ chuẩn
                communicate = edge_tts.Communicate(van_ban, ma_giong)
                await communicate.save("file_phat_thanh.mp3")
            
            try:
                # Chạy tiến trình tạo file
                asyncio.run(tao_am_thanh())
                
                if os.path.exists("file_phat_thanh.mp3"):
                    st.audio("file_phat_thanh.mp3")
                    
                    with open("file_phat_thanh.mp3", "rb") as f:
                        st.download_button(
                            label="💾 TẢI FILE MP3 VỀ MÁY",
                            data=f,
                            file_name="VanBan_YenPhu.mp3",
                            mime="audio/mp3"
                        )
                    st.success("Thành công! Đồng chí có thể nghe thử hoặc tải về.")
                else:
                    st.error("Lỗi: Không tạo được file âm thanh.")
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")

# --- PHẦN 2: BỘ ĐỌC NÂNG CAO & HƯỚNG DẪN ---
st.markdown("---")
st.markdown("### 🌟 BỘ ĐỌC NÂNG CAO (HÃNG THỨ 3)")
st.caption("Khuyến nghị dùng cho các văn bản quan trọng. Các đồng chí bấm nút để chuyển sang trang web của hãng.")

with st.expander("📖 HƯỚNG DẪN ĐĂNG KÝ & GHI CHÚ ĐỊNH MỨC MIỄN PHÍ"):
    st.markdown("""
    **1. Hướng dẫn nghiệp vụ:**
    * **Bước 1:** Bấm vào các nút truy cập (FPT, Viettel, VNPT) bên dưới.
    * **Bước 2:** Chọn **Đăng nhập** bằng **Google (Gmail)**.
    * **Bước 3:** Sử dụng công cụ của hãng để chọn các giọng đọc AI nâng cao.

    **2. Ghi chú giới hạn dùng miễn phí:**
    * **FPT.AI:** Miễn phí **100.000 ký tự/tháng**.
    * **Viettel AI:** Miễn phí **50.000 ký tự/tháng**.
    * **VNPT AI:** Hỗ trợ gói dùng thử cho cán bộ công chức.
    * **Bộ đọc tiêu chuẩn (Phần trên):** **Miễn phí 100%**, không giới hạn ký tự.
    """)

# NÚT BẤM ĐIỀU HƯỚNG
c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("🌐 TRUY CẬP FPT.AI", "https://fpt.ai/vi/tts")
with c2:
    st.link_button("🌐 TRUY CẬP VIETTEL AI", "https://viettelai.vn/tts")
with c3:
    st.link_button("🌐 TRUY CẬP VNPT AI", "https://vnpt.ai/tts")

# --- CHÂN TRANG ---
st.markdown("---")
st.caption("© 2026 Bản quyền thuộc về UBND xã Yên Phú - Thiết kế và phát triển bởi Trương Hải Đăng.")
