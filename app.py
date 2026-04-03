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

html_code = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hoang Minh | Product &amp; UX</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
:root{
  --ink:#0a0a0f;--ink2:#12121a;--ink3:#1c1c28;
  --surface:#1e1e2e;--surface2:#252538;--surface3:#2e2e45;
  --border:rgba(255,255,255,0.07);--border2:rgba(255,255,255,0.13);
  --text:#e8e8f0;--text2:#9898b0;--text3:#5a5a78;
  --accent:#7c6af7;--accent2:#a594fc;--accent3:#c4b8fe;
  --gold:#f0c060;--gold2:#fad87a;
  --green:#52d18a;--green2:#7de8a8;
  --coral:#ff7b6b;--coral2:#ffaa9f;
  --teal:#4dd9c0;--teal2:#80e8d5;
  --blue:#5b9bd5;--blue2:#82b8e8;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{font-size:16px;}
body{font-family:'DM Sans',sans-serif;background:var(--ink);color:var(--text);height:100vh;overflow:hidden;-webkit-font-smoothing:antialiased;}

/* === SCROLL PROGRESS === */
#scroll-progress{position:fixed;top:0;left:90px;height:3px;background:linear-gradient(90deg,var(--accent),var(--teal));width:0%;z-index:1000;transition:width .1s ease-out;border-radius:0 2px 2px 0;}

/* === LANGUAGE OVERLAY === */
#lang-overlay{
  position:fixed;inset:0;background:var(--ink);z-index:9999;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;
  transition:opacity .5s ease,visibility .5s;
}
.lo-logo{font-family:'Syne',sans-serif;font-size:64px;font-weight:800;color:var(--accent2);letter-spacing:-3px;line-height:1;}
.lo-tagline{font-family:'DM Mono',monospace;font-size:12px;color:var(--text2);letter-spacing:3px;text-transform:uppercase;}
.lo-question{font-family:'Syne',sans-serif;font-size:22px;font-weight:600;color:var(--text);text-align:center;line-height:1.5;}
.lo-options{display:flex;gap:20px;}
.lo-btn{
  background:var(--surface);border:1px solid var(--border2);color:var(--text);
  padding:22px 52px;border-radius:16px;font-family:'Syne',sans-serif;font-size:20px;font-weight:700;
  cursor:pointer;transition:all .3s cubic-bezier(.16,1,.3,1);display:flex;flex-direction:column;align-items:center;gap:8px;
}
.lo-btn:hover{border-color:var(--accent);background:var(--surface2);transform:translateY(-6px);box-shadow:0 15px 35px rgba(124,106,247,.25);}
.lo-btn span{font-family:'DM Mono',monospace;font-size:11px;color:var(--text2);}
.lo-btn.lo-primary{background:var(--accent);border-color:var(--accent2);box-shadow:0 8px 24px rgba(124,106,247,.3);}
.lo-btn.lo-primary:hover{background:var(--accent2);box-shadow:0 16px 40px rgba(124,106,247,.45);}
.lo-btn.lo-primary span{color:rgba(255,255,255,.7);}

/* === APP LAYOUT === */
.app{display:flex;height:100vh;width:100%;opacity:0;transition:opacity .7s ease;}
.app.visible{opacity:1;}

/* === SIDENAV === */
.sidenav{
  width:90px;height:100%;background:var(--ink2);border-right:1px solid var(--border);
  display:flex;flex-direction:column;align-items:center;padding:28px 0 24px;gap:12px;flex-shrink:0;z-index:10;
}
.nav-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:18px;color:var(--accent2);margin-bottom:20px;letter-spacing:-0.5px;}
.nav-item{
  width:58px;height:58px;border-radius:16px;display:flex;flex-direction:column;align-items:center;
  justify-content:center;cursor:pointer;transition:all .2s;color:var(--text2);border:1px solid transparent;
  position:relative;gap:4px;
}
.nav-item svg{width:22px;height:22px;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0;}
.nav-item .nav-lbl{font-family:'DM Mono',monospace;font-size:8.5px;letter-spacing:.3px;text-transform:uppercase;opacity:.7;}
.nav-item:hover{background:var(--surface);color:var(--text);}
.nav-item.active{background:linear-gradient(135deg,rgba(124,106,247,.3),rgba(124,106,247,.12));color:var(--accent2);border-color:rgba(124,106,247,.35);box-shadow:0 0 18px rgba(124,106,247,.2);}
.nav-tooltip{position:absolute;left:74px;background:var(--surface2);color:var(--text);font-size:12px;font-family:'DM Mono',monospace;padding:6px 12px;border-radius:7px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .15s;border:1px solid var(--border2);z-index:100;}
.nav-item:hover .nav-tooltip{opacity:1;}
.nav-spacer{flex:1;}

/* === VISUAL PANEL === */
.visual-panel{flex:1;height:100%;overflow-y:auto;background:var(--ink);position:relative;}
.visual-panel::-webkit-scrollbar{width:5px;}
.visual-panel::-webkit-scrollbar-thumb{background:var(--border2);border-radius:5px;}

/* === TRANSITION OVERLAY === */
.view-tr{position:fixed;top:0;left:90px;right:420px;bottom:0;background:var(--ink);z-index:999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .25s ease;}
.view-tr.active{opacity:1;pointer-events:all;}
.spinner{width:36px;height:36px;border:3px solid var(--border2);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;}
@keyframes spin{100%{transform:rotate(360deg);}}

/* === CHAT PANEL === */
.chat-panel{width:420px;height:100%;flex-shrink:0;background:var(--ink2);border-left:1px solid var(--border);display:flex;flex-direction:column;}
.chat-header{padding:20px 22px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:14px;flex-shrink:0;}
.chat-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--teal));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 4px 15px rgba(124,106,247,.3);}
.chat-name{font-family:'Syne',sans-serif;font-size:15px;font-weight:700;}
.chat-sub{font-size:11px;color:var(--green);font-family:'DM Mono',monospace;margin-top:3px;}
.chat-actions{margin-left:auto;display:flex;gap:8px;}
.chat-btn{background:none;border:1px solid var(--border2);color:var(--text2);font-size:11px;padding:7px 13px;border-radius:8px;cursor:pointer;font-family:'DM Mono',monospace;transition:all .2s;white-space:nowrap;}
.chat-btn:hover{border-color:var(--accent);background:var(--surface2);color:var(--text);}
.chat-btn.danger:hover{border-color:var(--coral);color:var(--coral);}
.chat-messages{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:18px;scroll-behavior:smooth;}
.chat-messages::-webkit-scrollbar{width:3px;}
.chat-messages::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px;}
.msg-row{display:flex;gap:10px;align-items:flex-end;animation:msg-in .3s ease-out;}
@keyframes msg-in{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
.msg-row.user{flex-direction:row-reverse;}
.msg-av{width:30px;height:30px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;}
.msg-av.ai{background:linear-gradient(135deg,var(--accent),var(--teal));}
.msg-av.user{background:var(--surface2);border:1px solid var(--border2);}
.msg-bubble{max-width:82%;padding:13px 17px;border-radius:18px;font-size:13.5px;line-height:1.65;}
.msg-bubble.ai{background:var(--surface);border:1px solid var(--border2);color:var(--text);border-bottom-left-radius:4px;}
.msg-bubble.user{background:var(--accent);color:white;border-bottom-right-radius:4px;}
.cursor-blink{display:inline-block;width:8px;height:15px;background:var(--accent2);margin-left:3px;animation:blink 1s step-end infinite;vertical-align:middle;border-radius:1px;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}
.chat-footer{padding:16px;border-top:1px solid var(--border);flex-shrink:0;}
.prompts-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;}
.prompt-btn{background:var(--surface);border:1px solid var(--border2);border-radius:12px;padding:13px 12px;font-size:13px;font-weight:500;color:var(--text2);cursor:pointer;transition:all .2s cubic-bezier(.16,1,.3,1);text-align:left;display:flex;align-items:center;gap:9px;box-shadow:0 2px 4px rgba(0,0,0,.1);}
.prompt-btn:hover{border-color:var(--accent);color:var(--text);background:var(--surface2);transform:translateY(-2px);box-shadow:0 5px 14px rgba(0,0,0,.2);}
.prompt-btn:disabled{opacity:.38;cursor:not-allowed;transform:none;box-shadow:none;}

/* === NOISE === */
.noise{position:fixed;inset:0;opacity:.025;pointer-events:none;z-index:100;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* === SHARED VIEW STYLES === */
.view-content{padding:60px 72px;min-height:100%;position:relative;}
.section-tag{display:inline-flex;align-items:center;gap:8px;font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);text-transform:uppercase;letter-spacing:2.5px;margin-bottom:20px;}
.section-tag::before{content:'◈';font-size:13px;}
.view-title{font-family:'Syne',sans-serif;font-size:46px;font-weight:800;letter-spacing:-1.5px;color:var(--text);margin-bottom:52px;line-height:1;}
.view-title span{color:var(--accent2);}
.subtle-div{height:1px;background:var(--border);margin:44px 0;}

/* === WELCOME VIEW === */
.welcome-eyebrow{display:flex;align-items:center;gap:10px;margin-bottom:28px;}
.status-dot{width:10px;height:10px;background:var(--green);border-radius:50%;box-shadow:0 0 10px var(--green);animation:pg 2s infinite;}
@keyframes pg{0%,100%{box-shadow:0 0 6px var(--green);}50%{box-shadow:0 0 20px var(--green);}}
.status-text{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--green);letter-spacing:1px;text-transform:uppercase;}
.welcome-name{font-family:'Syne',sans-serif;font-size:clamp(46px,5vw,80px);font-weight:800;line-height:.95;letter-spacing:-2.5px;margin-bottom:14px;}
.welcome-name .accent-word{color:var(--accent2);display:block;}
.welcome-role{font-size:18px;color:var(--text2);font-weight:300;margin-bottom:36px;font-style:italic;letter-spacing:.3px;}
.welcome-summary{font-size:15.5px;line-height:1.85;color:var(--text2);max-width:580px;margin-bottom:44px;border-left:3px solid var(--accent);padding-left:24px;}
.contact-row{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:48px;}
.contact-chip{display:flex;align-items:center;gap:8px;padding:9px 18px;background:var(--surface);border:1px solid var(--border2);border-radius:10px;font-size:12.5px;font-family:'DM Mono',monospace;color:var(--text2);transition:all .2s;cursor:default;}
.contact-chip:hover{border-color:var(--accent);color:var(--text);background:var(--surface2);}
.stat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;max-width:700px;margin-bottom:52px;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px 18px;position:relative;overflow:hidden;transition:transform .25s,box-shadow .25s;}
.stat-card:hover{transform:translateY(-3px);box-shadow:0 12px 25px rgba(0,0,0,.2);}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--accent),var(--teal));}
.stat-number{font-family:'Syne',sans-serif;font-size:34px;font-weight:800;color:var(--text);line-height:1;}
.stat-label{font-size:11px;color:var(--text2);margin-top:8px;text-transform:uppercase;letter-spacing:.7px;font-family:'DM Mono',monospace;}

/* === TIMELINE === */
.timeline{position:relative;padding-left:32px;}
.timeline::before{content:'';position:absolute;left:0;top:8px;bottom:8px;width:2px;background:linear-gradient(to bottom,var(--accent),transparent);}
.timeline-item{position:relative;margin-bottom:52px;}
.timeline-item::before{content:'';position:absolute;left:-38px;top:7px;width:12px;height:12px;border-radius:50%;background:var(--accent2);box-shadow:0 0 14px rgba(165,148,252,.5);}
.timeline-item.past::before{background:var(--text2);box-shadow:none;}
.tl-period{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--accent2);letter-spacing:1px;margin-bottom:10px;text-transform:uppercase;}
.tl-role{font-family:'Syne',sans-serif;font-size:22px;font-weight:700;margin-bottom:6px;}
.tl-company{font-size:14px;color:var(--text2);font-style:italic;margin-bottom:20px;}
.tl-bullets{list-style:none;display:flex;flex-direction:column;gap:13px;}
.tl-bullets li{font-size:14.5px;color:var(--text2);line-height:1.72;padding-left:22px;position:relative;}
.tl-bullets li::before{content:'→';position:absolute;left:0;color:var(--accent);font-weight:700;}
.tl-bullets li strong{color:var(--text);font-weight:500;}
.tl-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;}
.tl-tag{font-family:'DM Mono',monospace;font-size:10.5px;padding:4px 12px;border-radius:6px;background:rgba(124,106,247,.1);border:1px solid rgba(124,106,247,.25);color:var(--accent3);}

/* === PROJECTS === */
.projects-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;}
.project-card{background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:30px;transition:all .3s;position:relative;overflow:hidden;}
.project-card:hover{border-color:var(--accent);transform:translateY(-4px);box-shadow:0 22px 44px rgba(0,0,0,.32);}
.project-card.featured{grid-column:1/-1;display:grid;grid-template-columns:1fr 220px;gap:32px;align-items:start;}
.project-badge{font-family:'DM Mono',monospace;font-size:10.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;}
.badge-featured{background:rgba(240,192,96,.15);color:var(--gold);border:1px solid rgba(240,192,96,.3);}
.badge-active{background:rgba(82,209,138,.12);color:var(--green);border:1px solid rgba(82,209,138,.3);}
.badge-top20{background:rgba(255,123,107,.14);color:var(--coral);border:1px solid rgba(255,123,107,.3);}
.project-name{font-family:'Syne',sans-serif;font-size:26px;font-weight:700;margin:12px 0 8px;letter-spacing:-.5px;}
.project-sub{font-size:13px;color:var(--text2);font-style:italic;margin-bottom:16px;}
.project-desc{font-size:14.5px;color:var(--text2);line-height:1.75;margin-bottom:20px;}
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0;}
.info-item{background:var(--ink3);border-radius:10px;padding:11px 15px;border:1px solid var(--border);}
.info-lbl{font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:5px;}
.info-val{font-size:12.5px;color:var(--text);font-weight:500;line-height:1.45;}
.project-metrics{display:flex;gap:22px;margin:16px 0;padding:16px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);}
.metric-val{font-family:'Syne',sans-serif;font-size:24px;font-weight:700;color:var(--accent2);}
.metric-lbl{font-size:9.5px;color:var(--text2);text-transform:uppercase;letter-spacing:.6px;margin-top:4px;font-family:'DM Mono',monospace;}
.tech-stack{display:flex;flex-wrap:wrap;gap:7px;}
.tech-pill{font-family:'DM Mono',monospace;font-size:10.5px;padding:4px 12px;border-radius:6px;background:var(--ink3);border:1px solid var(--border2);color:var(--text2);}

/* Chart containers in project */
.proj-chart-wrap{background:var(--ink3);border-radius:16px;border:1px solid var(--border);padding:20px;margin:16px 0;}
.proj-chart-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:14px;}

/* === SKILLS === */
.skills-layout{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
.skill-group{margin-bottom:30px;}
.skill-group-label{font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);text-transform:uppercase;letter-spacing:2px;margin-bottom:16px;}
.skill-bar-item{margin-bottom:15px;}
.skill-bar-header{display:flex;justify-content:space-between;margin-bottom:8px;}
.skill-bar-name{font-size:14px;font-weight:500;}
.skill-bar-pct{font-family:'DM Mono',monospace;font-size:12px;color:var(--text2);}
.skill-bar-track{height:6px;background:var(--surface2);border-radius:3px;overflow:hidden;}
.skill-bar-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--teal));transform-origin:left;transform:scaleX(0);transition:transform .85s cubic-bezier(.16,1,.3,1);}
.skill-bar-fill.animate{transform:scaleX(1);}
.cert-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:15px 18px;margin-bottom:10px;display:flex;align-items:center;gap:14px;transition:transform .2s,border-color .2s;}
.cert-card:hover{transform:translateX(4px);border-color:var(--accent2);}
.skills-chart-wrap{background:var(--ink3);border-radius:16px;border:1px solid var(--border);padding:20px;margin-bottom:24px;}

/* === EDUCATION === */
.edu-hero{background:linear-gradient(135deg,var(--surface),var(--surface2));border:1px solid var(--border);border-radius:24px;padding:40px;margin-bottom:28px;position:relative;overflow:hidden;}
.edu-hero::before{content:'UEH';position:absolute;right:-15px;bottom:-45px;font-family:'Syne',sans-serif;font-size:180px;font-weight:800;color:rgba(255,255,255,.025);line-height:1;pointer-events:none;user-select:none;}
.gpa-badge{display:inline-flex;align-items:center;gap:14px;background:rgba(240,192,96,.1);border:1px solid rgba(240,192,96,.3);border-radius:16px;padding:16px 24px;margin-top:18px;}
.gpa-val{font-family:'Syne',sans-serif;font-size:30px;font-weight:800;color:var(--gold);}

/* === ANIMATIONS === */
.fade-up{animation:fadeUp .6s ease-out forwards;opacity:0;}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px);}to{opacity:1;transform:translateY(0);}}
.d1{animation-delay:.1s}.d2{animation-delay:.2s}.d3{animation-delay:.3s}.d4{animation-delay:.4s}.d5{animation-delay:.5s}.d6{animation-delay:.6s}

/* === RESPONSIVE === */
@media(max-width:1200px){
  .chat-panel{width:360px;}
  .view-tr{right:360px;}
  .view-content{padding:44px 48px;}
  .stat-grid{grid-template-columns:repeat(2,1fr);}
  .skills-layout{grid-template-columns:1fr;gap:24px;}
}
@media(max-width:900px){
  .chat-panel{display:none;}
  .view-tr{left:72px;right:0;}
  .projects-grid{grid-template-columns:1fr;}
  .project-card.featured{grid-template-columns:1fr;}
  #scroll-progress{left:72px;}
  .sidenav{width:72px;}
  .nav-item{width:46px;height:46px;}
}
</style>
</head>
<body>
<div class="noise"></div>
<div id="scroll-progress"></div>

<!-- ======== LANGUAGE OVERLAY ======== -->
<div id="lang-overlay">
  <div style="text-align:center;">
    <div class="lo-logo">hwinh</div>
    <div class="lo-tagline" style="margin-top:10px;">AI Portfolio · Product &amp; UX</div>
  </div>
  <div class="lo-question">Choose your language<br><span style="font-size:18px;color:var(--text2);font-weight:400;">Chọn ngôn ngữ hiển thị</span></div>
  <div class="lo-options">
    <button class="lo-btn lo-primary" onclick="selectLang('en')">
      English
      <span>For Global Recruiters</span>
    </button>
    <button class="lo-btn" onclick="selectLang('vi')">
      Tiếng Việt
      <span>Dành cho NTD trong nước</span>
    </button>
  </div>
</div>

<!-- ======== MAIN APP ======== -->
<div class="app" id="main-app">

  <!-- SIDENAV -->
  <nav class="sidenav">
    <div class="nav-logo">HM</div>
    <div class="nav-item active" data-view="welcome" onclick="go('welcome',this)">
      <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      <span class="nav-lbl" id="nl0">Home</span>
      <span class="nav-tooltip" id="ntt0">Overview</span>
    </div>
    <div class="nav-item" data-view="experience" onclick="go('experience',this)">
      <svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
      <span class="nav-lbl" id="nl1">Career</span>
      <span class="nav-tooltip" id="ntt1">Experience</span>
    </div>
    <div class="nav-item" data-view="projects" onclick="go('projects',this)">
      <svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
      <span class="nav-lbl" id="nl2">Work</span>
      <span class="nav-tooltip" id="ntt2">Projects</span>
    </div>
    <div class="nav-item" data-view="skills" onclick="go('skills',this)">
      <svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
      <span class="nav-lbl" id="nl3">Skills</span>
      <span class="nav-tooltip" id="ntt3">Skills</span>
    </div>
    <div class="nav-item" data-view="education" onclick="go('education',this)">
      <svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
      <span class="nav-lbl" id="nl4">School</span>
      <span class="nav-tooltip" id="ntt4">Education</span>
    </div>
    <div class="nav-spacer"></div>
  </nav>

  <!-- VISUAL PANEL -->
  <main class="visual-panel" id="visual-panel">
    <div class="view-tr" id="view-tr"><div class="spinner"></div></div>

    <!-- ===== WELCOME ===== -->
    <div id="view-welcome" class="view-content">
      <div class="welcome-eyebrow fade-up">
        <div class="status-dot"></div>
        <span class="status-text" id="w-status">Available for Product &amp; UX opportunities · HCMC</span>
      </div>
      <h1 class="welcome-name fade-up d1">Nguyễn<span class="accent-word">Hoàng Minh</span></h1>
      <p class="welcome-role fade-up d2" id="w-role">Product Owner · UX Strategist · AI Builder</p>
      <p class="welcome-summary fade-up d3" id="w-summary"></p>
      <div class="contact-row fade-up d4">
        <div class="contact-chip">✉ hwinh.work@gmail.com</div>
        <div class="contact-chip">📞 +84 765 828 191</div>
        <div class="contact-chip">📍 Hồ Chí Minh</div>
        <div class="contact-chip">🎓 UEH · GPA 3.53/4.0</div>
      </div>
      <div class="stat-grid fade-up d5">
        <div class="stat-card"><div class="stat-number">2+</div><div class="stat-label" id="ws1">Years Exp.</div></div>
        <div class="stat-card"><div class="stat-number">150+</div><div class="stat-label" id="ws2">Stakeholders</div></div>
        <div class="stat-card"><div class="stat-number">72%</div><div class="stat-label" id="ws3">AI ROI Achieved</div></div>
        <div class="stat-card"><div class="stat-number">Top 20</div><div class="stat-label" id="ws4">City Finalist</div></div>
      </div>
      <div class="subtle-div fade-up"></div>
      <div class="section-tag fade-up d6" id="w-explore">Explore this portfolio</div>
      <p class="fade-up d6" style="font-size:14px;color:var(--text2);line-height:1.8;max-width:500px;margin-top:8px;" id="w-hint"></p>
    </div>

    <!-- ===== EXPERIENCE ===== -->
    <div id="view-experience" class="view-content" style="display:none">
      <div class="section-tag" id="e-tag">Work History</div>
      <h2 class="view-title" id="e-title">Work <span>Experience</span></h2>
      <div class="timeline" id="e-timeline"></div>
    </div>

    <!-- ===== PROJECTS ===== -->
    <div id="view-projects" class="view-content" style="display:none">
      <div class="section-tag" id="p-tag">Product Experience</div>
      <h2 class="view-title" id="p-title">Featured <span>Projects</span></h2>
      <div class="projects-grid" id="p-grid"></div>
    </div>

    <!-- ===== SKILLS ===== -->
    <div id="view-skills" class="view-content" style="display:none">
      <div class="section-tag" id="s-tag">Competencies</div>
      <h2 class="view-title" id="s-title">Professional <span>Skills</span></h2>
      <div class="skills-layout">
        <div id="s-bars"></div>
        <div>
          <div class="skills-chart-wrap">
            <div class="proj-chart-title" id="s-radar-lbl">Skill Radar</div>
            <div style="height:280px;position:relative;"><canvas id="skillsChart"></canvas></div>
          </div>
          <div class="proj-chart-title" id="s-cert-lbl">Certifications</div>
          <div id="s-certs"></div>
        </div>
      </div>
    </div>

    <!-- ===== EDUCATION ===== -->
    <div id="view-education" class="view-content" style="display:none">
      <div class="section-tag" id="ed-tag">Academic Background</div>
      <h2 class="view-title" id="ed-title">Education &amp; <span>Awards</span></h2>
      <div class="edu-hero">
        <div style="font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);letter-spacing:1px;margin-bottom:14px;">AUG 2022 — AUG 2026</div>
        <h3 style="font-family:'Syne',sans-serif;font-size:26px;font-weight:800;color:var(--text);margin-bottom:6px;" id="ed-uni">University of Economics HCMC (UEH)</h3>
        <p style="color:var(--text2);font-size:15px;margin-bottom:20px;" id="ed-major">Bachelor of Technology &amp; Innovation Management</p>
        <div class="gpa-badge">
          <span style="font-size:26px;">🏆</span>
          <div>
            <div style="font-size:11px;color:var(--text2);margin-bottom:3px;">Grade Point Average</div>
            <div class="gpa-val">3.53 / 4.0</div>
          </div>
        </div>
      </div>
      <div id="ed-courses"></div>
      <div class="subtle-div"></div>
      <div class="proj-chart-title" id="ed-cert-lbl">Certifications</div>
      <div id="ed-certs"></div>
    </div>
  </main>

  <!-- CHAT PANEL -->
  <aside class="chat-panel">
    <div class="chat-header">
      <div class="chat-avatar">🤖</div>
      <div>
        <div class="chat-name" id="c-name">Minh's AI Assistant</div>
        <div class="chat-sub" id="c-sub">● Online · Ready to answer</div>
      </div>
      <div class="chat-actions">
        <button class="chat-btn" onclick="resetChat()" id="c-reset">↺ Reset</button>
        <button class="chat-btn danger" onclick="logout()" id="c-logout">⏻ Lang</button>
      </div>
    </div>
    <div class="chat-messages" id="chat-messages"></div>
    <div class="chat-footer"><div class="prompts-grid" id="prompts-grid"></div></div>
  </aside>
</div>

<script>
// ============================================================
// DATA
// ============================================================
const T = {
en:{
  nav:['Home','Career','Work','Skills','School'],
  navTip:['Overview','Experience','Projects','Skills','Education'],
  w:{
    status:'Available for Product & UX opportunities · HCMC, Vietnam',
    role:'Product Owner · UX Strategist · AI Builder',
    summary:`Young professional in <strong style="color:var(--text)">Technology & Innovation Management</strong> — operating at the intersection of UX Design, System Thinking, and AI Engineering. I turn messy user data and tangled pain points into clean, measurable product experiences. Whether it's mapping a startup's entire onboarding journey or leading an AI project from a blank canvas to a working Transformer model, I believe the best products are built when deep empathy meets rigorous systems thinking.`,
    stats:['Years Exp.','Stakeholders Managed','AI Tech. ROI','City-level Finalist'],
    explore:'Explore this portfolio',
    hint:'Use the sidebar or chat with the AI Assistant on the right to dive into experience, projects, and skills in full detail.'
  },
  exp:{
    tag:'Work History',title:'Work <span>Experience</span>',
    items:[
      {
        period:'JAN 2025 — OCT 2025 · CURRENT',
        role:'Project Management Executive',
        company:'Startup & Innovation Hub of HCMC (SIHUB) · Under Dept. of Science & Technology HCMC',
        bullets:[
          `<strong>End-to-End Customer Journey Mapping & MVP Delivery:</strong> Designed the complete digital journey for tech startups from first touchpoint to activation — functioning as both an onboarding flow and a performance baseline. Translated messy founder frustrations into structured User Stories and delivered MVPs iteratively, reducing time-to-first-value for startups in the incubation program.`,
          `<strong>Data-Driven Pain Point Resolution:</strong> Continuously monitored omnichannel touchpoints to surface operational bottlenecks. Deployed A/B testing and Interleaving experiments to rigorously evaluate feature iterations — ensuring every product change was backed by behavioral evidence, not gut feeling. Resolved several high-friction activation blockers before full-scale rollout.`,
          `<strong>Stakeholder Management & NPS Intelligence:</strong> Acted as the central liaison for 150+ startup founders, managing communication across all stages of the incubation journey. Analyzed behavioral data to build NPS dashboards, presenting actionable retention insights directly to the Board of Directors. Helped shift the team's mindset from treating NPS as a single score to understanding it as a real-time behavioral signal system.`
        ],
        tags:['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Stakeholder Management (150+)','URD Documentation']
      },
      {
        period:'JUL 2024 — DEC 2024',
        role:'Research & Development Intern',
        company:'SIHUB · Executed data-driven project management for a city-level scientific competency framework',
        bullets:[
          `<strong>Large-Scale Data Analysis & Requirements Gathering:</strong> Led the end-to-end data lifecycle for a city-level competency gap analysis project involving 150+ key stakeholders — including government officials, research institutes, and corporate partners. Designed the data collection methodology, cleaned raw qualitative inputs, and extracted structured insights that directly shaped the final policy recommendations.`,
          `<strong>URD-Standard Structured Documentation:</strong> Authored comprehensive strategic reports and system requirement documents aligned with URD (User Requirements Document) standards. The challenge was bridging the gap between qualitative user feedback and concrete system requirements — a skill that directly informed how I later approached PRD writing and user story creation in product roles.`
        ],
        tags:['Data Lifecycle Management','Competency Gap Analysis','150+ Stakeholders','URD Standards','Requirements Engineering','Strategic Reporting']
      }
    ]
  },
  proj:{
    tag:'Product Experience',title:'Featured <span>Projects</span>',
    items:[
      {
        id:'echomind',badge:'★ Flagship AI Project',bClass:'badge-featured',date:'Sep — Dec 2025',
        name:'EchoMind AI',sub:'Non-Invasive Brain-to-Text System · Project Lead · MindConnect Labs · UEH Course: Project AI',
        desc:`EchoMind started with a human problem: patients with stroke, ALS, or TBI who are fully conscious but completely locked inside their bodies — unable to speak, unable to move, unable to tell the person next to them what they need. Traditional AAC (Augmentative & Alternative Communication) devices offer a workaround, but they're slow (25–30 WPM), laggy (3–5s), and achieve only 35–40% session success. We wanted to do better.\n\nAs <strong style="color:var(--text)">Project Lead</strong>, I managed the full AI product lifecycle using the <strong style="color:var(--text)">CPMAI 6-phase framework</strong> combined with 8 Agile Sprints and a RACI matrix for a 7-member team (3,833.5 total hours tracked). The technical journey was humbling: our first model — a Seq2Seq LSTM — collapsed into Mode Collapse, endlessly repeating "you you you..." regardless of input. The root cause was an information bottleneck: the LSTM was trying to compress an entire EEG sequence (hundreds of timesteps) into a single context vector. It couldn't hold that much.\n\nThe pivot to <strong style="color:var(--text)">Transformer V2</strong> (Multi-Head Attention, 8 heads, Positional Encoding, Label Smoothing ε=0.1, LR=0.00005) solved the bottleneck by letting the decoder attend directly to all encoder states at every decoding step. The results spoke: <strong style="color:var(--text)">55–65 WPM, &lt;1s latency, 92–95% accuracy, 72% Technical ROI</strong> vs traditional AAC. We also designed an Expert Dashboard with Attention Maps — so the black-box problem in healthcare could be addressed: doctors can see which brain regions the model focused on when decoding each word.`,
        info:[
          {l:'Final Architecture',v:'Transformer V2 · 8-head Multi-Head Attention · Positional Encoding · Label Smoothing ε=0.1'},
          {l:'Baseline vs Final',v:'Seq2Seq LSTM (Mode Collapse, WER ~85–90%) → Transformer V2 (Structured output, 6–7/10 correct)'},
          {l:'Dataset',v:'Brain-to-Text \'25 (Kaggle) · 256-channel non-invasive EEG · HDF5 format · avg 6.38 words/sentence'},
          {l:'PM Framework',v:'CPMAI 6-phase · 8 Agile Sprints · RACI Matrix · 3,833.5 total hours · 100% milestone completion'}
        ],
        metrics:[{v:'55–65',l:'WPM Output'},{v:'<1s',l:'Latency'},{v:'72%',l:'Technical ROI'},{v:'92–95%',l:'Accuracy'},{v:'6–7/10',l:'Sentences Correct'},{v:'100%',l:'Milestone'}],
        tech:['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','RACI Matrix','Agile/Scrum']
      },
      {
        id:'ereader',badge:'🏆 Top 20 Finalist',bClass:'badge-top20',date:'Mar — Jun 2025',
        name:'E-Reader Ecosystem',sub:'Product Lead · HCMC Digital Education · Directed by HCMC People\'s Committee',
        desc:`The brief was broad: design a digital education ecosystem for student e-reading devices. But beneath the surface, the real challenge was about cognitive friction — students were dropping off during the activation phase because the journey from "I received this device" to "I'm actually learning on it" was full of unnecessary obstacles.\n\nI applied <strong style="color:var(--text)">HCI (Human-Computer Interaction)</strong> principles systematically: mapped the full student journey from device provisioning and registration through content onboarding to daily use and content updates. For each stage, I ran a pain point decomposition — breaking down where cognitive load spikes, where confusion sets in, and where students give up. This translated into structured feature sets with clear User Stories, each tied to a specific friction point with a measurable success criterion.\n\nThe result was a cohesive ecosystem design where every touchpoint spoke the same language. The project was recognised as a <strong style="color:var(--text)">Top 20 Finalist</strong> at the HCMC People's Committee city-level digital education competition.`,
        tech:['HCI Principles','UX Design','Journey Mapping','Problem Decomposition','User Stories','Cognitive Load Analysis','Figma Prototyping']
      },
      {
        id:'events',badge:'● Ongoing',bClass:'badge-active',date:'Jul 2024 — Present',
        name:'Innovation Events Operations',sub:'Operations · SIHUB Startup Ecosystem · HCMC',
        desc:`Directly organized and operated two of HCMC's major city-level innovation events: <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> (flagship university startup competition) and <strong style="color:var(--text)">WHISE Week 2024</strong> (HCMC Innovation Week). Responsibilities spanned end-to-end event operations, cross-team coordination between SIHUB departments and external partners, real-time stakeholder communication with startup founders, investors, and government representatives, and on-ground experience quality management.`,
        tech:['Event Management','Cross-team Coordination','Stakeholder Communication','Operations Planning']
      }
    ]
  },
  skills:{
    tag:'Competencies',title:'Professional <span>Skills</span>',
    radarLbl:'Skill Radar Overview',certLbl:'Certifications',
    groups:[
      {name:'Product Management',items:[
        {n:'Customer Journey Mapping',p:95},{n:'UX / HCI Design',p:90},{n:'Agile / Scrum (CPMAI)',p:88},
        {n:'PRD & User Stories Writing',p:85},{n:'A/B Testing & Interleaving',p:82},{n:'Problem Decomposition',p:88}
      ]},
      {name:'Data & Engineering',items:[
        {n:'Python',p:80},{n:'Data Analysis & EDA',p:80},{n:'PyTorch / Deep Learning',p:72}
      ]}
    ],
    radarLabels:['UX/HCI','Agile','Journey Map','Data Analysis','Python','PyTorch/ML','A/B Testing'],
    certs:[
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false},
      {i:'🔄',n:'Agile Management Certification',org:'Professional Certification',dash:false},
    ]
  },
  edu:{
    tag:'Academic Background',title:'Education & <span>Awards</span>',
    uni:'University of Economics HCMC (UEH)',major:'Bachelor of Technology & Innovation Management',
    courseTag:'Relevant Coursework',
    courses:['Design Thinking','Human-Computer Interaction (HCI)','Innovation Management','Business Intelligence','Digital Business Transformation','Project AI'],
    certTag:'Certifications',
    certs:[
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false},
      {i:'🔄',n:'Agile Management Certification',org:'Professional Certification',dash:false},
    ]
  },
  chat:{
    name:"Minh's AI Assistant",sub:'● Online · Ready to answer',reset:'↺ Reset',logout:'⏻ Lang',
    greeting:`Hello! I'm the AI representing Nguyen Hoang Minh — a Product Owner & UX Strategist building at the intersection of user experience design, systems thinking, and AI engineering.\n\nMinh is actively seeking Product and UX roles where deep user empathy meets rigorous product execution. What would you like to know about him?`,
    prompts:[
      {id:'exp',i:'💼',l:'Experience'},
      {id:'proj',i:'🧠',l:'Projects'},
      {id:'skills',i:'⚡',l:'Skills'},
      {id:'edu',i:'🎓',l:'Education'}
    ],
    ans:{
      exp:`Minh has 2+ years at SIHUB — the Startup & Innovation Hub under HCMC's Department of Science & Technology.\n\n◈ Jan–Oct 2025 | Project Management Executive\nMinh designed end-to-end digital journey maps for tech startups, treating them not just as UX artifacts but as operational systems with activation flows, friction checkpoints, and conversion metrics. He managed 150+ startup founders as the central touchpoint, running A/B tests and Interleaving experiments to validate every feature change before rollout. His approach to NPS: not a single score, but a real-time behavioral signal system reported to the Board.\n\n◈ Jul–Dec 2024 | R&D Intern\nLed competency gap analysis for 150+ stakeholders in a city-level scientific framework project. Authored URD-standard documentation that bridged qualitative user insights with concrete system requirements — a skill that directly shaped his later PRD writing approach.`,
      proj:`Minh has three standout projects that together tell the story of someone who can think across the full product stack:\n\n🧠 EchoMind AI — Flagship (Sep–Dec 2025)\nBCI system decoding 256-channel EEG into text. As Project Lead: managed 8 Agile Sprints under CPMAI, diagnosed and pivoted from LSTM Mode Collapse to Transformer V2 (Multi-Head Attention + Label Smoothing). Final results: 55–65 WPM, <1s latency, 72% Technical ROI. Also designed an Expert Dashboard with Attention Maps to address healthcare's black-box problem.\n\n📚 E-Reader Ecosystem — Top 20 City Level (Mar–Jun 2025)\nHCI-focused user journey design from device provisioning to content updates. Decomposed student cognitive friction into feature sets. Top 20 at HCMC People's Committee competition.\n\n🚀 Innovation Events Operations — Ongoing\nOrganized Univ.Star 2024/2025 and WHISE Week 2024 at SIHUB.`,
      skills:`Minh's competency profile is built across 3 pillars:\n\n◈ Product Craft (Core Strength)\n→ Journey Mapping 95% · UX/HCI 90% · Agile/CPMAI 88%\n→ PRD & User Stories · A/B Testing & Interleaving · Problem Decomposition\n→ RACI Matrix · Burndown Tracking · Design Thinking\n\n◈ Data & Systems Thinking\n→ Python · Data Analysis & EDA · Google Colab\n→ PyTorch · Feature Engineering · WER Metrics\n→ Transformer architecture (applied in EchoMind)\n\n◈ Stakeholder & Execution\n→ 150+ stakeholder management at city/government level\n→ Strategic documentation to Board level\n→ Led 7-member cross-functional team across 8 Sprints`,
      edu:`Minh is finishing his final year at UEH (University of Economics HCMC), majoring in Technology & Innovation Management. GPA: 3.53/4.0.\n\nKey coursework directly applied to his product work:\n→ Human-Computer Interaction (HCI) — the foundation of his UX approach\n→ Design Thinking — how he frames product problems\n→ Business Intelligence — how he reads data as product signals\n→ Project AI — where EchoMind was born\n\nCertifications: Google Project Management · Google Business Intelligence · Agile Management\n\nCurrently preparing for TOEIC to expand into international product opportunities.`
    }
  }
},

vi:{
  nav:['Tổng quan','Kinh nghiệm','Dự án','Kỹ năng','Học vấn'],
  navTip:['Tổng quan','Kinh nghiệm','Dự án','Kỹ năng','Học vấn'],
  w:{
    status:'Sẵn sàng đón nhận cơ hội Product & UX mới · TP.HCM',
    role:'Product Owner · UX Strategist · AI Builder',
    summary:`Hoàng Minh là một ứng viên trẻ về <strong style="color:var(--text)">Quản lý Công nghệ & Đổi mới Sáng tạo</strong> — có nền và kiến thức của UX Design, System Thinking và AI Engineering. Tôi chuyển hóa dữ liệu người dùng phức tạp và các "điểm đau" (pain points) thành trải nghiệm sản phẩm, có thể đo lường. Từ việc lập bản đồ hành trình onboarding cho startup đến dẫn dắt một dự án AI từ tờ giấy trắng đến mô hình Transformer hoạt động được — tôi tin sản phẩm tốt nhất được tạo ra khi sự đồng cảm sâu sắc gặp tư duy hệ thống chặt chẽ.`,
    stats:['Năm kinh nghiệm','Stakeholders quản lý','ROI kỹ thuật AI','Chung cuộc cấp TP'],
    explore:'Khám phá hồ sơ này',
    hint:'Dùng thanh điều hướng hoặc chat với AI Assistant bên phải để khám phá kinh nghiệm, dự án và kỹ năng chi tiết.'
  },
  exp:{
    tag:'Lịch sử làm việc',title:'Kinh nghiệm <span>Làm việc</span>',
    items:[
      {
        period:'01/2025 — 10/2025 · HIỆN TẠI',
        role:'Chuyên viên Quản lý Dự án (Project Management Executive)',
        company:'Trung tâm Hỗ trợ Khởi nghiệp & Đổi mới Sáng tạo TP.HCM (SIHUB) · Trực thuộc Sở KH&CN',
        bullets:[
          `<strong>Lập bản đồ Hành trình Khách hàng & Triển khai MVP:</strong> Thiết kế hành trình số (digital journey map) nhằm hỗ trợ cho các startup công nghệ tại SIHUB. Cùng các Startup tìm kiếm "nỗi đau" của khách hàng và đưa nó thành User Stories có cấu trúc, triển khai MVP theo từng vòng lặp, và giúp rút ngắn đáng kể time-to-first-value cho các startup trong chương trình ươm tạo.`,
          `<strong>Giải quyết Pain Point dựa trên Dữ liệu:</strong> Liên tục theo dõi các touchpoints đa kênh để phát hiện điểm nghẽn vận hành. Hỗ trợ áp dụng A/B testing và Interleaving experiments để kiểm chứng chặt chẽ các thay đổi tính năng cho các Startup, nhằm đảm bảo mọi quyết định sản phẩm đều có giá trị, không phải cảm tính.`,
          `<strong>Quản lý Stakeholder & Hệ thống NPS:</strong> Làm đầu mối trung tâm cho 5+ startup founders xuyên suốt hành trình ươm tạo. Phân tích dữ liệu hành vi để xây dựng dashboard NPS, trình bày insights về giữ chân người dùng trực tiếp lên Ban Giám đốc. Giúp nhóm chuyển tư duy từ NPS là một con số thành NPS là hệ thống tín hiệu hành vi real-time.`
        ],
        tags:['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Quản lý 150+ Stakeholders','Tài liệu URD']
      },
      {
        period:'07/2024 — 12/2024',
        role:'Thực tập sinh Nghiên cứu & Phát triển (R&D Intern)',
        company:'SIHUB · Quản lý dự án dựa trên dữ liệu cho khung năng lực cấp thành phố',
        bullets:[
          `<strong>Phân tích Dữ liệu Quy mô Lớn & Lấy Yêu cầu:</strong> Dẫn dắt vòng đời dữ liệu (end-to-end) cho dự án phân tích khoảng trống năng lực trong bài nghiên cứu khoa học cấp thành phố — làm việc với 150+ stakeholders chủ chốt bao gồm cơ quan nhà nước, viện nghiên cứu và doanh nghiệp. Thiết kế phương pháp thu thập dữ liệu, làm sạch đầu vào định tính và trích xuất insights để định hình khuyến nghị chính sách cuối cùng.`,
          `<strong>Tài liệu hóa Chuẩn URD:</strong> Soạn thảo báo cáo chiến lược và tài liệu yêu cầu hệ thống theo chuẩn URD. Thách thức cốt lõi là kết nối phản hồi định tính của người dùng với yêu cầu hệ thống cụ thể — kỹ năng này trực tiếp định hình cách Minh viết PRD và User Stories sau này.`
        ],
        tags:['Quản lý Vòng đời Dữ liệu','Phân tích Khoảng trống Năng lực','150+ Stakeholders','Chuẩn URD','Kỹ thuật Yêu cầu']
      }
    ]
  },
  proj:{
    tag:'Kinh nghiệm Sản phẩm',title:'Dự án <span>Nổi bật</span>',
    items:[
      {
        id:'echomind',badge:'★ Dự án AI Trọng điểm',bClass:'badge-featured',date:'Tháng 9 — 12/2025',
        name:'EchoMind AI',sub:'Hệ thống Não-Chữ Phi Xâm Lấn · Project Lead · MindConnect Labs · Môn Dự án AI - UEH',
        desc:`EchoMind bắt đầu từ một vấn đề mang tính nhân văn sâu sắc: những bệnh nhân đột quỵ, ALS, hoặc chấn thương sọ não — hoàn toàn tỉnh táo nhưng bị nhốt trong cơ thể mình, không thể nói, không thể cử động, không thể nói với người bên cạnh rằng họ đang cần gì. Các thiết bị AAC (Augmentative & Alternative Communication) truyền thống chỉ đạt 25–30 WPM, độ trễ 3–5s và tỷ lệ thành công 35–40%. Chúng tôi muốn làm tốt hơn.\n\nVới vai trò <strong style="color:var(--text)">Project Lead</strong>, Minh quản lý toàn bộ vòng đời sản phẩm AI theo <strong style="color:var(--text)">khung CPMAI 6 pha</strong> kết hợp 8 Agile Sprints và ma trận RACI cho nhóm 7 người (3.833,5 tổng giờ được theo dõi). Hành trình kỹ thuật không phải lúc nào cũng bằng phẳng: mô hình baseline Seq2Seq LSTM sụp đổ hoàn toàn vào Mode Collapse — lặp đi lặp lại "you you you..." bất kể đầu vào là gì. Nguyên nhân gốc rễ: nút thắt cổ chai thông tin — LSTM phải nén toàn bộ chuỗi EEG vào một vector bối cảnh duy nhất, và nó không chứa nổi.\n\nQuyết định chuyển sang <strong style="color:var(--text)">Transformer V2</strong> (Multi-Head Attention 8 đầu, Positional Encoding, Label Smoothing ε=0.1, LR=0.00005) giải quyết triệt để bằng cách cho phép decoder "nhìn" trực tiếp vào toàn bộ encoder states tại mỗi bước giải mã. Kết quả: <strong style="color:var(--text)">55–65 WPM, độ trễ &lt;1s, chính xác 92–95%, ROI kỹ thuật 72%</strong>. Nhóm cũng thiết kế Expert Dashboard với Attention Maps — để giải quyết vấn đề "hộp đen" trong y tế.`,
        info:[
          {l:'Kiến trúc cuối',v:'Transformer V2 · 8-head Multi-Head Attention · Positional Encoding · Label Smoothing ε=0.1'},
          {l:'Baseline vs Cuối',v:'Seq2Seq LSTM (Mode Collapse, WER ~85–90%) → Transformer V2 (Câu có cấu trúc, 6–7/10 đúng)'},
          {l:'Bộ dữ liệu',v:'Brain-to-Text \'25 (Kaggle) · EEG phi xâm lấn 256 kênh · Định dạng HDF5 · Trung bình 6,38 từ/câu'},
          {l:'Khung quản lý',v:'CPMAI 6 pha · 8 Agile Sprints · Ma trận RACI · 3.833,5 tổng giờ · 100% milestone hoàn thành'}
        ],
        metrics:[{v:'55–65',l:'Từ/phút'},{v:'<1s',l:'Độ trễ'},{v:'72%',l:'ROI kỹ thuật'},{v:'92–95%',l:'Độ chính xác'},{v:'6–7/10',l:'Câu đúng'},{v:'100%',l:'Milestone'}],
        tech:['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','Ma trận RACI','Agile/Scrum']
      },
      {
        id:'ereader',badge:'🏆 Top 20 Chung cuộc',bClass:'badge-top20',date:'Tháng 3 — 6/2025',
        name:'Hệ sinh thái E-Reader',sub:'Product Lead · Giáo dục Số TP.HCM · Chỉ đạo bởi UBND TP.HCM',
        desc:`Bài toán ban đầu rộng: thiết kế hệ sinh thái giáo dục số cho thiết bị e-reading học sinh. Nhưng ẩn sau đó là thách thức thực sự: học sinh bỏ dở ở giai đoạn activation vì hành trình từ "tôi nhận được thiết bị này" đến "tôi đang thực sự học trên đó" đầy rào cản không cần thiết.\n\nMinh áp dụng hệ thống <strong style="color:var(--text)">nguyên tắc HCI</strong>: lập bản đồ toàn bộ hành trình học sinh từ cấp phát thiết bị, đăng ký, onboarding nội dung đến sử dụng hằng ngày và cập nhật. Tại mỗi giai đoạn, chạy phân tích pain point — xác định nơi cognitive load tăng đột biến, nơi nhầm lẫn xuất hiện, nơi học sinh bỏ cuộc. Kết quả là các bộ tính năng có cấu trúc với User Stories rõ ràng, mỗi cái gắn với một điểm ma sát cụ thể và tiêu chí thành công đo lường được.\n\nKết quả được ghi nhận là <strong style="color:var(--text)">Top 20 Chung cuộc</strong> cuộc thi giáo dục số cấp thành phố do UBND TP.HCM chỉ đạo.`,
        tech:['Nguyên tắc HCI','Thiết kế UX','Journey Mapping','Phân tích Pain Point','User Stories','Phân tích Cognitive Load','Figma Prototyping']
      },
      {
        id:'events',badge:'● Đang diễn ra',bClass:'badge-active',date:'Tháng 7/2024 — Hiện tại',
        name:'Vận hành Sự kiện Đổi mới Sáng tạo',sub:'Vận hành · Hệ sinh thái Startup SIHUB · TP.HCM',
        desc:`Trực tiếp tổ chức và vận hành hai sự kiện đổi mới sáng tạo lớn cấp thành phố: <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> (cuộc thi startup sinh viên flagship) và <strong style="color:var(--text)">Tuần lễ WHISE 2024</strong> (Tuần lễ Đổi mới Sáng tạo TP.HCM). Phạm vi bao gồm vận hành sự kiện end-to-end, phối hợp cross-team giữa các phòng ban SIHUB và đối tác bên ngoài, giao tiếp stakeholders real-time với startup founders, nhà đầu tư và đại diện chính quyền, và quản lý chất lượng trải nghiệm tại chỗ.`,
        tech:['Quản lý Sự kiện','Phối hợp Cross-team','Giao tiếp Stakeholder','Lập kế hoạch Vận hành']
      }
    ]
  },
  skills:{
    tag:'Năng lực Lõi',title:'Kỹ năng <span>Chuyên môn</span>',
    radarLbl:'Biểu đồ Radar Kỹ năng',certLbl:'Chứng chỉ',
    groups:[
      {name:'Product Management',items:[
        {n:'Customer Journey Mapping',p:95},{n:'Thiết kế UX / HCI',p:90},{n:'Agile / Scrum (CPMAI)',p:88},
        {n:'Viết PRD & User Stories',p:85},{n:'A/B Testing & Interleaving',p:82},{n:'Problem Decomposition',p:88}
      ]},
      {name:'Dữ liệu & Kỹ thuật',items:[
        {n:'Python',p:80},{n:'Phân tích Dữ liệu & EDA',p:80},{n:'PyTorch / Deep Learning',p:72}
      ]}
    ],
    radarLabels:['UX/HCI','Agile','Journey Map','Phân tích DL','Python','PyTorch/ML','A/B Testing'],
    certs:[
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false},
      {i:'🔄',n:'Chứng chỉ Agile Management',org:'Chứng nhận Chuyên nghiệp',dash:false},
    ]
  },
  edu:{
    tag:'Nền tảng Học vấn',title:'Học vấn & <span>Thành tích</span>',
    uni:'Đại học Kinh tế TP.HCM (UEH)',major:'Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo',
    courseTag:'Các môn học Cốt lõi',
    courses:['Tư duy Thiết kế (Design Thinking)','Tương tác Người-Máy (HCI)','Quản trị Đổi mới Sáng tạo','Trí tuệ Doanh nghiệp (BI)','Chuyển đổi Kinh doanh Số','Dự án AI'],
    certTag:'Chứng chỉ',
    certs:[
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false},
      {i:'🔄',n:'Chứng chỉ Agile Management',org:'Chứng nhận Chuyên nghiệp',dash:false},
    ]
  },
  chat:{
    name:'Trợ lý AI của Minh',sub:'● Trực tuyến · Sẵn sàng giải đáp',reset:'↺ Làm lại',logout:'⏻ Ngôn ngữ',
    greeting:`Xin chào! Tôi là AI đại diện cho Nguyễn Hoàng Minh — Product Owner & UX Strategist xây dựng sản phẩm tại giao điểm của thiết kế trải nghiệm người dùng, tư duy hệ thống và AI Engineering.\n\nMinh đang tích cực tìm kiếm các cơ hội Product và UX nơi sự đồng cảm sâu sắc với người dùng gặp khả năng thực thi sản phẩm chặt chẽ. Bạn muốn biết thêm điều gì?`,
    prompts:[
      {id:'exp',i:'💼',l:'Kinh nghiệm'},
      {id:'proj',i:'🧠',l:'Dự án'},
      {id:'skills',i:'⚡',l:'Kỹ năng'},
      {id:'edu',i:'🎓',l:'Học vấn'}
    ],
    ans:{
      exp:`Minh có hơn 2 năm kinh nghiệm tại SIHUB — Trung tâm Hỗ trợ Khởi nghiệp & ĐMST thuộc Sở KH&CN TP.HCM.\n\n◈ 01–10/2025 | Project Management Executive\nMinh thiết kế end-to-end digital journey maps cho các startup công nghệ, không chỉ như artifacts UX mà như hệ thống vận hành với activation flows, điểm kiểm soát ma sát và metrics chuyển đổi. Quản lý 150+ startup founders là đầu mối trung tâm, chạy A/B tests và Interleaving experiments để kiểm chứng mọi thay đổi tính năng trước rollout. Cách tiếp cận NPS: không phải một con số, mà là hệ thống tín hiệu hành vi real-time báo cáo lên Board.\n\n◈ 07–12/2024 | R&D Intern\nDẫn dắt phân tích khoảng trống năng lực cho 150+ stakeholders trong dự án khung năng lực cấp thành phố. Soạn thảo tài liệu chuẩn URD kết nối insights định tính với yêu cầu hệ thống cụ thể — kỹ năng trực tiếp định hình cách viết PRD sau này.`,
      proj:`Ba dự án nổi bật của Minh kể câu chuyện về người có thể tư duy xuyên suốt toàn bộ product stack:\n\n🧠 EchoMind AI — Flagship (09–12/2025)\nHệ thống BCI giải mã EEG 256 kênh thành văn bản. Với vai trò Project Lead: quản lý 8 Agile Sprints theo CPMAI, chẩn đoán và pivot từ LSTM Mode Collapse sang Transformer V2 (Multi-Head Attention + Label Smoothing). Kết quả: 55–65 WPM, độ trễ <1s, ROI kỹ thuật 72%. Thiết kế Expert Dashboard với Attention Maps để giải quyết vấn đề hộp đen trong y tế.\n\n📚 Hệ sinh thái E-Reader — Top 20 cấp TP (03–06/2025)\nThiết kế user journey HCI-focused từ device provisioning đến content updates. Phân tách cognitive friction thành feature sets. Top 20 cuộc thi UBND TP.HCM.\n\n🚀 Vận hành Sự kiện ĐMST — Đang diễn ra\nTổ chức Univ.Star 2024/2025 và Tuần lễ WHISE 2024 tại SIHUB.`,
      skills:`Năng lực của Minh trải dài 3 trụ cột:\n\n◈ Product Craft (Thế mạnh Cốt lõi)\n→ Journey Mapping 95% · UX/HCI 90% · Agile/CPMAI 88%\n→ PRD & User Stories · A/B Testing & Interleaving · Problem Decomposition\n→ Ma trận RACI · Burndown Tracking · Design Thinking\n\n◈ Dữ liệu & Tư duy Hệ thống\n→ Python · Phân tích Dữ liệu & EDA · Google Colab\n→ PyTorch · Feature Engineering · WER Metrics\n→ Kiến trúc Transformer (ứng dụng trong EchoMind)\n\n◈ Stakeholder & Thực thi\n→ Quản lý 150+ stakeholders cấp thành phố/chính quyền\n→ Tài liệu chiến lược báo cáo lên Board\n→ Dẫn nhóm 7 người cross-functional qua 8 Sprints`,
      edu:`Minh đang học năm cuối tại UEH, chuyên ngành Quản lý Công nghệ & Đổi mới Sáng tạo. GPA: 3.53/4.0.\n\nCác môn học cốt lõi ứng dụng trực tiếp:\n→ Human-Computer Interaction (HCI) — nền tảng tiếp cận UX\n→ Tư duy Thiết kế — cách đặt khung vấn đề sản phẩm\n→ Business Intelligence — cách đọc dữ liệu như tín hiệu sản phẩm\n→ Dự án AI — nơi EchoMind ra đời\n\nChứng chỉ: Google Project Management · Google Business Intelligence · Agile Management\n\nĐang chuẩn bị TOEIC để mở rộng cơ hội với sản phẩm quốc tế.`
    }
  }
}
};

// ============================================================
// STATE
// ============================================================
let lang = 'en';
let isTyping = false;
let isTrans = false;
let chartInst = null;

// ============================================================
// LANGUAGE SELECT + LOGOUT
// ============================================================
function selectLang(l) {
  lang = l;
  document.getElementById('lang-overlay').style.opacity = '0';
  document.getElementById('lang-overlay').style.visibility = 'hidden';
  const app = document.getElementById('main-app');
  app.classList.add('visible');
  renderUI();
  initChat();
}

function logout() {
  const overlay = document.getElementById('lang-overlay');
  overlay.style.opacity = '1';
  overlay.style.visibility = 'visible';
  const app = document.getElementById('main-app');
  app.classList.remove('visible');
  // Reset chat
  document.getElementById('chat-messages').innerHTML = '';
}

// ============================================================
// RENDER UI
// ============================================================
function renderUI() {
  const t = T[lang];

  // Nav labels + tooltips
  for (let i = 0; i < 5; i++) {
    const nl = document.getElementById('nl' + i);
    const ntt = document.getElementById('ntt' + i);
    if (nl) nl.textContent = t.nav[i];
    if (ntt) ntt.textContent = t.navTip[i];
  }

  // Welcome
  document.getElementById('w-status').textContent = t.w.status;
  document.getElementById('w-role').textContent = t.w.role;
  document.getElementById('w-summary').innerHTML = t.w.summary;
  ['ws1','ws2','ws3','ws4'].forEach((id,i) => {
    const el = document.getElementById(id);
    if (el) el.textContent = t.w.stats[i];
  });
  document.getElementById('w-explore').textContent = t.w.explore;
  document.getElementById('w-hint').textContent = t.w.hint;

  // Experience
  document.getElementById('e-tag').textContent = t.exp.tag;
  document.getElementById('e-title').innerHTML = t.exp.title;
  document.getElementById('e-timeline').innerHTML = t.exp.items.map((item, idx) => `
    <div class="timeline-item ${idx > 0 ? 'past' : ''}">
      <div class="tl-period">${item.period}</div>
      <div class="tl-role">${item.role}</div>
      <div class="tl-company">${item.company}</div>
      <ul class="tl-bullets">${item.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
      <div class="tl-tags">${item.tags.map(tg => `<span class="tl-tag">${tg}</span>`).join('')}</div>
    </div>
  `).join('');

  // Projects
  document.getElementById('p-tag').textContent = t.proj.tag;
  document.getElementById('p-title').innerHTML = t.proj.title;
  renderProjects();

  // Skills
  document.getElementById('s-tag').textContent = t.skills.tag;
  document.getElementById('s-title').innerHTML = t.skills.title;
  document.getElementById('s-radar-lbl').textContent = t.skills.radarLbl;
  document.getElementById('s-cert-lbl').textContent = t.skills.certLbl;
  document.getElementById('s-bars').innerHTML = t.skills.groups.map(g => `
    <div class="skill-group">
      <div class="skill-group-label">${g.name}</div>
      ${g.items.map(item => `
        <div class="skill-bar-item">
          <div class="skill-bar-header"><span class="skill-bar-name">${item.n}</span><span class="skill-bar-pct">${item.p}%</span></div>
          <div class="skill-bar-track"><div class="skill-bar-fill" style="width:${item.p}%"></div></div>
        </div>
      `).join('')}
    </div>
  `).join('');
  document.getElementById('s-certs').innerHTML = renderCerts(t.skills.certs);

  // Education
  document.getElementById('ed-tag').textContent = t.edu.tag;
  document.getElementById('ed-title').innerHTML = t.edu.title;
  document.getElementById('ed-uni').textContent = t.edu.uni;
  document.getElementById('ed-major').textContent = t.edu.major;
  document.getElementById('ed-courses').innerHTML = `
    <div class="proj-chart-title" style="margin-bottom:14px;">${t.edu.courseTag}</div>
    <div style="display:flex;flex-wrap:wrap;gap:10px;">${t.edu.courses.map(c => `<span style="font-size:13px;padding:7px 16px;background:var(--surface);border:1px solid var(--border2);border-radius:9px;color:var(--text2);">${c}</span>`).join('')}</div>
  `;
  document.getElementById('ed-cert-lbl').textContent = t.edu.certTag;
  document.getElementById('ed-certs').innerHTML = renderCerts(t.edu.certs);

  // Chat
  document.getElementById('c-name').textContent = t.chat.name;
  document.getElementById('c-sub').textContent = t.chat.sub;
  document.getElementById('c-reset').textContent = t.chat.reset;
  document.getElementById('c-logout').textContent = t.chat.logout;
}

function renderCerts(certs) {
  return certs.map(c => `
    <div class="cert-card" style="${c.dash ? 'border-style:dashed;border-color:rgba(240,192,96,.3);' : ''}">
      <span style="font-size:22px;flex-shrink:0;">${c.i}</span>
      <div style="flex:1;">
        <div style="color:var(--text);font-size:14px;font-weight:500;">${c.n}</div>
        <div style="font-size:11.5px;color:var(--text2);margin-top:2px;">${c.org}</div>
      </div>
      ${c.prog ? `<span style="font-family:'DM Mono',monospace;font-size:10.5px;color:var(--gold);padding:4px 12px;background:rgba(240,192,96,.1);border-radius:20px;white-space:nowrap;">${c.prog}</span>` : ''}
    </div>
  `).join('');
}

// ============================================================
// PROJECT RENDER WITH CHARTS
// ============================================================
function renderProjects() {
  const t = T[lang];
  const grid = document.getElementById('p-grid');
  grid.innerHTML = t.proj.items.map(p => {
    if (p.id === 'echomind') {
      return `
        <div class="project-card featured" id="ec-card">
          <div>
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
              <span class="project-badge ${p.bClass}">${p.badge}</span>
              <span class="project-badge badge-active">${p.date}</span>
            </div>
            <div class="project-name">${p.name}</div>
            <div class="project-sub">${p.sub}</div>
            <p class="project-desc">${p.desc.replace(/\n/g,'<br>')}</p>
            <div class="info-grid">${p.info.map(i => `<div class="info-item"><div class="info-lbl">${i.l}</div><div class="info-val">${i.v}</div></div>`).join('')}</div>
            <div class="project-metrics">${p.metrics.map(m => `<div class="metric"><div class="metric-val">${m.v}</div><div class="metric-lbl">${m.l}</div></div>`).join('')}</div>
            <!-- ROI CHART -->
            <div class="proj-chart-wrap">
              <div class="proj-chart-title" id="roi-chart-title">Technical ROI Breakdown — vs Traditional AAC</div>
              <div style="height:200px;position:relative;"><canvas id="roiChart"></canvas></div>
            </div>
            <!-- MODEL COMPARISON CHART -->
            <div class="proj-chart-wrap">
              <div class="proj-chart-title" id="model-chart-title">Model Comparison: LSTM V1 vs Transformer V2</div>
              <div style="height:180px;position:relative;"><canvas id="modelChart"></canvas></div>
            </div>
            <div class="tech-stack">${p.tech.map(tch => `<span class="tech-pill">${tch}</span>`).join('')}</div>
          </div>
          <div style="background:var(--ink3);border-radius:18px;border:1px solid var(--border);padding:22px;text-align:center;">
            <div style="font-size:40px;margin-bottom:14px;">🧠</div>
            <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);line-height:2.2;text-align:left;">
              EEG Input (256ch)<br>↓ HDF5 → Tensor<br>↓ Positional Enc.<br>↓ Transformer V2<br>↓ Beam Search<br>→ Text Output
            </div>
            <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
              <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);margin-bottom:4px;" id="ec-role-lbl">Role</div>
              <div style="font-size:13px;color:var(--text);font-weight:600;">Project Lead</div>
              <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);margin:10px 0 4px;" id="ec-team-lbl">Team</div>
              <div style="font-size:12px;color:var(--text);">7 members · 8 sprints</div>
              <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);margin:10px 0 4px;" id="ec-adv-lbl">Advisor</div>
              <div style="font-size:11px;color:var(--text2);">ThS. Tạ Việt Phương</div>
            </div>
            <!-- SPRINT CHART -->
            <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
              <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--accent2);letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;" id="ec-sprint-lbl">Sprint Burndown</div>
              <div style="height:140px;position:relative;"><canvas id="burndownChart"></canvas></div>
            </div>
          </div>
        </div>`;
    } else {
      return `
        <div class="project-card">
          <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:12px;">
            <span class="project-badge ${p.bClass}">${p.badge}</span>
            <span style="font-family:'DM Mono',monospace;font-size:10.5px;color:var(--text2);">${p.date}</span>
          </div>
          <div class="project-name" style="font-size:22px;">${p.name}</div>
          <div class="project-sub">${p.sub}</div>
          <p class="project-desc">${p.desc.replace(/\n/g,'<br>')}</p>
          <div class="tech-stack">${p.tech.map(tch => `<span class="tech-pill">${tch}</span>`).join('')}</div>
        </div>`;
    }
  }).join('');

  // Render charts after DOM is set
  setTimeout(() => {
    renderROIChart();
    renderModelChart();
    renderBurndownChart();
    // Update sidebar labels for echomind card
    const roleLbl = document.getElementById('ec-role-lbl');
    const teamLbl = document.getElementById('ec-team-lbl');
    const advLbl = document.getElementById('ec-adv-lbl');
    const sprintLbl = document.getElementById('ec-sprint-lbl');
    if (roleLbl) roleLbl.textContent = lang === 'en' ? 'Role' : 'Vai trò';
    if (teamLbl) teamLbl.textContent = lang === 'en' ? 'Team' : 'Nhóm';
    if (advLbl) advLbl.textContent = lang === 'en' ? 'Advisor' : 'GVHD';
    if (sprintLbl) sprintLbl.textContent = lang === 'en' ? 'Sprint Burndown' : 'Burndown Sprints';
    // Chart titles
    const rlt = document.getElementById('roi-chart-title');
    const mlt = document.getElementById('model-chart-title');
    if (rlt) rlt.textContent = lang === 'en' ? 'Technical ROI Breakdown — vs Traditional AAC' : 'Phân tích ROI Kỹ thuật — So với AAC Truyền thống';
    if (mlt) mlt.textContent = lang === 'en' ? 'Model Comparison: LSTM V1 vs Transformer V2' : 'So sánh Mô hình: LSTM V1 vs Transformer V2';
  }, 60);
}

function renderROIChart() {
  const ctx = document.getElementById('roiChart');
  if (!ctx) return;
  const isVI = lang === 'vi';
  const labels = isVI
    ? ['Độ chính xác', 'Tốc độ (WPM)', 'Độ trễ (cải thiện)', 'Tỷ lệ thành công']
    : ['Accuracy', 'Speed (WPM)', 'Latency (improvement)', 'Session Success'];
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        { label: isVI ? 'AAC Truyền thống' : 'Traditional AAC', data: [60, 30, 0, 40], backgroundColor: 'rgba(98,98,128,.4)', borderColor: 'rgba(98,98,128,.8)', borderWidth: 1, borderRadius: 5 },
        { label: 'EchoMind V2', data: [93, 60, 75, 72], backgroundColor: 'rgba(124,106,247,.55)', borderColor: 'rgba(165,148,252,.9)', borderWidth: 1, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: {
        x: { grid: { color: 'rgba(255,255,255,.05)' }, ticks: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 11 } } },
        y: { grid: { color: 'rgba(255,255,255,.05)' }, ticks: { color: '#9898b0', font: { family: "'DM Mono',monospace", size: 10 } }, max: 100, min: 0 }
      },
      plugins: {
        legend: { labels: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 11 }, boxWidth: 12 } },
        tooltip: { backgroundColor: '#252538', titleFont: { family: "'DM Mono',monospace" }, bodyFont: { family: "'DM Sans',sans-serif" }, borderColor: 'rgba(255,255,255,.1)', borderWidth: 1,
          callbacks: { label: ctx => ` ${ctx.dataset.label}: ${ctx.raw}${ctx.dataIndex === 2 ? '% ' + (isVI ? 'giảm' : 'reduction') : '%'}` }
        }
      }
    }
  });
}

function renderModelChart() {
  const ctx = document.getElementById('modelChart');
  if (!ctx) return;
  const isVI = lang === 'vi';
  const lbls = isVI
    ? ['WER (%)', 'Độ chính xác (%)', 'Tốc độ (WPM)', 'Tỷ lệ Mode Collapse']
    : ['WER (%)', 'Accuracy (%)', 'Speed (WPM)', 'Mode Collapse Rate'];
  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: lbls,
      datasets: [
        { label: 'LSTM V1 (Baseline)', data: [85, 15, 25, 95], borderColor: 'rgba(255,123,107,.7)', backgroundColor: 'rgba(255,123,107,.08)', borderWidth: 1.5, pointRadius: 3, pointBackgroundColor: 'rgba(255,123,107,.8)' },
        { label: 'Transformer V2', data: [8, 93, 60, 0], borderColor: 'rgba(165,148,252,.8)', backgroundColor: 'rgba(124,106,247,.12)', borderWidth: 1.8, pointRadius: 3, pointBackgroundColor: '#a594fc' }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: { r: { min: 0, max: 100, ticks: { display: false }, angleLines: { color: 'rgba(255,255,255,.07)' }, grid: { color: 'rgba(255,255,255,.07)' }, pointLabels: { color: '#9898b0', font: { size: 10, family: "'DM Sans',sans-serif" } } } },
      plugins: { legend: { labels: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 11 }, boxWidth: 12, padding: 14 } }, tooltip: { backgroundColor: '#252538', titleFont: { family: "'DM Mono',monospace" }, bodyFont: { family: "'DM Sans',sans-serif" }, borderColor: 'rgba(255,255,255,.1)', borderWidth: 1 } }
    }
  });
}

function renderBurndownChart() {
  const ctx = document.getElementById('burndownChart');
  if (!ctx) return;
  const isVI = lang === 'vi';
  const sprintLabels = ['Start','S0','S1','S2-3','S4','S5','S6','S7'];
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: sprintLabels,
      datasets: [
        { label: isVI ? 'Lý tưởng' : 'Ideal', data: [3833, 3280, 2727, 2174, 1621, 1068, 515, 0], borderColor: 'rgba(98,98,128,.5)', borderWidth: 1.5, borderDash: [5,4], pointRadius: 0, fill: false },
        { label: isVI ? 'Thực tế' : 'Actual', data: [3833, 3253, 2560, 2086, 1534, 1057, 612, 0], borderColor: '#a594fc', borderWidth: 2, pointRadius: 3, pointBackgroundColor: '#a594fc', fill: { target: 'origin', above: 'rgba(124,106,247,.06)' } }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: {
        x: { grid: { display: false }, ticks: { color: '#5a5a78', font: { family: "'DM Mono',monospace", size: 9 } } },
        y: { grid: { color: 'rgba(255,255,255,.04)' }, ticks: { color: '#5a5a78', font: { family: "'DM Mono',monospace", size: 9 }, callback: v => (v/1000).toFixed(1)+'k' } }
      },
      plugins: { legend: { labels: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 10 }, boxWidth: 10, padding: 10 } }, tooltip: { backgroundColor: '#252538', titleFont: { family: "'DM Mono',monospace" }, bodyFont: { family: "'DM Sans',sans-serif" }, borderColor: 'rgba(255,255,255,.1)', borderWidth: 1 } }
    }
  });
}

// ============================================================
// VIEW SWITCHING
// ============================================================
function go(viewId, navEl) {
  if (isTrans) return;
  const target = document.getElementById('view-' + viewId);
  if (!target || target.style.display !== 'none') return;

  isTrans = true;
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  if (navEl) navEl.classList.add('active');
  else { const n = document.querySelector(`[data-view="${viewId}"]`); if (n) n.classList.add('active'); }

  const tr = document.getElementById('view-tr');
  tr.classList.add('active');

  setTimeout(() => {
    document.querySelectorAll('.view-content').forEach(v => v.style.display = 'none');
    target.style.display = '';
    document.getElementById('scroll-progress').style.width = '0%';
    document.getElementById('visual-panel').scrollTop = 0;

    if (viewId === 'skills') {
      document.querySelectorAll('.skill-bar-fill').forEach(b => b.classList.remove('animate'));
      setTimeout(() => { initSkillsChart(); animBars(); }, 60);
    }
    if (viewId === 'projects') {
      setTimeout(() => { renderROIChart(); renderModelChart(); renderBurndownChart(); }, 60);
    }

    const animEls = target.querySelectorAll('.fade-up');
    animEls.forEach(el => { el.style.animation = 'none'; void el.offsetWidth; el.style.animation = null; });

    setTimeout(() => { tr.classList.remove('active'); isTrans = false; }, 120);
  }, 260);
}

function animBars() {
  document.querySelectorAll('.skill-bar-fill').forEach(b => b.classList.add('animate'));
}

// ============================================================
// SKILLS CHART
// ============================================================
function initSkillsChart() {
  const ctx = document.getElementById('skillsChart');
  if (!ctx) return;
  if (chartInst) { chartInst.destroy(); chartInst = null; }
  const t = T[lang];
  chartInst = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: t.skills.radarLabels,
      datasets: [{ data: [90, 88, 95, 80, 80, 72, 82], fill: true, backgroundColor: 'rgba(124,106,247,.14)', borderColor: '#7c6af7', pointBackgroundColor: '#a594fc', pointBorderColor: '#1e1e2e', borderWidth: 2, pointRadius: 4 }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: { r: { min: 0, max: 100, ticks: { display: false }, angleLines: { color: 'rgba(255,255,255,.07)' }, grid: { color: 'rgba(255,255,255,.07)' }, pointLabels: { font: { size: 12, family: "'DM Sans',sans-serif", weight: '500' }, color: '#9898b0' } } },
      plugins: { legend: { display: false }, tooltip: { backgroundColor: '#252538', borderColor: 'rgba(255,255,255,.1)', borderWidth: 1, padding: 12, callbacks: { label: c => { const v = c.raw; if (lang === 'vi') return v >= 90 ? ' Chuyên gia' : v >= 80 ? ' Cao cấp' : v >= 70 ? ' Thành thạo' : ' Có nền'; return v >= 90 ? ' Expert' : v >= 80 ? ' Advanced' : v >= 70 ? ' Proficient' : ' Familiar'; } } } }
    }
  });
}

// ============================================================
// SCROLL PROGRESS
// ============================================================
document.getElementById('visual-panel').addEventListener('scroll', function() {
  const h = this.scrollHeight - this.clientHeight;
  if (h > 0) document.getElementById('scroll-progress').style.width = (this.scrollTop / h * 100) + '%';
});

// ============================================================
// CHAT
// ============================================================
function initChat() {
  const cm = document.getElementById('chat-messages');
  cm.innerHTML = '';
  renderPrompts();
  setTimeout(() => appendMsg('ai', T[lang].chat.greeting, true), 400);
}

function renderPrompts() {
  const pg = document.getElementById('prompts-grid');
  pg.innerHTML = T[lang].chat.prompts.map(p =>
    `<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.i} ${p.l}')" ${isTyping || isTrans ? 'disabled' : ''}><span style="font-size:16px;">${p.i}</span>${p.l}</button>`
  ).join('');
}

function handlePrompt(id, label) {
  if (isTyping || isTrans) return;
  document.getElementById('prompts-grid').style.opacity = '.4';
  appendMsg('user', label, false);
  const vMap = { exp: 'experience', proj: 'projects', edu: 'education', skills: 'skills' };
  setTimeout(() => go(vMap[id] || 'welcome', null), 300);
  setTimeout(() => {
    appendMsg('ai', T[lang].chat.ans[id], true, () => {
      document.getElementById('prompts-grid').style.opacity = '1';
      renderPrompts();
    });
  }, 650);
}

function appendMsg(s, txt, tw = false, cb = null) {
  const cm = document.getElementById('chat-messages');
  const row = document.createElement('div'); row.className = 'msg-row ' + s;
  const av = document.createElement('div'); av.className = 'msg-av ' + s; av.textContent = s === 'ai' ? '🤖' : '👤';
  const bub = document.createElement('div'); bub.className = 'msg-bubble ' + s;
  row.appendChild(av); row.appendChild(bub); cm.appendChild(row);
  if (s === 'ai' && tw) typeW(txt, bub, cb);
  else { bub.innerHTML = txt.replace(/\n/g, '<br>'); cm.scrollTop = cm.scrollHeight; if (cb) cb(); }
}

function typeW(txt, el, cb) {
  isTyping = true; renderPrompts();
  const cm = document.getElementById('chat-messages');
  const tmpDiv = document.createElement('div');
  tmpDiv.innerHTML = txt.replace(/\n/g, '<br>');
  const nodes = Array.from(tmpDiv.childNodes);
  el.innerHTML = '<span class="tc"></span><span class="cursor-blink"></span>';
  const tc = el.querySelector('.tc');
  let ni = 0, ci = 0;

  function type() {
    if (ni < nodes.length) {
      const nd = nodes[ni];
      if (nd.nodeType === 3) {
        if (ci < nd.textContent.length) {
          tc.innerHTML += nd.textContent.charAt(ci++);
          cm.scrollTop = cm.scrollHeight;
          setTimeout(type, Math.floor(Math.random() * 18) + 4);
        } else { ni++; ci = 0; type(); }
      } else {
        tc.appendChild(nd.cloneNode(true));
        ni++; cm.scrollTop = cm.scrollHeight;
        setTimeout(type, 8);
      }
    } else {
      isTyping = false;
      const cur = el.querySelector('.cursor-blink');
      if (cur) cur.remove();
      renderPrompts();
      if (cb) cb();
    }
  }
  type();
}

function resetChat() { if (isTyping || isTrans) return; initChat(); }
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
