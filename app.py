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
            -webkit-font-smoothing: antialiased;
        }

        /* === SCROLL PROGRESS BAR === */
        #scroll-progress {
            position: fixed;
            top: 0;
            left: 90px;
            height: 3px;
            background: linear-gradient(90deg, var(--accent), var(--teal));
            width: 0%;
            z-index: 1000;
            transition: width 0.1s ease-out;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
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
            transition: opacity 0.5s ease, visibility 0.5s;
        }

        .lang-title {
            font-family: 'Syne', sans-serif;
            font-size: 32px;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 40px;
            text-align: center;
            line-height: 1.4;
        }

        .lang-options {
            display: flex;
            gap: 24px;
        }

        .lang-btn {
            background: var(--surface);
            border: 1px solid var(--border2);
            color: var(--text);
            padding: 24px 48px;
            border-radius: 16px;
            font-family: 'DM Sans', sans-serif;
            font-size: 20px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        }

        .lang-btn:hover {
            border-color: var(--accent);
            background: var(--surface2);
            transform: translateY(-6px);
            box-shadow: 0 15px 35px rgba(124,106,247,0.2);
        }

        .lang-btn span {
            font-family: 'DM Mono', monospace;
            font-size: 13px;
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
            font-size: 20px;
            color: var(--accent2);
            margin-bottom: 24px;
            letter-spacing: -1px;
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

        /* === VIEW TRANSITION OVERLAY === */
        .view-transition-overlay {
            position: fixed;
            top: 0;
            left: 90px;
            right: 420px;
            bottom: 0;
            background: var(--ink);
            z-index: 999;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }
        .view-transition-overlay.active {
            opacity: 1;
            pointer-events: all;
        }
        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid var(--border2);
            border-top-color: var(--accent);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }

        /* === CHAT PANEL === */
        .chat-panel {
            width: 420px;
            height: 100%;
            flex-shrink: 0;
            background: var(--ink2);
            border-left: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            transition: width 0.3s ease;
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
            position: relative;
        }

        .welcome-eyebrow { display: flex; align-items: center; gap: 10px; margin-bottom: 32px; }
        .status-dot { width: 10px; height: 10px; background: var(--green); border-radius: 50%; box-shadow: 0 0 10px var(--green); animation: pulse-green 2s infinite; }
        @keyframes pulse-green { 0%, 100% { box-shadow: 0 0 6px var(--green); } 50% { box-shadow: 0 0 18px var(--green); } }
        .status-text { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--green); letter-spacing: 1px; text-transform: uppercase; }

        .welcome-name { font-family: 'Syne', sans-serif; font-size: clamp(48px, 5vw, 80px); font-weight: 800; line-height: 1; letter-spacing: -2px; margin-bottom: 16px; }
        .welcome-name .accent-word { color: var(--accent2); display: block; }
        .welcome-role { font-size: 22px; color: var(--text2); font-weight: 400; margin-bottom: 40px; font-style: italic; }
        
        .welcome-summary { font-size: 16px; line-height: 1.8; color: var(--text2); max-width: 650px; margin-bottom: 48px; border-left: 3px solid var(--accent); padding-left: 24px; }
        
        .contact-row { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 56px; }
        .contact-chip { display: flex; align-items: center; gap: 8px; padding: 10px 20px; background: var(--surface); border: 1px solid var(--border2); border-radius: 10px; font-size: 13px; font-family: 'DM Mono', monospace; color: var(--text2); transition: all 0.2s; cursor: default; }
        .contact-chip:hover { border-color: var(--accent); color: var(--text); background: var(--surface2); }

        .stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 650px; margin-bottom: 56px; }
        .stat-card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 24px; position: relative; overflow: hidden; transition: transform 0.3s, box-shadow 0.3s; }
        .stat-card:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.2); border-color: rgba(124,106,247,0.4); }
        .stat-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--accent), var(--teal)); }
        .stat-number { font-family: 'Syne', sans-serif; font-size: 36px; font-weight: 800; color: var(--text); line-height: 1; }
        .stat-label { font-size: 12px; color: var(--text2); margin-top: 8px; text-transform: uppercase; letter-spacing: 0.5px; }

        .section-tag { display: inline-flex; align-items: center; gap: 8px; font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px; font-weight: 600; }
        .section-tag::before { content: '◈'; font-size: 14px; }

        .view-title { font-family: 'Syne', sans-serif; font-size: 48px; font-weight: 800; letter-spacing: -1.5px; color: var(--text); margin-bottom: 56px; line-height: 1; }
        .view-title span { color: var(--accent2); }

        /* TIMELINE */
        .timeline { position: relative; padding-left: 32px; }
        .timeline::before { content: ''; position: absolute; left: 0; top: 8px; bottom: 8px; width: 2px; background: linear-gradient(to bottom, var(--accent), transparent); }
        .timeline-item { position: relative; margin-bottom: 56px; transition: transform 0.2s ease; }
        .timeline-item:hover { transform: translateX(4px); }
        .timeline-item::before { content: ''; position: absolute; left: -37px; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: var(--accent2); box-shadow: 0 0 12px rgba(165,148,252,0.5); }
        .timeline-item.past::before { background: var(--text2); box-shadow: none; }
        
        .tl-period { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); letter-spacing: 1px; margin-bottom: 10px; text-transform: uppercase; }
        .tl-role { font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 700; margin-bottom: 8px; color: var(--text); }
        .tl-company { font-size: 15px; color: var(--text2); font-style: italic; margin-bottom: 24px; }
        .tl-bullets { list-style: none; display: flex; flex-direction: column; gap: 14px; }
        .tl-bullets li { font-size: 15px; color: var(--text2); line-height: 1.8; padding-left: 24px; position: relative; }
        .tl-bullets li::before { content: '→'; position: absolute; left: 0; color: var(--accent); font-weight: bold; }
        .tl-bullets li strong { color: var(--text); font-weight: 500; }
        .tl-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 20px; }
        .tl-tag { font-family: 'DM Mono', monospace; font-size: 11px; padding: 6px 14px; border-radius: 6px; background: rgba(124,106,247,0.1); border: 1px solid rgba(124,106,247,0.25); color: var(--accent3); }

        /* PROJECTS */
        .projects-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
        .project-card { background: var(--surface); border: 1px solid var(--border); border-radius: 24px; padding: 36px; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); position: relative; overflow: hidden; }
        .project-card::after { content: ''; position: absolute; inset: 0; border-radius: 24px; opacity: 0; transition: opacity 0.3s; pointer-events: none; }
        .project-card.featured::after { background: linear-gradient(135deg, rgba(124,106,247,0.06) 0%, transparent 60%); }
        .project-card:hover { border-color: rgba(124,106,247,0.4); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
        .project-card:hover::after { opacity: 1; }
        .project-card.featured { grid-column: 1 / -1; display: grid; grid-template-columns: 1fr 300px; gap: 40px; align-items: stretch; }
        
        .project-badge { font-family: 'DM Mono', monospace; font-size: 11px; padding: 6px 12px; border-radius: 20px; font-weight: 500; text-transform: uppercase;}
        .badge-featured { background: rgba(240,192,96,0.15); color: var(--gold); border: 1px solid rgba(240,192,96,0.3); }
        .badge-active { background: rgba(82,209,138,0.15); color: var(--green); border: 1px solid rgba(82,209,138,0.3); }
        .badge-top20 { background: rgba(255,123,107,0.15); color: var(--coral); border: 1px solid rgba(255,123,107,0.3); }

        .project-name { font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 700; margin: 16px 0 8px; letter-spacing: -0.5px; color: var(--text); }
        .project-desc { font-size: 15px; color: var(--text2); line-height: 1.8; margin-bottom: 24px; }
        .project-metrics { display: flex; gap: 32px; margin: 20px 0 24px; padding: 16px; background: rgba(0,0,0,0.2); border-radius: 16px; border: 1px solid var(--border2); }
        .metric { text-align: center; flex: 1; }
        .metric-val { font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 700; color: var(--accent2); }
        .metric-lbl { font-size: 11px; color: var(--text2); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
        .tech-stack { display: flex; flex-wrap: wrap; gap: 8px; }
        .tech-pill { font-family: 'DM Mono', monospace; font-size: 11px; padding: 6px 12px; border-radius: 6px; background: var(--ink3); border: 1px solid var(--border2); color: var(--text2); }

        /* CSS Architecture Diagrams */
        .arch-diagram { display: flex; flex-direction: column; gap: 8px; background: var(--ink3); border: 1px solid var(--border2); border-radius: 20px; padding: 24px; justify-content: center; height: 100%; }
        .arch-box { background: var(--surface); border: 1px solid var(--border2); border-radius: 12px; padding: 12px; text-align: center; transition: all 0.2s; }
        .arch-box:hover { border-color: var(--accent); background: var(--surface2); }
        .arch-title { font-size: 14px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
        .arch-sub { font-family: 'DM Mono', monospace; font-size: 10px; color: var(--accent2); }
        .arch-arrow { text-align: center; color: var(--text3); font-size: 16px; margin: 2px 0; }

        /* SKILLS */
        .skills-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start; }
        .skill-group { margin-bottom: 32px; }
        .skill-group-label { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--accent2); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px; font-weight: 500; }
        .skill-bar-item { margin-bottom: 20px; }
        .skill-bar-header { display: flex; justify-content: space-between; margin-bottom: 10px; }
        .skill-bar-name { font-size: 15px; font-weight: 500; color: var(--text); }
        .skill-bar-pct { font-family: 'DM Mono', monospace; font-size: 12px; color: var(--text2); }
        .skill-bar-track { height: 6px; background: var(--surface2); border-radius: 3px; overflow: hidden; }
        .skill-bar-fill { height: 100%; border-radius: 3px; background: linear-gradient(90deg, var(--accent), var(--teal)); transform-origin: left; transform: scaleX(0); transition: transform 1s cubic-bezier(0.16, 1, 0.3, 1); }
        .skill-bar-fill.animate { transform: scaleX(1); }

        /* EDU */
        .edu-hero { background: linear-gradient(135deg, var(--surface) 0%, var(--surface2) 100%); border: 1px solid var(--border); border-radius: 24px; padding: 48px; margin-bottom: 40px; position: relative; overflow: hidden; }
        .edu-hero::before { content: 'UEH'; position: absolute; right: -20px; bottom: -50px; font-family: 'Syne', sans-serif; font-size: 200px; font-weight: 800; color: rgba(255,255,255,0.02); line-height: 1; pointer-events: none; }
        .gpa-badge { display: inline-flex; align-items: center; gap: 16px; background: rgba(240,192,96,0.1); border: 1px solid rgba(240,192,96,0.3); border-radius: 16px; padding: 16px 24px; margin-top: 24px; }

        .cert-card { background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 20px; margin-bottom: 16px; display: flex; align-items: center; gap: 20px; transition: transform 0.2s, border-color 0.2s; }
        .cert-card:hover { transform: translateX(4px); border-color: rgba(124,106,247,0.4); }
        
        /* CHAT PANEL */
        .chat-header { padding: 24px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 16px; }
        .chat-avatar { width: 44px; height: 44px; border-radius: 14px; background: linear-gradient(135deg, var(--accent), var(--teal)); display: flex; align-items: center; justify-content: center; font-size: 20px; box-shadow: 0 4px 15px rgba(124,106,247,0.3);}
        .chat-name { font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700; color: var(--text); }
        .chat-subtitle { font-size: 12px; color: var(--green); font-family: 'DM Mono', monospace; margin-top: 4px; }
        .chat-actions { margin-left: auto; display: flex; gap: 8px; }
        .action-btn { background: none; border: 1px solid var(--border2); color: var(--text2); font-size: 12px; padding: 8px 14px; border-radius: 8px; cursor: pointer; font-family: 'DM Mono', monospace; transition: all 0.2s; display: flex; align-items: center; gap: 6px; }
        .action-btn:hover { border-color: var(--accent); background: var(--surface2); color: var(--text); }

        .chat-messages { flex: 1; overflow-y: auto; padding: 24px; display: flex; flex-direction: column; gap: 24px; scroll-behavior: smooth; }
        .chat-messages::-webkit-scrollbar { width: 4px; }
        .chat-messages::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

        .msg-row { display: flex; gap: 14px; align-items: flex-end; animation: msg-in 0.3s ease-out; }
        @keyframes msg-in { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .msg-row.user { flex-direction: row-reverse; }
        .msg-avatar-small { width: 32px; height: 32px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 14px; flex-shrink: 0; }
        .msg-avatar-small.ai { background: linear-gradient(135deg, var(--accent), var(--teal)); }
        .msg-avatar-small.user { background: var(--surface2); border: 1px solid var(--border2); }
        
        .msg-bubble { max-width: 82%; padding: 16px 20px; border-radius: 18px; font-size: 14px; line-height: 1.7; }
        .msg-bubble.ai { background: var(--surface); border: 1px solid var(--border2); color: var(--text); border-bottom-left-radius: 4px; }
        .msg-bubble.user { background: var(--accent); color: white; border-bottom-right-radius: 4px; }

        .cursor-blink { display: inline-block; width: 8px; height: 16px; background: var(--accent2); margin-left: 4px; animation: blink 1s step-end infinite; vertical-align: middle; }
        @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

        .chat-footer { padding: 20px; border-top: 1px solid var(--border); }
        .prompts-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .prompt-btn { background: var(--surface); border: 1px solid var(--border2); border-radius: 12px; padding: 14px; font-size: 13px; font-weight: 500; color: var(--text2); cursor: pointer; transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1); text-align: left; display: flex; align-items: center; gap: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .prompt-btn:hover { border-color: var(--accent); color: var(--text); background: var(--surface2); transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .prompt-btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; box-shadow: none; }

        .fade-up { animation: fadeUp 0.6s ease-out forwards; opacity: 0; }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .d1{animation-delay:0.1s} .d2{animation-delay:0.2s} .d3{animation-delay:0.3s} .d4{animation-delay:0.4s} .d5{animation-delay:0.5s}

        /* === RESPONSIVE MEDIA QUERIES === */
        @media (max-width: 1200px) {
            .chat-panel { width: 340px; }
            .view-transition-overlay { right: 340px; }
            .view-content { padding: 40px; }
            .stat-grid { grid-template-columns: repeat(2, 1fr); }
            .skills-layout { grid-template-columns: 1fr; gap: 32px;}
            .project-card.featured { grid-template-columns: 1fr; }
            .arch-diagram { height: auto; }
        }
        @media (max-width: 900px) {
            .chat-panel { display: none; }
            .view-transition-overlay { left: 72px; right: 0; }
            .projects-grid { grid-template-columns: 1fr; }
            #scroll-progress { left: 72px; }
            .sidenav { width: 72px; }
            .nav-item { width: 44px; height: 44px; }
            .nav-tooltip { left: 56px; }
        }

    </style>
</head>
<body>
<div class="noise"></div>

<div id="scroll-progress"></div>

<div id="lang-overlay">
    <div class="lang-title">Choose your language <br><span style="font-size:24px; color:var(--text2); font-weight:400; margin-top:12px; display:inline-block;">Chọn ngôn ngữ hiển thị</span></div>
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

    <main class="visual-panel" id="visual-panel">
        
        <div id="view-transition-overlay" class="view-transition-overlay">
            <div class="spinner"></div>
        </div>

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
                <div class="contact-chip" title="Email me">✉ hwinh.work@gmail.com</div>
                <div class="contact-chip" title="Call me">📞 +84 765 828 191</div>
                <div class="contact-chip" title="Location">📍 Hồ Chí Minh</div>
                <div class="contact-chip" title="Academic">🎓 UEH · GPA 3.53</div>
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
                    <div style="width:100%;height:320px;position:relative;margin-bottom:40px;">
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
                <h3 style="font-family:'Syne',sans-serif;font-size:32px;font-weight:800;color:var(--text);margin-bottom:12px;" id="ed-uni">Đại học Kinh tế TP.HCM</h3>
                <p style="color:var(--text2);font-size:18px;margin-bottom:32px;" id="ed-major"></p>
                <div class="gpa-badge">
                    <span style="font-size:32px;">🏆</span>
                    <div>
                        <div style="font-size:13px;color:var(--text2);margin-bottom:4px;">Grade Point Average</div>
                        <div class="gpa-value" style="font-family:'Syne',sans-serif;font-size:32px;font-weight:800;color:var(--gold);">3.53 <span style="font-size:20px;color:var(--text2);font-weight:600;">/ 4.0</span></div>
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
            <div class="chat-actions">
                <button class="action-btn" onclick="openLangOverlay()" id="c-lang" title="Change Language">🌐</button>
                <button class="action-btn" onclick="resetChat()" id="c-reset">↺</button>
            </div>
        </div>
        <div class="chat-messages" id="chat-messages"></div>
        <div class="chat-footer">
            <div class="prompts-grid" id="prompts-grid"></div>
        </div>
    </aside>
</div>

<script>
// === SCROLL LOGIC FOR PROGRESS BAR ===
const vPanel = document.getElementById('visual-panel');
const scrollProgress = document.getElementById('scroll-progress');

vPanel.addEventListener('scroll', () => {
    const winScroll = vPanel.scrollTop;
    const height = vPanel.scrollHeight - vPanel.clientHeight;
    if(height > 0) {
        const scrolled = (winScroll / height) * 100;
        scrollProgress.style.width = scrolled + '%';
    } else {
        scrollProgress.style.width = '0%';
    }
});


// === MULTILINGUAL DATA (English & Vietnamese) ===
// Cập nhật nội dung cực kỳ tự nhiên, loại bỏ các thẻ [cite] rác và thêm chi tiết từ CV/Báo cáo
const i18n = {
    en: {
        nav: { overview: "Overview", exp: "Experience", proj: "Projects", skills: "Skills", edu: "Education" },
        welcome: {
            status: "Available for opportunities · HCMC, Vietnam",
            role: "Product Owner Intern · UX Strategist",
            summary: "I am a young professional in Technology & Innovation Management, building products at the intersection of <strong style='color:var(--text)'>UX Design</strong>, <strong style='color:var(--text)'>System Thinking</strong>, and <strong style='color:var(--text)'>AI Engineering</strong>. My true passion lies in translating complex user data and behavioral 'pain points' into seamless, measurable, and impactful digital experiences.",
            stat1: "Years Exp.", stat2: "Stakeholders", stat3: "Agile Sprints"
        },
        experience: {
            tag: "Work History", title: "Work <span>Experience</span>",
            items: [
                {
                    period: "JAN 2025 — OCT 2025 · PRESENT", role: "Project Management Executive",
                    company: "Startup & Innovation Hub of HCMC (SIHUB) · Under Dept. of Science & Technology",
                    bullets: [
                        "<strong>Customer Journey Mapping & MVP Delivery:</strong> I didn't just draw flowcharts; I engaged deeply in user empathy. I designed end-to-end digital journey maps for tech startups and formulated clear, actionable user stories for rapid MVP development.",
                        "<strong>Pain Point Resolution & Advanced Testing:</strong> Continuously monitored user touchpoints to spot operational bottlenecks. I heavily applied A/B testing and Interleaving experiments to scientifically validate feature iterations before full-scale rollout.",
                        "<strong>Omnichannel Data & Stakeholder Management:</strong> Transformed NPS from a dry metric into an early warning system for user churn. I acted as the focal point for startup founders, analyzing behavioral data to report strategic insights directly to the Board."
                    ],
                    tags: ["Customer Journey", "A/B Testing", "MVP Delivery", "Stakeholder Mgmt"]
                },
                {
                    period: "JUL 2024 — DEC 2024", role: "Research & Development Intern",
                    company: "SIHUB · Executed data-driven project management for city-level framework",
                    bullets: [
                        "<strong>Systematizing Chaos:</strong> Navigated conflicting opinions from over 150 key stakeholders during a city-level competency gap analysis.",
                        "<strong>Structured Documentation:</strong> Acted as the bridge between real-world needs and system solutions by drafting clear URD (User Requirement Document) standards and strategic reports."
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
                    desc: "My most ambitious project. Stemming from the desire to help paralyzed patients communicate, this system reads non-invasive EEG signals and translates them into text. When our baseline LSTM model suffered from Mode Collapse, I decisively led the team to pivot to a Transformer V2 architecture. To overcome hardware limits, I applied Int8 Quantization, allowing the model to run smoothly on personal laptops without GPUs. We also built an 'Expert Dashboard' using Gradio with real-time inference and Attention Maps, bringing Explainable AI to doctors.",
                    m1: "55-65", m1l: "WPM Output", m2: "<1s", m2l: "Latency", m3: "Int8", m3l: "Quantization",
                    tech: ["Python", "PyTorch", "Transformer V2", "Gradio", "Agile/Scrum", "Product Strategy"],
                    arch: { step1: "EEG Signal", sub1: "Data Augmentation", step2: "Transformer V2", sub2: "Int8 Quantization", step3: "Gradio UI", sub3: "Realtime + Attention Maps" }
                },
                {
                    id: "ereader", badge: "🏆 Top 20 Finalist", badgeClass: "badge-top20",
                    date: "Mar–Jun 2025", name: "E-Reader Ecosystem", role: "Product Lead · HCMC People's Committee",
                    desc: "A Top 20 City-level project. The main challenge was designing a learning device without causing cognitive overload for students. I heavily applied Human-Computer Interaction (HCI) principles to streamline the user journey from device activation to content syncing. Every user 'pain point' was systematically decomposed into measurable, actionable User Stories.",
                    tech: ["HCI Principles", "UX Strategy", "Journey Mapping", "URD"]
                },
                {
                    id: "startup", badge: "● Ongoing", badgeClass: "badge-active",
                    date: "Jul 2024 — Now", name: "Startup Events Ops", role: "Operations · Innovation Ecosystem",
                    desc: "Directly operated large-scale, city-level innovation events including Univ.Star 2024/2025 and the WHISE 2024 week. Served as the operational bridge connecting startup founders, angel investors, and ecosystem builders.",
                    tech: ["Event Management", "Stakeholder Comm", "Cross-team Coord"]
                }
            ]
        },
        skills: {
            tag: "Competencies", title: "Professional <span>Skills</span>", radar: "Radar Overview", certTag: "Certifications",
            groups: [
                { name: "Product Management (Core)", items: [{n: "Journey Mapping & UX/HCI", p: "95%"}, {n: "Agile / Scrum (CPMAI)", p: "88%"}, {n: "PRD & User Stories", p: "85%"}, {n: "A/B Testing & Metrics", p: "82%"}] },
                { name: "Data & Engineering", items: [{n: "Python & Data Analysis", p: "80%"}, {n: "PyTorch / System Architecture", p: "75%"}] }
            ],
            certs: [
                { i: "🏅", n: "Google Project Management", org: "Coursera · Google" },
                { i: "📊", n: "Google Business Intelligence", org: "Coursera · Google" },
                { i: "🔄", n: "Agile Management", org: "Professional Certification" }
            ]
        },
        education: {
            tag: "Academic Background", title: "Education & <span>Awards</span>", uni: "University of Economics HCMC (UEH)",
            major: "Bachelor in Technology & Innovation Management",
            courseTag: "Core Coursework driving my Product Mindset",
            courses: ["Design Thinking", "Human-Computer Interaction (HCI)", "Innovation Management", "Business Intelligence", "AI Project Management"]
        },
        chat: {
            name: "Minh's AI Assistant", sub: "● Online · Ready to connect", reset: "Reset Chat", lang: "EN/VI",
            greeting: "Hello! I am the AI representative for Nguyen Hoang Minh — a Product Owner Intern with a robust foundation in UX Strategy and System Thinking.\n\nMinh is currently looking for a dynamic product team to contribute his skills in user journey mapping and data-driven product decisions. Which aspect of his profile would you like to explore?",
            prompts: [
                { id: "exp", icon: "💼", label: "Experience" },
                { id: "proj", icon: "🚀", label: "Projects" },
                { id: "edu", icon: "🎓", label: "Education" },
                { id: "skills", icon: "🛠️", label: "Skills" }
            ],
            ans_exp: "Minh has spent over 3 years sharpening his product management skills at SIHUB (Startup & Innovation Hub of HCMC).\n\n◈ Current Role: Project Management Executive\nInstead of just drawing flows, Minh actively solves startup pain points through end-to-end journey maps and A/B testing validation. He utilizes NPS as a behavioral signal, not just a score.\n\n◈ Previous: R&D Intern\nHe successfully managed data from over 150 stakeholders, translating chaotic qualitative feedback into structured URD documents.",
            ans_proj: "Minh's portfolio highlights his ability to bridge UX and Technical Engineering. Here are his top 3 projects:\n\n🧠 EchoMind AI (Flagship)\nAs Project Lead, Minh managed an 8-Sprint Agile cycle. When the LSTM model failed, he pivoted the team to a Transformer model and applied Int8 Quantization to ensure smooth, GPU-free deployment via a Gradio UI.\n\n📚 E-Reader Ecosystem\nApplied deep HCI principles to reduce cognitive load for students. Recognized as a Top 20 Finalist at a City-level competition.\n\n🚀 Startup Events\nOperated large-scale events (Univ.Star, WHISE), seamlessly coordinating between founders and investors.",
            ans_edu: "Minh is completing his senior year at UEH, majoring in Technology & Innovation Management with an excellent GPA of 3.53/4.0.\n\nHis academic focus directly empowers his product mindset, with core subjects including Design Thinking, Human-Computer Interaction (HCI), Business Intelligence, and AI Projects.",
            ans_skills: "Minh sits perfectly at the intersection of three key domains:\n\n◈ Product Craft (Core Strength)\n→ Deep expertise in Journey Mapping and UX/HCI.\n→ Execution via Agile/Scrum (CPMAI framework, RACI matrix).\n→ Strong ability to write PRDs, User Stories, and conduct A/B Testing.\n\n◈ Data & Systems Thinking\n→ Proficient in Python and Data Analysis.\n→ Solid understanding of AI architecture (proven by leading the PyTorch EchoMind project).\n\n◈ Stakeholder Management\n→ Experienced in aligning 150+ cross-functional contacts and reporting to executive boards."
        }
    },
    vi: {
        nav: { overview: "Tổng quan", exp: "Kinh nghiệm", proj: "Dự án", skills: "Kỹ năng", edu: "Học vấn" },
        welcome: {
            status: "Sẵn sàng đón nhận cơ hội mới · TP.HCM",
            role: "Product Owner Intern · UX Strategist",
            summary: "Tôi là một chuyên gia trẻ trong lĩnh vực Quản lý Công nghệ & Đổi mới Sáng tạo — xây dựng sản phẩm tại điểm giao thoa giữa <strong style='color:var(--text)'>UX Design</strong>, <strong style='color:var(--text)'>System Thinking</strong>, và <strong style='color:var(--text)'>AI</strong>. Đam mê lớn nhất của tôi là chuyển hoá dữ liệu và 'nỗi đau' (pain points) phức tạp của người dùng thành các trải nghiệm số mượt mà, có thể đo lường và mang lại giá trị thực.",
            stat1: "Năm kinh nghiệm", stat2: "Stakeholders", stat3: "Agile Sprints"
        },
        experience: {
            tag: "Lịch sử làm việc", title: "Kinh nghiệm <span>Làm việc</span>",
            items: [
                {
                    period: "THÁNG 1 2025 — THÁNG 10 2025 · HIỆN TẠI", role: "Chuyên viên Quản lý Dự án (Project Management Executive)",
                    company: "Trung tâm Hỗ trợ Khởi nghiệp & Đổi mới sáng tạo TP.HCM (SIHUB) · Trực thuộc Sở KH&CN",
                    bullets: [
                        "<strong>Thiết kế Hành trình Khách hàng & Triển khai MVP:</strong> Tôi không chỉ dừng ở việc vẽ flowchart, mà trực tiếp thấu cảm người dùng. Tôi thiết kế bản đồ hành trình số (digital journey maps) cho các startup và định nghĩa User Stories rõ ràng để phát triển MVP nhanh chóng.",
                        "<strong>Giải quyết Vấn đề & Kiểm thử:</strong> Liên tục theo dõi các điểm chạm để phát hiện điểm nghẽn. Tôi áp dụng mạnh mẽ A/B testing và Interleaving experiments để kiểm chứng bằng dữ liệu thật trước khi tung tính năng ra diện rộng.",
                        "<strong>Quản lý Dữ liệu & Stakeholder:</strong> Biến NPS từ một con số khô khan thành hệ thống cảnh báo sớm về hành vi rời bỏ. Tôi làm đầu mối phân tích dữ liệu và báo cáo insight chiến lược lên Ban Giám đốc."
                    ],
                    tags: ["Customer Journey", "A/B Testing", "MVP Delivery", "Stakeholder Mgmt"]
                },
                {
                    period: "THÁNG 7 2024 — THÁNG 12 2024", role: "Thực tập sinh R&D",
                    company: "SIHUB · Quản lý dự án dựa trên dữ liệu cho khung năng lực cấp thành phố",
                    bullets: [
                        "<strong>Hệ thống hóa sự hỗn loạn:</strong> Đối mặt với hơn 150 stakeholders chủ chốt, tôi đã thu thập, làm sạch và chuẩn hóa các luồng ý kiến trái chiều trong dự án phân tích khoảng trống năng lực.",
                        "<strong>Tài liệu hóa:</strong> Trở thành cầu nối giữa nhu cầu thực tế và giải pháp hệ thống bằng việc soạn thảo các tài liệu chuẩn URD và báo cáo chiến lược rõ ràng."
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
                    desc: "Dự án tâm huyết nhất của tôi, nhằm hỗ trợ bệnh nhân mất khả năng giao tiếp. Hệ thống dịch tín hiệu điện não (EEG) thành văn bản. Khi mô hình LSTM ban đầu gặp hiện tượng Mode Collapse, tôi đã quyết đoán định hướng team chuyển sang kiến trúc Transformer V2. Để giải quyết bài toán phần cứng, tôi áp dụng Quantization (đưa mô hình từ Float32 xuống Int8) giúp chạy mượt mà trên máy cá nhân không cần GPU. Giao diện thiết kế bằng Gradio (dự đoán realtime không cần nút Submit) kết hợp Expert Dashboard với Attention Maps nhằm minh bạch hóa AI (Explainable AI) cho bác sĩ.",
                    m1: "55-65", m1l: "Tốc độ (WPM)", m2: "<1s", m2l: "Độ trễ", m3: "Int8", m3l: "Quantization",
                    tech: ["Python", "PyTorch", "Transformer V2", "Gradio", "Agile/Scrum", "Product Strategy"],
                    arch: { step1: "Tín hiệu EEG", sub1: "Data Augmentation", step2: "Transformer V2", sub2: "Int8 Quantization", step3: "Giao diện Gradio", sub3: "Realtime + Attention Maps" }
                },
                {
                    id: "ereader", badge: "🏆 Top 20 Chung cuộc", badgeClass: "badge-top20",
                    date: "Tháng 3–6 2025", name: "Hệ sinh thái E-Reader", role: "Product Lead · UBND TP.HCM",
                    desc: "Dự án lọt Top 20 cấp Thành phố. Thách thức lớn nhất là thiết kế luồng sử dụng mà không làm học sinh bị 'quá tải nhận thức'. Tôi áp dụng triệt để nguyên lý Tương tác Người-Máy (HCI) để tối ưu hành trình từ lúc mở máy đến khi đồng bộ nội dung. Mọi 'nỗi đau' của người dùng được phân rã thành các User Story có tính thực thi cao.",
                    tech: ["Nguyên lý HCI", "Chiến lược UX", "Bản đồ Hành trình", "URD"]
                },
                {
                    id: "startup", badge: "● Đang diễn ra", badgeClass: "badge-active",
                    date: "Tháng 7 2024 — Nay", name: "Vận hành Sự kiện Startup", role: "Vận hành · Hệ sinh thái Đổi mới sáng tạo",
                    desc: "Trực tiếp vận hành các sự kiện đổi mới sáng tạo quy mô lớn của thành phố: Univ.Star 2024/2025 và tuần lễ WHISE 2024. Đóng vai trò cầu nối vận hành giữa các nhà sáng lập startup, nhà đầu tư thiên thần và hệ sinh thái.",
                    tech: ["Quản lý Sự kiện", "Giao tiếp Stakeholder", "Điều phối Cross-team"]
                }
            ]
        },
        skills: {
            tag: "Năng lực Lõi", title: "Kỹ năng <span>Chuyên môn</span>", radar: "Biểu đồ Phân tích", certTag: "Chứng chỉ",
            groups: [
                { name: "Product Management (Cốt lõi)", items: [{n: "Bản đồ Hành trình & UX/HCI", p: "95%"}, {n: "Agile / Scrum (Khung CPMAI)", p: "88%"}, {n: "Viết PRD & User Stories", p: "85%"}, {n: "A/B Testing & Phân tích Chỉ số", p: "82%"}] },
                { name: "Data & Systems Thinking", items: [{n: "Python & Phân tích Dữ liệu", p: "80%"}, {n: "PyTorch / Kiến trúc Hệ thống", p: "75%"}] }
            ],
            certs: [
                { i: "🏅", n: "Quản lý Dự án (Google Project Management)", org: "Coursera · Google" },
                { i: "📊", n: "Trí tuệ Doanh nghiệp (Google BI)", org: "Coursera · Google" },
                { i: "🔄", n: "Quản trị Agile", org: "Chứng nhận Chuyên nghiệp" }
            ]
        },
        education: {
            tag: "Nền tảng Học vấn", title: "Học vấn & <span>Thành tích</span>", uni: "Đại học Kinh tế TP.HCM (UEH)",
            major: "Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo",
            courseTag: "Các môn học định hình tư duy Sản phẩm",
            courses: ["Tư duy Thiết kế (Design Thinking)", "Tương tác Người-Máy (HCI)", "Quản trị Đổi mới Sáng tạo", "Trí tuệ Doanh nghiệp (BI)", "Quản lý Dự án AI"]
        },
        chat: {
            name: "Trợ lý AI của Minh", sub: "● Trực tuyến · Sẵn sàng kết nối", reset: "Khởi tạo lại", lang: "Ngôn ngữ",
            greeting: "Xin chào! Tôi là AI đại diện cho Nguyễn Hoàng Minh — Product Owner Intern với nền tảng vững chắc về UX Strategy và System Thinking.\n\nMinh đang tìm kiếm một đội ngũ phát triển sản phẩm năng động để cống hiến khả năng thiết kế hành trình người dùng và ra quyết định dựa trên dữ liệu. Bạn muốn tìm hiểu khía cạnh nào trong hồ sơ của Minh?",
            prompts: [
                { id: "exp", icon: "💼", label: "Kinh nghiệm" },
                { id: "proj", icon: "🚀", label: "Dự án" },
                { id: "edu", icon: "🎓", label: "Học vấn" },
                { id: "skills", icon: "🛠️", label: "Kỹ năng" }
            ],
            ans_exp: "Minh đã có hơn 3 năm rèn giũa kỹ năng quản lý sản phẩm tại SIHUB.\n\n◈ Vai trò hiện tại: Project Management Executive\nThay vì chỉ vẽ luồng lý thuyết, Minh trực tiếp giải quyết bài toán của startup qua bản đồ hành trình số và A/B testing. Minh sử dụng NPS như một tín hiệu dự báo hành vi, không chỉ là điểm số.\n\n◈ Trước đó: Thực tập sinh R&D\nMinh đã chứng minh khả năng hệ thống hóa sự hỗn loạn khi quản lý dữ liệu từ hơn 150 stakeholders, biên dịch phản hồi định tính thành tài liệu URD cấu trúc.",
            ans_proj: "Các dự án của Minh chứng minh khả năng gắn kết UX và Kỹ thuật:\n\n🧠 EchoMind AI (Dự án Trọng điểm)\nLà Project Lead, Minh quản lý 8 Sprints theo Agile. Khi mô hình LSTM thất bại, Minh đã quyết định chuyển hướng sang Transformer, áp dụng Int8 Quantization để mô hình chạy mượt mà trên máy tính cá nhân qua giao diện Gradio.\n\n📚 Hệ sinh thái E-Reader\nÁp dụng sâu sắc nguyên lý HCI để giảm tải nhận thức cho học sinh. Lọt Top 20 cuộc thi cấp Thành phố.\n\n🚀 Sự kiện Startup\nVận hành các sự kiện quy mô lớn (Univ.Star, WHISE), điều phối trơn tru giữa founders và nhà đầu tư.",
            ans_edu: "Minh đang học năm cuối tại UEH, chuyên ngành Quản lý Công nghệ và Đổi mới Sáng tạo với thành tích xuất sắc (GPA 3.53/4.0).\n\nCác môn học nòng cốt giúp định hình tư duy sản phẩm của Minh gồm: Tư duy Thiết kế, Tương tác Người-Máy (HCI), Trí tuệ Doanh nghiệp (BI) và Dự án AI.",
            ans_skills: "Minh định vị mình ở điểm giao thoa hoàn hảo của 3 năng lực:\n\n◈ Product Craft (Thế mạnh Cốt lõi)\n→ Nắm vững Journey Mapping và thiết kế UX/HCI.\n→ Thực thi xuất sắc qua Agile/Scrum (Khung CPMAI, Ma trận RACI).\n→ Năng lực viết PRD, User Stories và đo lường A/B Testing.\n\n◈ Data & Systems Thinking\n→ Thành thạo Python & Phân tích Dữ liệu.\n→ Hiểu rõ kiến trúc hệ thống AI (minh chứng qua việc lead dự án PyTorch EchoMind).\n\n◈ Quản lý Stakeholder\n→ Dày dặn kinh nghiệm làm việc đa phòng ban với hơn 150 liên hệ, báo cáo cấp Ban Giám đốc."
        }
    }
};

let currentLang = 'en'; 
let isTyping = false;
let isTransitioning = false; // Ngăn spam click khi chuyển cảnh
let chartInstance = null;

const chatMessages = document.getElementById('chat-messages');
const promptsGrid = document.getElementById('prompts-grid');

// === OVERLAY MỞ CHỌN NGÔN NGỮ (LOGOUT TÍNH NĂNG) ===
function openLangOverlay() {
    if (isTyping || isTransitioning) return;
    const overlay = document.getElementById('lang-overlay');
    const mainApp = document.getElementById('main-app');
    
    overlay.style.visibility = 'visible';
    overlay.style.opacity = '1';
    mainApp.style.opacity = '0';
    
    // Reset view về Welcome
    setTimeout(() => {
        switchView('welcome', document.querySelector('.nav-item[data-view="welcome"]'));
    }, 500);
}

// === LANGUAGE SELECTOR ===
function selectLanguage(lang) {
    currentLang = lang;
    document.getElementById('lang-overlay').style.opacity = '0';
    document.getElementById('main-app').style.opacity = '1';
    
    setTimeout(() => {
        document.getElementById('lang-overlay').style.visibility = 'hidden';
    }, 500);
    
    renderUI();
    initChat();
    // Render lại biểu đồ nếu đang đứng ở tab Kỹ năng
    if(document.getElementById('view-skills').style.display !== 'none') {
        setTimeout(initSkillsChart, 50); 
    }
}

// === RENDER UI TEXT DYNAMICALLY ===
function renderUI() {
    const t = i18n[currentLang];

    // Sidebar Nav
    document.getElementById('nav-overview').textContent = t.nav.overview;
    document.getElementById('nav-exp').textContent = t.nav.exp;
    document.getElementById('nav-proj').textContent = t.nav.proj;
    document.getElementById('nav-skills').textContent = t.nav.skills;
    document.getElementById('nav-edu').textContent = t.nav.edu;

    // View: Welcome
    document.getElementById('w-status').textContent = t.welcome.status;
    document.getElementById('w-role').textContent = t.welcome.role;
    document.getElementById('w-summary').innerHTML = t.welcome.summary;
    document.getElementById('w-stat1').textContent = t.welcome.stat1;
    document.getElementById('w-stat2').textContent = t.welcome.stat2;
    document.getElementById('w-stat3').textContent = t.welcome.stat3;

    // View: Experience
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

    // View: Projects (With CSS Architecture Diagrams)
    document.getElementById('p-tag').textContent = t.projects.tag;
    document.getElementById('p-title').innerHTML = t.projects.title;
    document.getElementById('p-grid').innerHTML = t.projects.items.map(p => `
        <div class="project-card ${p.id==='echomind'?'featured':''}">
            ${p.id==='echomind' ? `
                <div>
                    <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
                        <span class="project-badge ${p.badgeClass}">${p.badge}</span>
                        <span class="project-badge badge-active" style="background:rgba(82,209,138,0.1); border-color:transparent;">${p.date}</span>
                    </div>
                    <div class="project-name">${p.name}</div>
                    <div style="font-size:14px;color:var(--text2);margin-bottom:20px;font-style:italic;">${p.role}</div>
                    <p class="project-desc">${p.desc}</p>
                    <div class="project-metrics">
                        <div class="metric"><div class="metric-val">${p.m1}</div><div class="metric-lbl">${p.m1l}</div></div>
                        <div class="metric"><div class="metric-val">${p.m2}</div><div class="metric-lbl">${p.m2l}</div></div>
                        <div class="metric"><div class="metric-val">${p.m3}</div><div class="metric-lbl">${p.m3l}</div></div>
                    </div>
                    <div class="tech-stack">${p.tech.map(th => `<span class="tech-pill">${th}</span>`).join('')}</div>
                </div>
                
                <div class="arch-diagram">
                    <div class="arch-box">
                        <div class="arch-title">1. ${p.arch.step1}</div>
                        <div class="arch-sub">${p.arch.sub1}</div>
                    </div>
                    <div class="arch-arrow">↓</div>
                    <div class="arch-box" style="border-color:var(--accent);">
                        <div class="arch-title">2. ${p.arch.step2}</div>
                        <div class="arch-sub">${p.arch.sub2}</div>
                    </div>
                    <div class="arch-arrow">↓</div>
                    <div class="arch-box">
                        <div class="arch-title">3. ${p.arch.step3}</div>
                        <div class="arch-sub">${p.arch.sub3}</div>
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

    // View: Skills
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
        <div class="cert-card">
            <span style="font-size:28px; flex-shrink:0;">${c.i}</span>
            <div>
                <div style="color:var(--text);font-size:15px;font-weight:600;margin-bottom:4px;">${c.n}</div>
                <div style="font-size:13px;color:var(--text2);">${c.org}</div>
            </div>
        </div>
    `).join('');

    // View: Education
    document.getElementById('ed-tag').textContent = t.education.tag;
    document.getElementById('ed-title').innerHTML = t.education.title;
    document.getElementById('ed-uni').textContent = t.education.uni;
    document.getElementById('ed-major').textContent = t.education.major;
    document.getElementById('ed-courses').innerHTML = `
        <div class="skill-group-label" style="font-family:'DM Mono',monospace;font-size:12px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:20px;">${t.education.courseTag}</div>
        <div style="display:flex;flex-wrap:wrap;gap:12px;">
            ${t.education.courses.map(c => `<span style="font-size:14px;padding:10px 20px;background:var(--surface);border:1px solid var(--border2);border-radius:12px;color:var(--text);">${c}</span>`).join('')}
        </div>
    `;

    // Chat Labels
    document.getElementById('c-name').textContent = t.chat.name;
    document.getElementById('c-sub').textContent = t.chat.sub;
    
    // Nút Header Chat Tooltips
    document.getElementById('c-lang').title = t.chat.lang;
    document.getElementById('c-reset').title = t.chat.reset;
}

// === VIEW SWITCHING (WITH SMOOTH UX TRANSITION) ===
function switchView(viewId, navEl) {
    if (isTransitioning) return;
    
    const targetView = document.getElementById('view-' + viewId);
    if (!targetView || targetView.style.display !== 'none') return; // Không xử lý nếu đang mở sẵn

    isTransitioning = true;
    
    // 1. Cập nhật Sidebar Active ngay lập tức
    document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
    if (navEl) navEl.classList.add('active');
    else {
        const nav = document.querySelector(`[data-view="${viewId}"]`);
        if (nav) nav.classList.add('active');
    }

    // 2. Hiện Spinner Overlay mượt mà
    const transOverlay = document.getElementById('view-transition-overlay');
    transOverlay.classList.add('active');

    // 3. Chờ Spinner phủ kín (300ms) rồi thay đổi giao diện DOM ẩn bên dưới
    setTimeout(() => {
        // Tắt hết view cũ
        document.querySelectorAll('.view-content').forEach(v => { v.style.display = 'none'; });
        // Bật view mới
        targetView.style.display = '';
        
        // Reset thanh Scroll Progress Bar
        document.getElementById('scroll-progress').style.width = '0%';
        document.getElementById('visual-panel').scrollTop = 0;

        // Reset & Re-animate biểu đồ cho mục Kỹ năng
        if (viewId === 'skills') {
            document.querySelectorAll('.skill-bar-fill').forEach(bar => bar.classList.remove('animate'));
            setTimeout(() => {
                initSkillsChart();
                animateBars();
            }, 50); // Delay nhỏ để Canvas nhận diện kích thước
        }

        // Tái tạo hiệu ứng Fade-up đẹp mắt của CSS
        const animElements = targetView.querySelectorAll('.fade-up');
        animElements.forEach(el => {
            el.style.animation = 'none';
            void el.offsetWidth; // Trigger DOM reflow
            el.style.animation = null; 
        });

        // 4. Cho Spinner Overlay biến mất
        setTimeout(() => {
            transOverlay.classList.remove('active');
            isTransitioning = false; // Mở khóa tương tác
        }, 150); 

    }, 300);
}

function animateBars() {
    document.querySelectorAll('.skill-bar-fill').forEach(bar => bar.classList.add('animate'));
}

// === CHAT SYSTEM ===
function initChat() {
    chatMessages.innerHTML = '';
    renderPrompts();
    setTimeout(() => appendMessage('ai', i18n[currentLang].chat.greeting, true), 500);
}

function renderPrompts() {
    const pData = i18n[currentLang].chat.prompts;
    promptsGrid.innerHTML = pData.map(p =>
        `<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.icon} ${p.label}')" ${isTyping || isTransitioning ? 'disabled' : ''}>
            <span style="font-size:18px;">${p.icon}</span>${p.label}
        </button>`
    ).join('');
}

function handlePrompt(id, label) {
    if (isTyping || isTransitioning) return;
    promptsGrid.style.opacity = '0.4';
    appendMessage('user', label, false);
    
    const viewMap = { exp: 'experience', proj: 'projects', edu: 'education', skills: 'skills' };
    
    // Đồng bộ thao tác Chat và Chuyển màn hình
    setTimeout(() => switchView(viewMap[id] || 'welcome', null), 400);

    setTimeout(() => {
        appendMessage('ai', i18n[currentLang].chat['ans_'+id], true, () => {
            promptsGrid.style.opacity = '1';
            renderPrompts();
        });
    }, 800);
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
        typeWriter(text, bubble, callback);
    } else {
        bubble.innerHTML = text.replace(/\n/g, '<br>');
        scrollBottom();
        if (callback) callback();
    }
}

// Hiệu ứng "AI đang gõ phím" với thời gian ngẫu nhiên tạo cảm giác tự nhiên
function typeWriter(text, el, callback) {
    isTyping = true;
    renderPrompts(); 
    
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
                    
                    // Tốc độ gõ từ 5ms - 20ms
                    let randomSpeed = Math.floor(Math.random() * 15) + 5;
                    setTimeout(type, randomSpeed);
                } else {
                    nodeIndex++;
                    charIndex = 0;
                    type();
                }
            } else { // HTML tags (<strong>, <br>)
                tc.appendChild(node.cloneNode(true));
                nodeIndex++;
                scrollBottom();
                setTimeout(type, 10);
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
    if (isTyping || isTransitioning) return;
    initChat();
}

// === SKILLS RADAR CHART (CHART.JS) ===
function initSkillsChart() {
    const ctx = document.getElementById('skillsChart');
    if (!ctx) return;
    if (chartInstance) { chartInstance.destroy(); chartInstance = null; }

    const labels = currentLang === 'en' 
        ? ['UX / HCI Design', 'Agile / Scrum', 'Journey Mapping', 'Data Analysis', 'Python / Tech', 'PyTorch / ML', 'A/B Testing']
        : ['Thiết kế UX/HCI', 'Agile / Scrum', 'Hành trình KH', 'Phân tích Dữ liệu', 'Python / Kỹ thuật', 'PyTorch / ML', 'Kiểm thử A/B'];

    chartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                data: [90, 88, 95, 80, 80, 75, 82],
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
                        font: { size: 12, family: "'DM Sans', sans-serif", weight: '600' },
                        color: '#9898b0'
                    }
                }
            },
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: '#252538',
                    borderColor: 'rgba(255,255,255,0.15)',
                    borderWidth: 1,
                    padding: 14,
                    titleFont: { family: "'DM Mono', monospace", size: 12 },
                    bodyFont: { family: "'DM Sans', sans-serif", size: 14 },
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
