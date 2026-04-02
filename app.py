import streamlit as st
import time

# 1. CÀI ĐẶT TRANG & TIÊU ĐỀ
st.set_page_config(layout="wide", page_title="Nguyen Hoang Minh - Portfolio", page_icon="🚀")

# 2. CSS TÙY CHỈNH: TỐI GIẢN, HIỆN ĐẠI (TRẮNG, XANH BIỂN, ĐEN)
st.markdown("""
<style>
    /* Tổng thể nền trắng, chữ xám đen */
    .stApp {
        background-color: #FFFFFF;
        color: #1F2937;
        font-family: 'Inter', sans-serif;
    }
    /* Thanh bên (Sidebar) màu xám nhạt */
    [data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }
    /* Nút bấm gợi ý (Pills) xanh biển */
    .stButton>button {
        background-color: #E0F2FE;
        color: #0284C7;
        border: 1px solid #BAE6FD;
        border-radius: 20px;
        padding: 5px 15px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0284C7;
        color: #FFFFFF;
        box-shadow: 0 4px 6px -1px rgba(2, 132, 199, 0.2);
    }
    /* Khung chat tin nhắn */
    .stChatMessage {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #E2E8F0;
    }
    /* Ẩn bớt viền không cần thiết */
    div[data-testid="stChatInput"] {
        border-color: #0284C7 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. CƠ SỞ DỮ LIỆU TỪ CV CỦA MINH (Dành cho AI)
KNOWLEDGE_BASE = {
    "tóm tắt": "Minh là một chuyên gia trẻ về Quản lý Công nghệ & Đổi mới Sáng tạo. Thế mạnh cốt lõi của Minh là giải quyết vấn đề hệ thống và tối ưu hóa Trải nghiệm Người dùng (UX). Minh cực kỳ đam mê việc thiết kế Bản đồ Hành trình Khách hàng (Customer Journey Map) và giải quyết các 'nỗi đau' (pain points) của người dùng.",
    "sihub": "Tại SIHUB (Trung tâm Khởi nghiệp đổi mới sáng tạo TP.HCM), Minh đảm nhận vai trò Project Management Executive. Minh đã thiết kế luồng kích hoạt (activation flow) cho các startup, biến các vấn đề của người dùng thành User Stories rõ ràng, và áp dụng thử nghiệm A/B để tối ưu hóa sản phẩm trước khi tung ra thị trường.",
    "nghiên cứu": "Trong vai trò Thực tập sinh Nghiên cứu (R&D Intern) tại SIHUB (07/2024 - 12/2024), Minh đã dẫn dắt vòng đời dữ liệu để phân tích khoảng trống năng lực cho hơn 150 bên liên quan và soạn thảo các tài liệu chiến lược theo chuẩn URD.",
    "echomind": "Dự án EchoMind là một hệ thống AI chuyển đổi tín hiệu não thành văn bản (Brain-to-Text). Minh đã lập trình logic hệ thống bằng Python và PyTorch, tối ưu hóa hiệu suất bằng mô hình Transformer, đạt tốc độ giải mã ấn tượng 55-65 WPM với độ trễ dưới 1 giây.",
    "e-reader": "Với dự án E-Reader (Hệ sinh thái Giáo dục Số), Minh đã lọt vào Top 20 Chung cuộc của TP.HCM. Minh áp dụng các nguyên tắc Tương tác Người - Máy (HCI) để thiết kế hành trình người dùng xuyên suốt, giảm tải nhận thức cho học sinh.",
    "kỹ năng": "Minh sử dụng thành thạo phương pháp Agile/Scrum, thiết kế hành trình khách hàng (Journey Mapping), Tư duy Thiết kế (Design Thinking). Về mặt kỹ thuật, Minh nắm vững Python, phân tích dữ liệu và sở hữu các chứng chỉ của Google về Quản lý Dự án và Business Intelligence."
}

def stream_response(text):
    for char in text:
        yield char
        time.sleep(0.01) # Tốc độ gõ siêu mượt

def get_ai_response(query):
    query = query.lower()
    if any(kw in query for kw in ["tóm tắt", "giới thiệu", "bản thân", "summary"]): return KNOWLEDGE_BASE["tóm tắt"]
    if any(kw in query for kw in ["sihub", "kinh nghiệm", "làm việc", "work"]): return KNOWLEDGE_BASE["sihub"]
    if any(kw in query for kw in ["nghiên cứu", "r&d", "data", "dữ liệu"]): return KNOWLEDGE_BASE["nghiên cứu"]
    if any(kw in query for kw in ["echomind", "ai", "brain", "não", "pytorch"]): return KNOWLEDGE_BASE["echomind"]
    if any(kw in query for kw in ["e-reader", "giáo dục", "hci"]): return KNOWLEDGE_BASE["e-reader"]
    if any(kw in query for kw in ["kỹ năng", "skill", "chứng chỉ", "công cụ"]): return KNOWLEDGE_BASE["kỹ năng"]
    
    return "Câu hỏi rất hay! Để trả lời chính xác nhất theo hồ sơ của Minh, Quý vị có thể hỏi tôi về: **Kinh nghiệm tại SIHUB, Dự án AI EchoMind, Dự án E-Reader**, hoặc các **Kỹ năng Quản lý Sản phẩm** nhé."

# 4. GIAO DIỆN THANH BÊN (SIDEBAR) - THÔNG TIN CỐ ĐỊNH TỪ CV
with st.sidebar:
    st.markdown("## 👨‍💻 NGUYỄN HOÀNG MINH")
    st.markdown("**Thực tập sinh Chủ sở hữu Sản phẩm** *(Product Owner Intern)*")
    st.markdown("---")
    st.markdown("📍 **Liên hệ:**")
    st.markdown("📞 +84 765828191")
    st.markdown("✉️ hwinh.work@gmail.com")
    st.markdown("---")
    st.markdown("🎓 **Học vấn:**")
    st.markdown("Cử nhân Quản lý Công nghệ & ĐMST - Đại học Kinh tế TP.HCM")
    st.markdown("**GPA:** 3.53/4.0")
    st.markdown("---")
    st.markdown("🛠️ **Kỹ năng Cốt lõi:**")
    st.markdown("- Trải nghiệm Người dùng (UX)")
    st.markdown("- Agile / Scrum")
    st.markdown("- A/B Testing & Data Analysis")
    st.markdown("- Python & PyTorch")

# 5. GIAO DIỆN CHÍNH (MAIN AREA) - TRỢ LÝ ẢO
st.markdown("### 💬 Trợ lý HR AI của hwinh")
st.markdown("Chào mừng Quý Nhà tuyển dụng! Tôi được thiết kế dựa trên dữ liệu hồ sơ năng lực của Nguyễn Hoàng Minh. Bạn muốn tìm hiểu thông tin gì?")

# Khởi tạo lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if "trigger_query" not in st.session_state:
    st.session_state.trigger_query = None

# Hàng nút bấm gợi ý thông minh (Nâng cao UX)
st.markdown("💡 **Gợi ý hỏi nhanh:**")
col1, col2, col3, col4 = st.columns([1, 1.2, 1, 1.5])
with col1:
    if st.button("Tóm tắt bản thân"): st.session_state.trigger_query = "tóm tắt bản thân"
with col2:
    if st.button("Kinh nghiệm SIHUB"): st.session_state.trigger_query = "kinh nghiệm sihub"
with col3:
    if st.button("Dự án AI EchoMind"): st.session_state.trigger_query = "dự án ai echomind"
with col4:
    if st.button("Kỹ năng & Chứng chỉ"): st.session_state.trigger_query = "kỹ năng chứng chỉ"

st.markdown("---")

# Vùng chứa tin nhắn
chat_container = st.container()

# Xử lý logic Chat
user_input = st.chat_input("Hỏi tôi bất cứ điều gì về hồ sơ của Minh...")

# Nếu có click từ nút bấm HOẶC nhập từ bàn phím
query_to_process = st.session_state.trigger_query if st.session_state.trigger_query else user_input

if query_to_process:
    st.session_state.messages.append({"role": "user", "content": query_to_process})
    response_text = get_ai_response(query_to_process)
    st.session_state.messages.append({"role": "assistant", "content": response_text, "stream": response_text})
    st.session_state.trigger_query = None # Reset sau khi xử lý xong

# Hiển thị lịch sử chat
with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            # Nếu là tin nhắn của AI mới nhất thì chạy hiệu ứng gõ
            if msg["role"] == "assistant" and "stream" in msg:
                st.write_stream(stream_response(msg["stream"]))
                del msg["stream"] # Xóa cờ stream để lần tải lại sau không bị gõ lại
            else:
                st.write(msg["content"])
