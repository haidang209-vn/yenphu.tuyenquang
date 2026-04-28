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
    giong_doc = st.radio("Đồng chí chọn giọng đọc:", ["Nam Minh (Giọng Nam - Miền Bắc)", "Hoài My (Giọng Nữ - Miền Nam)"])
    ma_giong = "vi-VN-NamMinhNeural" if "Nam Minh" in giong_doc else "vi-VN-HoaiMyNeural"

with cot_phai:
    van_ban = st.text_area("Nhập nội dung văn bản hành chính vào đây:", height=200, placeholder="Dán nội dung Thông báo, Kế hoạch...")

if st.button("▶️ BẮT ĐẦU CHUYỂN ĐỔI"):
    if van_ban.strip() == "":
        st.warning("Đồng chí chưa nhập nội dung văn bản!")
    else:
        with st.spinner('Hệ thống đang nhào nặn âm thanh, đồng chí đợi vài giây...'):
            async def tao_am_thanh():
                communicate = edge_tts.Communicate(van_ban, ma_giong)
                await communicate.save("file_phat_thanh.mp3")
            
            try:
                asyncio.run(tao_am_thanh())
                st.audio("file_phat_thanh.mp3")
                
                with open("file_phat_thanh.mp3", "rb") as f:
                    st.download_button(
                        label="💾 TẢI FILE MP3 VỀ MÁY",
                        data=f,
                        file_name="VanBan_YenPhu.mp3",
                        mime="audio/mp3"
                    )
                st.success("Thành công! Đồng chí có thể nghe thử hoặc tải về.")
            except Exception as e:
                st.error("Lỗi mạng! Đề nghị kiểm tra lại kết nối Internet.")

# --- PHẦN 2: BỘ ĐỌC NÂNG CAO & HƯỚNG DẪN ---
st.markdown("---")
st.markdown("### 🌟 BỘ ĐỌC NÂNG CAO (GIỌNG AI CHUYÊN NGHIỆP)")
st.caption("Khuyến nghị dùng cho các văn bản quan trọng. Đề nghị các đồng chí tự đăng nhập bằng Gmail cá nhân để sử dụng.")

# HỘP HƯỚNG DẪN MỞ RỘNG (GỌN GÀNG, CHUYÊN NGHIỆP)
with st.expander("📖 BẤM VÀO ĐÂY ĐỂ XEM HƯỚNG DẪN ĐĂNG KÝ VÀ SỬ DỤNG"):
    st.markdown("""
    **HƯỚNG DẪN NGHIỆP VỤ CHUYỂN ĐỔI GIỌNG NÓI NÂNG CAO**
    
    **1. Hệ thống FPT AI (Khuyên dùng: Giọng Nữ Ban Mai - Miền Bắc chuẩn)**
    * **Bước 1:** Bấm vào nút truy cập FPT.AI bên dưới.
    * **Bước 2:** Tại góc phải màn hình, chọn **Đăng nhập** -> Chọn biểu tượng **Google (Gmail)** để đăng nhập nhanh.
    * **Bước 3:** Dán văn bản vào ô trống, chọn giọng đọc và bấm "Tạo âm thanh". 
    * *(Lưu ý: FPT cấp miễn phí 100.000 ký tự/tháng cho mỗi tài khoản).*

    **2. Hệ thống Viettel AI (Khuyên dùng: Giọng Nam đanh thép, uy lực)**
    * **Bước 1:** Bấm vào nút truy cập Viettel AI bên dưới.
    * **Bước 2:** Bấm nút **Dùng thử miễn phí** hoặc **Đăng ký** bằng Số điện thoại/Email.
    * **Bước 3:** Sử dụng công cụ Text-to-Speech trên giao diện của Viettel.

    **Yêu cầu:** Các đồng chí tự quản lý tài khoản Gmail cá nhân để đảm bảo an toàn thông tin theo quy định.
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
