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
        nav: { overview: "Tổng quan",
