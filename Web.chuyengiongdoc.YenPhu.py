import streamlit as st
import asyncio
import edge_tts
import os

# Cấu hình trang
st.set_page_config(page_title="Chuyển giọng đọc xã Yên Phú", page_icon="🎙️")

st.title("🎙️ Hệ thống Chuyển đổi Văn bản thành Giọng nói")
st.subheader("Đơn vị: UBND xã Yên Phú - Tuyên Quang")

# Phần hướng dẫn và Ghi chú định mức
with st.expander("📖 Hướng dẫn sử dụng & Ghi chú quan trọng"):
    st.write("""
    1. Nhập hoặc dán nội dung văn bản hành chính vào ô dưới đây.
    2. Chọn giọng đọc phù hợp (mặc định là Microsoft HoaiNoi).
    3. Nhấn nút 'Chuyển đổi thành giọng nói' và đợi trong giây lát.
    """)
    
    st.warning("⚠️ **Ghi chú về giới hạn sử dụng miễn phí (API Key):**")
    st.info("""
    - **FPT.AI:** Miễn phí **100.000 ký tự/tháng**. Phù hợp dùng hàng ngày.
    - **Viettel AI:** Miễn phí **50.000 ký tự/tháng**. Giọng đọc rất chuyên nghiệp.
    - **Google Cloud:** Miễn phí từ **1 - 4 triệu ký tự/tháng**. Dồi dào nhất nhưng cần thẻ Visa để kích hoạt.
    - **Microsoft Edge-TTS:** **HOÀN TOÀN MIỄN PHÍ** và không giới hạn. Đây là chế độ mặc định hiện tại.
    """)

# Ô nhập văn bản
text_input = st.text_area("Nhập nội dung văn bản cần đọc:", height=250, placeholder="Mời đồng chí nhập nội dung tại đây...")

# Lựa chọn giọng đọc (Sử dụng Edge-TTS làm mặc định cho ổn định)
voice_option = st.selectbox(
    "Chọn giọng đọc:",
    ["vi-VN-HoaiNoiNeural (Nữ - Miền Bắc)", "vi-VN-NamMinhNeural (Nam - Miền Bắc)"]
)

# Hàm xử lý chuyển đổi giọng nói
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
                
                # Hiển thị trình phát nhạc
                audio_bytes = open(audio_file, "rb").read()
                st.audio(audio_bytes, format="audio/mp3")
                
                # Nút tải về
                st.download_button(label="📥 Tải file âm thanh về máy", data=audio_bytes, file_name="giong_doc_yen_phu.mp3", mime="audio/mp3")
                os.remove(audio_file) # Xóa file tạm
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {e}")
    else:
        st.warning("Đồng chí chưa nhập nội dung văn bản!")

# Chân trang
st.markdown("---")
st.markdown("© 2026 **UBND xã Yên Phú**. Thực hiện bởi: **Trương Hải Đăng**")
