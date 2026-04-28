import streamlit as st
import asyncio
import edge_tts
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Chuyển đổi Văn bản số - Xã Yên Phú", page_icon="📢")

st.title("📢 CÔNG CỤ CHUYỂN ĐỔI VĂN BẢN SỐ")
st.markdown("#### ỦY BAN NHÂN DÂN XÃ YÊN PHÚ - TUYÊN QUANG")
st.info("Hệ thống hỗ trợ tự đimport streamlit as st
import asyncio
import edge_tts
import os

# --- CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Chuyển đổi Văn bản số - Xã Yên Phú", page_icon="📢")

st.title("📢 CÔNG CỤ CHUYỂN ĐỔI VĂN BẢN SỐ")
st.markdown("#### ỦY BAN NHÂN DÂN XÃ YÊN PHÚ - TUYÊN QUANG")
st.info("Hệ thống hỗ trợ tự động chuyển văn bản hành chính thành giọng nói.")

# --- PHẦN 1: BỘ ĐỌC TIÊU CHUẨN (MIỄN PHÍ) ---
st.markdown("---")
st.markdown("### 🎙️ BỘ ĐỌC TIÊU CHUẨN (MIỄN PHÍ, KHÔNG GIỚI HẠN)")

cot_trai, cot_phai = st.columns([1, 2])

with cot_trai:
    giong_chon = st.radio("Đồng chí chọn giọng đọc:", [
        "Hoài My (Nữ - Miền Nam)",
        "Nam Minh (Nam - Miền Bắc)",
        "Giọng Nữ chuẩn (Dự phòng)"
    ])
    
    # ÁNH XẠ MÃ GIỌNG (SỬ DỤNG CÁC GIỌNG CŨ ỔN ĐỊNH NHẤT)
    if "Hoài My" in giong_chon:
        ma_giong = "vi-VN-HoaiMyNeural"
    elif "Nam Minh" in giong_chon:
        ma_giong = "vi-VN-NamMinhNeural"
    else:
        # Nếu Hoài Nội lỗi, dùng Hoài My làm dự phòng nhưng vẫn ghi là giọng Nữ
        ma_giong = "vi-VN-HoaiMyNeural" 

with cot_phai:
    van_ban = st.text_area("Nhập nội dung văn bản vào đây:", height=250, placeholder="Dán nội dung Thông báo, Kế hoạch...")

if st.button("▶️ BẮT ĐẦU CHUYỂN ĐỔI"):
    if not van_ban.strip():
        st.warning("Đồng chí chưa nhập nội dung văn bản!")
    else:
        with st.spinner('Hệ thống đang xử lý, đồng chí đợi vài giây...'):
            output_file = "output_audio.mp3"
            
            async def generate():
                try:
                    # Giao thức Communicate chuẩn
                    communicate = edge_tts.Communicate(van_ban, ma_giong)
                    await communicate.save(output_file)
                    return True
                except Exception as e:
                    return False

            try:
                # Chạy loop sự kiện
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                success = loop.run_until_complete(generate())

                if success and os.path.exists(output_file):
                    st.audio(output_file)
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label="💾 TẢI FILE MP3 VỀ MÁY",
                            data=f,
                            file_name="VanBan_YenPhu.mp3",
                            mime="audio/mp3"
                        )
                    st.success("Thành công! Đồng chí có thể nghe thử hoặc tải về.")
                    os.remove(output_file)
                else:
                    st.error("Hiện tại máy chủ Microsoft đang bảo trì giọng miền Bắc. Đồng chí vui lòng chọn 'Hoài My (Nữ - Miền Nam)' để xuất file ngay lập tức!")
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")

# --- PHẦN 2: BỘ ĐỌC NÂNG CAO & HƯỚNG DẪN ---
st.markdown("---")
st.markdown("### 🌟 BỘ ĐỌC NÂNG CAO (HÃNG THỨ 3)")
with st.expander("📖 HƯỚNG DẪN ĐĂNG KÝ & GHI CHÚ ĐỊNH MỨC MIỄN PHÍ"):
    st.markdown("""
    **1. Hướng dẫn nghiệp vụ:**
    * **Bước 1:** Bấm vào các nút truy cập bên dưới.
    * **Bước 2:** Đăng nhập bằng Gmail để sử dụng giọng AI chuyên nghiệp của FPT, Viettel, VNPT.
    
    **2. Ghi chú giới hạn dùng miễn phí:**
    * **FPT.AI:** 100.000 ký tự/tháng.
    * **Viettel AI:** 50.000 ký tự/tháng.
    * **Bộ đọc tiêu chuẩn:** Miễn phí 100%, không giới hạn.
    """)

c1, c2, c3 = st.columns(3)
with c1: st.link_button("🌐 TRUY CẬP FPT.AI", "https://fpt.ai/vi/tts")
with c2: st.link_button("🌐 TRUY CẬP VIETTEL AI", "https://viettelai.vn/tts")
with c3: st.link_button("🌐 TRUY CẬP VNPT AI", "https://vnpt.ai/tts")

st.markdown("---")
st.caption("© 2026 UBND xã Yên Phú - Thiết kế bởi Trương Hải Đăng.")ộng chuyển văn bản hành chính thành giọng nói.")

# --- PHẦN 1: CÔNG CỤ ĐỌC TRỰC TIẾP (MIỄN PHÍ) ---
st.markdown("---")
st.markdown("### 🎙️ BỘ ĐỌC TIÊU CHUẨN (MIỄN PHÍ, KHÔNG GIỚI HẠN)")

cot_trai, cot_phai = st.columns([1, 2])

with cot_trai:
    giong_chon = st.radio("Đồng chí chọn giọng đọc:", [
        "Hoài Nội (Nữ - Miền Bắc)", 
        "Nam Minh (Nam - Miền Bắc)", 
        "Hoài My (Nữ - Miền Nam)"
    ])
    
    # ÁNH XẠ MÃ GIỌNG THEO DANH SÁCH CHUẨN CỦA MICROSOFT
    danh_sach_giong = {
        "Hoài Nội (Nữ - Miền Bắc)": "vi-VN-HoaiNoiNeural",
        "Nam Minh (Nam - Miền Bắc)": "vi-VN-NamMinhNeural",
        "Hoài My (Nữ - Miền Nam)": "vi-VN-HoaiMyNeural"
    }
    ma_giong = danh_sach_giong.get(giong_chon, "vi-VN-HoaiNoiNeural")

with cot_phai:
    van_ban = st.text_area("Nhập nội dung văn bản hành chính vào đây:", height=250, placeholder="Dán nội dung Thông báo, Kế hoạch...")

if st.button("▶️ BẮT ĐẦU CHUYỂN ĐỔI"):
    if not van_ban.strip():
        st.warning("Đồng chí chưa nhập nội dung văn bản!")
    else:
        with st.spinner('Hệ thống đang xử lý, đồng chí đợi vài giây...'):
            output_file = "output_audio.mp3"
            
            async def generate():
                try:
                    # Gửi yêu cầu chuyển đổi
                    communicate = edge_tts.Communicate(van_ban, ma_giong)
                    await communicate.save(output_file)
                    return True
                except Exception as e:
                    st.error(f"Chi tiết lỗi: {e}")
                    return False

            # Chạy tiến trình
            try:
                # Cách chạy ổn định nhất trên Streamlit Cloud
                import asyncio
                new_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(new_loop)
                success = new_loop.run_until_complete(generate())

                if success and os.path.exists(output_file):
                    st.audio(output_file)
                    with open(output_file, "rb") as f:
                        st.download_button(
                            label="💾 TẢI FILE MP3 VỀ MÁY",
                            data=f,
                            file_name="VanBan_YenPhu.mp3",
                            mime="audio/mp3"
                        )
                    st.success("Thành công! Đồng chí có thể nghe thử hoặc tải về.")
                    # Xóa file sau khi dùng để tránh nặng máy chủ
                    os.remove(output_file)
                else:
                    st.error("Giọng đọc này đang trục trặc, đồng chí hãy thử lại sau 30 giây hoặc chọn giọng khác!")
            except Exception as e:
                st.error(f"Lỗi hệ thống: {e}")

# --- PHẦN 2: BỘ ĐỌC NÂNG CAO & HƯỚNG DẪN ---
st.markdown("---")
st.markdown("### 🌟 BỘ ĐỌC NÂNG CAO (HÃNG THỨ 3)")
st.caption("Khuyến nghị dùng cho các văn bản quan trọng.")

with st.expander("📖 HƯỚNG DẪN ĐĂNG KÝ & GHI CHÚ ĐỊNH MỨC MIỄN PHÍ"):
    st.markdown("""
    **1. Hướng dẫn nghiệp vụ:**
    * **Bước 1:** Bấm vào các nút truy cập (FPT, Viettel, VNPT) bên dưới.
    * **Bước 2:** Đăng nhập bằng Gmail để vào thẳng hệ thống.
    * **Bước 3:** Sử dụng công cụ của hãng để chọn các giọng đọc AI nâng cao.

    **2. Ghi chú giới hạn dùng miễn phí:**
    * **FPT.AI:** Miễn phí **100.000 ký tự/tháng**.
    * **Viettel AI:** Miễn phí **50.000 ký tự/tháng**.
    * **VNPT AI:** Hỗ trợ gói dùng thử cho đơn vị nhà nước.
    * **Bộ đọc tiêu chuẩn (Phần trên):** **Miễn phí 100%**, không giới hạn ký tự.
    """)

c1, c2, c3 = st.columns(3)
with c1: st.link_button("🌐 TRUY CẬP FPT.AI", "https://fpt.ai/vi/tts")
with c2: st.link_button("🌐 TRUY CẬP VIETTEL AI", "https://viettelai.vn/tts")
with c3: st.link_button("🌐 TRUY CẬP VNPT AI", "https://vnpt.ai/tts")

st.markdown("---")
st.caption("© 2026 Bản quyền thuộc về UBND xã Yên Phú - Thiết kế bởi Trương Hải Đăng.")
