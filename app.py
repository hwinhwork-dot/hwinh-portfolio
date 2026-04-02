import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Hoàng Minh | Product & UX", page_icon="◈", initial_sidebar_state="collapsed")

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
    <title>Hoang Minh | Product & UX</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --ink: #0a0a0f;
            --ink2: #12121a;
            --ink3: #1c1c28;
            --surface: #1e1e2e;
            --surface2: #252538;
            --border: rgba(255,255,255,0.07);
            --border2: rgba(255,255,255,0.12);
            --text: #e8e8f0;
            --text2: #9898b0;
            --accent: #7c6af7;
            --accent2: #a594fc;
            --accent3: #c4b8fe;
            --gold: #f0c060;
            --green: #52d18a;
            --coral: #ff7b6b;
            --teal: #4dd9c0;
        }

        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: 'DM Sans', sans-serif;
            background: var(--ink);
            color: var(--text);
            height: 100vh;
            overflow: hidden;
        }

        /* === LANGUAGE OVERLAY === */
        #lang-overlay {
            position: fixed;
            inset: 0;
            background: var(--ink);
            z-index: 9999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: opacity 0.6s ease, visibility 0.6s;
        }

        .lang-title {
            font-family: 'Syne', sans-serif;
            font-size: 32px;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 40px;
            text-align: center;
        }

        .lang-options {
            display: flex;
            gap: 24px;
        }

        .lang-btn {
            background: var(--surface);
            border: 1px solid var(--border2);
            color: var(--text);
            padding: 20px 40px;
            border-radius: 16px;
            font-family: 'DM Sans', sans-serif;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
        }

        .lang-btn:hover {
            border-color: var(--accent);
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(124,106,247,0.2);
        }

        .lang-btn span {
            font-family: 'DM Mono', monospace;
            font-size: 12px;
            color: var(--text2);
        }

        /* === LAYOUT === */
        .app {
            display: flex;
            height: 100vh;
            width: 100%;
            opacity: 0;
            transition: opacity 0.8s ease;
        }

        /* === LEFT SIDEBAR NAV === */
        .sidenav {
            width: 90px;
            height: 100%;
            background: var(--ink2);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 32px 0;
            gap: 16px;
            flex-shrink: 0;
            z-index: 10;
        }

        .nav-logo {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 18px;
            color: var(--accent2);
            margin-bottom: 24px;
        }

        .nav-item {
            width: 56px;
            height: 56px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            color: var(--text2);
            border: 1px solid transparent;
            position: relative;
        }

        .nav-item svg {
            width: 24px;
            height: 24px;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .nav-item:hover { background: var(--surface); color: var(--text); }
        .nav-item.active {
            background: var(--accent);
            color: white;
            border-color: var(--accent2);
            box-shadow: 0 0 20px rgba(124,106,247,0.3);
        }

        .nav-tooltip {
            position: absolute;
            left: 72px;
            background: var(--surface2);
            color: var(--text);
            font-size: 12px;
            font-family: 'DM Mono', monospace;
            padding: 6px 12px;
            border-radius: 6px;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.15s;
            border: 1px solid var(--border2);
            z-index: 100;
        }
        .nav-item:hover .nav-tooltip { opacity: 1; }

        /* === VISUAL PANEL === */
        .visual-panel {
            flex: 1;
            height: 100%;
            overflow-y: auto;
            background: var(--ink);
            position: relative;
        }

        .visual-panel::-webkit-scrollbar { width: 6px; }
        .visual-panel::-webkit-scrollbar-track { background: transparent; }
        .visual-panel::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 6px; }

        /* === CHAT PANEL === */
        .chat-panel {
            width: 420px;
            height: 100%;
            flex-shrink: 0;
            background: var(--ink2);
            border-left: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }

        /* === NOISE TEXTURE OVERLAY === */
        .noise {
            position: fixed;
            inset: 0;
            opacity: 0.03;
            pointer-events: none;
            z-index: 100;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
        }

        /* ==================== VIEWS ==================== */
        .view-content {
            padding: 60px 80px;
            min-height: 100%;
        }

        .welcome-eyebrow { display: flex; align-items: center; gap: 10px; margin-bottom: 32px; }
        .status-dot { width: 10px; height: 10px; background: var(--green); border-radius: 50%; box-shadow: 0 0 10px var(--green); animation: pulse-green 2s infinite; }
        @keyframes pulse-green { 0%, 100% { box-shadow: 0 0 6px var(--green); } 50% { box-shadow: 0 0 18px var(--green); } }
        .status-text { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--green); letter-spacing: 1px; text-transform: uppercase; }

        .welcome-name { font-family: 'Syne', sans-serif; font-size: clamp(48px, 5vw, 80px); font-weight: 800; line-height: 1; letter-spacing: -2px; margin-bottom: 16px; }
        .welcome-name .accent-word { color: var(--accent2); display: block; }
        .welcome-role { font-size: 20px; color: var(--text2); font-weight: 300; margin-bottom: 40px; font-style: italic; }
        
        .welcome-summary { font-size: 16px; line-height: 1.8; color: var(--text2); max-width: 600px; margin-bottom: 48px; border-left: 3px solid var(--accent); padding-left: 24px; }
        
        .contact-row { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 56px; }
        .contact-chip { display: flex; align-items: center; gap: 8px; padding: 10px 20px; background: var(--surface); border: 1px solid var(--border2); border-radius: 10px; font-size: 13px; font-family: 'DM Mono', monospace; color: var(--text2); transition: all 0.2s; }
        .contact-chip:hover { border-color: var(--accent); color: var(--text); }

        .stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 650px; margin-bottom: 56px; }
        .stat-card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 24px; position: relative; overflow: hidden; }
        .stat-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--accent), var(--teal)); }
        .stat-number { font-family: 'Syne', sans-serif; font-size: 36px; font-weight: 800; color: var(--text); line-height: 1; }
        .stat-label { font-size: 12px; color: var(--text2); margin-top: 8px; text-transform: uppercase; letter-spacing: 0.5px; }

        .section-tag { display: inline-flex; align-items: center; gap: 8px; font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px; }
        .section-tag::before { content: '◈'; font-size: 14px; }

        .view-title { font-family: 'Syne', sans-serif; font-size: 48px; font-weight: 800; letter-spacing: -1.5px; color: var(--text); margin-bottom: 56px; line-height: 1; }
        .view-title span { color: var(--accent2); }

        /* TIMELINE */
        .timeline { position: relative; padding-left: 32px; }
        .timeline::before { content: ''; position: absolute; left: 0; top: 8px; bottom: 8px; width: 2px; background: linear-gradient(to bottom, var(--accent), transparent); }
        .timeline-item { position: relative; margin-bottom: 48px; }
        .timeline-item::before { content: ''; position: absolute; left: -37px; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: var(--accent2); box-shadow: 0 0 12px rgba(165,148,252,0.5); }
        .timeline-item.past::before { background: var(--text2); box-shadow: none; }
        
        .tl-period { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); letter-spacing: 1px; margin-bottom: 10px; text-transform: uppercase; }
        .tl-role { font-family: 'Syne', sans-serif; font-size: 24px; font-weight: 700; margin-bottom: 6px; }
        .tl-company { font-size: 15px; color: var(--text2); font-style: italic; margin-bottom: 20px; }
        .tl-bullets { list-style: none; display: flex; flex-direction: column; gap: 12px; }
        .tl-bullets li { font-size: 15px; color: var(--text2); line-height: 1.7; padding-left: 20px; position: relative; }
        .tl-bullets li::before { content: '→'; position: absolute; left: 0; color: var(--accent); font-weight: bold; }
        .tl-bullets li strong { color: var(--text); font-weight: 500; }
        .tl-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 16px; }
        .tl-tag { font-family: 'DM Mono', monospace; font-size: 11px; padding: 4px 12px; border-radius: 6px; background: rgba(124,106,247,0.1); border: 1px solid rgba(124,106,247,0.25); color: var(--accent3); }

        /* PROJECTS */
        .projects-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
        .project-card { background: var(--surface); border: 1px solid var(--border); border-radius: 24px; padding: 32px; cursor: pointer; transition: all 0.3s; position: relative; overflow: hidden; }
        .project-card::after { content: ''; position: absolute; inset: 0; border-radius: 24px; opacity: 0; transition: opacity 0.3s; }
        .project-card.featured::after { background: linear-gradient(135deg, rgba(124,106,247,0.08) 0%, transparent 60%); }
        .project-card:hover { border-color: var(--accent); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
        .project-card:hover::after { opacity: 1; }
        .project-card.featured { grid-column: 1 / -1; display: grid; grid-template-columns: 1fr auto; gap: 32px; align-items: start; }
        
        .project-badge { font-family: 'DM Mono', monospace; font-size: 11px; padding: 6px 12px; border-radius: 20px; font-weight: 400; text-transform: uppercase;}
        .badge-featured { background: rgba(240,192,96,0.15); color: var(--gold); border: 1px solid rgba(240,192,96,0.3); }
        .badge-active { background: rgba(82,209,138,0.15); color: var(--green); border: 1px solid rgba(82,209,138,0.3); }
        .badge-top20 { background: rgba(255,123,107,0.15); color: var(--coral); border: 1px solid rgba(255,123,107,0.3); }

        .project-name { font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 700; margin: 12px 0 8px; letter-spacing: -0.5px; }
        .project-desc { font-size: 15px; color: var(--text2); line-height: 1.7; margin-bottom: 20px; }
        .project-metrics { display: flex; gap: 24px; margin: 16px 0; }
        .metric { text-align: center; }
        .metric-val { font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 700; color: var(--accent2); }
        .metric-lbl { font-size: 11px; color: var(--text2); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
        .tech-stack { display: flex; flex-wrap: wrap; gap: 8px; }
        .tech-pill { font-family: 'DM Mono', monospace; font-size: 11px; padding: 4px 12px; border-radius: 6px; background: var(--ink3); border: 1px solid var(--border2); color: var(--text2); }

        /* SKILLS */
        .skills-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start; }
        .skill-group { margin-bottom: 32px; }
        .skill-group-label { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px; }
        .skill-bar-item { margin-bottom: 16px; }
        .skill-bar-header { display: flex; justify-content: space-between; margin-bottom: 8px; }
        .skill-bar-name { font-size: 14px; font-weight: 500; }
        .skill-bar-pct { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--text2); }
        .skill-bar-track { height: 6px; background: var(--surface2); border-radius: 3px; overflow: hidden; }
        .skill-bar-fill { height: 100%; border-radius: 3px; background: linear-gradient(90deg, var(--accent), var(--teal)); transform-origin: left; transform: scaleX(0); transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
        .skill-bar-fill.animate { transform: scaleX(1); }

        /* EDU */
        .edu-hero { background: linear-gradient(135deg, var(--surface) 0%, var(--surface2) 100%); border: 1px solid var(--border); border-radius: 24px; padding: 40px; margin-bottom: 32px; position: relative; overflow: hidden; }
        .edu-hero::before { content: 'UEH'; position: absolute; right: -20px; bottom: -40px; font-family: 'Syne', sans-serif; font-size: 160px; font-weight: 800; color: rgba(255,255,255,0.02); line-height: 1; pointer-events: none; }
        .gpa-badge { display: inline-flex; align-items: center; gap: 12px; background: rgba(240,192,96,0.1); border: 1px solid rgba(240,192,96,0.3); border-radius: 16px; padding: 16px 24px; margin-top: 16px; }

        .cert-card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 16px 20px; margin-bottom: 12px; display: flex; align-items: center; gap: 16px; }
        
        /* CHAT PANEL */
        .chat-header { padding: 24px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 16px; }
        .chat-avatar { width: 44px; height: 44px; border-radius: 14px; background: linear-gradient(135deg, var(--accent), var(--teal)); display: flex; align-items: center; justify-content: center; font-size: 20px; }
        .chat-name { font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700; }
        .chat-subtitle { font-size: 12px; color: var(--green); font-family: 'DM Mono', monospace; margin-top: 4px; }
        .reset-btn { margin-left: auto; background: none; border: 1px solid var(--border2); color: var(--text2); font-size: 12px; padding: 8px 16px; border-radius: 8px; cursor: pointer; font-family: 'DM Mono', monospace; transition: all 0.2s; }
        .reset-btn:hover { border-color: var(--accent); color: var(--accent2); }

        .chat-messages { flex: 1; overflow-y: auto; padding: 24px; display: flex; flex-direction: column; gap: 20px; }
        .chat-messages::-webkit-scrollbar { width: 4px; }
        .chat-messages::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

        .msg-row { display: flex; gap: 12px; align-items: flex-end; animation: msg-in 0.3s ease-out; }
        @keyframes msg-in { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .msg-row.user { flex-direction: row-reverse; }
        .msg-avatar-small { width: 32px; height: 32px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; }
        .msg-avatar-small.ai { background: linear-gradient(135deg, var(--accent), var(--teal)); }
        .msg-avatar-small.user { background: var(--surface2); border: 1px solid var(--border2); }
        
        .msg-bubble { max-width: 80%; padding: 14px 18px; border-radius: 18px; font-size: 14px; line-height: 1.6; }
        .msg-bubble.ai { background: var(--surface); border: 1px solid var(--border2); color: var(--text); border-bottom-left-radius: 4px; }
        .msg-bubble.user { background: var(--accent); color: white; border-bottom-right-radius: 4px; }

        .cursor-blink { display: inline-block; width: 8px; height: 16px; background: var(--accent2); margin-left: 4px; animation: blink 1s step-end infinite; vertical-align: middle; }
        @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

        .chat-footer { padding: 20px; border-top: 1px solid var(--border); }
        .prompts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .prompt-btn { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 12px; font-size: 13px; color: var(--text2); cursor: pointer; transition: all 0.2s; text-align: left; display: flex; align-items: center; gap: 8px; }
        .prompt-btn:hover { border-color: var(--accent); color: var(--text); background: var(--surface2); }
        .prompt-btn:disabled { opacity: 0.4; cursor: not-allowed; }

        .fade-up { animation: fadeUp 0.6s ease-out forwards; opacity: 0; }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .d1{animation-delay:0.1s} .d2{animation-delay:0.2s} .d3{animation-delay:0.3s} .d4{animation-delay:0.4s} .d5{animation-delay:0.5s}
        .subtle-div { height: 1px; background: var(--border); margin: 40px 0; }

        /* citations */
        .cite { opacity: 0.4; font-size: 0.85em; cursor: help; }
        .cite:hover { opacity: 1; color: var(--accent2); }

    </style>
</head>
<body>
<div class="noise"></div>

<div id="lang-overlay">
    <div class="lang-title">Choose your language <br><span style="font-size:24px; color:var(--text2); font-weight:400;">Chọn ngôn ngữ hiển thị</span></div>
    <div class="lang-options">
        <button class="lang-btn" onclick="selectLanguage('en')">
            English
            <span>Global Recruiter</span>
        </button>
        <button class="lang-btn" onclick="selectLanguage('vi')">
            Tiếng Việt
            <span>Nhà Tuyển Dụng VN</span>
        </button>
    </div>
</div>

<div class="app" id="main-app">
    <nav class="sidenav">
        <div class="nav-logo">HM</div>

        <div class="nav-item active" data-view="welcome" onclick="switchView('welcome', this)">
            <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            <span class="nav-tooltip" id="nav-overview">Overview</span>
        </div>
        <div class="nav-item" data-view="experience" onclick="switchView('experience', this)">
            <svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            <span class="nav-tooltip" id="nav-exp">Experience</span>
        </div>
        <div class="nav-item" data-view="projects" onclick="switchView('projects', this)">
            <svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
            <span class="nav-tooltip" id="nav-proj">Projects</span>
        </div>
        <div class="nav-item" data-view="skills" onclick="switchView('skills', this)">
            <svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            <span class="nav-tooltip" id="nav-skills">Skills</span>
        </div>
        <div class="nav-item" data-view="education" onclick="switchView('education', this)">
            <svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            <span class="nav-tooltip" id="nav-edu">Education</span>
        </div>
    </nav>

    <main class="visual-panel">
        <div id="view-welcome" class="view-content">
            <div class="welcome-eyebrow fade-up">
                <div class="status-dot"></div>
                <span class="status-text" id="w-status">Available for opportunities · HCMC, Vietnam</span>
            </div>
            <h1 class="welcome-name fade-up d1">
                Nguyễn <span class="accent-word">Hoàng Minh</span>
            </h1>
            <p class="welcome-role fade-up d2" id="w-role">Product Owner Intern · UX Strategist</p>
            <p class="welcome-summary fade-up d3" id="w-summary"></p>
            <div class="contact-row fade-up d4">
                <div class="contact-chip">✉ hwinh.work@gmail.com</div>
                <div class="contact-chip">📞 +84 765 828 191</div>
                <div class="contact-chip">📍 Hồ Chí Minh</div>
                <div class="contact-chip">🎓 UEH · GPA 3.53</div>
            </div>
            <div class="stat-grid fade-up d5">
                <div class="stat-card">
                    <div class="stat-number">3+</div>
                    <div class="stat-label" id="w-stat1">Years Exp.</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">150+</div>
                    <div class="stat-label" id="w-stat2">Stakeholders</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">8</div>
                    <div class="stat-label" id="w-stat3">Agile Sprints</div>
                </div>
            </div>
        </div>

        <div id="view-experience" class="view-content" style="display:none">
            <div class="section-tag" id="e-tag">Work History</div>
            <h2 class="view-title" id="e-title"></h2>
            <div class="timeline" id="e-timeline"></div>
        </div>

        <div id="view-projects" class="view-content" style="display:none">
            <div class="section-tag" id="p-tag">Product Experience</div>
            <h2 class="view-title" id="p-title"></h2>
            <div class="projects-grid" id="p-grid"></div>
        </div>

        <div id="view-skills" class="view-content" style="display:none">
            <div class="section-tag" id="s-tag">Competencies</div>
            <h2 class="view-title" id="s-title"></h2>
            <div class="skills-layout">
                <div id="s-bars"></div>
                <div>
                    <div class="skill-group-label" id="s-radar-tag">Radar Overview</div>
                    <div style="width:100%;height:300px;position:relative;margin-bottom:32px;">
                        <canvas id="skillsChart"></canvas>
                    </div>
                    <div class="skill-group-label" id="s-cert-tag">Certifications</div>
                    <div id="s-certs"></div>
                </div>
            </div>
        </div>

        <div id="view-education" class="view-content" style="display:none">
            <div class="section-tag" id="ed-tag">Academic Background</div>
            <h2 class="view-title" id="ed-title"></h2>
            <div class="edu-hero">
                <div style="font-family:'DM Mono',monospace;font-size:12px;color:var(--accent2);letter-spacing:1px;margin-bottom:16px;">AUG 2022 — AUG 2026</div>
                <h3 style="font-family:'Syne',sans-serif;font-size:28px;font-weight:800;color:var(--text);margin-bottom:8px;" id="ed-uni">Đại học Kinh tế TP.HCM</h3>
                <p style="color:var(--text2);font-size:16px;margin-bottom:24px;" id="ed-major"></p>
                <div class="gpa-badge">
                    <span style="font-size:28px;">🏆</span>
                    <div>
                        <div style="font-size:12px;color:var(--text2);margin-bottom:4px;">Grade Point Average</div>
                        <div class="gpa-value">3.53 / 4.0</div>
                    </div>
                </div>
            </div>
            <div style="margin-bottom:32px;" id="ed-courses"></div>
        </div>
    </main>

    <aside class="chat-panel">
        <div class="chat-header">
            <div class="chat-avatar">🤖</div>
            <div>
                <div class="chat-name" id="c-name">Minh's AI Assistant</div>
                <div class="chat-subtitle" id="c-sub">● Online · Ready to answer</div>
            </div>
            <button class="reset-btn" onclick="resetChat()" id="c-reset">↺ Reset</button>
        </div>
        <div class="chat-messages" id="chat-messages"></div>
        <div class="chat-footer">
            <div class="prompts-grid" id="prompts-grid"></div>
        </div>
    </aside>
</div>

<script>
// === MULTILINGUAL DATA (English & Vietnamese) ===
const i18n = {
    en: {
        nav: { overview: "Overview", exp: "Experience", proj: "Projects", skills: "Skills", edu: "Education" },
        welcome: {
            status: "Available for opportunities · HCMC, Vietnam",
            role: "Product Owner Intern · UX Strategist",
            summary: "Young professional in Technology & Innovation Management — building at the intersection of <strong style='color:var(--text)'>UX Design</strong>, <strong style='color:var(--text)'>System Thinking</strong>, and <strong style='color:var(--text)'>AI</strong>. I translate complex user data and pain points into seamless, measurable product experiences.",
            stat1: "Years Exp.", stat2: "Stakeholders", stat3: "Agile Sprints"
        },
        experience: {
            tag: "Work History", title: "Work <span>Experience</span>",
            items: [
                {
                    period: "JAN 2025 — OCT 2025 · PRESENT", role: "Project Management Executive",
                    company: "Startup & Innovation Hub of HCMC (SIHUB) · Under Dept. of Science & Technology",
                    bullets: [
                        "<strong>Customer Journey Mapping & MVP Delivery:</strong> Designed end-to-end digital journey maps for tech startups, building onboarding & activation flows. Defined core user problems and translated them into clear user stories.",
                        "<strong>Pain Point Resolution & Testing:</strong> Monitored touchpoints to detect operational bottlenecks. Applied A/B testing and Interleaving experiments to validate feature iterations before full-scale rollout.",
                        "<strong>Omnichannel Data & Stakeholders:</strong> Acted as the main focal point with startup founders, analyzing behavioral data to improve satisfaction metrics (NPS focus) and reporting insights to the Board."
                    ],
                    tags: ["Customer Journey", "A/B Testing", "MVP", "Stakeholder Mgmt"]
                },
                {
                    period: "JUL 2024 — DEC 2024", role: "Research & Development Intern",
                    company: "SIHUB · Executed data-driven project management for city-level framework",
                    bullets: [
                        "<strong>Data Analysis & Requirements:</strong> Led end-to-end data lifecycle for competency gap analysis involving 150+ key stakeholders.",
                        "<strong>Structured Documentation:</strong> Drafted strategic reports and structured documentation (URD standards), translating qualitative user problems into actionable system requirements."
                    ],
                    tags: ["Data Analysis", "URD Standards", "150+ Stakeholders"]
                }
            ]
        },
        projects: {
            tag: "Product Experience", title: "Featured <span>Projects</span>",
            items: [
                {
                    id: "echomind", badge: "★ Flagship Project", badgeClass: "badge-featured",
                    date: "Sep–Dec 2025", name: "EchoMind AI", role: "AI-Based Brain-to-Text System · Project Lead",
                    desc: "An AI system translating non-invasive EEG signals into text. As Project Lead, I managed the full lifecycle using the CPMAI framework and Agile/Scrum methodologies across 8 Sprints <span class='cite'>[cite: 1467, 1481]</span>. When our baseline Seq2Seq LSTM model failed due to an information bottleneck (Mode Collapse), I strategically pivoted the team to a Transformer-based architecture with Multi-Head Attention <span class='cite'></span>. We designed an Expert Dashboard with Attention Maps to solve the 'black box' problem in healthcare <span class='cite'>[cite: 1453]</span>.",
                    m1: "55-65", m1l: "WPM Output", m2: "<1s", m2l: "Latency", m3: "72%", m3l: "Tech ROI",
                    tech: ["Python", "PyTorch", "Transformer", "Agile/Scrum", "RACI Matrix", "Product Strategy"]
                },
                {
                    id: "ereader", badge: "🏆 Top 20 Finalist", badgeClass: "badge-top20",
                    date: "Mar–Jun 2025", name: "E-Reader Ecosystem", role: "Product Lead · HCMC People's Committee",
                    desc: "Designed an end-to-end user journey from device provisioning to content updates, applying Human-Computer Interaction (HCI) standards to minimize cognitive load. Decomposed student pain points into structured feature sets with clear user stories and logical flows.",
                    tech: ["HCI Principles", "UX Design", "Journey Mapping"]
                },
                {
                    id: "startup", badge: "● Ongoing", badgeClass: "badge-active",
                    date: "Jul 2024 — Now", name: "Startup Events Ops", role: "Operations · Innovation Ecosystem",
                    desc: "Directly operated city-level innovation events: Univ.Star 2024/2025 and WHISE 2024 week — connecting startup founders, investors, and ecosystem builders.",
                    tech: ["Event Management", "Stakeholder Comm"]
                }
            ]
        },
        skills: {
            tag: "Competencies", title: "Professional <span>Skills</span>", radar: "Radar Overview", certTag: "Certifications",
            groups: [
                { name: "Product Management", items: [{n: "Journey Mapping", p: "95%"}, {n: "UX / HCI Design", p: "90%"}, {n: "Agile / Scrum (CPMAI)", p: "85%"}, {n: "PRD & User Stories", p: "85%"}, {n: "A/B Testing", p: "82%"}] },
                { name: "Data & Tech", items: [{n: "Python & PyTorch", p: "80%"}, {n: "Data Analysis", p: "80%"}, {n: "System Architecture", p: "75%"}] }
            ],
            certs: [
                { i: "🏅", n: "Google Project Management", org: "Coursera · Google" },
                { i: "📊", n: "Google Business Intelligence", org: "Coursera · Google" },
                { i: "🔄", n: "Agile Management", org: "Professional Certification" },
                { i: "🗣️", n: "TOEIC · English Proficiency", org: "Preparing for certification", dash: true, prog: "In Progress" }
            ]
        },
        education: {
            tag: "Academic Background", title: "Education & <span>Awards</span>", uni: "University of Economics HCMC",
            major: "Bachelor in Technology & Innovation Management",
            courseTag: "Relevant Coursework",
            courses: ["Design Thinking", "Human-Computer Interaction (HCI)", "Innovation Management", "Business Intelligence", "Project AI"]
        },
        chat: {
            name: "Minh's AI Assistant", sub: "● Online · Ready to answer", reset: "↺ Reset",
            greeting: "Hello! I am the AI representative for Nguyen Hoang Minh — a Product Owner Intern with a strong foundation in UX Strategy and System Thinking.\n\nMinh is seeking opportunities to apply his user journey design and product management skills in real-world product environments. What would you like to know more about?",
            prompts: [
                { id: "exp", icon: "💼", label: "Experience" },
                { id: "proj", icon: "🚀", label: "Projects" },
                { id: "echomind", icon: "🧠", label: "EchoMind AI" },
                { id: "skills", icon: "🛠️", label: "Skills" }
            ],
            ans_exp: "Minh has over 3 years of experience at SIHUB (Startup & Innovation Hub of HCMC).\n\n◈ Current Role: Project Management Executive\nMinh designs end-to-end digital journey maps for tech startups, builds activation flows, and validates features via A/B testing. He approaches NPS not just as a metric, but as a system of behavioral signals.\n\n◈ Previous: R&D Intern\nLed competency gap analysis for 150+ key stakeholders and drafted URD standard documentation.",
            ans_proj: "Minh has 3 standout projects demonstrating his Product & Technical thinking:\n\n🧠 EchoMind AI (Flagship)\nA Brain-to-text system where Minh acted as Project Lead. Managed 8 Sprints using Agile & CPMAI. Pivoted the model from LSTM to Transformer to solve bottlenecks.\n\n📚 E-Reader Ecosystem\nApplied HCI principles for student user journeys. Top 20 Finalist at a City-level competition.\n\n🚀 Startup Events\nOperated large-scale innovation events (Univ.Star, WHISE) connecting founders and investors.",
            ans_echomind: "EchoMind AI is Minh's flagship project (Sep-Dec 2025). As Project Lead, he didn't just write code; he managed the product vision.\n\n◈ The Problem: Locked-in syndrome patients cannot communicate.\n◈ The Solution: A non-invasive EEG-to-text system.\n◈ Product Decisions: When the initial LSTM model failed (Mode Collapse), Minh directed the pivot to a Transformer model <span class='cite'></span>.\n◈ Outcomes: Achieved 55-65 Words Per Minute with <1s latency <span class='cite'>[cite: 1476]</span>. Calculated a Technical ROI of 72% compared to traditional AAC devices <span class='cite'>[cite: 1650]</span>.\n◈ UX Focus: Designed an 'Expert Dashboard' with Attention Maps to provide transparency (Explainable AI) for doctors <span class='cite'>[cite: 1453]</span>.",
            ans_skills: "Minh positions himself at the intersection of 3 competencies:\n\n◈ Product Craft (Core strength)\n→ Journey Mapping · UX/HCI Design\n→ Agile/Scrum Execution (CPMAI, RACI)\n→ PRD Writing, User Stories, A/B Testing\n\n◈ Data & Systems Thinking\n→ Python · Data Analysis\n→ Understanding of PyTorch/ML (proven in EchoMind)\n\n◈ Soft Skills\n→ Cross-functional stakeholder management (150+ contacts)\n→ Strategic documentation to Board level"
        }
    },
    vi: {
        nav: { overview: "Tổng quan", exp: "Kinh nghiệm", proj: "Dự án", skills: "Kỹ năng", edu: "Học vấn" },
        welcome: {
            status: "Sẵn sàng đón nhận cơ hội mới · TP.HCM",
            role: "Product Owner Intern · UX Strategist",
            summary: "Chuyên gia trẻ về Quản lý Công nghệ & Đổi mới Sáng tạo — xây dựng sản phẩm tại giao điểm của <strong style='color:var(--text)'>UX Design</strong>, <strong style='color:var(--text)'>System Thinking</strong>, và <strong style='color:var(--text)'>AI</strong>. Tôi chuyển hoá dữ liệu người dùng và 'nỗi đau' (pain points) phức tạp thành các trải nghiệm sản phẩm mượt mà và đo lường được.",
            stat1: "Năm kinh nghiệm", stat2: "Stakeholders", stat3: "Agile Sprints"
        },
        experience: {
            tag: "Lịch sử làm việc", title: "Kinh nghiệm <span>Làm việc</span>",
            items: [
                {
                    period: "THÁNG 1 2025 — THÁNG 10 2025 · HIỆN TẠI", role: "Chuyên viên Quản lý Dự án (Project Mgmt Exec)",
                    company: "Trung tâm Hỗ trợ Khởi nghiệp & Đổi mới sáng tạo TP.HCM (SIHUB) · Trực thuộc Sở KH&CN",
                    bullets: [
                        "<strong>Thiết kế Hành trình Khách hàng & Triển khai MVP:</strong> Thiết kế bản đồ hành trình số (digital journey maps) cho các startup công nghệ. Định nghĩa các vấn đề cốt lõi của người dùng và chuyển đổi thành User Stories rõ ràng.",
                        "<strong>Giải quyết Vấn đề & Kiểm thử:</strong> Theo dõi các điểm chạm (touchpoints) để phát hiện điểm nghẽn vận hành. Áp dụng A/B testing để kiểm chứng các tính năng trước khi tung ra diện rộng.",
                        "<strong>Quản lý Dữ liệu Đa kênh & Stakeholder:</strong> Làm đầu mối chính với các founder startup, phân tích dữ liệu hành vi để cải thiện chỉ số hài lòng (tập trung vào NPS) và báo cáo chiến lược lên Ban Giám đốc."
                    ],
                    tags: ["Customer Journey", "A/B Testing", "MVP", "Stakeholder Mgmt"]
                },
                {
                    period: "THÁNG 7 2024 — THÁNG 12 2024", role: "Thực tập sinh R&D",
                    company: "SIHUB · Quản lý dự án dựa trên dữ liệu cho khung năng lực cấp thành phố",
                    bullets: [
                        "<strong>Phân tích Dữ liệu & Lấy Yêu cầu:</strong> Dẫn dắt vòng đời dữ liệu (end-to-end) cho việc phân tích khoảng trống năng lực, làm việc với hơn 150 stakeholders chủ chốt.",
                        "<strong>Tài liệu hóa Hệ thống:</strong> Soạn thảo các báo cáo chiến lược và tài liệu hệ thống (chuẩn URD), dịch các vấn đề định tính của người dùng thành các yêu cầu hệ thống khả thi."
                    ],
                    tags: ["Phân tích Dữ liệu", "Chuẩn URD", "150+ Stakeholders"]
                }
            ]
        },
        projects: {
            tag: "Kinh nghiệm Sản phẩm", title: "Dự án <span>Nổi bật</span>",
            items: [
                {
                    id: "echomind", badge: "★ Dự án Trọng điểm", badgeClass: "badge-featured",
                    date: "Tháng 9–12 2025", name: "EchoMind AI", role: "Hệ thống AI chuyển đổi Sóng não thành Văn bản · Project Lead",
                    desc: "Hệ thống AI dịch tín hiệu điện não đồ (EEG) phi xâm lấn thành văn bản. Với vai trò Project Lead, tôi quản lý toàn bộ vòng đời dự án bằng khung CPMAI và Agile/Scrum qua 8 Sprints <span class='cite'>[cite: 1467, 1481]</span>. Khi mô hình Baseline (Seq2Seq LSTM) thất bại do 'nút thắt cổ chai' thông tin (Mode Collapse), tôi đã quyết đoán định hướng nhóm chuyển sang kiến trúc Transformer <span class='cite'></span>. Nhóm cũng thiết kế Dashboard chuyên gia với Attention Maps để giải quyết rào cản 'hộp đen' trong y tế <span class='cite'>[cite: 1453]</span>.",
                    m1: "55-65", m1l: "Tốc độ (WPM)", m2: "<1s", m2l: "Độ trễ", m3: "72%", m3l: "ROI Kỹ thuật",
                    tech: ["Python", "PyTorch", "Transformer", "Agile/Scrum", "Ma trận RACI", "Product Strategy"]
                },
                {
                    id: "ereader", badge: "🏆 Top 20 Chung cuộc", badgeClass: "badge-top20",
                    date: "Tháng 3–6 2025", name: "Hệ sinh thái E-Reader", role: "Product Lead · UBND TP.HCM",
                    desc: "Thiết kế hành trình người dùng (end-to-end) từ việc cấp phát thiết bị đến cập nhật nội dung, áp dụng tiêu chuẩn Tương tác Người-Máy (HCI) để giảm thiểu tải nhận thức (cognitive load). Phân rã 'nỗi đau' của học sinh thành các bộ tính năng với User Stories và luồng logic rõ ràng.",
                    tech: ["Nguyên tắc HCI", "Thiết kế UX", "Hành trình Người dùng"]
                },
                {
                    id: "startup", badge: "● Đang diễn ra", badgeClass: "badge-active",
                    date: "Tháng 7 2024 — Nay", name: "Vận hành Sự kiện Startup", role: "Vận hành · Hệ sinh thái Đổi mới sáng tạo",
                    desc: "Trực tiếp vận hành các sự kiện đổi mới sáng tạo cấp thành phố: Univ.Star 2024/2025 và tuần lễ WHISE 2024 — kết nối các nhà sáng lập startup, nhà đầu tư và các tổ chức hỗ trợ.",
                    tech: ["Quản lý Sự kiện", "Giao tiếp Stakeholder"]
                }
            ]
        },
        skills: {
            tag: "Năng lực Lõi", title: "Kỹ năng <span>Chuyên môn</span>", radar: "Biểu đồ Phân tích", certTag: "Chứng chỉ",
            groups: [
                { name: "Product Management", items: [{n: "Bản đồ Hành trình (Journey Mapping)", p: "95%"}, {n: "Thiết kế UX / HCI", p: "90%"}, {n: "Agile / Scrum (CPMAI)", p: "85%"}, {n: "Viết PRD & User Stories", p: "85%"}, {n: "A/B Testing", p: "82%"}] },
                { name: "Data & Tech", items: [{n: "Python & PyTorch", p: "80%"}, {n: "Phân tích Dữ liệu", p: "80%"}, {n: "Kiến trúc Hệ thống", p: "75%"}] }
            ],
            certs: [
                { i: "🏅", n: "Quản lý Dự án (Google Project Management)", org: "Coursera · Google" },
                { i: "📊", n: "Trí tuệ Doanh nghiệp (Google BI)", org: "Coursera · Google" },
                { i: "🔄", n: "Quản trị Agile", org: "Chứng nhận Chuyên nghiệp" },
                { i: "🗣️", n: "TOEIC · Năng lực Tiếng Anh", org: "Đang ôn thi chứng chỉ", dash: true, prog: "Đang tiến hành" }
            ]
        },
        education: {
            tag: "Nền tảng Học vấn", title: "Học vấn & <span>Thành tích</span>", uni: "Đại học Kinh tế TP.HCM (UEH)",
            major: "Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo",
            courseTag: "Các môn học Cốt lõi",
            courses: ["Tư duy Thiết kế (Design Thinking)", "Tương tác Người-Máy (HCI)", "Quản trị Đổi mới Sáng tạo", "Trí tuệ Doanh nghiệp (BI)", "Dự án AI"]
        },
        chat: {
            name: "Trợ lý AI của Minh", sub: "● Trực tuyến · Sẵn sàng giải đáp", reset: "↺ Khởi tạo lại",
            greeting: "Xin chào! Tôi là AI đại diện cho Nguyễn Hoàng Minh — Product Owner Intern với nền tảng vững chắc về UX Strategy và System Thinking.\n\nMinh đang tìm kiếm cơ hội để áp dụng kỹ năng thiết kế hành trình người dùng và tư duy quản lý sản phẩm vào các môi trường thực chiến. Bạn muốn biết thêm điều gì?",
            prompts: [
                { id: "exp", icon: "💼", label: "Kinh nghiệm" },
                { id: "proj", icon: "🚀", label: "Dự án" },
                { id: "echomind", icon: "🧠", label: "EchoMind AI" },
                { id: "skills", icon: "🛠️", label: "Kỹ năng" }
            ],
            ans_exp: "Minh có hơn 3 năm kinh nghiệm tại SIHUB (Trung tâm Hỗ trợ Khởi nghiệp & Đổi mới sáng tạo TP.HCM).\n\n◈ Vai trò hiện tại: Project Management Exec\nMinh thiết kế end-to-end digital journey map cho các startup công nghệ, xây dựng luồng kích hoạt và kiểm chứng tính năng qua A/B testing. Minh tiếp cận NPS không chỉ là con số mà là một hệ thống tín hiệu hành vi.\n\n◈ Trước đó: Thực tập sinh R&D\nDẫn dắt phân tích khoảng trống năng lực cho hơn 150 stakeholders chủ chốt và soạn thảo tài liệu chuẩn URD.",
            ans_proj: "Minh có 3 dự án nổi bật thể hiện khả năng kết hợp tư duy Product & Kỹ thuật:\n\n🧠 EchoMind AI (Dự án Trọng điểm)\nHệ thống Brain-to-text mà Minh làm Project Lead. Quản lý 8 Sprints qua Agile & CPMAI. Quyết định chuyển mô hình từ LSTM sang Transformer để giải quyết điểm nghẽn.\n\n📚 Hệ sinh thái E-Reader\nÁp dụng tiêu chuẩn HCI cho hành trình người dùng. Lọt Top 20 cuộc thi cấp Thành phố.\n\n🚀 Sự kiện Startup\nVận hành các sự kiện đổi mới sáng tạo lớn (Univ.Star, WHISE) kết nối founders và nhà đầu tư.",
            ans_echomind: "EchoMind AI là dự án tâm huyết của Minh (Tháng 9-12 2025). Với vai trò Project Lead, Minh không chỉ code mà quản lý cả tầm nhìn sản phẩm.\n\n◈ Vấn đề: Bệnh nhân hội chứng khóa trong không thể giao tiếp.\n◈ Giải pháp: Hệ thống dịch sóng não (EEG) phi xâm lấn.\n◈ Quyết định Sản phẩm: Khi mô hình LSTM ban đầu thất bại (Mode Collapse), Minh đã định hướng nhóm chuyển sang mô hình Transformer <span class='cite'></span>.\n◈ Kết quả: Đạt tốc độ 55-65 từ/phút với độ trễ <1s <span class='cite'>[cite: 1476]</span>. Tính toán mức ROI Kỹ thuật đạt 72% so với thiết bị truyền thống <span class='cite'>[cite: 1650]</span>.\n◈ Tập trung UX: Thiết kế 'Dashboard Chuyên gia' với Attention Maps nhằm minh bạch hóa AI cho bác sĩ <span class='cite'>[cite: 1453]</span>.",
            ans_skills: "Minh định vị mình ở giao điểm của 3 năng lực:\n\n◈ Product Craft (Thế mạnh Cốt lõi)\n→ Bản đồ Hành trình · Thiết kế UX/HCI\n→ Quản trị Agile/Scrum (Khung CPMAI, Ma trận RACI)\n→ Viết PRD, User Stories, A/B Testing\n\n◈ Data & Systems Thinking\n→ Python · Phân tích Dữ liệu\n→ Kiến thức nền tảng PyTorch/ML (chứng minh qua dự án EchoMind)\n\n◈ Kỹ năng Mềm\n→ Quản trị stakeholder đa phòng ban (150+ liên hệ)\n→ Soạn thảo tài liệu chiến lược báo cáo cấp Ban Giám đốc"
        }
    }
};

let currentLang = 'en'; // Default
let isTyping = false;
let chartInstance = null;

const chatMessages = document.getElementById('chat-messages');
const promptsGrid = document.getElementById('prompts-grid');

// === LANGUAGE SELECTOR ===
function selectLanguage(lang) {
    currentLang = lang;
    document.getElementById('lang-overlay').style.opacity = '0';
    document.getElementById('lang-overlay').style.visibility = 'hidden';
    document.getElementById('main-app').style.opacity = '1';
    
    renderUI();
    initChat();
    // Re-init chart if on skills view
    if(document.getElementById('view-skills').style.display !== 'none') {
        initSkillsChart();
    }
}

// === RENDER UI TEXT ===
function renderUI() {
    const t = i18n[currentLang];

    // Nav
    document.getElementById('nav-overview').textContent = t.nav.overview;
    document.getElementById('nav-exp').textContent = t.nav.exp;
    document.getElementById('nav-proj').textContent = t.nav.proj;
    document.getElementById('nav-skills').textContent = t.nav.skills;
    document.getElementById('nav-edu').textContent = t.nav.edu;

    // Welcome
    document.getElementById('w-status').textContent = t.welcome.status;
    document.getElementById('w-role').textContent = t.welcome.role;
    document.getElementById('w-summary').innerHTML = t.welcome.summary;
    document.getElementById('w-stat1').textContent = t.welcome.stat1;
    document.getElementById('w-stat2').textContent = t.welcome.stat2;
    document.getElementById('w-stat3').textContent = t.welcome.stat3;

    // Experience
    document.getElementById('e-tag').textContent = t.experience.tag;
    document.getElementById('e-title').innerHTML = t.experience.title;
    document.getElementById('e-timeline').innerHTML = t.experience.items.map((item, index) => `
        <div class="timeline-item ${index !== 0 ? 'past' : ''}">
            <div class="tl-period">${item.period}</div>
            <div class="tl-role">${item.role}</div>
            <div class="tl-company">${item.company}</div>
            <ul class="tl-bullets">
                ${item.bullets.map(b => `<li>${b}</li>`).join('')}
            </ul>
            <div class="tl-tags">
                ${item.tags.map(tag => `<span class="tl-tag">${tag}</span>`).join('')}
            </div>
        </div>
    `).join('');

    // Projects
    document.getElementById('p-tag').textContent = t.projects.tag;
    document.getElementById('p-title').innerHTML = t.projects.title;
    document.getElementById('p-grid').innerHTML = t.projects.items.map(p => `
        <div class="project-card ${p.id==='echomind'?'featured':''}" onclick="askAboutProject('${p.id}')">
            ${p.id==='echomind' ? `
                <div>
                    <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
                        <span class="project-badge ${p.badgeClass}">${p.badge}</span>
                        <span class="project-badge badge-active" style="background:rgba(82,209,138,0.1); border-color:transparent;">${p.date}</span>
                    </div>
                    <div class="project-name">${p.name}</div>
                    <div style="font-size:13px;color:var(--text2);margin-bottom:16px;font-style:italic;">${p.role}</div>
                    <p class="project-desc">${p.desc}</p>
                    <div class="project-metrics">
                        <div class="metric"><div class="metric-val">${p.m1}</div><div class="metric-lbl">${p.m1l}</div></div>
                        <div class="metric"><div class="metric-val">${p.m2}</div><div class="metric-lbl">${p.m2l}</div></div>
                        <div class="metric"><div class="metric-val">${p.m3}</div><div class="metric-lbl">${p.m3l}</div></div>
                    </div>
                    <div class="tech-stack">${p.tech.map(th => `<span class="tech-pill">${th}</span>`).join('')}</div>
                </div>
                <div style="width:200px;text-align:center;padding:24px;background:var(--ink3);border-radius:20px;border:1px solid var(--border2); align-self:center;">
                    <div style="font-size:48px;margin-bottom:16px;">🧠</div>
                    <div style="font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);line-height:1.8;">
                        EEG Signal<br>↓<br>Transformer V2<br>↓<br>Text Output
                    </div>
                </div>
            ` : `
                <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:12px;">
                    <span class="project-badge ${p.badgeClass}">${p.badge}</span>
                    <span style="font-family:'DM Mono',monospace;font-size:11px;color:var(--text2);">${p.date}</span>
                </div>
                <div class="project-name" style="font-size:24px;">${p.name}</div>
                <div style="font-size:13px;color:var(--text2);margin-bottom:16px;font-style:italic;">${p.role}</div>
                <p class="project-desc">${p.desc}</p>
                <div class="tech-stack">${p.tech.map(th => `<span class="tech-pill">${th}</span>`).join('')}</div>
            `}
        </div>
    `).join('');

    // Skills
    document.getElementById('s-tag').textContent = t.skills.tag;
    document.getElementById('s-title').innerHTML = t.skills.title;
    document.getElementById('s-radar-tag').textContent = t.skills.radar;
    document.getElementById('s-cert-tag').textContent = t.skills.certTag;
    
    document.getElementById('s-bars').innerHTML = t.skills.groups.map(g => `
        <div class="skill-group">
            <div class="skill-group-label">${g.name}</div>
            ${g.items.map(i => `
                <div class="skill-bar-item">
                    <div class="skill-bar-header"><span class="skill-bar-name">${i.n}</span><span class="skill-bar-pct">${i.p}</span></div>
                    <div class="skill-bar-track"><div class="skill-bar-fill" style="width:${i.p}"></div></div>
                </div>
            `).join('')}
        </div>
    `).join('');

    document.getElementById('s-certs').innerHTML = t.skills.certs.map(c => `
        <div class="cert-card" style="${c.dash ? 'border-style:dashed;border-color:rgba(240,192,96,0.3);' : ''}">
            <span style="font-size:24px; flex-shrink:0;">${c.i}</span>
            <div style="flex:1;">
                <div style="color:var(--text);font-size:14px;font-weight:500;">${c.n}</div>
                <div style="font-size:12px;color:var(--text2); margin-top:2px;">${c.org}</div>
            </div>
            ${c.prog ? `<span style="font-family:'DM Mono',monospace;font-size:11px;color:var(--gold);padding:4px 12px;background:rgba(240,192,96,0.1);border-radius:20px;">${c.prog}</span>` : ''}
        </div>
    `).join('');

    // Education
    document.getElementById('ed-tag').textContent = t.education.tag;
    document.getElementById('ed-title').innerHTML = t.education.title;
    document.getElementById('ed-uni').textContent = t.education.uni;
    document.getElementById('ed-major').textContent = t.education.major;
    document.getElementById('ed-courses').innerHTML = `
        <div class="skill-group-label" style="font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:16px;">${t.education.courseTag}</div>
        <div style="display:flex;flex-wrap:wrap;gap:10px;">
            ${t.education.courses.map(c => `<span style="font-size:13px;padding:8px 16px;background:var(--surface);border:1px solid var(--border2);border-radius:10px;color:var(--text2);">${c}</span>`).join('')}
        </div>
    `;

    // Chat labels
    document.getElementById('c-name').textContent = t.chat.name;
    document.getElementById('c-sub').textContent = t.chat.sub;
    document.getElementById('c-reset').textContent = t.chat.reset;
}

// === VIEW SWITCHING ===
function switchView(viewId, navEl) {
    document.querySelectorAll('.view-content').forEach(v => v.style.display = 'none');
    document.getElementById('view-' + viewId).style.display = '';
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    if (navEl) navEl.classList.add('active');
    else {
        const nav = document.querySelector(`[data-view="${viewId}"]`);
        if (nav) nav.classList.add('active');
    }
    if (viewId === 'skills') setTimeout(initSkillsChart, 100);
    if (viewId === 'skills') setTimeout(animateBars, 200);
}

function animateBars() {
    document.querySelectorAll('.skill-bar-fill').forEach(bar => bar.classList.add('animate'));
}

// === CHAT SYSTEM ===
function initChat() {
    chatMessages.innerHTML = '';
    renderPrompts();
    setTimeout(() => appendMessage('ai', i18n[currentLang].chat.greeting, true), 400);
}

function renderPrompts() {
    const pData = i18n[currentLang].chat.prompts;
    promptsGrid.innerHTML = pData.map(p =>
        `<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.icon} ${p.label}')" ${isTyping ? 'disabled' : ''}>
            <span style="font-size:16px;">${p.icon}</span>${p.label}
        </button>`
    ).join('');
}

function handlePrompt(id, label) {
    if (isTyping) return;
    promptsGrid.style.opacity = '0.4';
    appendMessage('user', label, false);
    
    // Switch view logic
    const viewMap = { exp: 'experience', proj: 'projects', echomind: 'projects', skills: 'skills' };
    setTimeout(() => switchView(viewMap[id] || 'welcome', null), 200);

    setTimeout(() => {
        appendMessage('ai', i18n[currentLang].chat['ans_'+id], true, () => {
            promptsGrid.style.opacity = '1';
            renderPrompts();
        });
    }, 500);
}

function askAboutProject(id) {
    if (isTyping) return;
    const label = currentLang === 'en' ? "Tell me more about this project." : "Cho tôi biết thêm về dự án này.";
    appendMessage('user', label, false);
    
    let ansKey = id === 'echomind' ? 'ans_echomind' : 'ans_proj';
    
    setTimeout(() => {
        appendMessage('ai', i18n[currentLang].chat[ansKey], true);
    }, 500);
}

function appendMessage(sender, text, useTypewriter = false, callback = null) {
    const row = document.createElement('div');
    row.className = `msg-row ${sender}`;

    const avatar = document.createElement('div');
    avatar.className = `msg-avatar-small ${sender}`;
    avatar.textContent = sender === 'ai' ? '🤖' : '👤';

    const bubble = document.createElement('div');
    bubble.className = `msg-bubble ${sender}`;

    row.appendChild(avatar);
    row.appendChild(bubble);
    chatMessages.appendChild(row);

    if (sender === 'ai' && useTypewriter) {
        typeWriter(text, bubble, 12, callback); // Faster typing
    } else {
        bubble.innerHTML = text.replace(/\n/g, '<br>');
        scrollBottom();
        if (callback) callback();
    }
}

function typeWriter(text, el, speed, callback) {
    isTyping = true;
    renderPrompts(); // disable buttons
    
    // Parse HTML properly during typewriter effect
    let tempDiv = document.createElement('div');
    tempDiv.innerHTML = text.replace(/\n/g, '<br>');
    let nodes = Array.from(tempDiv.childNodes);
    
    el.innerHTML = '<span class="tc"></span><span class="cursor-blink"></span>';
    const tc = el.querySelector('.tc');
    
    let nodeIndex = 0;
    let charIndex = 0;

    function type() {
        if (nodeIndex < nodes.length) {
            let node = nodes[nodeIndex];
            if (node.nodeType === 3) { // Text node
                if (charIndex < node.textContent.length) {
                    tc.innerHTML += node.textContent.charAt(charIndex);
                    charIndex++;
                    scrollBottom();
                    setTimeout(type, speed);
                } else {
                    nodeIndex++;
                    charIndex = 0;
                    type();
                }
            } else { // Element node (like <br>, <strong>, <span>)
                tc.appendChild(node.cloneNode(true));
                nodeIndex++;
                scrollBottom();
                setTimeout(type, speed);
            }
        } else {
            isTyping = false;
            const cur = el.querySelector('.cursor-blink');
            if (cur) cur.remove();
            renderPrompts();
            if (callback) callback();
        }
    }
    type();
}

function scrollBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function resetChat() {
    if (isTyping) return;
    initChat();
}

// === SKILLS CHART ===
function initSkillsChart() {
    const ctx = document.getElementById('skillsChart');
    if (!ctx) return;
    if (chartInstance) { chartInstance.destroy(); chartInstance = null; }

    const labels = currentLang === 'en' 
        ? ['UX/HCI', 'Agile/Scrum', 'Journey Map', 'Data Analysis', 'Python', 'PyTorch/ML', 'A/B Testing']
        : ['Thiết kế UX/HCI', 'Agile/Scrum', 'Hành trình KH', 'Phân tích Dữ liệu', 'Python', 'PyTorch/ML', 'A/B Testing'];

    chartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                data: [90, 85, 95, 80, 80, 72, 82],
                fill: true,
                backgroundColor: 'rgba(124,106,247,0.15)',
                borderColor: '#7c6af7',
                pointBackgroundColor: '#a594fc',
                pointBorderColor: '#1e1e2e',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#7c6af7',
                borderWidth: 2,
                pointRadius: 4,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    min: 0, max: 100,
                    ticks: { display: false, stepSize: 20 },
                    angleLines: { color: 'rgba(255,255,255,0.08)' },
                    grid: { color: 'rgba(255,255,255,0.08)' },
                    pointLabels: {
                        font: { size: 12, family: "'DM Sans', sans-serif", weight: '500' },
                        color: '#9898b0'
                    }
                }
            },
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: '#252538',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderWidth: 1,
                    padding: 12,
                    titleFont: { family: "'DM Mono', monospace", size: 12 },
                    bodyFont: { family: "'DM Sans', sans-serif", size: 13 },
                    callbacks: {
                        label: ctx => {
                            const v = ctx.raw;
                            if(currentLang === 'en'){
                                return v >= 90 ? ' Expert' : v >= 80 ? ' Advanced' : v >= 70 ? ' Proficient' : ' Familiar';
                            } else {
                                return v >= 90 ? ' Chuyên gia' : v >= 80 ? ' Cao cấp' : v >= 70 ? ' Thành thạo' : ' Có kiến thức';
                            }
                        }
                    }
                }
            }
        }
    });
}
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
