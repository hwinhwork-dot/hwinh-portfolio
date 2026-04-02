import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="hwinh | Product Owner", page_icon="◈", initial_sidebar_state="collapsed")

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
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hwinh | Product Owner</title>
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
            --text3: #6060780;
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

        /* === LAYOUT === */
        .app {
            display: flex;
            height: 100vh;
            width: 100%;
        }

        /* === LEFT SIDEBAR NAV === */
        .sidenav {
            width: 72px;
            height: 100%;
            background: var(--ink2);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 24px 0;
            gap: 8px;
            flex-shrink: 0;
            z-index: 10;
        }

        .nav-logo {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 14px;
            color: var(--accent2);
            letter-spacing: -0.5px;
            margin-bottom: 16px;
            writing-mode: horizontal-tb;
        }

        .nav-item {
            width: 44px;
            height: 44px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            color: var(--text2);
            font-size: 18px;
            border: 1px solid transparent;
            position: relative;
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
            left: 56px;
            background: var(--surface2);
            color: var(--text);
            font-size: 11px;
            font-family: 'DM Mono', monospace;
            padding: 4px 10px;
            border-radius: 6px;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.15s;
            border: 1px solid var(--border2);
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

        .visual-panel::-webkit-scrollbar { width: 4px; }
        .visual-panel::-webkit-scrollbar-track { background: transparent; }
        .visual-panel::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

        /* === CHAT PANEL === */
        .chat-panel {
            width: 400px;
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

        /* WELCOME VIEW */
        .view-welcome {
            min-height: 100%;
            display: flex;
            flex-direction: column;
            padding: 60px 56px;
        }

        .welcome-eyebrow {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 32px;
        }

        .status-dot {
            width: 8px; height: 8px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--green);
            animation: pulse-green 2s infinite;
        }

        @keyframes pulse-green {
            0%, 100% { box-shadow: 0 0 6px var(--green); }
            50% { box-shadow: 0 0 18px var(--green); }
        }

        .status-text {
            font-family: 'DM Mono', monospace;
            font-size: 11px;
            color: var(--green);
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .welcome-name {
            font-family: 'Syne', sans-serif;
            font-size: clamp(40px, 5vw, 72px);
            font-weight: 800;
            line-height: 0.95;
            letter-spacing: -2px;
            color: var(--text);
            margin-bottom: 12px;
        }

        .welcome-name .accent-word {
            color: var(--accent2);
            display: block;
        }

        .welcome-role {
            font-size: 16px;
            color: var(--text2);
            font-weight: 300;
            margin-bottom: 40px;
            font-style: italic;
        }

        .welcome-summary {
            font-size: 15px;
            line-height: 1.8;
            color: var(--text2);
            max-width: 520px;
            margin-bottom: 48px;
            border-left: 2px solid var(--accent);
            padding-left: 20px;
        }

        .contact-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 56px;
        }

        .contact-chip {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: var(--surface);
            border: 1px solid var(--border2);
            border-radius: 8px;
            font-size: 12px;
            font-family: 'DM Mono', monospace;
            color: var(--text2);
            transition: all 0.2s;
        }

        .contact-chip:hover {
            border-color: var(--accent);
            color: var(--text);
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            max-width: 560px;
            margin-bottom: 56px;
        }

        .stat-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--accent), var(--teal));
        }

        .stat-number {
            font-family: 'Syne', sans-serif;
            font-size: 32px;
            font-weight: 800;
            color: var(--text);
            line-height: 1;
        }

        .stat-label {
            font-size: 11px;
            color: var(--text2);
            margin-top: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .section-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            color: var(--accent2);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 24px;
        }

        .section-tag::before {
            content: '◈';
            font-size: 12px;
        }

        /* EXPERIENCE VIEW */
        .view-content {
            padding: 56px;
            min-height: 100%;
        }

        .view-title {
            font-family: 'Syne', sans-serif;
            font-size: 42px;
            font-weight: 800;
            letter-spacing: -1.5px;
            color: var(--text);
            margin-bottom: 48px;
            line-height: 1;
        }

        .view-title span { color: var(--accent2); }

        .timeline {
            position: relative;
            padding-left: 28px;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 0;
            top: 8px;
            bottom: 8px;
            width: 1px;
            background: linear-gradient(to bottom, var(--accent), transparent);
        }

        .timeline-item {
            position: relative;
            margin-bottom: 40px;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -32px;
            top: 8px;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent2);
            box-shadow: 0 0 12px rgba(165,148,252,0.5);
        }

        .timeline-item.past::before { background: var(--text2); box-shadow: none; }

        .tl-period {
            font-family: 'DM Mono', monospace;
            font-size: 11px;
            color: var(--accent2);
            letter-spacing: 1px;
            margin-bottom: 8px;
        }

        .tl-role {
            font-family: 'Syne', sans-serif;
            font-size: 20px;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 4px;
        }

        .tl-company {
            font-size: 13px;
            color: var(--text2);
            font-style: italic;
            margin-bottom: 16px;
        }

        .tl-bullets {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .tl-bullets li {
            font-size: 14px;
            color: var(--text2);
            line-height: 1.6;
            padding-left: 16px;
            position: relative;
        }

        .tl-bullets li::before {
            content: '→';
            position: absolute;
            left: 0;
            color: var(--accent);
            font-size: 12px;
        }

        .tl-bullets li strong {
            color: var(--text);
            font-weight: 500;
        }

        .tl-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 14px;
        }

        .tl-tag {
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            padding: 3px 10px;
            border-radius: 4px;
            background: rgba(124,106,247,0.1);
            border: 1px solid rgba(124,106,247,0.25);
            color: var(--accent3);
            letter-spacing: 0.5px;
        }

        /* PROJECTS VIEW */
        .projects-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .project-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 28px;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }

        .project-card::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 20px;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .project-card.featured::after {
            background: linear-gradient(135deg, rgba(124,106,247,0.08) 0%, transparent 60%);
        }

        .project-card:hover {
            border-color: var(--accent);
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        .project-card:hover::after { opacity: 1; }

        .project-card.featured {
            grid-column: 1 / -1;
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 24px;
            align-items: start;
        }

        .project-badge {
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: 400;
            letter-spacing: 0.5px;
        }

        .badge-featured { background: rgba(240,192,96,0.15); color: var(--gold); border: 1px solid rgba(240,192,96,0.3); }
        .badge-active { background: rgba(82,209,138,0.15); color: var(--green); border: 1px solid rgba(82,209,138,0.3); }
        .badge-top20 { background: rgba(255,123,107,0.15); color: var(--coral); border: 1px solid rgba(255,123,107,0.3); }

        .project-name {
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 700;
            color: var(--text);
            margin: 10px 0 6px;
            letter-spacing: -0.5px;
        }

        .project-period {
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            color: var(--text2);
            margin-bottom: 12px;
            letter-spacing: 0.5px;
        }

        .project-desc {
            font-size: 13px;
            color: var(--text2);
            line-height: 1.7;
            margin-bottom: 16px;
        }

        .project-metrics {
            display: flex;
            gap: 20px;
            margin: 14px 0;
        }

        .metric {
            text-align: center;
        }

        .metric-val {
            font-family: 'Syne', sans-serif;
            font-size: 22px;
            font-weight: 700;
            color: var(--accent2);
        }

        .metric-lbl {
            font-size: 10px;
            color: var(--text2);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 2px;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .tech-pill {
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            padding: 3px 10px;
            border-radius: 4px;
            background: var(--ink3);
            border: 1px solid var(--border2);
            color: var(--text2);
        }

        /* SKILLS VIEW */
        .skills-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
            align-items: start;
        }

        .skill-group { margin-bottom: 28px; }

        .skill-group-label {
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            color: var(--accent2);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 14px;
        }

        .skill-bar-item {
            margin-bottom: 12px;
        }

        .skill-bar-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 6px;
        }

        .skill-bar-name {
            font-size: 13px;
            color: var(--text);
        }

        .skill-bar-pct {
            font-family: 'DM Mono', monospace;
            font-size: 11px;
            color: var(--text2);
        }

        .skill-bar-track {
            height: 4px;
            background: var(--surface2);
            border-radius: 2px;
            overflow: hidden;
        }

        .skill-bar-fill {
            height: 100%;
            border-radius: 2px;
            background: linear-gradient(90deg, var(--accent), var(--teal));
            transform-origin: left;
            transform: scaleX(0);
            transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .skill-bar-fill.animate { transform: scaleX(1); }

        .cert-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 18px;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 13px;
            color: var(--text2);
        }

        .cert-icon {
            font-size: 18px;
            flex-shrink: 0;
        }

        /* EDUCATION VIEW */
        .edu-hero {
            background: linear-gradient(135deg, var(--surface) 0%, var(--surface2) 100%);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 36px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }

        .edu-hero::before {
            content: 'UEH';
            position: absolute;
            right: -20px;
            bottom: -30px;
            font-family: 'Syne', sans-serif;
            font-size: 120px;
            font-weight: 800;
            color: rgba(255,255,255,0.03);
            line-height: 1;
            pointer-events: none;
            user-select: none;
        }

        .gpa-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(240,192,96,0.1);
            border: 1px solid rgba(240,192,96,0.3);
            border-radius: 12px;
            padding: 12px 20px;
        }

        .gpa-value {
            font-family: 'Syne', sans-serif;
            font-size: 28px;
            font-weight: 800;
            color: var(--gold);
        }

        /* CHAT PANEL */
        .chat-header {
            padding: 20px 24px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }

        .chat-avatar {
            width: 38px; height: 38px;
            border-radius: 12px;
            background: linear-gradient(135deg, var(--accent), var(--teal));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            flex-shrink: 0;
        }

        .chat-name {
            font-family: 'Syne', sans-serif;
            font-size: 14px;
            font-weight: 700;
            color: var(--text);
        }

        .chat-subtitle {
            font-size: 11px;
            color: var(--green);
            font-family: 'DM Mono', monospace;
        }

        .reset-btn {
            margin-left: auto;
            background: none;
            border: 1px solid var(--border2);
            color: var(--text2);
            font-size: 11px;
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'DM Mono', monospace;
            transition: all 0.2s;
        }

        .reset-btn:hover {
            border-color: var(--accent);
            color: var(--accent2);
        }

        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .chat-messages::-webkit-scrollbar { width: 3px; }
        .chat-messages::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }

        .msg-row {
            display: flex;
            gap: 10px;
            align-items: flex-end;
            animation: msg-in 0.3s ease-out;
        }

        @keyframes msg-in {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .msg-row.user { flex-direction: row-reverse; }

        .msg-avatar-small {
            width: 28px; height: 28px;
            border-radius: 8px;
            background: linear-gradient(135deg, var(--accent), var(--teal));
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            flex-shrink: 0;
        }

        .msg-bubble {
            max-width: 82%;
            padding: 12px 16px;
            border-radius: 16px;
            font-size: 13px;
            line-height: 1.65;
        }

        .msg-bubble.ai {
            background: var(--surface);
            border: 1px solid var(--border2);
            color: var(--text);
            border-bottom-left-radius: 4px;
        }

        .msg-bubble.user {
            background: var(--accent);
            color: white;
            border-bottom-right-radius: 4px;
        }

        .cursor-blink {
            display: inline-block;
            width: 7px; height: 14px;
            background: var(--accent2);
            margin-left: 2px;
            animation: cursor-blink 1s step-end infinite;
            vertical-align: middle;
            border-radius: 1px;
        }

        @keyframes cursor-blink { 0%,100%{opacity:1} 50%{opacity:0} }

        .chat-footer {
            padding: 16px;
            border-top: 1px solid var(--border);
            flex-shrink: 0;
        }

        .prompts-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }

        .prompt-btn {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 10px 12px;
            font-size: 12px;
            color: var(--text2);
            cursor: pointer;
            transition: all 0.2s;
            text-align: left;
            font-family: 'DM Sans', sans-serif;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .prompt-btn:hover {
            border-color: var(--accent);
            color: var(--text);
            background: var(--surface2);
        }

        .prompt-btn:disabled {
            opacity: 0.4;
            cursor: not-allowed;
        }

        .prompt-icon { font-size: 14px; flex-shrink: 0; }

        /* ANIMATIONS */
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(24px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .fade-up { animation: fadeUp 0.5s ease-out forwards; opacity: 0; }
        .delay-1 { animation-delay: 0.1s; }
        .delay-2 { animation-delay: 0.2s; }
        .delay-3 { animation-delay: 0.3s; }
        .delay-4 { animation-delay: 0.4s; }
        .delay-5 { animation-delay: 0.5s; }

        /* divider */
        .subtle-div {
            height: 1px;
            background: var(--border);
            margin: 32px 0;
        }

        /* highlight accent text */
        .hl { color: var(--accent2); }
        .hl-gold { color: var(--gold); }
        .hl-green { color: var(--green); }
        .hl-coral { color: var(--coral); }

        /* responsive */
        @media (max-width: 900px) {
            .chat-panel { width: 340px; }
            .projects-grid { grid-template-columns: 1fr; }
            .project-card.featured { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
<div class="noise"></div>

<div class="app">
    <!-- SIDEBAR NAV -->
    <nav class="sidenav">
        <div class="nav-logo">hw</div>

        <div class="nav-item active" data-view="welcome" onclick="switchView('welcome', this)" title="">
            ◈
            <span class="nav-tooltip">Overview</span>
        </div>
        <div class="nav-item" data-view="experience" onclick="switchView('experience', this)">
            ⟳
            <span class="nav-tooltip">Experience</span>
        </div>
        <div class="nav-item" data-view="projects" onclick="switchView('projects', this)">
            ⬡
            <span class="nav-tooltip">Projects</span>
        </div>
        <div class="nav-item" data-view="skills" onclick="switchView('skills', this)">
            ◎
            <span class="nav-tooltip">Skills</span>
        </div>
        <div class="nav-item" data-view="education" onclick="switchView('education', this)">
            ▣
            <span class="nav-tooltip">Education</span>
        </div>
    </nav>

    <!-- VISUAL PANEL -->
    <main class="visual-panel" id="visual-panel">

        <!-- WELCOME -->
        <div id="view-welcome" class="view-welcome">
            <div class="welcome-eyebrow fade-up">
                <div class="status-dot"></div>
                <span class="status-text">Available for opportunities · HCMC, Vietnam</span>
            </div>

            <h1 class="welcome-name fade-up delay-1">
                Nguyễn
                <span class="accent-word">Hoàng Minh</span>
            </h1>
            <p class="welcome-role fade-up delay-2">Product Owner Intern · UX Strategist · AI Builder</p>

            <p class="welcome-summary fade-up delay-3">
                Chuyên gia trẻ về Quản lý Công nghệ & Đổi mới Sáng tạo — xây dựng tại giao điểm của <strong style="color:var(--text)">UX Design</strong>, <strong style="color:var(--text)">System Thinking</strong> và <strong style="color:var(--text)">AI Engineering</strong>. Tôi chuyển hoá dữ liệu người dùng phức tạp thành trải nghiệm sản phẩm mượt mà và đo lường được.
            </p>

            <div class="contact-row fade-up delay-4">
                <div class="contact-chip">✉ hwinh.work@gmail.com</div>
                <div class="contact-chip">📞 +84 765 828 191</div>
                <div class="contact-chip">📍 Hồ Chí Minh</div>
                <div class="contact-chip">🎓 UEH · GPA 3.53</div>
            </div>

            <div class="stat-grid fade-up delay-5">
                <div class="stat-card">
                    <div class="stat-number">3+</div>
                    <div class="stat-label">Năm kinh nghiệm</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">150+</div>
                    <div class="stat-label">Stakeholders quản lý</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">Top 20</div>
                    <div class="stat-label">Finalist cấp TP</div>
                </div>
            </div>

            <div class="subtle-div fade-up"></div>

            <div class="section-tag fade-up">Hãy khám phá hồ sơ</div>
            <p style="font-size:13px;color:var(--text2);line-height:1.7;max-width:480px;" class="fade-up">
                Sử dụng thanh điều hướng bên trái hoặc trò chuyện với AI Assistant bên phải để khám phá kinh nghiệm, dự án và kỹ năng của tôi.
            </p>
        </div>

        <!-- EXPERIENCE -->
        <div id="view-experience" class="view-content" style="display:none">
            <div class="section-tag">Work History</div>
            <h2 class="view-title">Kinh nghiệm <span>làm việc</span></h2>

            <div class="timeline">

                <div class="timeline-item">
                    <div class="tl-period">JAN 2025 — OCT 2025 · HIỆN TẠI</div>
                    <div class="tl-role">Project Management Executive</div>
                    <div class="tl-company">Startup & Innovation Hub of HCMC (SIHUB) · Under Dept. of Science & Technology</div>
                    <ul class="tl-bullets">
                        <li><strong>Customer Journey Mapping & MVP Delivery:</strong> Thiết kế end-to-end digital journey map cho tech startups, xây dựng onboarding & activation flow. Định nghĩa core user problems và dịch sang user stories rõ ràng để dẫn dắt phát triển MVP nhanh.</li>
                        <li><strong>Pain Point Resolution & Advanced Testing:</strong> Liên tục theo dõi các touchpoint để phát hiện operational bottlenecks. Áp dụng A/B testing và Interleaving experiments để validate feature iterations trước full-scale rollout.</li>
                        <li><strong>Omnichannel Data & Stakeholder Management:</strong> Làm đầu mối chính với startup founders, phân tích behavioral data để cải thiện satisfaction metrics (NPS focus) và báo cáo insights tới Ban Giám đốc.</li>
                    </ul>
                    <div class="tl-tags">
                        <span class="tl-tag">Customer Journey</span>
                        <span class="tl-tag">A/B Testing</span>
                        <span class="tl-tag">MVP Delivery</span>
                        <span class="tl-tag">NPS Metrics</span>
                        <span class="tl-tag">Stakeholder Mgmt</span>
                    </div>
                </div>

                <div class="timeline-item past">
                    <div class="tl-period">JUL 2024 — DEC 2024</div>
                    <div class="tl-role">Research & Development Intern</div>
                    <div class="tl-company">SIHUB · Executed data-driven project management for city-level framework</div>
                    <ul class="tl-bullets">
                        <li><strong>Data Analysis & Requirements Gathering:</strong> Dẫn dắt end-to-end data lifecycle cho competency gap analysis liên quan đến 150+ key stakeholders trong báo cáo nghiên cứu khoa học cấp thành phố.</li>
                        <li><strong>Structured Documentation:</strong> Soạn thảo strategic reports và structured documentation (chuẩn URD), dịch qualitative user problems thành actionable system requirements.</li>
                    </ul>
                    <div class="tl-tags">
                        <span class="tl-tag">Data Analysis</span>
                        <span class="tl-tag">URD Standards</span>
                        <span class="tl-tag">Requirements Gathering</span>
                        <span class="tl-tag">150+ Stakeholders</span>
                    </div>
                </div>

            </div>
        </div>

        <!-- PROJECTS -->
        <div id="view-projects" class="view-content" style="display:none">
            <div class="section-tag">Product Experience</div>
            <h2 class="view-title">Dự án <span>nổi bật</span></h2>

            <div class="projects-grid">

                <!-- Featured: EchoMind -->
                <div class="project-card featured" onclick="askAbout('EchoMind AI')">
                    <div>
                        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                            <span class="project-badge badge-featured">★ Flagship Project</span>
                            <span class="project-badge badge-active" style="background:rgba(82,209,138,0.1);">Sep–Dec 2025</span>
                        </div>
                        <div class="project-name">EchoMind AI</div>
                        <div style="font-size:12px;color:var(--text2);margin-bottom:14px;font-style:italic;">AI-Based Brain-to-Text System · Project Lead</div>
                        <p class="project-desc">
                            Hệ thống AI dựa trên PyTorch chuyển đổi tín hiệu não thành văn bản theo thời gian thực. Tối ưu kiến trúc từ baseline lên Transformer-based model, giải quyết bottleneck xử lý tín hiệu phức tạp. Quản lý full product lifecycle bằng Agile framework và RACI matrix — đảm bảo 100% milestone completion.
                        </p>
                        <div class="project-metrics">
                            <div class="metric">
                                <div class="metric-val">55–65</div>
                                <div class="metric-lbl">WPM Output</div>
                            </div>
                            <div class="metric">
                                <div class="metric-val">&lt;1s</div>
                                <div class="metric-lbl">Latency</div>
                            </div>
                            <div class="metric">
                                <div class="metric-val">100%</div>
                                <div class="metric-lbl">Milestone</div>
                            </div>
                        </div>
                        <div class="tech-stack">
                            <span class="tech-pill">Python</span>
                            <span class="tech-pill">PyTorch</span>
                            <span class="tech-pill">Transformer</span>
                            <span class="tech-pill">Agile/Scrum</span>
                            <span class="tech-pill">RACI Matrix</span>
                            <span class="tech-pill">System Optimization</span>
                        </div>
                    </div>
                    <div style="width:180px;text-align:center;padding:20px;background:var(--ink3);border-radius:16px;border:1px solid var(--border2);">
                        <div style="font-size:40px;margin-bottom:12px;">🧠</div>
                        <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);line-height:1.8;">
                            Signal decoding<br>
                            ↓<br>
                            Transformer<br>
                            ↓<br>
                            Text output
                        </div>
                    </div>
                </div>

                <!-- E-Reader -->
                <div class="project-card" onclick="askAbout('E-Reader Ecosystem')">
                    <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:8px;">
                        <span class="project-badge badge-top20">🏆 Top 20 Finalist</span>
                        <span style="font-family:'DM Mono',monospace;font-size:10px;color:var(--text2);">Mar–Jun 2025</span>
                    </div>
                    <div class="project-name">E-Reader Ecosystem</div>
                    <div style="font-size:12px;color:var(--text2);margin-bottom:12px;font-style:italic;">Product Lead · HCMC People's Committee</div>
                    <p class="project-desc">
                        Thiết kế end-to-end user journey từ device provisioning đến content updates, ứng dụng chuẩn HCI để giảm cognitive load tối đa. Phân tách student pain points thành structured feature sets với clear user stories và logical flows.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-pill">HCI Principles</span>
                        <span class="tech-pill">UX Design</span>
                        <span class="tech-pill">Journey Mapping</span>
                        <span class="tech-pill">Feature Decomposition</span>
                    </div>
                </div>

                <!-- Startup Events -->
                <div class="project-card" onclick="askAbout('Startup Events')">
                    <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:8px;">
                        <span class="project-badge badge-active">● Ongoing</span>
                        <span style="font-family:'DM Mono',monospace;font-size:10px;color:var(--text2);">Jul 2024 — Now</span>
                    </div>
                    <div class="project-name">Startup Events Ops</div>
                    <div style="font-size:12px;color:var(--text2);margin-bottom:12px;font-style:italic;">Operations · Innovation Ecosystem</div>
                    <p class="project-desc">
                        Trực tiếp vận hành các sự kiện đổi mới sáng tạo cấp thành phố: Univ.Star 2024/2025 và tuần lễ WHISE 2024 — kết nối startup founders, investors và ecosystem builders.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-pill">Event Management</span>
                        <span class="tech-pill">Startup Ecosystem</span>
                        <span class="tech-pill">Cross-team Coordination</span>
                    </div>
                </div>

            </div>
        </div>

        <!-- SKILLS -->
        <div id="view-skills" class="view-content" style="display:none">
            <div class="section-tag">Competencies</div>
            <h2 class="view-title">Kỹ năng <span>chuyên môn</span></h2>

            <div class="skills-layout">
                <div>
                    <div class="skill-group">
                        <div class="skill-group-label">Product Management</div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">Journey Mapping</span><span class="skill-bar-pct">95%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:95%"></div></div>
                        </div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">UX / HCI Design</span><span class="skill-bar-pct">90%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:90%"></div></div>
                        </div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">Agile / Scrum</span><span class="skill-bar-pct">85%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:85%"></div></div>
                        </div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">PRD & User Stories</span><span class="skill-bar-pct">85%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:85%"></div></div>
                        </div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">A/B Testing</span><span class="skill-bar-pct">82%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:82%"></div></div>
                        </div>
                    </div>

                    <div class="skill-group">
                        <div class="skill-group-label">Data & Tech</div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">Python</span><span class="skill-bar-pct">80%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:80%"></div></div>
                        </div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">Data Analysis</span><span class="skill-bar-pct">80%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:80%"></div></div>
                        </div>
                        <div class="skill-bar-item">
                            <div class="skill-bar-header"><span class="skill-bar-name">PyTorch / ML</span><span class="skill-bar-pct">72%</span></div>
                            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:72%"></div></div>
                        </div>
                    </div>
                </div>

                <div>
                    <div class="skill-group-label" style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;">Radar Overview</div>
                    <div style="width:100%;height:280px;position:relative;margin-bottom:28px;">
                        <canvas id="skillsChart"></canvas>
                    </div>

                    <div class="skill-group-label" style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;">Certifications</div>
                    <div class="cert-card"><span class="cert-icon">🏅</span> Google Project Management</div>
                    <div class="cert-card"><span class="cert-icon">📊</span> Google Business Intelligence</div>
                    <div class="cert-card"><span class="cert-icon">🔄</span> Agile Management Certification</div>
                    <div class="cert-card" style="border-style:dashed;"><span class="cert-icon">⚡</span> AI Thực Chiến · Vingroup <span style="font-size:10px;color:var(--accent2);margin-left:auto;font-family:'DM Mono',monospace;">In Progress</span></div>
                </div>
            </div>
        </div>

        <!-- EDUCATION -->
        <div id="view-education" class="view-content" style="display:none">
            <div class="section-tag">Academic Background</div>
            <h2 class="view-title">Học vấn & <span>Thành tích</span></h2>

            <div class="edu-hero">
                <div style="font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);letter-spacing:1px;margin-bottom:16px;">AUG 2022 — AUG 2026</div>
                <h3 style="font-family:'Syne',sans-serif;font-size:24px;font-weight:800;color:var(--text);margin-bottom:4px;">Đại học Kinh tế TP.HCM</h3>
                <p style="color:var(--text2);font-size:14px;margin-bottom:20px;">Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo</p>
                <div class="gpa-badge">
                    <span style="font-size:24px;">🏆</span>
                    <div>
                        <div style="font-size:11px;color:var(--text2);margin-bottom:2px;">Grade Point Average</div>
                        <div class="gpa-value">3.53 / 4.0</div>
                    </div>
                </div>
            </div>

            <div style="margin-bottom:28px;">
                <div class="skill-group-label" style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;">Relevant Coursework</div>
                <div style="display:flex;flex-wrap:wrap;gap:8px;">
                    <span style="font-size:12px;padding:6px 14px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;color:var(--text2);">Design Thinking</span>
                    <span style="font-size:12px;padding:6px 14px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;color:var(--text2);">Human-Computer Interaction (HCI)</span>
                    <span style="font-size:12px;padding:6px 14px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;color:var(--text2);">Innovation Management</span>
                    <span style="font-size:12px;padding:6px 14px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;color:var(--text2);">Business Intelligence</span>
                    <span style="font-size:12px;padding:6px 14px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;color:var(--text2);">Digital Business Transformation</span>
                    <span style="font-size:12px;padding:6px 14px;background:var(--surface);border:1px solid var(--border2);border-radius:8px;color:var(--text2);">Project AI</span>
                </div>
            </div>

            <div>
                <div class="skill-group-label" style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;">Certifications & In Progress</div>
                <div class="cert-card"><span class="cert-icon">🏅</span><div><div style="color:var(--text);font-size:13px;">Google Project Management</div><div style="font-size:11px;color:var(--text2);">Coursera · Google</div></div></div>
                <div class="cert-card"><span class="cert-icon">📊</span><div><div style="color:var(--text);font-size:13px;">Google Business Intelligence</div><div style="font-size:11px;color:var(--text2);">Coursera · Google</div></div></div>
                <div class="cert-card"><span class="cert-icon">🔄</span><div><div style="color:var(--text);font-size:13px;">Agile Management</div><div style="font-size:11px;color:var(--text2);">Professional Certification</div></div></div>
                <div class="cert-card" style="border-style:dashed;border-color:rgba(124,106,247,0.3);">
                    <span class="cert-icon">⚡</span>
                    <div style="flex:1;">
                        <div style="color:var(--text);font-size:13px;">AI Thực Chiến · Vingroup</div>
                        <div style="font-size:11px;color:var(--text2);">VinBigData Institute</div>
                    </div>
                    <span style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);padding:3px 10px;background:rgba(124,106,247,0.1);border-radius:20px;">In Progress</span>
                </div>
                <div class="cert-card" style="border-style:dashed;border-color:rgba(240,192,96,0.3);">
                    <span class="cert-icon">🗣️</span>
                    <div style="flex:1;">
                        <div style="color:var(--text);font-size:13px;">TOEIC · English Proficiency</div>
                        <div style="font-size:11px;color:var(--text2);">Preparing for certification</div>
                    </div>
                    <span style="font-family:'DM Mono',monospace;font-size:10px;color:var(--gold);padding:3px 10px;background:rgba(240,192,96,0.1);border-radius:20px;">In Progress</span>
                </div>
            </div>
        </div>

    </main>

    <!-- CHAT PANEL -->
    <aside class="chat-panel">
        <div class="chat-header">
            <div class="chat-avatar">🤖</div>
            <div>
                <div class="chat-name">Minh's AI Assistant</div>
                <div class="chat-subtitle">● Online · Powered by portfolio data</div>
            </div>
            <button class="reset-btn" onclick="resetChat()">↺ Reset</button>
        </div>

        <div class="chat-messages" id="chat-messages"></div>

        <div class="chat-footer">
            <div class="prompts-grid" id="prompts-grid"></div>
        </div>
    </aside>
</div>

<script>
const cvData = {
    greeting: `Xin chào! Tôi là AI đại diện cho Nguyễn Hoàng Minh — Product Owner Intern với nền tảng vững chắc về UX Strategy và AI Engineering.\n\nMinh đang tìm kiếm cơ hội để áp dụng kỹ năng thiết kế hành trình người dùng và tư duy sản phẩm hệ thống vào các môi trường sản phẩm thực chiến. Bạn muốn biết thêm điều gì?`,

    experience: `Minh có hơn 3 năm kinh nghiệm tại SIHUB — trung tâm khởi nghiệp trực thuộc Sở Khoa học & Công nghệ TP.HCM.\n\n◈ Vai trò gần nhất (Jan–Oct 2025): Project Management Executive\nMinh thiết kế end-to-end digital journey map cho hàng chục tech startups, xây dựng activation flows và validate features qua A/B testing. Điểm đặc biệt: Minh tiếp cận NPS không chỉ như một con số mà như một hệ thống signals hành vi người dùng cần phân tích liên tục.\n\n◈ Trước đó (Jul–Dec 2024): R&D Intern\nDẫn dắt competency gap analysis cho 150+ key stakeholders trong dự án cấp thành phố — đây là nơi Minh rèn giũa khả năng xử lý dữ liệu chất lượng lẫn số lượng và tài liệu hóa chuẩn URD.`,

    projects: `Minh có 3 dự án nổi bật thể hiện khả năng kết hợp Technical & Product thinking:\n\n🧠 EchoMind AI (Flagship)\nBrain-to-text system dùng PyTorch Transformer — đạt 55–65 WPM với latency <1s. Minh quản lý toàn bộ lifecycle bằng Agile + RACI, đảm bảo 100% milestone. Đây là bằng chứng Minh không chỉ nghĩ về UX mà còn thực sự build và optimize hệ thống AI.\n\n📚 E-Reader Ecosystem (Top 20 TP)\nÁp dụng HCI principles thiết kế user journey từ device provisioning đến content updates — lọt Top 20 cuộc thi cấp Thành phố do UBND TP.HCM tổ chức.\n\n🚀 Startup Events Operations\nVận hành các sự kiện đổi mới sáng tạo lớn: Univ.Star 2024/2025 và WHISE 2024 — kết nối hệ sinh thái startup.`,

    skills: `Minh định vị mình ở giao điểm của 3 năng lực:\n\n◈ Product Craft (Core strength)\n→ Journey Mapping (95%) · UX/HCI Design (90%)\n→ Agile/Scrum Execution với CPMAI tools, RACI matrix\n→ PRD Writing, User Stories, A/B Testing & Interleaving\n\n◈ Data & Systems Thinking\n→ Python · Data Analysis · Google Colab\n→ PyTorch / ML basics (applied in EchoMind project)\n\n◈ Soft Skills\n→ Cross-functional stakeholder management (150+ contacts)\n→ Strategic documentation & reporting to Board level\n\nMinh đang gia tăng depth ở AI Engineering qua khoá Vingroup, và chuẩn bị TOEIC để mở rộng cơ hội làm việc với sản phẩm quốc tế.`,

    education: `Minh đang học năm cuối tại Đại học Kinh tế TP.HCM (UEH), chuyên ngành Quản lý Công nghệ & Đổi mới Sáng tạo.\n\n🏆 GPA: 3.53 / 4.0 — thuộc top đầu ngành\n\nCác môn học cốt lõi trực tiếp áp dụng vào công việc:\n→ Human-Computer Interaction (HCI)\n→ Design Thinking & Innovation Management\n→ Business Intelligence & Digital Transformation\n→ Project AI\n\n🏅 Chứng chỉ đã có:\n→ Google Project Management (Coursera)\n→ Google Business Intelligence (Coursera)\n→ Agile Management Certification\n\n⚡ Đang hoàn thiện:\n→ AI Thực Chiến by VinBigData · TOEIC`
};

const prompts = [
    { id: 'experience', icon: '⟳', label: 'Kinh nghiệm' },
    { id: 'projects', icon: '⬡', label: 'Dự án' },
    { id: 'skills', icon: '◎', label: 'Kỹ năng' },
    { id: 'education', icon: '▣', label: 'Học vấn' }
];

let isTyping = false;
let chartInstance = null;

const chatMessages = document.getElementById('chat-messages');
const promptsGrid = document.getElementById('prompts-grid');

// === INIT ===
function initChat() {
    chatMessages.innerHTML = '';
    renderPrompts();
    setTimeout(() => appendMessage('ai', cvData.greeting, true), 600);
}

function renderPrompts() {
    promptsGrid.innerHTML = prompts.map(p =>
        `<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.icon} ${p.label}')" ${isTyping ? 'disabled' : ''}>
            <span class="prompt-icon">${p.icon}</span>${p.label}
        </button>`
    ).join('');
}

// === VIEW SWITCHING ===
function switchView(viewId, navEl) {
    document.querySelectorAll('[id^="view-"]').forEach(v => v.style.display = 'none');
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

// === CHAT ===
function handlePrompt(id, label) {
    if (isTyping) return;
    promptsGrid.style.opacity = '0.4';
    appendMessage('user', label, false);
    setTimeout(() => {
        switchView(id, null);
        appendMessage('ai', cvData[id], true, () => {
            promptsGrid.style.opacity = '1';
        });
    }, 500);
}

function askAbout(topic) {
    if (isTyping) return;
    appendMessage('user', `Cho tôi biết thêm về: ${topic}`, false);
    const key = topic.toLowerCase().includes('echomind') ? 'projects' :
                topic.toLowerCase().includes('e-reader') ? 'projects' : 'projects';
    setTimeout(() => {
        appendMessage('ai', cvData[key], true);
    }, 500);
}

function appendMessage(sender, text, useTypewriter = false, callback = null) {
    const row = document.createElement('div');
    row.className = `msg-row ${sender}`;

    const avatar = document.createElement('div');
    avatar.className = 'msg-avatar-small';
    avatar.textContent = sender === 'ai' ? '🤖' : '👤';

    const bubble = document.createElement('div');
    bubble.className = `msg-bubble ${sender}`;

    row.appendChild(avatar);
    row.appendChild(bubble);
    chatMessages.appendChild(row);

    if (sender === 'ai' && useTypewriter) {
        typeWriter(text, bubble, 18, callback);
    } else {
        bubble.innerHTML = text.replace(/\n/g, '<br>');
        scrollBottom();
        if (callback) callback();
    }
}

function typeWriter(text, el, speed, callback) {
    isTyping = true;
    renderPrompts();
    let i = 0;
    el.innerHTML = '<span class="tc"></span><span class="cursor-blink"></span>';
    const tc = el.querySelector('.tc');

    function type() {
        if (i < text.length) {
            let ch = text.charAt(i);
            if (ch === '\n') ch = '<br>';
            tc.innerHTML += ch;
            i++;
            scrollBottom();
            setTimeout(type, speed);
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

    chartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['UX/HCI', 'Agile', 'Journey Map', 'Data Analysis', 'Python', 'PyTorch', 'A/B Testing'],
            datasets: [{
                data: [90, 85, 95, 80, 80, 72, 82],
                fill: true,
                backgroundColor: 'rgba(124,106,247,0.15)',
                borderColor: '#7c6af7',
                pointBackgroundColor: '#a594fc',
                pointBorderColor: '#1e1e2e',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#7c6af7',
                borderWidth: 1.5,
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
                    angleLines: { color: 'rgba(255,255,255,0.06)' },
                    grid: { color: 'rgba(255,255,255,0.06)' },
                    pointLabels: {
                        font: { size: 11, family: "'DM Sans', sans-serif", weight: '500' },
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
                    padding: 10,
                    titleFont: { family: "'DM Mono', monospace", size: 11 },
                    bodyFont: { family: "'DM Sans', sans-serif", size: 12 },
                    callbacks: {
                        label: ctx => {
                            const v = ctx.raw;
                            return v >= 90 ? ' Expert' : v >= 80 ? ' Advanced' : v >= 70 ? ' Proficient' : ' Familiar';
                        }
                    }
                }
            }
        }
    });
}

// === BOOT ===
window.addEventListener('DOMContentLoaded', () => {
    initChat();
    // Animate welcome stats
    setTimeout(() => {
        document.querySelectorAll('.fade-up').forEach((el, i) => {
            el.style.animationPlayState = 'running';
        });
    }, 100);
});
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
