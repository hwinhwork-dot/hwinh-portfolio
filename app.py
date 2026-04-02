import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang Streamlit
st.set_page_config(layout="wide", page_title="hwinh | Product & UX Specialist", page_icon="◈", initial_sidebar_state="collapsed")

# Ẩn các thành phần thừa của Streamlit
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
    <title>hwinh | Product & UX</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --ink: #08080c;
            --ink2: #0f0f17;
            --ink3: #161621;
            --surface: #1c1c2b;
            --surface2: #242438;
            --border: rgba(255,255,255,0.08);
            --text: #f0f0f5;
            --text2: #a0a0b8;
            --accent: #7c6af7;
            --accent2: #a594fc;
            --green: #52d18a;
            --gold: #f0c060;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'DM Sans', sans-serif; background: var(--ink); color: var(--text); height: 100vh; overflow: hidden; }

        /* === LANGUAGE OVERLAY === */
        #lang-overlay {
            position: fixed; inset: 0; background: var(--ink); z-index: 1000;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            transition: opacity 0.5s ease;
        }
        .lang-card {
            text-align: center; max-width: 500px; padding: 40px;
        }
        .lang-logo { font-family: 'Syne', sans-serif; font-size: 64px; font-weight: 800; margin-bottom: 20px; color: var(--accent2); }
        .lang-btn-group { display: flex; gap: 20px; margin-top: 30px; }
        .lang-btn {
            padding: 16px 32px; border-radius: 12px; border: 1px solid var(--border);
            background: var(--ink2); color: var(--text); cursor: pointer; font-family: 'Syne', sans-serif;
            font-weight: 600; transition: all 0.3s; font-size: 18px; width: 160px;
        }
        .lang-btn:hover { background: var(--accent); border-color: var(--accent2); transform: translateY(-3px); box-shadow: 0 10px 20px rgba(124,106,247,0.3); }

        /* === LAYOUT === */
        .app { display: flex; height: 100vh; width: 100%; opacity: 0; transition: opacity 0.5s; }
        .app.visible { opacity: 1; }

        /* === SIDENAV (Optimized UX) === */
        .sidenav {
            width: 100px; height: 100%; background: var(--ink2); border-right: 1px solid var(--border);
            display: flex; flex-direction: column; align-items: center; padding: 32px 0; gap: 12px; z-index: 100;
        }
        .nav-logo { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 20px; color: var(--accent2); margin-bottom: 32px; }
        .nav-item {
            width: 76px; height: 76px; border-radius: 16px; display: flex; flex-direction: column;
            align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s;
            color: var(--text2); gap: 6px; border: 1px solid transparent;
        }
        .nav-item i { font-size: 24px; font-style: normal; }
        .nav-item span { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; text-align: center; }
        .nav-item:hover { background: var(--surface); color: var(--text); }
        .nav-item.active { background: var(--accent); color: white; box-shadow: 0 0 20px rgba(124,106,247,0.2); }

        /* === CONTENT === */
        .visual-panel { flex: 1; height: 100%; overflow-y: auto; background: var(--ink); padding: 60px 80px; scroll-behavior: smooth; }
        .visual-panel::-webkit-scrollbar { width: 6px; }
        .visual-panel::-webkit-scrollbar-thumb { background: var(--surface2); border-radius: 10px; }

        /* === CHAT PANEL === */
        .chat-panel { width: 420px; height: 100%; background: var(--ink2); border-left: 1px solid var(--border); display: flex; flex-direction: column; }

        /* === STYLE HELPERS === */
        .section-tag { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); text-transform: uppercase; letter-spacing: 3px; margin-bottom: 16px; display: block; }
        .view-title { font-family: 'Syne', sans-serif; font-size: 56px; font-weight: 800; margin-bottom: 48px; letter-spacing: -2px; line-height: 1.1; }
        .view-title span { color: var(--accent2); }

        /* === SKILLS (Bigger Bars) === */
        .skill-bar-item { margin-bottom: 24px; }
        .skill-bar-header { display: flex; justify-content: space-between; margin-bottom: 10px; font-weight: 600; }
        .skill-bar-track { height: 10px; background: var(--surface2); border-radius: 5px; overflow: hidden; }
        .skill-bar-fill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent2)); width: 0; transition: width 1.5s cubic-bezier(0.19, 1, 0.22, 1); }

        /* === PROJECTS === */
        .projects-grid { display: grid; grid-template-columns: 1fr; gap: 32px; }
        .project-card { 
            background: var(--ink3); border: 1px solid var(--border); border-radius: 24px; 
            padding: 40px; transition: all 0.3s; position: relative; overflow: hidden;
        }
        .project-card:hover { border-color: var(--accent); transform: translateY(-5px); background: var(--surface); }
        .project-card.featured { border-left: 4px solid var(--accent); }
        .project-badge { font-family: 'DM Mono', monospace; font-size: 11px; padding: 6px 14px; border-radius: 8px; background: rgba(124,106,247,0.15); color: var(--accent2); margin-bottom: 16px; display: inline-block; }
        .project-metrics { display: flex; gap: 40px; margin: 24px 0; padding: 20px; background: rgba(0,0,0,0.2); border-radius: 16px; }
        .metric-val { font-size: 28px; font-weight: 800; color: var(--text); font-family: 'Syne', sans-serif; }
        .metric-label { font-size: 12px; color: var(--text2); text-transform: uppercase; margin-top: 4px; }

        /* === TIMELINE === */
        .timeline { border-left: 2px solid var(--border); padding-left: 40px; position: relative; }
        .timeline-item { margin-bottom: 56px; position: relative; }
        .timeline-item::before { content: ''; position: absolute; left: -49px; top: 0; width: 16px; height: 16px; border-radius: 50%; background: var(--accent); border: 4px solid var(--ink); }
        .tl-date { font-family: 'DM Mono', monospace; color: var(--accent2); font-size: 14px; margin-bottom: 8px; }
        .tl-role { font-size: 24px; font-weight: 700; margin-bottom: 4px; font-family: 'Syne', sans-serif; }
        .tl-company { color: var(--text2); font-style: italic; margin-bottom: 16px; display: block; }
        .tl-desc { list-style: none; }
        .tl-desc li { margin-bottom: 12px; color: var(--text2); line-height: 1.6; position: relative; padding-left: 20px; }
        .tl-desc li::before { content: '→'; position: absolute; left: 0; color: var(--accent); }

        /* CHAT */
        .chat-messages { flex: 1; overflow-y: auto; padding: 24px; display: flex; flex-direction: column; gap: 16px; }
        .msg { padding: 16px; border-radius: 16px; font-size: 14px; line-height: 1.6; max-width: 85%; }
        .msg.ai { background: var(--surface); color: var(--text); align-self: flex-start; border-bottom-left-radius: 2px; }
        .msg.user { background: var(--accent); color: white; align-self: flex-end; border-bottom-right-radius: 2px; }

        .noise { position: fixed; inset: 0; opacity: 0.02; pointer-events: none; z-index: 1000; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E"); }
    </style>
</head>
<body>
<div class="noise"></div>

<!-- LANGUAGE SELECTOR -->
<div id="lang-overlay">
    <div class="lang-card">
        <div class="lang-logo">hwinh.</div>
        <p style="color:var(--text2); margin-bottom: 10px;">Select your preferred language / Chọn ngôn ngữ của bạn</p>
        <div class="lang-btn-group">
            <button class="lang-btn" onclick="startApp('en')">English</button>
            <button class="lang-btn" onclick="startApp('vi')">Tiếng Việt</button>
        </div>
    </div>
</div>

<div class="app" id="app-root">
    <!-- NAVIGATION -->
    <nav class="sidenav">
        <div class="nav-logo">hw</div>
        <div class="nav-item active" onclick="showView('home', this)"><i>◈</i><span id="nav-home">Home</span></div>
        <div class="nav-item" onclick="showView('exp', this)"><i>⟳</i><span id="nav-exp">Experience</span></div>
        <div class="nav-item" onclick="showView('project', this)"><i>⬡</i><span id="nav-proj">Projects</span></div>
        <div class="nav-item" onclick="showView('skill', this)"><i>◎</i><span id="nav-skill">Skills</span></div>
    </nav>

    <!-- MAIN VIEW -->
    <main class="visual-panel">
        
        <!-- HOME SECTION -->
        <div id="view-home" class="view-section">
            <span class="section-tag" id="home-tag">Portfolio 2025</span>
            <h1 class="view-title" id="home-title">Nguyễn <br><span>Hoàng Minh</span></h1>
            <h2 style="font-size: 24px; color: var(--accent2); margin-top: -30px; margin-bottom: 40px;" id="home-role">Product Owner & UX Strategist</h2>
            <p style="font-size: 18px; color: var(--text2); max-width: 700px; line-height: 1.8;" id="home-desc">
                I bridge the gap between complex AI systems and seamless human experiences. Specialized in Product Management with a focus on System Thinking and Human-Computer Interaction (HCI).
            </p>
            <div style="margin-top: 50px; display: flex; gap: 20px;">
                <div style="padding: 20px; background: var(--ink2); border-radius: 16px; border: 1px solid var(--border); flex: 1;">
                    <div style="font-size: 32px; font-weight: 800; color: var(--accent2);">3.53</div>
                    <div style="font-size: 12px; text-transform: uppercase; color: var(--text2);">GPA @ UEH University</div>
                </div>
                <div style="padding: 20px; background: var(--ink2); border-radius: 16px; border: 1px solid var(--border); flex: 1;">
                    <div style="font-size: 32px; font-weight: 800; color: var(--accent2);">72%</div>
                    <div style="font-size: 12px; text-transform: uppercase; color: var(--text2);">Technical ROI in AI Projects</div>
                </div>
                <div style="padding: 20px; background: var(--ink2); border-radius: 16px; border: 1px solid var(--border); flex: 1;">
                    <div style="font-size: 32px; font-weight: 800; color: var(--accent2);">Top 20</div>
                    <div style="font-size: 12px; text-transform: uppercase; color: var(--text2);">Innovation Finalist</div>
                </div>
            </div>
        </div>

        <!-- EXPERIENCE SECTION -->
        <div id="view-exp" class="view-section" style="display:none;">
            <span class="section-tag">Career Path</span>
            <h1 class="view-title"><span id="exp-title-1">Work</span> <span id="exp-title-2">Experience</span></h1>
            <div class="timeline" id="experience-list">
                <!-- Content injected by JS -->
            </div>
        </div>

        <!-- PROJECT SECTION -->
        <div id="view-project" class="view-section" style="display:none;">
            <span class="section-tag">Case Studies</span>
            <h1 class="view-title"><span id="proj-title-1">Featured</span> <span id="proj-title-2">Projects</span></h1>
            <div class="projects-grid" id="project-list">
                <!-- Content injected by JS -->
            </div>
        </div>

        <!-- SKILLS SECTION -->
        <div id="view-skill" class="view-section" style="display:none;">
            <span class="section-tag">Expertise</span>
            <h1 class="view-title"><span id="skill-title-1">Technical</span> <span id="skill-title-2">Stack</span></h1>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px;">
                <div id="skill-bars-pm">
                    <!-- PM skills here -->
                </div>
                <div id="skill-bars-tech">
                    <!-- Tech skills here -->
                </div>
            </div>
        </div>

    </main>

    <!-- CHAT ASSISTANT -->
    <aside class="chat-panel">
        <div style="padding: 24px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 12px;">
            <div style="width: 40px; height: 40px; background: var(--accent); border-radius: 10px; display: flex; align-items: center; justify-content: center;">🤖</div>
            <div>
                <div style="font-weight: 700; font-size: 14px;">Minh's Assistant</div>
                <div style="font-size: 11px; color: var(--green);">● Online</div>
            </div>
        </div>
        <div class="chat-messages" id="chat-box"></div>
        <div style="padding: 20px; border-top: 1px solid var(--border); display: grid; grid-template-columns: 1fr 1fr; gap: 10px;" id="chat-prompts">
            <!-- Prompts here -->
        </div>
    </aside>
</div>

<script>
const data = {
    en: {
        nav: { home: "Home", exp: "Work", proj: "Projects", skill: "Skills" },
        home: {
            tag: "Available for Roles 2025",
            title: "Nguyễn <br><span>Hoàng Minh</span>",
            role: "Product Owner Intern & UX Strategist",
            desc: "Expert in transforming complex technical requirements into user-centric digital products. Specialized in AI Management and Strategic UX Design. Driven by metrics (ROI/NPS) and System Thinking."
        },
        experience: [
            {
                date: "JAN 2025 - OCT 2025",
                role: "Project Management Executive",
                company: "Startup & Innovation Hub (SIHUB) - Dept. of Science & Technology",
                bullets: [
                    "Designed end-to-end customer journey maps for tech startups to optimize activation flows.",
                    "Managed feature prioritization using Agile framework and validated iterations via A/B testing.",
                    "Translated qualitative user pain points into structured User Requirements (URD).",
                    "Communicated insights to 150+ key stakeholders and the Board of Directors."
                ]
            },
            {
                date: "JUL 2024 - DEC 2024",
                role: "Research & Development Intern",
                company: "SIHUB - City-level Innovation Framework",
                bullets: [
                    "Conducted competency gap analysis for urban innovation initiatives.",
                    "Built structured documentation for city-level scientific research reports.",
                    "Collaborated with cross-functional teams to define core system functionalities."
                ]
            }
        ],
        projects: [
            {
                badge: "FLAGSHIP AI PROJECT",
                name: "EchoMind AI",
                desc: "A brain-to-text system decoding EEG signals into natural language. Managed full product lifecycle using Agile & RACI matrix. Focused on technical ROI and clinical application.",
                metrics: [
                    { val: "55-65", label: "Words/Min" },
                    { val: "< 1s", label: "Latency" },
                    { val: "72%", label: "Technical ROI" }
                ],
                stack: ["PyTorch", "Transformer", "CPMAI Framework", "Agile Sprints"]
            },
            {
                badge: "UX CASE STUDY",
                name: "E-Reader Ecosystem",
                desc: "Winner of Top 20 City-level Finalists. Applied HCI principles to design an educational device ecosystem. Mapped complex user stories for students and educators.",
                metrics: [
                    { val: "Top 20", label: "Innovation Awards" },
                    { val: "90%", label: "UX Score" }
                ],
                stack: ["HCI Principles", "Journey Mapping", "Figma", "User Stories"]
            }
        ],
        skills: {
            pm: [
                { name: "Journey Mapping", val: 95 },
                { name: "UX / HCI Design", val: 90 },
                { name: "Agile / Scrum (RACI)", val: 85 },
                { name: "Product Requirements (PRD)", val: 88 }
            ],
            tech: [
                { name: "Python / Data Analysis", val: 82 },
                { name: "PyTorch / ML Modeling", val: 75 },
                { name: "A/B Testing", val: 80 }
            ]
        },
        chat: {
            greeting: "Hello! I am Minh's AI. I can tell you about his work in SIHUB or his EchoMind project. What do you want to know?",
            prompts: ["Work Experience", "EchoMind Project", "Education", "UX Skills"],
            answers: {
                "Work Experience": "Minh has 3+ years in the startup ecosystem. At SIHUB, he managed 150+ stakeholders and focused on MVP delivery.",
                "EchoMind Project": "EchoMind is his masterpiece. It achieved a 72% ROI by decoding brain signals at 55-65 WPM using Transformer models.",
                "Education": "Minh is a top-tier student at UEH with a 3.53 GPA, specializing in Technology & Innovation Management.",
                "UX Skills": "He specializes in HCI (Human-Computer Interaction) and Journey Mapping to solve complex user bottlenecks."
            }
        }
    },
    vi: {
        nav: { home: "Trang chủ", exp: "Việc làm", proj: "Dự án", skill: "Kỹ năng" },
        home: {
            tag: "Sẵn sàng cho công việc 2025",
            title: "Nguyễn <br><span>Hoàng Minh</span>",
            role: "Product Owner & UX Strategist",
            desc: "Chuyên gia kết nối giữa hệ thống kỹ thuật phức tạp và trải nghiệm người dùng mượt mà. Tập trung vào Quản trị sản phẩm, Tư duy hệ thống và Tương tác Người-Máy (HCI)."
        },
        experience: [
            {
                date: "THÁNG 1/2025 - THÁNG 10/2025",
                role: "Chuyên viên Quản lý Dự án",
                company: "Trung tâm Đổi mới Sáng tạo SIHUB - Trực thuộc Sở Khoa học Công nghệ",
                bullets: [
                    "Thiết kế bản đồ hành trình người dùng (Journey Map) cho các startup công nghệ.",
                    "Quản lý ưu tiên tính năng sản phẩm bằng khung Agile và xác thực qua A/B Testing.",
                    "Chuyển đổi Pain-points của người dùng thành tài liệu yêu cầu hệ thống (URD) chuyên nghiệp.",
                    "Làm việc trực tiếp với hơn 150 stakeholders và Ban giám đốc."
                ]
            },
            {
                date: "THÁNG 7/2024 - THÁNG 12/2024",
                role: "Thực tập sinh Nghiên cứu & Phát triển (R&D)",
                company: "SIHUB - Đề án Đổi mới Sáng tạo cấp Thành phố",
                bullets: [
                    "Phân tích lỗ hổng năng lực (Competency Gap) cho các sáng kiến đổi mới đô thị.",
                    "Xây dựng hệ thống tài liệu chuẩn cho các báo cáo khoa học cấp thành phố.",
                    "Phối hợp liên đội nhóm để định nghĩa các tính năng cốt lõi của hệ thống."
                ]
            }
        ],
        projects: [
            {
                badge: "DỰ ÁN AI TRỌNG ĐIỂM",
                name: "EchoMind AI",
                desc: "Hệ thống chuyển đổi tín hiệu não (EEG) thành văn bản tự nhiên. Quản lý toàn bộ vòng đời sản phẩm bằng Agile & ma trận RACI. Tập trung vào chỉ số ROI kỹ thuật (72%) và ứng dụng lâm sàng.",
                metrics: [
                    { val: "55-65", label: "Từ/Phút" },
                    { val: "< 1s", label: "Độ trễ" },
                    { val: "72%", label: "ROI Kỹ thuật" }
                ],
                stack: ["PyTorch", "Transformer", "Khung CPMAI", "Agile Sprints"]
            },
            {
                badge: "UX CASE STUDY",
                name: "E-Reader Ecosystem",
                desc: "Top 20 Chung kết Đổi mới sáng tạo cấp Thành phố. Áp dụng nguyên lý HCI để thiết kế hệ sinh thái thiết bị giáo dục. Xây dựng User Stories phức tạp cho học sinh và giáo viên.",
                metrics: [
                    { val: "Top 20", label: "Giải thưởng" },
                    { val: "90%", label: "Điểm UX" }
                ],
                stack: ["Nguyên lý HCI", "Journey Mapping", "Figma", "User Stories"]
            }
        ],
        skills: {
            pm: [
                { name: "Journey Mapping", val: 95 },
                { name: "UX / HCI Design", val: 90 },
                { name: "Agile / Scrum (RACI)", val: 85 },
                { name: "Product Requirements (PRD)", val: 88 }
            ],
            tech: [
                { name: "Python / Data Analysis", val: 82 },
                { name: "PyTorch / ML Modeling", val: 75 },
                { name: "A/B Testing", val: 80 }
            ]
        },
        chat: {
            greeting: "Chào bạn! Tôi là AI của Minh. Tôi có thể kể cho bạn về kinh nghiệm của Minh tại SIHUB hoặc dự án EchoMind. Bạn muốn tìm hiểu gì?",
            prompts: ["Kinh nghiệm làm việc", "Dự án EchoMind", "Học vấn", "Kỹ năng UX"],
            answers: {
                "Kinh nghiệm làm việc": "Minh có hơn 3 năm trong hệ sinh thái startup. Tại SIHUB, anh ấy quản lý hơn 150 stakeholders và tập trung vào phát triển MVP.",
                "Dự án EchoMind": "Đây là dự án tâm huyết nhất của Minh. Sử dụng Transformer model đạt tốc độ 55-65 từ/phút và ROI kỹ thuật đạt 72%.",
                "Học vấn": "Minh là sinh viên ưu tú tại UEH với GPA 3.53, chuyên ngành Quản lý Công nghệ và Đổi mới Sáng tạo.",
                "Kỹ năng UX": "Anh ấy chuyên về HCI và Journey Mapping để giải quyết các nút thắt phức tạp trong trải nghiệm người dùng."
            }
        }
    }
};

let currentLang = 'en';

function startApp(lang) {
    currentLang = lang;
    document.getElementById('lang-overlay').style.opacity = '0';
    setTimeout(() => {
        document.getElementById('lang-overlay').style.display = 'none';
        document.getElementById('app-root').classList.add('visible');
        renderApp();
    }, 500);
}

function renderApp() {
    const l = data[currentLang];
    // Nav
    document.getElementById('nav-home').innerText = l.nav.home;
    document.getElementById('nav-exp').innerText = l.nav.exp;
    document.getElementById('nav-proj').innerText = l.nav.proj;
    document.getElementById('nav-skill').innerText = l.nav.skill;
    
    // Home
    document.getElementById('home-tag').innerText = l.home.tag;
    document.getElementById('home-title').innerHTML = l.home.title;
    document.getElementById('home-role').innerText = l.home.role;
    document.getElementById('home-desc').innerText = l.home.desc;
    
    // Experience
    let expHtml = '';
    l.experience.forEach(item => {
        expHtml += `
            <div class="timeline-item">
                <div class="tl-date">${item.date}</div>
                <div class="tl-role">${item.role}</div>
                <div class="tl-company">${item.company}</div>
                <ul class="tl-desc">
                    ${item.bullets.map(b => `<li>${b}</li>`).join('')}
                </ul>
            </div>
        `;
    });
    document.getElementById('experience-list').innerHTML = expHtml;

    // Projects
    let projHtml = '';
    l.projects.forEach(p => {
        projHtml += `
            <div class="project-card ${p.name.includes('EchoMind') ? 'featured' : ''}">
                <span class="project-badge">${p.badge}</span>
                <h3 style="font-size:28px; margin-bottom:12px;">${p.name}</h3>
                <p style="color:var(--text2); line-height:1.7;">${p.desc}</p>
                <div class="project-metrics">
                    ${p.metrics.map(m => `
                        <div>
                            <div class="metric-val">${m.val}</div>
                            <div class="metric-label">${m.label}</div>
                        </div>
                    `).join('')}
                </div>
                <div style="display:flex; gap:8px; flex-wrap:wrap;">
                    ${p.stack.map(s => `<span style="font-size:10px; padding:4px 10px; background:var(--ink); border-radius:4px; border:1px solid var(--border);">${s}</span>`).join('')}
                </div>
            </div>
        `;
    });
    document.getElementById('project-list').innerHTML = projHtml;

    // Skills
    const renderBars = (id, list) => {
        document.getElementById(id).innerHTML = list.map(s => `
            <div class="skill-bar-item">
                <div class="skill-bar-header"><span>${s.name}</span><span>${s.val}%</span></div>
                <div class="skill-bar-track"><div class="skill-bar-fill" style="width:${s.val}%"></div></div>
            </div>
        `).join('');
    };
    renderBars('skill-bars-pm', l.skills.pm);
    renderBars('skill-bars-tech', l.skills.tech);

    // Chat
    document.getElementById('chat-box').innerHTML = `<div class="msg ai">${l.chat.greeting}</div>`;
    document.getElementById('chat-prompts').innerHTML = l.chat.prompts.map(p => `
        <button class="lang-btn" style="font-size:12px; padding:10px; width:100%;" onclick="askAI('${p}')">${p}</button>
    `).join('');
}

function showView(viewId, el) {
    document.querySelectorAll('.view-section').forEach(v => v.style.display = 'none');
    document.getElementById('view-' + viewId).style.display = 'block';
    document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
    el.classList.add('active');
}

function askAI(prompt) {
    const l = data[currentLang];
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="msg user">${prompt}</div>`;
    setTimeout(() => {
        chatBox.innerHTML += `<div class="msg ai">${l.chat.answers[prompt] || "..."}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 600);
}

// Default View
window.onload = () => { /* Lang overlay handles start */ };
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
