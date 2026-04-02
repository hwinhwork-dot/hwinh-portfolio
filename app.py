import streamlit as st
import time

# 1. Cài đặt trang & Tiêu đề
st.set_page_config(layout="wide", page_title="Portfolio - hwinh")

# 2. Tiêm CSS tùy chỉnh để làm đẹp giao diện (Trắng - Xanh Biển - Đen)
st.markdown("""
<style>
    /* Chỉnh màu nền và chữ tổng thể */
    .stApp {
        background-color: #FAFAFA;
        color: #111827;
    }
    /* Chỉnh màu các nút bấm thành Xanh biển */
    .stButton>button {
        background-color: #0284C7;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0369A1;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    /* Tùy chỉnh thanh phân cách */
    hr {
        border-color: #E5E7EB;
    }
</style>
""", unsafe_allow_html=True)

# 3. Hàm hiệu ứng gõ TỪNG KÝ TỰ (sửa lại để mượt hơn)
def stream_data(text):
    for char in text:
        yield char
        time.sleep(0.015) # Tốc độ gõ từng chữ cái (nhanh và mượt)

# 4. Cơ sở dữ liệu tri thức của AI (Để AI tự trả lời khi HR gõ câu hỏi)
knowledge_base = {
    "ai": "Về Trí tuệ Nhân tạo, Minh có tư duy sản phẩm sắc bén. Minh từng phát triển dự án chuyển đổi tín hiệu não thành văn bản (Brain-to-Text) sử dụng PyTorch và đang hướng tới chương trình AI Thực Chiến.",
    "cơ khí": "Về Cơ khí, Minh nắm vững các tiêu chuẩn kỹ thuật. Đọc hiểu tốt bản vẽ, dung sai (H7/js6), độ nhám bề mặt và rành rọt các quy trình gia công như phay, mài, doa.",
    "khởi nghiệp": "Minh có nền tảng vững chắc về Đổi mới sáng tạo. Từng làm Nghiên cứu sinh tại Trung tâm ĐMST TP.HCM, tham gia tổ chức Univ.Star và tuần lễ WHISE.",
    "tiếng anh": "Minh đang trong quá trình rèn luyện tiếng Anh, mục tiêu đạt chứng chỉ TOEIC 600+ để phục vụ công việc chuyên môn.",
    "chào": "Dạ xin chào! Mình là AI hỗ trợ của Minh. Bạn muốn biết thêm về kỹ năng nào của Minh ạ?",
}

def get_ai_response(user_query):
    query = user_query.lower()
    for key, response in knowledge_base.items():
        if key in query:
            return response
    return "Câu hỏi rất thú vị! Tuy nhiên bộ nhớ của tôi hiện tập trung vào: AI, Cơ Khí, và Khởi Nghiệp. Quý vị có thể hỏi tôi về các mảng này nhé!"

# Khởi tạo bộ nhớ trò chuyện
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "assistant", "content": "Xin chào Quý Nhà tuyển dụng! Tôi là Trợ lý AI của Nguyễn Hoàng Minh (hwinh). Mời Quý vị nhấn vào các mục bên phải hoặc gõ câu hỏi trực tiếp ở dưới để tôi giới thiệu về Minh nhé!"}
    ]
if "pending_stream" not in st.session_state:
    st.session_state.pending_stream = None

# 5. Phân chia giao diện chính
col_chat, col_empty, col_info = st.columns([5.5, 0.5, 4]) # Thêm cột rỗng ở giữa để tạo khoảng thở (UX tốt hơn)

# --- CỘT TRÁI: CHATBOT THÔNG MINH ---
with col_chat:
    st.markdown("### 💬 Trợ lý ảo AI")
    st.markdown("---")
    
    # Khung hiển thị tin nhắn (giới hạn chiều cao để không bị đẩy quá dài)
    chat_container = st.container(height=500, border=False)
    
    with chat_container:
        for msg in st.session_state.history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        # Xử lý hiệu ứng nhảy chữ
        if st.session_state.pending_stream:
            with st.chat_message("assistant"):
                st.write_stream(stream_data(st.session_state.pending_stream))
            st.session_state.history.append({"role": "assistant", "content": st.session_state.pending_stream})
            st.session_state.pending_stream = None

    # THANH NHẬP LIỆU CHO HR (Tính năng mới)
    user_input = st.chat_input("Nhập câu hỏi (VD: Kinh nghiệm AI của Minh là gì?)...")
    if user_input:
        # Lưu câu hỏi của HR
        st.session_state.history.append({"role": "user", "content": user_input})
        # Lấy câu trả lời từ AI
        st.session_state.pending_stream = get_ai_response(user_input)
        st.rerun()

# --- CỘT PHẢI: HỒ SƠ & MENU NÚT BẤM ---
with col_info:
    st.markdown("### 📌 Hồ Sơ Năng Lực")
    
    # Card Giới thiệu
    st.markdown("""
    <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px;">
        <h3 style="margin-top:0; color:#0284C7;">Nguyễn Hoàng Minh</h3>
        <p style="color:gray; font-size: 14px;"><strong>Cử nhân Quản lý Công nghệ và Đổi mới sáng tạo</strong><br>Bí danh: hwinh</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 💡 Dự án & Năng lực")
    if st.button("🤖 Trí tuệ Nhân tạo & Học máy"):
        st.session_state.history.append({"role": "user", "content": "Hãy thuyết trình về các dự án AI của Minh."})
        st.session_state.pending_stream = knowledge_base["ai"]
        st.rerun()

    if st.button("⚙️ Kỹ thuật Cơ khí"):
        st.session_state.history.append({"role": "user", "content": "Thế mạnh của Minh trong mảng Cơ khí là gì?"})
        st.session_state.pending_stream = knowledge_base["cơ khí"]
        st.rerun()

    if st.button("🏢 Khởi nghiệp & ĐMST"):
        st.session_state.history.append({"role": "user", "content": "Hãy tóm tắt kinh nghiệm làm việc thực tế."})
        st.session_state.pending_stream = knowledge_base["khởi nghiệp"]
        st.rerun()
