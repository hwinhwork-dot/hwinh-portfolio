import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Minh Nguyen | Product & UX", page_icon="◈", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; overflow: hidden; }
        header { display: none !important; }
        footer { display: none !important; }
        iframe { border: none !important; height: 100vh !important; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minh Nguyen | Product & UX</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            /* Elite Dark Theme Palette */
            --bg-base: #050505;
            --bg-panel: #0a0a0c;
            --bg-card: #121217;
            --bg-hover: #1a1a24;
            --border-dim: rgba(255,255,255,0.08);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            
            /* Accents */
            --accent-primary: #8b5cf6; 
            --accent-secondary: #3b82f6; 
            --accent-tertiary: #10b981;
            --accent-gradient: linear-gradient(135deg, #8b5cf6, #3b82f6);
            --glow-shadow: 0 0 24px rgba(139, 92, 246, 0.2);
        }

        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'DM Sans', sans-serif; background: var(--bg-base); color: var(--text-main); height: 100vh; overflow: hidden; -webkit-font-smoothing: antialiased; }
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }

        /* Splash Screen (Language Selector) */
        #splash-screen {
            position: fixed; inset: 0; z-index: 9999; background: rgba(5,5,5,0.85); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            display: flex; flex-direction: column; align-items: center; justify-content: center; transition: opacity 0.5s ease;
        }
        .splash-card {
            background: var(--bg-card); border: 1px solid var(--border-dim); border-radius: 24px; padding: 48px; text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 0 40px rgba(139,92,246,0.1); max-width: 500px; width: 90%;
        }
        .splash-card h2 { font-family: 'Syne', sans-serif; font-size: 28px; margin-bottom: 8px; color: var(--text-main); }
        .splash-card p { color: var(--text-muted); font-size: 15px; margin-bottom: 32px; }
        .lang-btn {
            width: 100%; padding: 16px; border-radius: 14px; border: 1px solid var(--border-dim); background: var(--bg-panel); color: var(--text-main);
            font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; gap: 12px;
        }
        .lang-btn:hover { border-color: var(--accent-primary); background: rgba(139,92,246,0.1); transform: translateY(-2px); }

        .app { display: none; height: 100vh; width: 100%; position: relative; opacity: 0; transition: opacity 0.8s ease; }
        .grid-bg { position: absolute; inset: 0; z-index: 0; opacity: 0.03; pointer-events: none; background-image: linear-gradient(var(--text-main) 1px, transparent 1px), linear-gradient(90deg, var(--text-main) 1px, transparent 1px); background-size: 32px 32px; }

        /* SIDENAV (Fixed UX: Bigger and Clearer) */
        .sidenav { width: 90px; height: 100%; background: var(--bg-panel); border-right: 1px solid var(--border-dim); display: flex; flex-direction: column; align-items: center; padding: 32px 0; gap: 20px; z-index: 10; }
        .nav-logo { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 20px; color: var(--text-main); margin-bottom: 32px; background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .nav-item { width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.3s; color: var(--text-muted); font-size: 24px; position: relative; background: var(--bg-card); border: 1px solid transparent; }
        .nav-item:hover { background: var(--bg-hover); color: var(--text-main); transform: scale(1.05); border-color: var(--border-dim); }
        .nav-item.active { background: var(--accent-primary); color: white; box-shadow: var(--glow-shadow); border-color: transparent; }
        .nav-tooltip { position: absolute; left: 76px; background: var(--bg-card); color: var(--text-main); font-size: 13px; font-weight: 500; padding: 8px 14px; border-radius: 8px; white-space: nowrap; opacity: 0; pointer-events: none; transition: all 0.2s; border: 1px solid var(--border-dim); transform: translateX(-10px); }
        .nav-item:hover .nav-tooltip { opacity: 1; transform: translateX(0); }

        /* VISUAL PANEL */
        .visual-panel { flex: 1; height: 100%; overflow-y: auto; position: relative; z-index: 5; scroll-behavior: smooth; }
        .view-content { padding: 60px 8%; min-height: 100%; display: none; animation: fadeUp 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards; }
        .view-content.active { display: block; }
        .welcome-wrap { display: flex; flex-direction: column; justify-content: center; min-height: 100%; padding: 0 8%; }
        
        .pulse-status { display: inline-flex; align-items: center; gap: 8px; padding: 8px 18px; border-radius: 20px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); font-family: 'DM Mono', monospace; font-size: 12px; font-weight: 500; color: var(--accent-tertiary); margin-bottom: 32px; width: fit-content; }
        .pulse-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent-tertiary); animation: ping 2s infinite; }
        @keyframes ping { 75%, 100% { transform: scale(2.5); opacity: 0; } }

        .hero-title { font-family: 'Syne', sans-serif; font-size: clamp(48px, 6vw, 84px); font-weight: 800; line-height: 1.1; letter-spacing: -2px; margin-bottom: 16px; }
        .hero-title span { background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero-subtitle { font-size: 22px; color: var(--text-muted); font-weight: 500; margin-bottom: 32px; }
        .hero-desc { font-size: 17px; line-height: 1.8; color: var(--text-muted); max-width: 650px; margin-bottom: 48px; border-left: 3px solid var(--accent-primary); padding-left: 24px; }
        
        .contact-row { display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 60px; }
        .contact-chip { padding: 10px 20px; background: var(--bg-card); border: 1px solid var(--border-dim); border-radius: 10px; font-size: 14px; font-family: 'DM Mono', monospace; color: var(--text-muted); transition: all 0.3s; }
        .contact-chip:hover { border-color: var(--accent-secondary); color: var(--text-main); background: rgba(59,130,246,0.1); }

        .section-tag { display: inline-flex; font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent-primary); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px; font-weight: 500;}
        .view-title { font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800; color: var(--text-main); margin-bottom: 48px; letter-spacing: -1px; }

        .glass-card { background: rgba(18, 18, 23, 0.6); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid var(--border-dim); border-radius: 20px; padding: 32px; transition: all 0.4s; position: relative; overflow: hidden; margin-bottom: 24px; }
        .glass-card:hover { border-color: var(--accent-primary); transform: translateY(-4px); box-shadow: 0 10px 40px rgba(0,0,0,0.5); }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }

        .card-tag { font-family: 'DM Mono', monospace; font-size: 11px; padding: 6px 14px; border-radius: 20px; font-weight: 500; background: rgba(255,255,255,0.05); }
        .card-tag.gold { color: #fbbf24; background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.2); }
        .card-title { font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 700; margin: 20px 0 8px; }
        .card-sub { font-size: 15px; color: var(--accent-secondary); margin-bottom: 16px; font-weight: 500;}
        .card-desc { font-size: 15px; color: var(--text-muted); line-height: 1.7; margin-bottom: 24px; }
        .tech-pill { font-family: 'DM Mono', monospace; font-size: 12px; padding: 6px 14px; border-radius: 8px; background: var(--bg-base); border: 1px solid var(--border-dim); color: var(--text-muted); }

        .chart-box { background: var(--bg-card); border: 1px solid var(--border-dim); border-radius: 24px; padding: 32px; height: 420px; width: 100%; display: flex; justify-content: center; margin-bottom: 40px; }

        /* CHAT PANEL (Fixed UX) */
        .chat-panel { width: 480px; height: 100%; background: var(--bg-panel); border-left: 1px solid var(--border-dim); display: flex; flex-direction: column; flex-shrink: 0; z-index: 10; }
        .chat-header { padding: 28px 32px; border-bottom: 1px solid var(--border-dim); display: flex; align-items: center; gap: 16px; background: rgba(10,10,12,0.8); backdrop-filter: blur(10px); }
        .ai-avatar { width: 48px; height: 48px; border-radius: 14px; background: var(--accent-gradient); display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: var(--glow-shadow); }
        .chat-name { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; }
        .chat-status { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent-tertiary); margin-top: 4px; }

        .chat-messages { flex: 1; overflow-y: auto; padding: 32px; display: flex; flex-direction: column; gap: 24px; }
        .msg-row { display: flex; gap: 14px; align-items: flex-start; animation: fadeUp 0.3s ease-out; }
        .msg-row.user { flex-direction: row-reverse; }
        .msg-icon { width: 32px; height: 32px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; background: var(--bg-card); border: 1px solid var(--border-dim); }
        .msg-bubble { max-width: 85%; padding: 18px 22px; border-radius: 18px; font-size: 15px; line-height: 1.7; font-weight: 400; }
        .msg-bubble.ai { background: var(--bg-card); border: 1px solid var(--border-dim); color: var(--text-main); border-top-left-radius: 4px; }
        .msg-bubble.user { background: var(--accent-primary); color: white; border-top-right-radius: 4px; box-shadow: var(--glow-shadow); }

        .typing-indicator { display: none; gap: 6px; padding: 14px 20px; background: var(--bg-card); border: 1px solid var(--border-dim); border-radius: 16px; border-top-left-radius: 4px; width: fit-content; margin-left: 46px; margin-bottom: 20px;}
        .typing-indicator.active { display: flex; align-items: center; }
        .typing-dot { width: 8px; height: 8px; background: var(--accent-primary); border-radius: 50%; animation: typing 1.4s infinite ease-in-out both; }
        .typing-dot:nth-child(1) { animation-delay: -0.32s; }
        .typing-dot:nth-child(2) { animation-delay: -0.16s; }
        @keyframes typing { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
        .typing-text { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--text-muted); margin-left: 10px; }

        .chat-footer { padding: 28px 32px; border-top: 1px solid var(--border-dim); background: var(--bg-panel); }
        .prompts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
        
        /* Prompts (Bigger & Clearer) */
        .prompt-btn { background: var(--bg-card); border: 1px solid var(--border-dim); border-radius: 14px; padding: 16px; font-size: 14px; color: var(--text-main); cursor: pointer; transition: all 0.2s; text-align: left; display: flex; flex-direction: column; gap: 8px; font-weight: 600; line-height: 1.4;}
        .prompt-btn span.icon { font-size: 22px; }
        .prompt-btn:hover { border-color: var(--accent-primary); background: rgba(139,92,246,0.1); transform: translateY(-2px); }
        .prompt-btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }

        @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

<div id="splash-screen">
    <div class="splash-card">
        <h2>Nguyễn Hoàng Minh</h2>
        <p>Product Manager & UX Designer Portfolio</p>
        <button class="lang-btn" onclick="startGame('en')"><span style="font-size: 24px;">🇬🇧</span> Continue in English</button>
        <button class="lang-btn" onclick="startGame('vi')"><span style="font-size: 24px;">🇻🇳</span> Khám phá bằng Tiếng Việt</button>
    </div>
</div>

<div class="grid-bg"></div>

<div class="app" id="main-app">
    <nav class="sidenav" id="sidenav-container"></nav>

    <main class="visual-panel" id="visual-panel">
        <div id="view-welcome" class="view-content welcome-wrap active"></div>
        <div id="view-experience" class="view-content"></div>
        <div id="view-projects" class="view-content"></div>
        <div id="view-skills" class="view-content"></div>
        <div id="view-education" class="view-content"></div>
    </main>

    <aside class="chat-panel">
        <div class="chat-header" id="chat-header-container"></div>
        <div class="chat-messages" id="chat-messages"></div>
        <div class="typing-indicator" id="typing-indicator">
            <div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>
            <div class="typing-text" id="typing-text-ui">Analyzing data...</div>
        </div>
        <div class="chat-footer">
            <div class="prompts-grid" id="prompts-grid"></div>
        </div>
    </aside>
</div>

<script>
// ==========================================
// 1. DICTIONARY & CONTENT DATA (VI & EN)
// ==========================================
const contentData = {
    vi: {
        navTooltip: ["Tổng quan", "Sự nghiệp", "Sản phẩm", "Năng lực", "Học vấn"],
        status: "Sẵn sàng đón nhận cơ hội mới",
        role: "Product Manager | UX Designer",
        desc: "Xây dựng sản phẩm số tại giao điểm của <b>Tâm lý học Người dùng (HCI)</b> và <b>Kiến trúc Hệ thống (AI/Tech)</b>. Thay vì chỉ thiết kế giao diện, tôi thiết kế 'hành trình' — giải quyết tận gốc nỗi đau người dùng bằng dữ liệu thực nghiệm.",
        location: "Hồ Chí Minh, VN",
        secExp: "Hành trình Sự nghiệp",
        secProj: "Sản phẩm Tiêu biểu",
        secSkill: "Triết lý T-Shaped PM",
        secEdu: "Học vấn & Nền tảng",
        chatTitle: "Đặc vụ AI của Minh",
        chatStatus: "● Đã kết nối Dữ liệu",
        typing: "AI đang phân tích dữ liệu...",
        prompts: [
            { id: 'experience', icon: '💼', label: 'Tầm nhìn<br>Sự nghiệp' },
            { id: 'projects', icon: '🚀', label: 'Sản phẩm<br>Cốt lõi' },
            { id: 'skills', icon: '⚡', label: 'Ma trận<br>Năng lực' },
            { id: 'education', icon: '🎓', label: 'Học vấn &<br>Chứng chỉ' }
        ],
        chatbot: {
            greeting: `Kính chào Quý Nhà tuyển dụng. Tôi là Đặc vụ AI đại diện cho <b>Nguyễn Hoàng Minh</b>.\n\nMinh là một chuyên viên Quản lý Sản phẩm (Product Manager) và Thiết kế UX sở hữu tư duy hệ thống sắc bén. Giá trị lõi của Minh nằm ở khả năng thấu hiểu hành vi người dùng và hiện thực hóa nó bằng quy trình phát triển sản phẩm chuẩn mực.\n\nNgài muốn đánh giá khía cạnh nào trong hồ sơ năng lực của Minh? Xin mời chọn chủ đề.`,
            
            experience: `Tại <b>Saigon Innovation Hub (SIHUB)</b>, Minh không chỉ làm vận hành, Minh thiết kế "hành trình".\n\nTrong vai trò <b>Project Management Executive</b>, Minh đã vẽ nên bản đồ hành trình số (End-to-end Journey Map) cho hàng loạt Tech Startups. Thay vì phỏng đoán, Minh sử dụng <b>A/B Testing</b> và <b>Interleaving</b> để xác thực tính năng, giải quyết tận gốc các điểm nghẽn (bottlenecks) trước khi ra mắt.\n\nNgoài ra, kinh nghiệm phân tích khoảng trống năng lực cho 150+ bên liên quan và tài liệu hóa chuẩn URD chứng minh khả năng quản trị dự án quy mô lớn của Minh.`,
            
            projects: `Sản phẩm của Minh là sự hòa quyện giữa Deep-tech và UX.\n\nTuyệt tác kỹ thuật là <b>EchoMind AI</b>. Áp dụng khung quản lý CPMAI & Agile, Minh đã tái cấu trúc hệ thống giải mã sóng não (EEG 256 kênh) từ LSTM sang kiến trúc <b>Transformer (Multi-Head Attention, Label Smoothing)</b>, triệt tiêu hoàn toàn lỗi 'Mode Collapse'. Kết quả: Tốc độ giải mã đạt 55-65 WPM, độ trễ <1s, ROI kỹ thuật 72%. <i>Giao diện được trực quan hóa hoàn chỉnh bằng Gradio.</i>\n\nỞ khía cạnh UX, <b>E-Reader Ecosystem</b> (Top 20 TP.HCM) là minh chứng cho việc áp dụng nguyên lý <b>HCI (Tương tác Người-Máy)</b> để giảm tải nhận thức và ma sát cho người dùng.`,
            
            skills: `Minh theo đuổi mô hình <b>T-Shaped Product Manager</b>:\n\n<b>1. Bề rộng (Product & UX):</b>\nThành thạo Customer Journey Mapping, UX/HCI Design, và viết tài liệu PRD/User Stories. Quản trị dự án xuất sắc bằng phương pháp Agile/Scrum & RACI Matrix.\n\n<b>2. Bề sâu (Data & Tech):</b>\nNắm vững Python, Phân tích Dữ liệu và kiến trúc Machine Learning (PyTorch). Sử dụng dữ liệu để ra quyết định thay vì cảm tính.\n\nBiểu đồ Radar bên trái sẽ cho Ngài thấy bức tranh toàn cảnh về năng lực này.`,
            
            education: `Minh sở hữu nền tảng học thuật tinh hoa.\n\nLà sinh viên năm cuối ngành <b>Quản lý Công nghệ & Đổi mới Sáng tạo tại Đại học Kinh tế TP.HCM (UEH)</b>, Minh duy trì mức GPA xuất sắc <b>3.53/4.0</b>.\n\nĐộng lực học tập của Minh không dừng lại ở giảng đường. Minh đã chinh phục các chứng chỉ chuyên nghiệp của Google (Project Management, Business Intelligence) và hiện đang hoàn thiện TOEIC để sẵn sàng hội nhập môi trường quốc tế.`
        },
        htmlBlocks: {
            exp: `
                <div class="glass-card">
                    <div style="font-family: 'DM Mono', monospace; font-size: 13px; color: var(--accent-secondary); margin-bottom: 12px;">JAN 2025 — HIỆN TẠI</div>
                    <h3 class="card-title" style="margin-top: 0;">Project Management Executive</h3>
                    <div class="card-sub">Startup & Innovation Hub (SIHUB) · Sở KH&CN TP.HCM</div>
                    <p class="card-desc">Kiến trúc sư trải nghiệm cho hệ sinh thái Tech Startups. Thiết kế bản đồ hành trình số (End-to-end Journey Map) và luồng kích hoạt sản phẩm. Trực tiếp chẩn đoán điểm nghẽn hệ thống (bottlenecks), ứng dụng A/B Testing và Interleaving experiments để xác thực tính năng trước khi tung ra thị trường.</p>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <span class="tech-pill">A/B Testing</span><span class="tech-pill">Journey Mapping</span><span class="tech-pill">MVP Delivery</span>
                    </div>
                </div>
                <div class="glass-card">
                    <div style="font-family: 'DM Mono', monospace; font-size: 13px; color: var(--text-dim); margin-bottom: 12px;">JUL 2024 — DEC 2024</div>
                    <h3 class="card-title" style="margin-top: 0;">R&D Intern</h3>
                    <div class="card-sub">SIHUB · Dự án cấp Thành phố</div>
                    <p class="card-desc">Đóng vai trò then chốt trong việc phân tích khoảng trống năng lực (Competency Gap Analysis). Điều phối vòng đời dữ liệu với hơn 150+ bên liên quan (Stakeholders). Tài liệu hóa chiến lược khắt khe theo chuẩn URD, chuyển đổi nhu cầu phức tạp thành các yêu cầu hệ thống thực thi được.</p>
                </div>
            `,
            proj: `
                <div class="glass-card" style="grid-column: 1 / -1;">
                    <span class="card-tag gold">★ Flagship: Deep Tech AI</span>
                    <h3 class="card-title">EchoMind System</h3>
                    <div class="card-sub">Non-invasive BCI System · AI Product Lead</div>
                    <p class="card-desc">Hệ thống giải mã tín hiệu điện não đồ (EEG 256 kênh) thành văn bản. Quản trị vòng đời sản phẩm bằng khung <b>CPMAI và Agile (RACI matrix)</b>. Đột phá công nghệ: Chỉ đạo tái cấu trúc từ Baseline LSTM sang <b>Transformer (Multi-Head Attention, Label Smoothing)</b>, xử lý triệt để nút thắt cổ chai thông tin và lỗi 'Mode Collapse'.<br><br><b>Hiệu suất:</b> Tốc độ giải mã 55–65 WPM, độ trễ <1s. Đạt mục tiêu ROI Kỹ thuật 72%. Giao diện người dùng được triển khai tối ưu trên Gradio.</p>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <span class="tech-pill">Transformer Architecture</span><span class="tech-pill">PyTorch</span><span class="tech-pill">Agile/Scrum</span><span class="tech-pill">WER Evaluation</span>
                    </div>
                </div>
                <div class="grid-2">
                    <div class="glass-card">
                        <span class="card-tag" style="background: rgba(59,130,246,0.1); color: #60a5fa;">🏆 Top 20 Finalist</span>
                        <h3 class="card-title">E-Reader Ecosystem</h3>
                        <div class="card-sub">Hệ sinh thái Giáo dục Số</div>
                        <p class="card-desc">Áp dụng nguyên lý Tương tác Người-Máy (HCI) để phân tách các 'nỗi đau' của học sinh. Thiết kế luồng UX mượt mà giúp giảm thiểu tải lượng nhận thức trong giai đoạn onboarding.</p>
                    </div>
                    <div class="glass-card">
                        <span class="card-tag" style="background: rgba(16,185,129,0.1); color: #34d399;">● Operations</span>
                        <h3 class="card-title">Startup Ecosystem</h3>
                        <div class="card-sub">Vận hành Sự kiện quy mô lớn</div>
                        <p class="card-desc">Trực tiếp vận hành các sự kiện hạt nhân của thành phố như Univ.Star 2024/2025 và WHISE 2024. Khẳng định năng lực điều phối Cross-functional team.</p>
                    </div>
                </div>
            `,
            edu: `
                <div class="glass-card" style="background: linear-gradient(135deg, rgba(18,18,23,0.8), rgba(139,92,246,0.1)); border-color: var(--accent-primary);">
                    <div style="font-family: 'DM Mono', monospace; font-size: 13px; color: var(--accent-secondary); margin-bottom: 12px;">2022 — 2026</div>
                    <h3 style="font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 800; margin-bottom: 8px;">Đại học Kinh tế TP.HCM (UEH)</h3>
                    <div style="font-size: 17px; color: var(--text-main); margin-bottom: 24px;">Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo</div>
                    <div style="display: inline-flex; align-items: center; gap: 16px; background: rgba(0,0,0,0.4); padding: 16px 28px; border-radius: 16px; border: 1px solid var(--border-dim);">
                        <span style="font-size: 28px;">🎓</span>
                        <div>
                            <div style="font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px;">Điểm Trung Bình (GPA)</div>
                            <div style="font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800; color: #fbbf24;">3.53 <span style="font-size: 18px; color: var(--text-muted);">/ 4.0</span></div>
                        </div>
                    </div>
                </div>
                <div class="grid-2">
                    <div class="glass-card" style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 36px;">📊</div>
                        <div>
                            <div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 6px;">Google Project Management & BI</div>
                            <div style="font-size: 14px; color: var(--text-muted);">Professional Certificate by Google</div>
                        </div>
                    </div>
                    <div class="glass-card" style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 36px;">🗣️</div>
                        <div>
                            <div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 6px;">TOEIC Proficiency</div>
                            <div style="font-size: 14px; color: var(--accent-tertiary);">In Progress · Preparing for Global Environment</div>
                        </div>
                    </div>
                </div>
            `
        }
    },
    en: {
        navTooltip: ["Overview", "Experience", "Projects", "Skills", "Education"],
        status: "Available for new opportunities",
        role: "Product Manager | UX Designer",
        desc: "Building digital products at the intersection of <b>Human-Computer Interaction (HCI)</b> and <b>System Architecture</b>. I don't just design interfaces; I design 'journeys' — solving core user pain points through empirical data and technical logic.",
        location: "Ho Chi Minh, VN",
        secExp: "Career Journey",
        secProj: "Core Products",
        secSkill: "T-Shaped PM Matrix",
        secEdu: "Academic Foundation",
        chatTitle: "Minh's AI Proxy",
        chatStatus: "● Data System Connected",
        typing: "AI is analyzing data...",
        prompts: [
            { id: 'experience', icon: '💼', label: 'Career<br>Vision' },
            { id: 'projects', icon: '🚀', label: 'Flagship<br>Products' },
            { id: 'skills', icon: '⚡', label: 'Skill<br>Matrix' },
            { id: 'education', icon: '🎓', label: 'Education &<br>Certs' }
        ],
        chatbot: {
            greeting: `Welcome. I am the AI Proxy representing <b>Nguyen Hoang Minh</b>.\n\nMinh is a Product Manager and UX Designer with a sharp systems-thinking mindset. His core value lies in understanding user behavior and translating it into reality through rigorous product development workflows.\n\nWhich aspect of Minh's portfolio would you like to evaluate? Please select a topic.`,
            
            experience: `At <b>Saigon Innovation Hub (SIHUB)</b>, Minh doesn't just operate; he designs "journeys".\n\nAs a <b>Project Management Executive</b>, Minh mapped the end-to-end digital journeys for numerous Tech Startups. Rather than guessing, he utilized <b>A/B Testing</b> and <b>Interleaving</b> experiments to validate features, resolving system bottlenecks at their root before market launch.\n\nAdditionally, his experience in conducting Competency Gap Analysis for 150+ stakeholders and standardizing URD documentation proves his capability in large-scale project governance.`,
            
            projects: `Minh's products are a seamless blend of Deep-tech and UX.\n\nHis technical masterpiece is <b>EchoMind AI</b>. Applying the CPMAI & Agile frameworks, Minh directed the restructuring of a 256-channel EEG decoding system from LSTM to a <b>Transformer architecture (Multi-Head Attention, Label Smoothing)</b>, completely eradicating 'Mode Collapse'. Results: 55-65 WPM decoding speed, <1s latency, and a 72% Technical ROI. <i>The GUI was fully visualized using Gradio.</i>\n\nOn the UX front, the <b>E-Reader Ecosystem</b> (Top 20 HCMC) exemplifies his application of <b>HCI (Human-Computer Interaction)</b> principles to reduce cognitive load and friction.`,
            
            skills: `Minh pursues the <b>T-Shaped Product Manager</b> model:\n\n<b>1. Breadth (Product & UX):</b>\nProficient in Customer Journey Mapping, UX/HCI Design, and drafting PRDs/User Stories. Excellent project governance using Agile/Scrum & RACI Matrices.\n\n<b>2. Depth (Data & Tech):</b>\nStrong grasp of Python, Data Analysis, and Machine Learning architectures (PyTorch). Uses data to drive decisions rather than relying on intuition.\n\nThe Radar Chart on the left provides a comprehensive view of these competencies.`,
            
            education: `Minh possesses an elite academic foundation.\n\nAs a final-year student majoring in <b>Technology & Innovation Management at University of Economics HCMC (UEH)</b>, Minh maintains an outstanding GPA of <b>3.53/4.0</b>.\n\nHis drive for learning extends beyond the classroom. Minh has conquered professional certifications from Google (Project Management, Business Intelligence) and is currently finalizing his TOEIC to be fully prepared for international environments.`
        },
        htmlBlocks: {
            exp: `
                <div class="glass-card">
                    <div style="font-family: 'DM Mono', monospace; font-size: 13px; color: var(--accent-secondary); margin-bottom: 12px;">JAN 2025 — PRESENT</div>
                    <h3 class="card-title" style="margin-top: 0;">Project Management Executive</h3>
                    <div class="card-sub">Startup & Innovation Hub (SIHUB) · Dept. of Science & Tech</div>
                    <p class="card-desc">Experience architect for the Tech Startup ecosystem. Designed End-to-end Journey Maps and product activation flows. Diagnosed operational bottlenecks and applied A/B Testing & Interleaving experiments to validate features before market rollout.</p>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <span class="tech-pill">A/B Testing</span><span class="tech-pill">Journey Mapping</span><span class="tech-pill">MVP Delivery</span>
                    </div>
                </div>
                <div class="glass-card">
                    <div style="font-family: 'DM Mono', monospace; font-size: 13px; color: var(--text-dim); margin-bottom: 12px;">JUL 2024 — DEC 2024</div>
                    <h3 class="card-title" style="margin-top: 0;">R&D Intern</h3>
                    <div class="card-sub">SIHUB · City-Level Framework</div>
                    <p class="card-desc">Played a pivotal role in Competency Gap Analysis. Coordinated the data lifecycle involving 150+ key stakeholders. Authored strict strategic documentation (URD standards), translating complex qualitative needs into executable system requirements.</p>
                </div>
            `,
            proj: `
                <div class="glass-card" style="grid-column: 1 / -1;">
                    <span class="card-tag gold">★ Flagship: Deep Tech AI</span>
                    <h3 class="card-title">EchoMind System</h3>
                    <div class="card-sub">Non-invasive BCI System · AI Product Lead</div>
                    <p class="card-desc">A system decoding 256-channel EEG brain signals into text. Governed the product lifecycle using <b>CPMAI and Agile frameworks (RACI matrix)</b>. Technological breakthrough: Directed the architecture migration from a Baseline LSTM to a <b>Transformer (Multi-Head Attention, Label Smoothing)</b>, effectively resolving information bottlenecks and 'Mode Collapse'.<br><br><b>Performance:</b> 55–65 WPM decoding speed, <1s latency. Achieved 72% Technical ROI. User interface optimally deployed via Gradio.</p>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        <span class="tech-pill">Transformer Architecture</span><span class="tech-pill">PyTorch</span><span class="tech-pill">Agile/Scrum</span><span class="tech-pill">WER Evaluation</span>
                    </div>
                </div>
                <div class="grid-2">
                    <div class="glass-card">
                        <span class="card-tag" style="background: rgba(59,130,246,0.1); color: #60a5fa;">🏆 Top 20 Finalist</span>
                        <h3 class="card-title">E-Reader Ecosystem</h3>
                        <div class="card-sub">Digital Education Ecosystem</div>
                        <p class="card-desc">Applied Human-Computer Interaction (HCI) principles to decompose student 'pain points'. Designed a seamless UX flow to minimize cognitive load during the onboarding phase.</p>
                    </div>
                    <div class="glass-card">
                        <span class="card-tag" style="background: rgba(16,185,129,0.1); color: #34d399;">● Operations</span>
                        <h3 class="card-title">Startup Ecosystem</h3>
                        <div class="card-sub">Large-scale Event Operations</div>
                        <p class="card-desc">Directly operated the city's core innovation events such as Univ.Star 2024/2025 and WHISE 2024. Demonstrated strong Cross-functional team coordination capabilities.</p>
                    </div>
                </div>
            `,
            edu: `
                <div class="glass-card" style="background: linear-gradient(135deg, rgba(18,18,23,0.8), rgba(139,92,246,0.1)); border-color: var(--accent-primary);">
                    <div style="font-family: 'DM Mono', monospace; font-size: 13px; color: var(--accent-secondary); margin-bottom: 12px;">2022 — 2026</div>
                    <h3 style="font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 800; margin-bottom: 8px;">University of Economics HCMC (UEH)</h3>
                    <div style="font-size: 17px; color: var(--text-main); margin-bottom: 24px;">Bachelor in Technology & Innovation Management</div>
                    <div style="display: inline-flex; align-items: center; gap: 16px; background: rgba(0,0,0,0.4); padding: 16px 28px; border-radius: 16px; border: 1px solid var(--border-dim);">
                        <span style="font-size: 28px;">🎓</span>
                        <div>
                            <div style="font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px;">Grade Point Average (GPA)</div>
                            <div style="font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800; color: #fbbf24;">3.53 <span style="font-size: 18px; color: var(--text-muted);">/ 4.0</span></div>
                        </div>
                    </div>
                </div>
                <div class="grid-2">
                    <div class="glass-card" style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 36px;">📊</div>
                        <div>
                            <div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 6px;">Google Project Management & BI</div>
                            <div style="font-size: 14px; color: var(--text-muted);">Professional Certificate by Google</div>
                        </div>
                    </div>
                    <div class="glass-card" style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 36px;">🗣️</div>
                        <div>
                            <div style="font-size: 16px; font-weight: 700; color: var(--text-main); margin-bottom: 6px;">TOEIC Proficiency</div>
                            <div style="font-size: 14px; color: var(--accent-tertiary);">In Progress · Preparing for Global Environment</div>
                        </div>
                    </div>
                </div>
            `
        }
    }
};

let currentLang = 'en';
let isTyping = false;
let chartInstance = null;

// ==========================================
// 2. CORE LOGIC
// ==========================================
function startGame(lang) {
    currentLang = lang;
    document.getElementById('splash-screen').style.opacity = '0';
    setTimeout(() => {
        document.getElementById('splash-screen').style.display = 'none';
        buildUI();
        document.getElementById('main-app').style.display = 'flex';
        setTimeout(() => {
            document.getElementById('main-app').style.opacity = '1';
            initChat();
        }, 100);
    }, 500);
}

function buildUI() {
    const d = contentData[currentLang];
    
    // Build Sidenav
    const navIcons = ['🏠', '💼', '🚀', '⚡', '🎓'];
    const navViews = ['welcome', 'experience', 'projects', 'skills', 'education'];
    let navHTML = `<div class="nav-logo">HW</div>`;
    for(let i=0; i<5; i++) {
        navHTML += `<div class="nav-item ${i===0?'active':''}" data-view="${navViews[i]}" onclick="switchView('${navViews[i]}', this)">${navIcons[i]}<span class="nav-tooltip">${d.navTooltip[i]}</span></div>`;
    }
    document.getElementById('sidenav-container').innerHTML = navHTML;

    // Build Welcome View
    document.getElementById('view-welcome').innerHTML = `
        <div class="pulse-status"><div class="pulse-dot"></div> ${d.status}</div>
        <h1 class="hero-title">Nguyễn <br><span>Hoàng Minh</span></h1>
        <p class="hero-subtitle">${d.role}</p>
        <p class="hero-desc">${d.desc}</p>
        <div class="contact-row">
            <div class="contact-chip">✉ hwinh.work@gmail.com</div>
            <div class="contact-chip">📞 +84 765 828 191</div>
            <div class="contact-chip">📍 ${d.location}</div>
            <div class="contact-chip" style="color:var(--accent-primary); border-color:var(--accent-primary); font-weight:bold;">🎓 GPA 3.53 / 4.0</div>
        </div>
    `;

    // Build Static Views
    document.getElementById('view-experience').innerHTML = `<div class="section-tag">Work History</div><h2 class="view-title">${d.secExp}</h2>${d.htmlBlocks.exp}`;
    document.getElementById('view-projects').innerHTML = `<div class="section-tag">Case Studies</div><h2 class="view-title">${d.secProj}</h2>${d.htmlBlocks.proj}`;
    
    document.getElementById('view-skills').innerHTML = `
        <div class="section-tag">Competencies Map</div><h2 class="view-title">${d.secSkill}</h2>
        <div class="chart-box"><canvas id="skillsChart"></canvas></div>
        <div style="display: flex; gap: 14px; flex-wrap: wrap; justify-content: center;">
            <span class="contact-chip" style="color:white; border-color:var(--accent-primary);">Journey Mapping</span>
            <span class="contact-chip" style="color:white; border-color:var(--accent-primary);">UX/HCI Design</span>
            <span class="contact-chip" style="color:white; border-color:var(--accent-primary);">Agile/Scrum</span>
            <span class="contact-chip">Python / PyTorch</span>
            <span class="contact-chip">A/B Testing</span>
        </div>
    `;
    
    document.getElementById('view-education').innerHTML = `<div class="section-tag">Academic Foundation</div><h2 class="view-title">${d.secEdu}</h2>${d.htmlBlocks.edu}`;

    // Build Chat Header & Footer
    document.getElementById('chat-header-container').innerHTML = `
        <div class="ai-avatar">🤖</div>
        <div><div class="chat-name">${d.chatTitle}</div><div class="chat-status">${d.chatStatus}</div></div>
    `;
    document.getElementById('typing-text-ui').innerText = d.typing;
}

function initChat() {
    const d = contentData[currentLang];
    document.getElementById('chat-messages').innerHTML = '';
    
    // Render Prompts
    document.getElementById('prompts-grid').innerHTML = d.prompts.map(p =>
        `<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.label.replace('<br>',' ')}')" ${isTyping ? 'disabled' : ''}>
            <span class="icon">${p.icon}</span> <span>${p.label}</span>
        </button>`
    ).join('');

    switchView('welcome');
    setTimeout(() => {
        showTyping();
        setTimeout(() => {
            hideTyping();
            appendMessage('ai', d.chatbot.greeting, true);
        }, 1200);
    }, 500);
}

function switchView(viewId, navEl) {
    document.querySelectorAll('[id^="view-"]').forEach(v => v.classList.remove('active'));
    document.getElementById('view-' + viewId).classList.add('active');
    
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    if (navEl) navEl.classList.add('active');
    else {
        const nav = document.querySelector(`[data-view="${viewId}"]`);
        if (nav) nav.classList.add('active');
    }
    
    if (viewId === 'skills') setTimeout(initSkillsChart, 100);
}

function handlePrompt(id, label) {
    if (isTyping) return;
    isTyping = true;
    const grid = document.getElementById('prompts-grid');
    grid.style.opacity = '0.3';
    grid.style.pointerEvents = 'none';
    
    appendMessage('user', label, false);
    
    setTimeout(() => {
        showTyping();
        setTimeout(() => {
            hideTyping();
            switchView(id, null);
            appendMessage('ai', contentData[currentLang].chatbot[id], true, () => {
                grid.style.opacity = '1';
                grid.style.pointerEvents = 'auto';
            });
        }, 1200);
    }, 300);
}

function showTyping() { document.getElementById('typing-indicator').classList.add('active'); scrollBottom(); }
function hideTyping() { document.getElementById('typing-indicator').classList.remove('active'); }

function appendMessage(sender, text, useTypewriter = false, callback = null) {
    const row = document.createElement('div');
    row.className = `msg-row ${sender}`;

    const icon = document.createElement('div');
    icon.className = 'msg-icon';
    icon.textContent = sender === 'ai' ? '🤖' : '👤';
    if(sender === 'ai') { icon.style.background = 'var(--accent-gradient)'; icon.style.color = 'white'; icon.style.border = 'none';}

    const bubble = document.createElement('div');
    bubble.className = `msg-bubble ${sender}`;

    row.appendChild(icon);
    row.appendChild(bubble);
    document.getElementById('chat-messages').appendChild(row);

    if (sender === 'ai' && useTypewriter) {
        typeWriter(text, bubble, 10, callback);
    } else {
        bubble.innerHTML = text.replace(/\n/g, '<br>');
        scrollBottom();
        if (callback) callback();
    }
}

function typeWriter(text, el, speed, callback) {
    let i = 0;
    el.innerHTML = '<span class="tc"></span><span class="cursor-blink"></span>';
    const tc = el.querySelector('.tc');

    function type() {
        if (i < text.length) {
            let ch = text.charAt(i);
            if(ch === '<') {
                let tag = '';
                while(text.charAt(i) !== '>' && i < text.length) { tag += text.charAt(i); i++; }
                tag += '>'; tc.innerHTML += tag;
            } else {
                if (ch === '\n') {
                    tc.innerHTML += '<br>';
                    if(text.charAt(i+1) === '\n') { tc.innerHTML += '<br>'; i++; }
                } else {
                    tc.innerHTML += ch;
                }
            }
            i++; scrollBottom(); setTimeout(type, speed);
        } else {
            isTyping = false;
            const cur = el.querySelector('.cursor-blink');
            if (cur) cur.remove();
            if (callback) callback();
        }
    }
    type();
}

function scrollBottom() { const c = document.getElementById('chat-messages'); c.scrollTop = c.scrollHeight + 50; }

function initSkillsChart() {
    const ctx = document.getElementById('skillsChart');
    if (!ctx) return;
    if (chartInstance) { chartInstance.destroy(); }

    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = "'DM Sans', sans-serif";

    chartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['UX/HCI', 'Agile/Scrum', 'Journey Map', 'Data Analysis', 'Python/Tech', 'PyTorch', 'A/B Testing'],
            datasets: [{
                label: currentLang==='en'?'Competency Level':'Độ thông thạo',
                data: [90, 85, 95, 80, 80, 72, 85],
                fill: true,
                backgroundColor: 'rgba(139, 92, 246, 0.2)',
                borderColor: '#8b5cf6', borderWidth: 2,
                pointBackgroundColor: '#3b82f6', pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff', pointHoverBorderColor: '#3b82f6',
                pointRadius: 4, pointHoverRadius: 6
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { r: { min: 0, max: 100, ticks: { display: false }, angleLines: { color: 'rgba(255,255,255,0.08)' }, grid: { color: 'rgba(255,255,255,0.08)' }, pointLabels: { font: { size: 14, weight: '600' }, color: '#cbd5e1' } } },
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(10, 10, 12, 0.95)', borderColor: 'rgba(139, 92, 246, 0.4)', borderWidth: 1, padding: 14,
                    titleFont: { family: "'DM Mono', monospace", size: 13 }, bodyFont: { size: 15, weight: 'bold' }, displayColors: false,
                    callbacks: { label: ctx => { const v = ctx.raw; if(v >= 90) return currentLang==='en'?' Level: Expert':' Mức độ: Xuất sắc'; if(v >= 80) return currentLang==='en'?' Level: Advanced':' Mức độ: Cao cấp'; return currentLang==='en'?' Level: Proficient':' Mức độ: Thành thạo'; } }
                }
            }
        }
    });
}
</script>
</body>
</html>
"""

components.html(html_code, height=950, scrolling=False)
