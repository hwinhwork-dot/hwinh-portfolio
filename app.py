import streamlit as st
import time

# 1. Cài đặt trang mạng mở rộng toàn màn hình
st.set_page_config(layout="wide", page_title="Hồ sơ năng lực - hwinh")

# 2. Hàm tạo hiệu ứng tự nhảy chữ (typing effect) cho Trợ lý ảo
def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05) # Tốc độ nhảy chữ

# 3. Khởi tạo bộ nhớ tạm để lưu lịch sử trò chuyện
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "assistant", "content": "Xin chào Quý Nhà tuyển dụng! Tôi là Trợ lý ảo của Nguyễn Hoàng Minh (hwinh). Minh là một nhân sự trẻ đầy nhiệt huyết trong lĩnh vực Quản lý Công nghệ và Đổi mới sáng tạo. Mời Quý vị nhấn vào các biểu tượng bên phải để tôi thuyết trình chi tiết về năng lực của Minh nhé!"}
    ]
if "pending_stream" not in st.session_state:
    st.session_state.pending_stream = None

# 4. Chia giao diện làm 2 cột: Cột trái (Chat) chiếm 6 phần, Cột phải (Thông tin) chiếm 4 phần
col_chat, col_info = st.columns([6, 4])

# --- CỘT TRÁI: KHU VỰC TRỢ LÝ ẢO ---
with col_chat:
    st.title("💬 Trợ lý ảo AI")
    st.markdown("---")
    
    # In ra các đoạn chat cũ
    for msg in st.session_state.history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Nếu HR vừa bấm vào 1 dự án, Trợ lý sẽ bắt đầu gõ chữ thuyết trình
    if st.session_state.pending_stream:
        with st.chat_message("assistant"):
            st.write_stream(stream_data(st.session_state.pending_stream))
        # Lưu lại câu thuyết trình vào lịch sử sau khi gõ xong
        st.session_state.history.append({"role": "assistant", "content": st.session_state.pending_stream})
        st.session_state.pending_stream = None

# --- CỘT PHẢI: KHU VỰC THÔNG TIN & DỰ ÁN ---
with col_info:
    st.title("Hồ Sơ Năng Lực 📌")
    
    # Nơi để chèn ảnh hồ sơ của bạn (Tạm thời dùng biểu tượng, sau này chèn link ảnh thật vào)
    st.markdown("## 🧑‍💻 Nguyễn Hoàng Minh (hwinh)")
    st.write("Cử nhân Quản lý Công nghệ và Đổi mới sáng tạo")
    
    st.markdown("---")
    st.subheader("💡 Các mảng dự án cốt lõi")
    
    # Nút bấm 1: Dự án AI
    if st.button("🤖 Trí tuệ Nhân tạo & Học máy"):
        # Lưu câu hỏi ảo của HR
        st.session_state.history.append({"role": "user", "content": "Hãy thuyết trình về các dự án AI của Minh."})
        # Chuẩn bị câu trả lời để máy tự gõ
        st.session_state.pending_stream = "Trong mảng AI, Minh có tư duy sản phẩm nhạy bén. Đáng chú ý là dự án nghiên cứu chuyển đổi tín hiệu não thành văn bản (Brain-to-Text) ứng dụng thư viện PyTorch. Hiện tại, Minh cũng đang dồn sức rèn luyện cho chương trình AI Thực Chiến."
        st.rerun() # Tải lại trang để áp dụng hiệu ứng

    # Nút bấm 2: Dự án Cơ khí
    if st.button("⚙️ Kỹ thuật Cơ khí & Chế tạo"):
        st.session_state.history.append({"role": "user", "content": "Thế mạnh của Minh trong mảng Cơ khí là gì?"})
        st.session_state.pending_stream = "Bên cạnh tư duy phần mềm, Minh sở hữu nền tảng phần cứng và cơ khí vững chắc. Minh thành thạo việc đọc hiểu bản vẽ kỹ thuật, phân tích dung sai (ví dụ: lắp ghép H7/js6), độ nhám bề mặt và nắm rõ quy trình phay, mài, doa."
        st.rerun()

    st.markdown("---")
    st.subheader("🏆 Kinh nghiệm & Thành tích")
    
    # Nút bấm 3: Kinh nghiệm Đổi mới sáng tạo
    if st.button("🏢 Hoạt động Khởi nghiệp & ĐMST"):
        st.session_state.history.append({"role": "user", "content": "Hãy tóm tắt kinh nghiệm làm việc thực tế."})
        st.session_state.pending_stream = "Từ tháng 07/2024, Minh đảm nhận vai trò Thực tập sinh Nghiên cứu tại Trung tâm Khởi nghiệp đổi mới sáng tạo TP.HCM. Minh đã trực tiếp tham gia tổ chức thành công cuộc thi Univ.Star và tuần lễ WHISE."
        st.rerun()
        
    # Nút bấm 4: Chứng chỉ
    if st.button("📜 Chứng chỉ Ngoại ngữ & Kỹ năng"):
        st.session_state.history.append({"role": "user", "content": "Các chứng chỉ nổi bật của Minh?"})
        st.session_state.pending_stream = "Minh đang chuẩn bị chinh phục chứng chỉ TOEIC với mục tiêu 600+, kết hợp cùng các chứng chỉ chuyên môn như ESB (Khởi nghiệp và Doanh nghiệp nhỏ) để bổ trợ cho định hướng phát triển sự nghiệp."
        st.rerun()
