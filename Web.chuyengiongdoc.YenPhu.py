import streamlit as st
import asyncio
import edge_tts
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Chuyển đổi Văn bản số - Xã Yên Phú", page_icon="📢")

st.title("📢 CÔNG CỤ CHUYỂN ĐỔI VĂN BẢN SỐ")
st.markdown("#### ỦY BAN NHÂN DÂN XÃ YÊN PHÚ - TUYÊN QUANG")
st.info("Hệ thống hỗ trợ tự động chuyển văn bản hành chính thành giọng nói miễn phí.")

# --- PHẦN 1: BỘ ĐỌC TIÊU CHUẨN ---
st.markdown("---")
st.markdown("### 🎙️ BỘ ĐỌC TIÊU CHUẨN (MIỄN PHÍ, KHÔNG GIỚI HẠN)")

# Chia màn hình làm 2 cột
cot_trai, cot_phai = st.columns([1, 2])

with cot_trai:
    giong_chon = st.radio("Đồng chí chọn giọng đọc:", [
        "Nam Minh (Nam - Miền Bắc)", 
        "Hoài My (Nữ - Miền Nam)"
    ])
    # Ánh xạ mã giọng chuẩn
    ma_giong = "vi-VN-NamMinhNeural" if "Nam Minh" in giong_chon else "vi-VN-HoaiMyNeural"

with cot_phai:
    van_ban = st.text_area("Nhập nội dung văn bản hành chính vào đây:", height=250, placeholder="Dán nội dung Thông báo, Kế hoạch vào đây...")

if st.button("▶️ BẮT ĐẦU CHUYỂN ĐỔI"):
    if not van_ban.strip():
        st.warning("Đồng chí chưa nhập nội dung văn bản!")
    else:
        with st.spinner('Hệ thống đang xử lý, đồng chí đợi vài giây...'):
            output_file = "VanBan_YenPhu.mp3"
            
            async def generate():
                try:
                    communicate = edge_tts.Communicate(van_ban, ma_giong)
                    await communicate.save(output_file)
                    return True
                except:
                    return False

            try:
                # Chạy tiến trình xử lý âm thanh
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                success = loop.run_until_complete(generate())

                if success and os.path.exists(output_file):
                    st.audio(output_file)
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label="💾 TẢI FILE MP3 VỀ MÁY",
                            data=f,
                            file_name="GiongDoc_YenPhu.mp3",
                            mime="audio/mp3"
                        )
                    st.success("Thành công! Đồng chí có thể nghe thử hoặc tải về.")
                    os.remove(output_file)
                else:
                    st.error("Lỗi kết nối máy chủ! Đồng chí vui lòng nhấn lại nút chuyển đổi lần nữa.")
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")

# --- PHẦN 2: LIÊN KẾT NÂNG CAO ---
st.markdown("---")
st.markdown("### 🌟 BỘ ĐỌC NÂNG CAO (HÃNG THỨ 3)")
with st.expander("📖 HƯỚNG DẪN ĐĂNG KÝ & GHI CHÚ ĐỊNH MỨC"):
    st.markdown("""
    **1. Cách sử dụng:** Các đồng chí bấm vào nút bên dưới để sang trang web của hãng, đăng nhập bằng Gmail cá nhân để sử dụng giọng AI chuyên biệt.
    
    **2. Định mức miễn phí:**
    * **FPT.AI:** 100.000 ký tự/tháng.
    * **Viettel AI:** 50.000 ký tự/tháng.
    * **VNPT AI:** Gói dùng thử cho cán bộ công chức.
    """)

c1, c2, c3 = st.columns(3)
with c1: st.link_button("🌐 TRUY CẬP FPT.AI", "https://fpt.ai/vi/tts")
with c2: st.link_button("🌐 TRUY CẬP VIETTEL AI", "https://viettelai.vn/tts")
with c3: st.link_button("🌐 TRUY CẬP VNPT AI", "https://vnpt.ai/tts")

# --- CHÂN TRANG ---
st.markdown("---")
st.caption("© 2026 Bản quyền thuộc về UBND xã Yên Phú - Thiết kế và phát triển bởi Trương Hải Đăng.")
