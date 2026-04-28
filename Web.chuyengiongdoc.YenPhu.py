import streamlit as st
import asyncio
import edge_tts
import os

# Cấu hình trang
st.set_page_config(page_title="Chuyển giọng đọc xã Yên Phú", page_icon="🎙️")

st.title("🎙️ Hệ thống Chuyển đổi Văn bản thành Giọng nói")
st.subheader("Đơn vị: UBND xã Yên Phú - Tuyên Quang")

# --- PHẦN HƯỚNG DẪN VÀ GHI CHÚ ĐỊNH MỨC ---
with st.expander("📖 Hướng dẫn sử dụng & Ghi chú định mức"):
    st.write("""
    1. Nhập hoặc dán nội dung văn bản vào ô dưới đây.
    2. Nếu có mã API của FPT, VNPT hoặc Viettel, hãy chọn và dán mã vào để dùng giọng đọc chuyên dụng.
    3. Mặc định hệ thống sử dụng giọng đọc chuẩn (Miễn phí không giới hạn).
    """)
    
    st.warning("⚠️ **Ghi chú về giới hạn sử dụng miễn phí (API Key):**")
    st.info("""
    - **FPT.AI:** Miễn phí **100.000 ký tự/tháng**. Phù hợp dùng hàng ngày.
    - **VNPT AI:** Thường dành cho gói dùng thử hoặc đơn vị có tài khoản công vụ.
    - **Viettel AI:** Miễn phí **50.000 ký tự/tháng**. Giọng đọc rất chuyên nghiệp.
    - **Chế độ mặc định:** HOÀN TOÀN MIỄN PHÍ và không giới hạn ký tự.
    """)

# --- PHẦN ĐIỀU HƯỚNG 3 PHẦN MỀM (FPT, VNPT, VIETTEL) ---
st.markdown("### 🛠️ Cấu hình API nâng cao")
option = st.radio("Chọn nền tảng ưu tiên (Nếu có Key):", 
                  ("Chế độ mặc định", "FPT.AI", "VNPT AI", "Viettel AI"),
                  horizontal=True)

col1, col2 = st.columns(2)
with col1:
    if option == "FPT.AI":
        api_key = st.text_input("Nhập FPT API Key:", type="password")
    elif option == "VNPT AI":
        api_key = st.text_input("Nhập VNPT API Key (Token):", type="password")
    elif option == "Viettel AI":
        api_key = st.text_input("Nhập Viettel API Key:", type="password")
    else:
        st.info("Đang sử dụng cấu hình miễn phí (Không cần nhập Key)")

# --- PHẦN NHẬP VĂN BẢN VÀ CHỌN GIỌNG ---
st.markdown("---")
text_input = st.text_area("Nhập nội dung văn bản cần đọc:", height=250, placeholder="Mời đồng chí nhập nội dung tại đây...")

voice_option = st.selectbox(
    "Chọn giọng đọc:",
    ["vi-VN-HoaiNoiNeural (Nữ - Miền Bắc)", "vi-VN-NamMinhNeural (Nam - Miền Bắc)"]
)

# Hàm xử lý chuyển đổi giọng nói (Cốt lõi Microsoft Edge-TTS)
async def generate_voice(text, voice):
    output_file = "output.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    return output_file

if st.button("🚀 Chuyển đổi thành giọng nói"):
    if text_input:
        with st.spinner("Đang xử lý dữ liệu, đồng chí vui lòng đợi..."):
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                audio_file = loop.run_until_complete(generate_voice(text_input, voice_option.split(" ")[0]))
                
                audio_bytes = open(audio_file, "rb").read()
                st.audio(audio_bytes, format="audio/mp3")
                
                st.download_button(label="📥 Tải file âm thanh về máy", 
                                   data=audio_bytes, 
                                   file_name="giong_doc_yen_phu.mp3", 
                                   mime="audio/mp3")
                os.remove(audio_file) 
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {e}")
    else:
        st.warning("Đồng chí chưa nhập nội dung văn bản!")

# Chân trang
st.markdown("---")
st.markdown("© 2026 **UBND xã Yên Phú**. Thực hiện bởi: **Trương Hải Đăng**")
