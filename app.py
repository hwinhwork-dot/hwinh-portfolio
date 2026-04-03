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
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
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
.lo-tagline{font-family:'Montserrat',sans-serif;font-size:12px;color:var(--text2);letter-spacing:3px;text-transform:uppercase;}
.lo-question{font-family:'Syne',sans-serif;font-size:22px;font-weight:600;color:var(--text);text-align:center;line-height:1.5;}
.lo-options{display:flex;gap:24px;}
.lo-btn{
  background:var(--surface);border:1px solid var(--border2);color:var(--text);
  padding:16px 48px;border-radius:12px;font-family:'Syne',sans-serif;font-size:20px;font-weight:600;
  cursor:pointer;transition:all .3s cubic-bezier(.16,1,.3,1);display:flex;align-items:center;justify-content:center;
}
.lo-btn:hover{border-color:var(--accent);background:var(--surface2);transform:translateY(-4px);box-shadow:0 12px 30px rgba(124,106,247,.25);color:var(--accent3);}

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
.nav-item .nav-lbl{font-family:'Montserrat',sans-serif;font-weight:500;font-size:8.5px;letter-spacing:.3px;text-transform:uppercase;opacity:.7;white-space:nowrap;}
.nav-item:hover{background:var(--surface);color:var(--text);}
.nav-item.active{background:linear-gradient(135deg,rgba(124,106,247,.3),rgba(124,106,247,.12));color:var(--accent2);border-color:rgba(124,106,247,.35);box-shadow:0 0 18px rgba(124,106,247,.2);}
.nav-tooltip{position:absolute;left:74px;background:var(--surface2);color:var(--text);font-size:12px;font-family:'Montserrat',sans-serif;font-weight:500;padding:6px 12px;border-radius:7px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .15s;border:1px solid var(--border2);z-index:100;}
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
.chat-sub{font-size:11px;color:var(--green);font-family:'Montserrat',sans-serif;font-weight:500;margin-top:3px;}
.chat-actions{margin-left:auto;display:flex;gap:8px;}
.chat-btn{background:none;border:1px solid var(--border2);color:var(--text2);font-size:11px;padding:7px 13px;border-radius:8px;cursor:pointer;font-family:'Montserrat',sans-serif;font-weight:500;transition:all .2s;white-space:nowrap;}
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
.msg-bubble{max-width:82%;padding:14px 18px;border-radius:18px;font-size:13.5px;line-height:1.65;}
.msg-bubble.ai{background:var(--surface);border:1px solid var(--border2);color:var(--text);border-bottom-left-radius:4px;}
.msg-bubble.user{background:var(--accent);color:white;border-bottom-right-radius:4px;}
.cursor-blink{display:inline-block;width:8px;height:15px;background:var(--accent2);margin-left:3px;animation:blink 1s step-end infinite;vertical-align:middle;border-radius:1px;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}

/* Chat footer & Prompt Cards */
.chat-footer{padding:16px;border-top:1px solid var(--border);flex-shrink:0;background:var(--ink2);}
.prompts-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.prompt-btn {
    background: linear-gradient(145deg, var(--surface) 0%, var(--surface2) 100%);
    border: 1px solid var(--border2); border-radius: 16px; padding: 16px 14px;
    font-size: 13px; color: var(--text); font-weight: 500; cursor: pointer;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex; flex-direction: column; align-items: flex-start; gap: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1); position: relative; overflow: hidden; text-align: left;
}
.prompt-btn::before {
    content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%;
    background: var(--accent); transform: scaleY(0); transition: transform 0.3s;
    transform-origin: bottom;
}
.prompt-btn:hover {
    transform: translateY(-4px); box-shadow: 0 8px 20px rgba(124,106,247,0.2);
    border-color: rgba(124,106,247,0.4); background: var(--surface2);
}
.prompt-btn:hover::before { transform: scaleY(1); }
.p-icon { font-size: 20px; padding: 6px; background: rgba(124,106,247,0.1); border-radius: 10px; line-height: 1; margin-bottom: 2px; border: 1px solid rgba(124,106,247,0.2); }
.p-lbl { font-family: 'Syne', sans-serif; font-size: 14.5px; letter-spacing: -0.2px; font-weight: 700; color: var(--text); }
.prompt-btn:disabled{opacity:.4;cursor:not-allowed;transform:none;box-shadow:none;}
.prompt-btn:disabled::before { display: none; }

/* === NOISE === */
.noise{position:fixed;inset:0;opacity:.025;pointer-events:none;z-index:100;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* === SHARED VIEW STYLES === */
.view-content{padding:60px 72px;min-height:100%;position:relative;}
.section-tag{display:inline-flex;align-items:center;gap:8px;font-family:'Montserrat',sans-serif;font-weight:600;font-size:11px;color:var(--accent2);text-transform:uppercase;letter-spacing:2.5px;margin-bottom:20px;}
.section-tag::before{content:'◈';font-size:13px;}
.view-title{font-family:'Syne',sans-serif;font-size:46px;font-weight:800;letter-spacing:-1.5px;color:var(--text);margin-bottom:52px;line-height:1;}
.view-title span{color:var(--accent2);}
.subtle-div{height:1px;background:var(--border);margin:44px 0;}

/* === WELCOME VIEW === */
.welcome-eyebrow{display:flex;align-items:center;gap:10px;margin-bottom:28px;}
.status-dot{width:10px;height:10px;background:var(--green);border-radius:50%;box-shadow:0 0 10px var(--green);animation:pg 2s infinite;}
@keyframes pg{0%,100%{box-shadow:0 0 6px var(--green);}50%{box-shadow:0 0 20px var(--green);}}
.status-text{font-family:'Montserrat',sans-serif;font-weight:600;font-size:11.5px;color:var(--green);letter-spacing:1px;text-transform:uppercase;}
.welcome-name{font-family:'Syne',sans-serif;font-size:clamp(46px,5vw,80px);font-weight:800;line-height:.95;letter-spacing:-2.5px;margin-bottom:14px;}
.welcome-name .accent-word{color:var(--accent2);display:block;}
.welcome-role{font-size:18px;color:var(--text2);font-weight:300;margin-bottom:36px;font-style:italic;letter-spacing:.3px;}
.welcome-summary{font-size:15.5px;line-height:1.85;color:var(--text2);max-width:580px;margin-bottom:44px;border-left:3px solid var(--accent);padding-left:24px;}
.contact-row{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:48px;}
.contact-chip{display:flex;align-items:center;gap:8px;padding:9px 18px;background:var(--surface);border:1px solid var(--border2);border-radius:10px;font-size:12.5px;font-family:'Montserrat',sans-serif;font-weight:500;color:var(--text2);transition:all .2s;cursor:default;}
.contact-chip:hover{border-color:var(--accent);color:var(--text);background:var(--surface2);}
.stat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;max-width:700px;margin-bottom:52px;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px 18px;position:relative;overflow:hidden;transition:transform .25s,box-shadow .25s;}
.stat-card:hover{transform:translateY(-3px);box-shadow:0 12px 25px rgba(0,0,0,.2);}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--accent),var(--teal));}
.stat-number{font-family:'Syne',sans-serif;font-size:34px;font-weight:800;color:var(--text);line-height:1;}
.stat-label{font-size:11px;color:var(--text2);margin-top:8px;text-transform:uppercase;letter-spacing:.7px;font-family:'Montserrat',sans-serif;font-weight:600;}

/* === TIMELINE === */
.timeline{position:relative;padding-left:32px;}
.timeline::before{content:'';position:absolute;left:0;top:8px;bottom:8px;width:2px;background:linear-gradient(to bottom,var(--accent),transparent);}
.timeline-item{position:relative;margin-bottom:52px;}
.timeline-item::before{content:'';position:absolute;left:-38px;top:7px;width:12px;height:12px;border-radius:50%;background:var(--accent2);box-shadow:0 0 14px rgba(165,148,252,.5);}
.timeline-item.past::before{background:var(--text2);box-shadow:none;}
.tl-period{font-family:'Montserrat',sans-serif;font-weight:600;font-size:11.5px;color:var(--accent2);letter-spacing:1px;margin-bottom:10px;text-transform:uppercase;}
.tl-role{font-family:'Syne',sans-serif;font-size:22px;font-weight:700;margin-bottom:6px;}
.tl-company{font-size:14px;color:var(--text2);font-style:italic;margin-bottom:20px;}
.tl-bullets{list-style:none;display:flex;flex-direction:column;gap:13px;}
.tl-bullets li{font-size:14.5px;color:var(--text2);line-height:1.72;padding-left:22px;position:relative;}
.tl-bullets li::before{content:'→';position:absolute;left:0;color:var(--accent);font-weight:700;}
.tl-bullets li strong{color:var(--text);font-weight:500;}
.tl-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;}
.tl-tag{font-family:'Montserrat',sans-serif;font-weight:500;font-size:10.5px;padding:4px 12px;border-radius:6px;background:rgba(124,106,247,.1);border:1px solid rgba(124,106,247,.25);color:var(--accent3);}

/* === PROJECTS === */
.projects-grid{display:grid;grid-template-columns:1fr 1fr;gap:22px;}
.project-card{background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:30px;transition:all .3s;position:relative;overflow:hidden;}
.project-card:hover{border-color:var(--accent);transform:translateY(-4px);box-shadow:0 22px 44px rgba(0,0,0,.32);}
.project-card.featured{grid-column:1/-1;display:grid;grid-template-columns:1fr 220px;gap:32px;align-items:start;}
.project-badge{font-family:'Montserrat',sans-serif;font-weight:600;font-size:10.5px;padding:5px 12px;border-radius:20px;text-transform:uppercase;}
.badge-featured{background:rgba(240,192,96,.15);color:var(--gold);border:1px solid rgba(240,192,96,.3);}
.badge-active{background:rgba(82,209,138,.12);color:var(--green);border:1px solid rgba(82,209,138,.3);}
.badge-top20{background:rgba(255,123,107,.14);color:var(--coral);border:1px solid rgba(255,123,107,.3);}
.project-name{font-family:'Syne',sans-serif;font-size:26px;font-weight:700;margin:12px 0 8px;letter-spacing:-.5px;}
.project-sub{font-size:13px;color:var(--text2);font-style:italic;margin-bottom:16px;}
.project-desc{font-size:14.5px;color:var(--text2);line-height:1.75;margin-bottom:20px;}
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0;}
.info-item{background:var(--ink3);border-radius:10px;padding:11px 15px;border:1px solid var(--border);}
.info-lbl{font-family:'Montserrat',sans-serif;font-weight:600;font-size:9px;color:var(--text2);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:5px;}
.info-val{font-size:12.5px;color:var(--text);font-weight:500;line-height:1.45;}
.project-metrics{display:flex;gap:22px;margin:16px 0;padding:16px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border);}
.metric-val{font-family:'Syne',sans-serif;font-size:24px;font-weight:700;color:var(--accent2);}
.metric-lbl{font-size:9.5px;color:var(--text2);text-transform:uppercase;letter-spacing:.6px;margin-top:4px;font-family:'Montserrat',sans-serif;font-weight:600;}
.tech-stack{display:flex;flex-wrap:wrap;gap:7px;}
.tech-pill{font-family:'Montserrat',sans-serif;font-weight:500;font-size:10.5px;padding:4px 12px;border-radius:6px;background:var(--ink3);border:1px solid var(--border2);color:var(--text2);}

/* Chart containers in project */
.proj-chart-wrap{background:var(--ink3);border-radius:16px;border:1px solid var(--border);padding:20px;margin:16px 0;}
.proj-chart-title{font-family:'Montserrat',sans-serif;font-weight:600;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:14px;}

/* === SKILLS (LinkedIn Style w/ Tooltip) === */
.skills-layout{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
.lk-skill-card{
    background:var(--surface); border:1px solid var(--border); border-radius:14px;
    padding:18px 20px; margin-bottom:14px; display:flex; flex-direction:column; gap:8px;
    transition:all .2s ease; position:relative; cursor:help; z-index: 10;
}
.lk-skill-card:hover{
    border-color:var(--accent); transform:translateY(-2px); box-shadow:0 8px 20px rgba(0,0,0,.15);
    z-index: 110; 
}
.lk-skill-header { display:flex; justify-content:space-between; align-items:center; }
.lk-skill-title { font-size:15px; font-weight:600; color:var(--text); display:flex; align-items:center; gap:10px; }
.lk-skill-ref { font-family:'Montserrat',sans-serif; font-size:11px; color:var(--text2); display:flex; align-items:center; gap:6px; line-height:1.4; font-weight:500;}
.lk-skill-ref::before { content:'↳'; color:var(--accent2); font-weight:bold; font-family:'DM Sans', sans-serif; }

/* Skill Popup Hover */
.skill-popup {
    position:absolute; bottom:100%; left:50%; transform:translateX(-50%) translateY(10px);
    width:max-content; max-width:320px; background:rgba(30,30,46,0.96);
    border:1px solid var(--accent); border-radius:12px; padding:16px;
    box-shadow:0 15px 35px rgba(0,0,0,0.5); backdrop-filter:blur(10px);
    opacity:0; visibility:hidden; transition:all 0.3s cubic-bezier(0.16,1,0.3,1);
    z-index:120; pointer-events:none; text-align:left; margin-bottom: 12px;
}
.lk-skill-card:hover .skill-popup { opacity:1; visibility:visible; transform:translateX(-50%) translateY(0); }
.skill-popup::after {
    content:''; position:absolute; top:100%; left:50%; transform:translateX(-50%);
    border-width:6px; border-style:solid; border-color:var(--accent) transparent transparent transparent;
}
.popup-title { font-family:'Montserrat',sans-serif; font-weight:600; font-size:10px; color:var(--accent2); text-transform:uppercase; letter-spacing:1px; margin-bottom:10px; }
.popup-metric { font-size:13px; color:var(--text); line-height:1.5; display:flex; align-items:start; gap:8px; margin-bottom:8px; }
.popup-metric:last-child { margin-bottom:0; }
.popup-metric::before { content:'•'; color:var(--green); font-weight:bold; }

.cert-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:15px 18px;margin-bottom:10px;display:flex;align-items:center;gap:14px;transition:transform .2s,border-color .2s;position:relative;}
a.cert-card{cursor:pointer; color:inherit; text-decoration:none;}
a.cert-card:hover{transform:translateX(4px);border-color:var(--accent);box-shadow:0 6px 16px rgba(124,106,247,.15);}
a.cert-card:hover .cert-link-icon{opacity:1 !important;color:var(--accent2) !important;transform:translate(2px,-2px);}
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

<div id="lang-overlay">
  <div style="text-align:center;">
    <div class="lo-logo">hwinh</div>
    <div class="lo-tagline" style="margin-top:10px;">AI Portfolio · Product &amp; UX</div>
  </div>
  <div class="lo-question">Choose your language<br><span style="font-family:'Montserrat',sans-serif;font-size:16px;color:var(--text2);font-weight:400;margin-top:8px;display:inline-block;">Chọn ngôn ngữ hiển thị</span></div>
  <div class="lo-options">
    <button class="lo-btn" onclick="selectLang('en')">English</button>
    <button class="lo-btn" onclick="selectLang('vi')">Tiếng Việt</button>
  </div>
</div>

<div class="app" id="main-app">

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

  <main class="visual-panel" id="visual-panel">
    <div class="view-tr" id="view-tr"><div class="spinner"></div></div>

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
        <div class="stat-card"><div class="stat-number">72%</div><div class="stat-label" id="ws3">AI Tech. KPI</div></div>
        <div class="stat-card"><div class="stat-number">Top 20</div><div class="stat-label" id="ws4">City Finalist</div></div>
      </div>
      <div class="subtle-div fade-up"></div>
      <div class="section-tag fade-up d6" id="w-explore">Explore this portfolio</div>
      <p class="fade-up d6" style="font-family:'Montserrat',sans-serif;font-size:13px;color:var(--text2);line-height:1.8;max-width:500px;margin-top:8px;" id="w-hint"></p>
    </div>

    <div id="view-experience" class="view-content" style="display:none">
      <div class="section-tag" id="e-tag">Work History</div>
      <h2 class="view-title" id="e-title">Work <span>Experience</span></h2>
      <div class="timeline" id="e-timeline"></div>
    </div>

    <div id="view-projects" class="view-content" style="display:none">
      <div class="section-tag" id="p-tag">Product Experience</div>
      <h2 class="view-title" id="p-title">Featured <span>Projects</span></h2>
      <div class="projects-grid" id="p-grid"></div>
    </div>

    <div id="view-skills" class="view-content" style="display:none">
      <div class="section-tag" id="s-tag">Competencies</div>
      <h2 class="view-title" id="s-title">Professional <span>Skills</span></h2>
      <div class="skills-layout">
        <div id="s-list"></div>
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

    <div id="view-education" class="view-content" style="display:none">
      <div class="section-tag" id="ed-tag">Academic Background</div>
      <h2 class="view-title" id="ed-title">Education &amp; <span>Awards</span></h2>
      <div class="edu-hero">
        <div style="font-family:'Montserrat',sans-serif;font-weight:600;font-size:11px;color:var(--accent2);letter-spacing:1px;margin-bottom:14px;">AUG 2022 — AUG 2026</div>
        <h3 style="font-family:'Syne',sans-serif;font-size:26px;font-weight:800;color:var(--text);margin-bottom:6px;" id="ed-uni">University of Economics HCMC (UEH)</h3>
        <p style="font-family:'Montserrat',sans-serif;color:var(--text2);font-size:14px;margin-bottom:20px;" id="ed-major">Bachelor of Technology &amp; Innovation Management</p>
        <div class="gpa-badge">
          <span style="font-size:26px;">🏆</span>
          <div>
            <div style="font-family:'Montserrat',sans-serif;font-weight:500;font-size:11px;color:var(--text2);margin-bottom:3px;">Grade Point Average</div>
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
    summary:`Young professional in <strong style="color:var(--text)">Technology & Innovation Management</strong> — operating at the intersection of UX Design, Systems Thinking, and AI. I specialize in turning complex user data and behavioral pain points into seamless, measurable digital experiences. I believe the best products emerge when deep empathy meets rigorous execution — whether it’s streamlining a startup's onboarding journey or leading an AI project from an initial concept to a fully functioning model.`,
    stats:['Years Exp.','Stakeholders Managed','AI Tech. KPI','City-level Finalist'],
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
          `<strong>End-to-End Customer Journey Mapping & MVP Delivery:</strong> Designed complete digital user journeys for tech startups. Instead of just creating flowcharts, I focused on identifying core user frustrations, translating them into structured User Stories, and driving rapid, iterative MVP development to reduce time-to-first-value.`,
          `<strong>Data-Driven Product Validation:</strong> Monitored omnichannel touchpoints to identify operational bottlenecks. I implemented A/B testing and Interleaving experiments to rigorously evaluate feature changes, ensuring that every product decision was backed by behavioral evidence rather than assumptions.`,
          `<strong>Stakeholder Management & NPS Analytics:</strong> Served as the primary liaison for 150+ startup founders. By analyzing behavioral data, I transformed NPS from a static metric into a real-time behavioral signal system, presenting actionable retention insights directly to the Board of Directors.`
        ],
        tags:['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Stakeholder Management (150+)','URD Documentation']
      },
      {
        period:'JUL 2024 — DEC 2024',
        role:'Research & Development Intern',
        company:'SIHUB · Executed data-driven project management for a city-level scientific competency framework',
        bullets:[
          `<strong>Large-Scale Data Analysis & Requirements Gathering:</strong> Directed the full data lifecycle for a city-level competency gap analysis. I successfully managed conflicting requirements from over 150 key stakeholders (government officials, research institutes, and corporate partners), extracting structured insights that shaped final policy recommendations.`,
          `<strong>URD-Standard Structured Documentation:</strong> Authored comprehensive strategic reports and system requirement documents aligned with URD (User Requirements Document) standards. This experience refined my ability to bridge the gap between qualitative user feedback and concrete technical requirements.`
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
        desc:`EchoMind addresses a profound human challenge: empowering patients with locked-in syndrome to communicate. Traditional AAC devices are slow (25–30 WPM), laggy, and have low session success rates. Our goal was to build a faster, more reliable non-invasive EEG-to-text system.\n\nAs <strong style="color:var(--text)">Project Lead</strong>, I managed the full AI product lifecycle utilizing the <strong style="color:var(--text)">CPMAI 6-phase framework</strong>, executing 8 Agile Sprints with a 7-member team. Early on, our baseline LSTM model suffered from Mode Collapse due to an information bottleneck. I made the strategic decision to pivot to a <strong style="color:var(--text)">Transformer V2</strong> architecture. To optimize for edge devices, we applied Int8 Quantization, allowing the model to run smoothly without GPUs. \n\nThe final system achieved <strong style="color:var(--text)">55–65 WPM, &lt;1s latency, and a 72% Technical KPI</strong> over traditional AAC. We also integrated an Expert Dashboard with Attention Maps to provide Explainable AI for healthcare professionals.`,
        info:[
          {l:'Final Architecture',v:'Transformer V2 · 8-head Multi-Head Attention · Positional Encoding · Label Smoothing ε=0.1'},
          {l:'Baseline vs Final',v:'Seq2Seq LSTM (Mode Collapse, WER ~85–90%) → Transformer V2 (Structured output, 6–7/10 correct)'},
          {l:'Dataset',v:'Brain-to-Text \'25 (Kaggle) · 256-channel non-invasive EEG · HDF5 format · avg 6.38 words/sentence'},
          {l:'PM Framework',v:'CPMAI 6-phase · 8 Agile Sprints · RACI Matrix · 3,833.5 total hours · 100% milestone completion'}
        ],
        metrics:[{v:'55–65',l:'WPM Output'},{v:'<1s',l:'Latency'},{v:'72%',l:'Technical KPI'},{v:'92–95%',l:'Accuracy'},{v:'6–7/10',l:'Sentences Correct'},{v:'100%',l:'Milestone'}],
        tech:['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','RACI Matrix','Agile/Scrum']
      },
      {
        id:'ereader',badge:'🏆 Top 20 Finalist',bClass:'badge-top20',date:'Mar — Jun 2025',
        name:'E-Reader Ecosystem',sub:'User Researcher · HCMC Digital Education · Directed by HCMC People\'s Committee',
        desc:`A Top 20 City-level initiative aimed at designing a digital education ecosystem for student e-reading devices. The core challenge was minimizing cognitive friction — ensuring students wouldn't abandon the device during the initial setup phase.\n\nAs a <strong style="color:var(--text)">User Researcher</strong>, I systematically applied <strong style="color:var(--text)">HCI (Human-Computer Interaction)</strong> principles to map the complete user journey. By methodically decomposing pain points, I identified specific stages causing cognitive overload. These behavioral observations were translated into actionable User Stories with clear success criteria, resulting in a cohesive ecosystem design that significantly streamlined the user experience.`,
        tech:['HCI Principles','UX Design','Journey Mapping','Problem Decomposition','User Stories','Cognitive Load Analysis','Figma Prototyping']
      },
      {
        id:'events',badge:'● Ongoing',bClass:'badge-active',date:'Jul 2024 — Present',
        name:'Innovation Events Operations',sub:'Operations · SIHUB Startup Ecosystem · HCMC',
        desc:`Managed end-to-end operations for two major city-level innovation events: <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> and <strong style="color:var(--text)">WHISE Week 2024</strong>. I coordinated cross-functional teams and facilitated real-time communication between startup founders, investors, and government representatives to ensure high-quality, seamless event experiences.`,
        tech:['Event Management','Cross-team Coordination','Stakeholder Communication','Operations Planning']
      }
    ]
  },
  skills:{
    tag:'Competencies',title:'Professional <span>Skills</span>',
    radarLbl:'Skill Radar Overview',certLbl:'Certifications',
    list:[
      {n:'Customer Journey Mapping',ref:'Validated by: Design Thinking (UEH)', m:['Mapped 15+ complex user flows for startups','Reduced onboarding friction points by 30%','Optimized 5+ critical conversion touchpoints']},
      {n:'UX / HCI Design',ref:'Validated by: Human-Computer Interaction (UEH)', m:['Applied to 3 major practical projects','Minimized cognitive load for E-Reader users','Designed Heuristic-standard Gradio UI']},
      {n:'Agile / Scrum (CPMAI)',ref:'Validated by: Google Project Management & EchoMind Project', m:['Managed 8 continuous Sprints','Led a cross-functional team of 7','Achieved 100% project milestones on time']},
      {n:'A/B Testing & Interleaving',ref:'Validated by: Human-Computer Interaction (UEH)', m:['Designed & ran 10+ feature experiments','Validated hypotheses with 95% significance','Prevented 3 major UX flaws before rollout']},
      {n:'Problem Decomposition',ref:'Validated by: Innovation Management (UEH)', m:['Broke down 5+ high-level Epics','Diagnosed LSTM Mode Collapse root cause','Structured 150+ stakeholder requirements']},
      {n:'PRD & User Stories Writing',ref:'Validated by: Entrepreneurship Innovation (UEH)', m:['Authored 10+ standardized PRDs','Maintained backlog of 200+ User Stories','Met city-level URD documentation standards']},
      {n:'Python & PyTorch (Familiar)',ref:'Applied in: Advanced Programming & EchoMind Project', m:['Optimized Transformer V2 architecture','Applied Int8 Quantization to reduce model size','Decreased model inference latency to <1s']}
    ],
    radarLabels:['UX/HCI','Agile','Journey Map','Data Analysis','Python','PyTorch/ML','A/B Testing'],
    certs:[
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
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
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
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
      exp:`Minh has over 2 years of experience at SIHUB (Startup & Innovation Hub of HCMC).\n\n◈ Jan–Oct 2025 | Project Management Executive\nMinh designed end-to-end digital journey maps for tech startups. He didn't just draw flowcharts; he implemented validation processes via A/B testing and Interleaving experiments. He also shifted the team's perspective on NPS, treating it as a real-time behavioral signal system rather than a static metric.\n\n◈ Jul–Dec 2024 | R&D Intern\nLed a competency gap analysis involving 150+ stakeholders. He successfully bridged qualitative user feedback with concrete system requirements by authoring URD-standard documentation.`,
      proj:`Minh's top three projects showcase his ability to execute across the full product stack:\n\n🧠 EchoMind AI — Flagship (Sep–Dec 2025)\nA BCI system decoding EEG signals into text. As Project Lead, Minh managed 8 Sprints using CPMAI, pivoting from a failing LSTM model to a successful Transformer V2 architecture. Results: 55–65 WPM, <1s latency. He also designed an Expert Dashboard with Attention Maps to tackle the healthcare "black box" problem.\n\n📚 E-Reader Ecosystem — Top 20 City Level (Mar–Jun 2025)\nAs a User Researcher, Minh mapped the HCI-focused user journey from device provisioning to content updates. Decomposed student cognitive friction into actionable feature sets. Recognized as a Top 20 Finalist by the HCMC People's Committee.\n\n🚀 Innovation Events Operations\nSuccessfully organized and coordinated large-scale events like Univ.Star and WHISE Week at SIHUB.`,
      skills:`Minh's competency profile is built on three strong pillars:\n\n◈ Product Craft (Core Strength)\n→ Journey Mapping (95%) · UX/HCI (90%) · Agile/CPMAI (88%)\n→ PRD & User Stories · A/B Testing · Problem Decomposition\n\n◈ Data & Systems Thinking\n→ Python (Familiar) · Data Analysis & EDA\n→ PyTorch / ML (Familiar) · Transformer Architectures\n\n◈ Stakeholder & Execution\n→ Managing 150+ stakeholders at the city/government level\n→ Translating complex data into strategic Board-level reports\n→ Leading cross-functional teams in Agile environments`,
      edu:`Minh is completing his final year at UEH (University of Economics HCMC), majoring in Technology & Innovation Management with a strong GPA of 3.53/4.0.\n\nKey coursework that shapes his product mindset:\n→ Human-Computer Interaction (HCI)\n→ Design Thinking\n→ Business Intelligence\n→ Project AI\n\nHe holds certifications in Google Project Management, Google Business Intelligence, and Agile Management.`
    }
  }
},

vi:{
  nav:['Tổng quan','Kinh nghiệm','Dự án','Kỹ năng','Học vấn'],
  navTip:['Tổng quan','Kinh nghiệm','Dự án','Kỹ năng','Học vấn'],
  w:{
    status:'Sẵn sàng đón nhận cơ hội Product & UX mới · TP.HCM',
    role:'Product Owner · UX Strategist · AI Builder',
    summary:`Hoàng Minh là một ứng viên trẻ về <strong style="color:var(--text)">Quản lý Công nghệ & Đổi mới Sáng tạo</strong> — có nền tảng vững chắc về UX Design, System Thinking và AI Engineering. Tôi chuyển hóa dữ liệu người dùng phức tạp và các "điểm đau" (pain points) thành trải nghiệm sản phẩm tối ưu, có thể đo lường. Từ việc lập bản đồ hành trình onboarding cho startup đến dẫn dắt một dự án AI từ tờ giấy trắng đến mô hình Transformer hoàn thiện — tôi tin sản phẩm tốt nhất được tạo ra khi sự thấu cảm người dùng kết hợp cùng tư duy hệ thống chặt chẽ.`,
    stats:['Năm kinh nghiệm','Stakeholders quản lý','KPI kỹ thuật AI','Chung cuộc cấp TP'],
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
          `<strong>Thiết kế Bản đồ Hành trình Số & Triển khai MVP:</strong> Thiết kế hành trình số (digital journey map) nhằm hỗ trợ các startup công nghệ tại SIHUB. Tôi làm việc sát sao cùng các Startup để tìm ra "nỗi đau" thực sự của khách hàng, cấu trúc chúng thành User Stories rõ ràng, triển khai MVP theo từng vòng lặp và giúp rút ngắn đáng kể time-to-first-value trong chương trình ươm tạo.`,
          `<strong>Giải quyết Pain Point dựa trên Dữ liệu:</strong> Liên tục theo dõi các touchpoints đa kênh để phát hiện điểm nghẽn vận hành. Triển khai A/B testing và Interleaving experiments để kiểm chứng chặt chẽ các thay đổi tính năng, đảm bảo mọi quyết định sản phẩm đều được chứng minh bằng dữ liệu hành vi, thay vì cảm tính.`,
          `<strong>Quản lý Stakeholder & Hệ thống NPS:</strong> Làm đầu mối trung tâm cho hơn 150 startup founders xuyên suốt hành trình ươm tạo. Phân tích dữ liệu hành vi để xây dựng dashboard NPS, báo cáo trực tiếp insight về tỷ lệ giữ chân người dùng lên Ban Giám đốc. Giúp đội ngũ chuyển đổi tư duy: nhìn nhận NPS như một hệ thống cảnh báo hành vi real-time thay vì một điểm số tĩnh.`
        ],
        tags:['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Quản lý 150+ Stakeholders','Tài liệu URD']
      },
      {
        period:'07/2024 — 12/2024',
        role:'Thực tập sinh Nghiên cứu & Phát triển (R&D Intern)',
        company:'SIHUB · Quản lý dự án dựa trên dữ liệu cho khung năng lực cấp thành phố',
        bullets:[
          `<strong>Phân tích Dữ liệu Quy mô Lớn & Lấy Yêu cầu:</strong> Dẫn dắt vòng đời dữ liệu (end-to-end) cho dự án phân tích khoảng trống năng lực trong bài nghiên cứu khoa học cấp thành phố — làm việc với 150+ stakeholders chủ chốt từ cơ quan nhà nước, viện nghiên cứu và doanh nghiệp. Thiết kế phương pháp thu thập, làm sạch đầu vào định tính và trích xuất insights để định hình chính sách.`,
          `<strong>Tài liệu hóa Chuẩn URD:</strong> Soạn thảo báo cáo chiến lược và tài liệu yêu cầu hệ thống theo chuẩn URD. Thách thức lớn nhất là làm thế nào để kết nối phản hồi định tính của người dùng với các yêu cầu hệ thống cụ thể — một kỹ năng đã trực tiếp mài giũa cách tôi viết PRD và User Stories sau này.`
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
        desc:`EchoMind khởi nguồn từ bài toán giúp bệnh nhân hội chứng khóa trong (locked-in syndrome) giao tiếp qua sóng não. Tuy nhiên, rào cản lớn nhất không chỉ nằm ở công nghệ mà ở việc dẫn dắt một nhóm đa chuyên môn đi từ số 0 đến sản phẩm hoàn thiện.\n\nTrong vai trò <strong style="color:var(--text)">Project Lead</strong>, tôi áp dụng khung CPMAI và quản lý 8 Sprints Agile. Khi mô hình LSTM ban đầu gặp 'Mode Collapse' (lặp từ liên tục) do nút thắt thông tin, tôi đã đánh giá các rủi ro và quyết đoán định hướng nhóm chuyển sang kiến trúc <strong style="color:var(--text)">Transformer V2</strong>. Đồng thời, để giải quyết giới hạn phần cứng khi Demo, tôi đưa ra giải pháp lượng tử hóa (Int8 Quantization) giúp mô hình chạy mượt trên laptop cá nhân không cần GPU.\n\nKết quả: hệ thống đạt <strong style="color:var(--text)">55-65 WPM, độ trễ &lt;1s và hoàn thành 100% KPI kỹ thuật</strong> (ROI 72% so với thiết bị truyền thống). Nhóm cũng thiết kế Expert Dashboard với Attention Maps để giải quyết bài toán "hộp đen" trong y tế, giúp bác sĩ hiểu rõ AI đang tập trung vào vùng não nào.`,
        info:[
          {l:'Kiến trúc cuối',v:'Transformer V2 · 8-head Multi-Head Attention · Positional Encoding · Label Smoothing ε=0.1'},
          {l:'Baseline vs Cuối',v:'Seq2Seq LSTM (Mode Collapse, WER ~85–90%) → Transformer V2 (Câu có cấu trúc, 6–7/10 đúng)'},
          {l:'Bộ dữ liệu',v:'Brain-to-Text \'25 (Kaggle) · EEG phi xâm lấn 256 kênh · Định dạng HDF5 · Trung bình 6,38 từ/câu'},
          {l:'Khung quản lý',v:'CPMAI 6 pha · 8 Agile Sprints · Ma trận RACI · 3.833,5 tổng giờ · 100% milestone hoàn thành'}
        ],
        metrics:[{v:'55–65',l:'Từ/phút'},{v:'<1s',l:'Độ trễ'},{v:'72%',l:'KPI kỹ thuật'},{v:'92–95%',l:'Độ chính xác'},{v:'6–7/10',l:'Câu đúng'},{v:'100%',l:'Milestone'}],
        tech:['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','Ma trận RACI','Agile/Scrum']
      },
      {
        id:'ereader',badge:'🏆 Top 20 Chung cuộc',bClass:'badge-top20',date:'Tháng 3 — 6/2025',
        name:'Hệ sinh thái E-Reader',sub:'User Researcher · Giáo dục Số TP.HCM · Chỉ đạo bởi UBND TP.HCM',
        desc:`Với vai trò <strong style="color:var(--text)">User Researcher</strong>, nhiệm vụ của tôi là đào sâu vào hành vi của học sinh để tìm ra lý do khiến các em từ bỏ thiết bị E-reader ngay ở khâu kích hoạt ban đầu. \n\nTôi đã thực hiện nghiên cứu người dùng và áp dụng nguyên lý Tương tác Người - Máy (HCI) để lập bản đồ hành trình chi tiết từ lúc mở hộp đến khi đồng bộ nội dung. Bằng cách phân rã các "điểm nghẽn" gây quá tải nhận thức, tôi đã đúc kết thành các insight cốt lõi và chuyển giao thành User Stories rõ ràng, dễ đo lường cho đội ngũ phát triển. Kết quả, dự án đã tạo ra một luồng trải nghiệm liền mạch và xuất sắc lọt Top 20 Chung cuộc cấp Thành phố.`,
        tech:['Nguyên tắc HCI','Thiết kế UX','Journey Mapping','Phân tích Pain Point','User Stories','Phân tích Cognitive Load','Figma Prototyping']
      },
      {
        id:'events',badge:'● Đang diễn ra',bClass:'badge-active',date:'Tháng 7/2024 — Hiện tại',
        name:'Vận hành Sự kiện Đổi mới Sáng tạo',sub:'Vận hành · Hệ sinh thái Startup SIHUB · TP.HCM',
        desc:`Trực tiếp tổ chức và điều phối vận hành hai sự kiện đổi mới sáng tạo quy mô lớn cấp thành phố: <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> (cuộc thi startup sinh viên flagship) và <strong style="color:var(--text)">Tuần lễ WHISE 2024</strong>. Công việc bao gồm vận hành sự kiện end-to-end, phối hợp cross-team giữa các phòng ban SIHUB và đối tác, duy trì giao tiếp liên tục với các nhà sáng lập, nhà đầu tư và chính quyền để đảm bảo trải nghiệm sự kiện hoàn hảo.`,
        tech:['Quản lý Sự kiện','Phối hợp Cross-team','Giao tiếp Stakeholder','Lập kế hoạch Vận hành']
      }
    ]
  },
  skills:{
    tag:'Năng lực Lõi',title:'Kỹ năng <span>Chuyên môn</span>',
    radarLbl:'Biểu đồ Radar Kỹ năng',certLbl:'Chứng chỉ',
    list:[
      {n:'Customer Journey Mapping',ref:'Minh chứng qua: Design Thinking (UEH)', m:['Đã thiết kế 15+ luồng người dùng (user flows) cho startup','Giảm thiểu rào cản onboarding cho 30% khách hàng mới','Tối ưu hóa 5+ touchpoints chuyển đổi quan trọng']},
      {n:'Thiết kế UX / HCI',ref:'Minh chứng qua: Human-Computer Interaction (UEH)', m:['Ứng dụng thành công vào 3 dự án thực tế','Giảm tải nhận thức (cognitive load) hệ thống E-Reader','Thiết kế giao diện Gradio đạt chuẩn Heuristic']},
      {n:'Agile / Scrum (CPMAI)',ref:'Minh chứng qua: Google Project Management & Dự án EchoMind', m:['Quản lý mượt mà 8 Sprints liên tục','Dẫn dắt đội ngũ 7 thành viên cross-functional','Hoàn thành 100% milestone dự án đúng hạn']},
      {n:'A/B Testing & Interleaving',ref:'Minh chứng qua: Human-Computer Interaction (UEH)', m:['Thiết kế và chạy 10+ thử nghiệm tính năng','Xác thực giả thuyết với độ tin cậy 95%','Ngăn chặn 3 lỗi thiết kế UX trước khi ra mắt']},
      {n:'Phân rã Vấn đề (Problem Decomposition)',ref:'Minh chứng qua: Innovation Management (UEH)', m:['Phân rã 5+ Epics cấp cao thành các task thực thi','Chẩn đoán root-cause lỗi Mode Collapse','Cấu trúc hóa 150+ yêu cầu từ các stakeholders']},
      {n:'Viết PRD & User Stories',ref:'Minh chứng qua: Entrepreneurship Innovation (UEH)', m:['Soạn thảo 10+ PRD chuẩn hóa','Quản lý backlog với 200+ User Stories','Đạt chuẩn tài liệu URD cấp thành phố']},
      {n:'Python & PyTorch (Có nền tảng)',ref:'Ứng dụng qua: Lập trình cơ bản, Nâng cao & EchoMind', m:['Tối ưu kiến trúc mô hình Transformer V2','Áp dụng lượng tử hóa Int8 giảm dung lượng','Giảm độ trễ suy luận AI xuống dưới 1s']}
    ],
    radarLabels:['UX/HCI','Agile','Journey Map','Phân tích DL','Python','PyTorch/ML','A/B Testing'],
    certs:[
      {i:'🏅',n:'Quản lý Dự án (Google Project Management)',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp',dash:false},
    ]
  },
  edu:{
    tag:'Nền tảng Học vấn',title:'Học vấn & <span>Thành tích</span>',
    uni:'Đại học Kinh tế TP.HCM (UEH)',major:'Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo',
    courseTag:'Các môn học Cốt lõi định hình Tư duy Sản phẩm',
    courses:['Tư duy Thiết kế (Design Thinking)','Tương tác Người-Máy (HCI)','Quản trị Đổi mới Sáng tạo','Trí tuệ Doanh nghiệp (BI)','Chuyển đổi Kinh doanh Số','Dự án AI'],
    certTag:'Chứng chỉ',
    certs:[
      {i:'🏅',n:'Quản lý Dự án (Google Project Management)',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',dash:false, link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp',dash:false},
    ]
  },
  chat:{
    name:'Trợ lý AI của Minh',sub:'● Trực tuyến · Sẵn sàng giải đáp',reset:'↺ Làm lại',logout:'⏻ Ngôn ngữ',
    greeting:`Xin chào! Tôi là AI đại diện cho Nguyễn Hoàng Minh — Product Owner & UX Strategist xây dựng sản phẩm tại giao điểm của thiết kế trải nghiệm người dùng, tư duy hệ thống và AI Engineering.\n\nMinh đang tìm kiếm các cơ hội Product và UX để cống hiến khả năng thiết kế hành trình người dùng và thực thi sản phẩm chuyên nghiệp. Bạn muốn tìm hiểu khía cạnh nào trong hồ sơ của Minh?`,
    prompts:[
      {id:'exp',i:'💼',l:'Kinh nghiệm'},
      {id:'proj',i:'🧠',l:'Dự án'},
      {id:'skills',i:'⚡',l:'Kỹ năng'},
      {id:'edu',i:'🎓',l:'Học vấn'}
    ],
    ans:{
      exp:`Minh có hơn 2 năm kinh nghiệm làm việc tại SIHUB (Sở KH&CN TP.HCM).\n\n◈ 01–10/2025 | Project Management Executive\nMinh không chỉ vẽ các luồng quy trình (flowchart); Minh áp dụng A/B testing và Interleaving để kiểm chứng mọi thay đổi bằng dữ liệu thật. Minh cũng thay đổi góc nhìn của đội ngũ về NPS, coi đó là một hệ thống tín hiệu hành vi theo thời gian thực thay vì một điểm số tĩnh.\n\n◈ 07–12/2024 | R&D Intern\nDẫn dắt dự án phân tích với hơn 150 bên liên quan, thành công trong việc biên dịch các nhu cầu định tính phức tạp của người dùng thành tài liệu yêu cầu hệ thống chuẩn URD.`,
      proj:`Ba dự án nổi bật minh chứng cho tư duy phát triển sản phẩm toàn diện của Minh:\n\n🧠 EchoMind AI — Flagship (09–12/2025)\nHệ thống giải mã sóng não (EEG) thành văn bản. Là Project Lead, Minh quản lý 8 Sprints theo khung CPMAI, quyết đoán chuyển đổi từ mô hình LSTM thất bại sang kiến trúc Transformer V2. Áp dụng lượng tử hóa (Int8) để chạy mượt không cần GPU. Kết quả: 55–65 WPM, KPI kỹ thuật 72%. Thiết kế Expert Dashboard với Attention Maps.\n\n📚 Hệ sinh thái E-Reader — Top 20 cấp TP (03–06/2025)\nTrong vai trò User Researcher, Minh thiết kế hành trình người dùng áp dụng nguyên lý HCI nhằm giảm tải nhận thức cho học sinh. Xuất sắc lọt Top 20 cuộc thi do UBND TP.HCM chỉ đạo.\n\n🚀 Vận hành Sự kiện ĐMST\nĐiều phối thành công các sự kiện quy mô lớn như Univ.Star và Tuần lễ WHISE.`,
      skills:`Năng lực cốt lõi của Minh được xây dựng trên 3 trụ cột vững chắc:\n\n◈ Product Craft (Thế mạnh Cốt lõi)\n→ Lập bản đồ hành trình (95%) · UX/HCI (90%) · Agile/CPMAI (88%)\n→ Viết PRD & User Stories · Kiểm thử A/B · Phân rã Vấn đề\n\n◈ Dữ liệu & Tư duy Hệ thống\n→ Python (Có nền tảng) · Phân tích Dữ liệu (EDA)\n→ Am hiểu PyTorch và kiến trúc Transformer (thể hiện qua EchoMind)\n\n◈ Quản lý Stakeholder & Thực thi\n→ Kinh nghiệm làm việc với 150+ đối tác cấp thành phố/chính quyền\n→ Trình bày báo cáo chiến lược cấp Ban Giám đốc\n→ Dẫn dắt đội ngũ kỹ thuật vận hành theo quy trình Agile`,
      edu:`Minh đang là sinh viên năm cuối tại Đại học Kinh tế TP.HCM (UEH), chuyên ngành Quản lý Công nghệ & Đổi mới Sáng tạo với điểm số ấn tượng GPA 3.53/4.0.\n\nNhững môn học định hình tư duy sản phẩm của Minh gồm:\n→ Tương tác Người - Máy (HCI)\n→ Tư duy Thiết kế (Design Thinking)\n→ Trí tuệ Doanh nghiệp (BI)\n→ Dự án AI\n\nMinh cũng sở hữu các chứng chỉ chuyên nghiệp từ Google về Quản lý Dự án và Business Intelligence.`
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

  // Skills (LinkedIn Style w/ Popups)
  document.getElementById('s-tag').textContent = t.skills.tag;
  document.getElementById('s-title').innerHTML = t.skills.title;
  document.getElementById('s-radar-lbl').textContent = t.skills.radarLbl;
  document.getElementById('s-cert-lbl').textContent = t.skills.certLbl;
  
  document.getElementById('s-list').innerHTML = t.skills.list.map(sk => `
    <div class="lk-skill-card">
      <div class="lk-skill-header">
        <div class="lk-skill-title"><span style="color:var(--accent2); font-size:18px;">❖</span> ${sk.n}</div>
        <span style="font-size:14px; opacity:0.5; color:var(--text2);">ℹ️</span>
      </div>
      <div class="lk-skill-ref">${sk.ref}</div>
      <div class="skill-popup">
        <div class="popup-title">${lang === 'en' ? 'Metrics & Impact' : 'Định lượng & Tác động'}</div>
        ${sk.m.map(metric => `<div class="popup-metric">${metric}</div>`).join('')}
      </div>
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
    <div style="display:flex;flex-wrap:wrap;gap:10px;">${t.edu.courses.map(c => `<span style="font-family:'Montserrat',sans-serif;font-weight:500;font-size:12px;padding:7px 16px;background:var(--surface);border:1px solid var(--border2);border-radius:9px;color:var(--text2);">${c}</span>`).join('')}</div>
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
  return certs.map(c => {
    const tag = c.link ? 'a' : 'div';
    const href = c.link ? ` href="${c.link}" target="_blank" rel="noopener noreferrer"` : '';
    const hoverIcon = c.link ? `<div style="color:var(--text2); opacity:0.5; font-size:16px; transition:opacity 0.2s;" class="cert-link-icon">↗</div>` : '';
    
    return `
    <${tag} class="cert-card" style="${c.dash ? 'border-style:dashed;border-color:rgba(240,192,96,.3);' : ''} text-decoration:none;"${href}>
      <span style="font-size:22px;flex-shrink:0;">${c.i}</span>
      <div style="flex:1;">
        <div style="color:var(--text);font-family:'Montserrat',sans-serif;font-size:13px;font-weight:600;">${c.n}</div>
        <div style="font-family:'Montserrat',sans-serif;font-size:11px;color:var(--text2);margin-top:4px;">${c.org}</div>
      </div>
      ${c.prog ? `<span style="font-family:'Montserrat',sans-serif;font-weight:600;font-size:9.5px;color:var(--gold);padding:4px 12px;background:rgba(240,192,96,.1);border-radius:20px;white-space:nowrap;">${c.prog}</span>` : ''}
      ${hoverIcon}
    </${tag}>
    `;
  }).join('');
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
            <div class="proj-chart-wrap">
              <div class="proj-chart-title" id="kpi-chart-title">Technical KPI Breakdown — vs Traditional AAC</div>
              <div style="height:200px;position:relative;"><canvas id="kpiChart"></canvas></div>
            </div>
            <div class="proj-chart-wrap">
              <div class="proj-chart-title" id="model-chart-title">Model Comparison: LSTM V1 vs Transformer V2</div>
              <div style="height:180px;position:relative;"><canvas id="modelChart"></canvas></div>
            </div>
            <div class="tech-stack">${p.tech.map(tch => `<span class="tech-pill">${tch}</span>`).join('')}</div>
          </div>
          <div style="background:var(--ink3);border-radius:18px;border:1px solid var(--border);padding:22px;text-align:center;">
            <div style="font-size:40px;margin-bottom:14px;">🧠</div>
            <div style="font-family:'Montserrat',sans-serif;font-weight:500;font-size:11px;color:var(--accent2);line-height:2.2;text-align:left;">
              EEG Input (256ch)<br>↓ HDF5 → Tensor<br>↓ Positional Enc.<br>↓ Transformer V2<br>↓ Int8 Quantization<br>↓ Gradio Expert UI<br>→ Text Output
            </div>
            <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
              <div style="font-family:'Montserrat',sans-serif;font-weight:600;font-size:9px;color:var(--text2);margin-bottom:4px;" id="ec-role-lbl">Role</div>
              <div style="font-family:'Montserrat',sans-serif;font-size:12px;color:var(--text);font-weight:600;">Project Lead</div>
              <div style="font-family:'Montserrat',sans-serif;font-weight:600;font-size:9px;color:var(--text2);margin:10px 0 4px;" id="ec-team-lbl">Team</div>
              <div style="font-family:'Montserrat',sans-serif;font-size:12px;color:var(--text);">7 members · 8 sprints</div>
              <div style="font-family:'Montserrat',sans-serif;font-weight:600;font-size:9px;color:var(--text2);margin:10px 0 4px;" id="ec-adv-lbl">Advisor</div>
              <div style="font-family:'Montserrat',sans-serif;font-size:11px;color:var(--text2);">ThS. Tạ Việt Phương</div>
            </div>
            <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
              <div style="font-family:'Montserrat',sans-serif;font-weight:600;font-size:9px;color:var(--accent2);letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;" id="ec-sprint-lbl">Sprint Burndown</div>
              <div style="height:140px;position:relative;"><canvas id="burndownChart"></canvas></div>
            </div>
          </div>
        </div>`;
    } else {
      return `
        <div class="project-card">
          <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:12px;">
            <span class="project-badge ${p.bClass}">${p.badge}</span>
            <span style="font-family:'Montserrat',sans-serif;font-weight:500;font-size:10px;color:var(--text2);">${p.date}</span>
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
    renderKPIChart();
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
    const rlt = document.getElementById('kpi-chart-title');
    const mlt = document.getElementById('model-chart-title');
    if (rlt) rlt.textContent = lang === 'en' ? 'Technical KPI Breakdown — vs Traditional AAC' : 'Phân tích KPI Kỹ thuật — So với AAC Truyền thống';
    if (mlt) mlt.textContent = lang === 'en' ? 'Model Comparison: LSTM V1 vs Transformer V2' : 'So sánh Mô hình: LSTM V1 vs Transformer V2';
  }, 60);
}

function renderKPIChart() {
  const ctx = document.getElementById('kpiChart');
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
        y: { grid: { color: 'rgba(255,255,255,.05)' }, ticks: { color: '#9898b0', font: { family: "'Montserrat',sans-serif", size: 10, weight: '500' } }, max: 100, min: 0 }
      },
      plugins: {
        legend: { labels: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 11 }, boxWidth: 12 } },
        tooltip: { backgroundColor: '#252538', titleFont: { family: "'Montserrat',sans-serif" }, bodyFont: { family: "'DM Sans',sans-serif" }, borderColor: 'rgba(255,255,255,.1)', borderWidth: 1,
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
      scales: { r: { min: 0, max: 100, ticks: { display: false }, angleLines: { color: 'rgba(255,255,255,.07)' }, grid: { color: 'rgba(255,255,255,.07)' }, pointLabels: { color: '#9898b0', font: { size: 10, family: "'DM Sans',sans-serif", weight: '500' } } } },
      plugins: { legend: { labels: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 11 }, boxWidth: 12, padding: 14 } }, tooltip: { backgroundColor: '#252538', titleFont: { family: "'Montserrat',sans-serif" }, bodyFont: { family: "'DM Sans',sans-serif" }, borderColor: 'rgba(255,255,255,.1)', borderWidth: 1 } }
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
        x: { grid: { display: false }, ticks: { color: '#5a5a78', font: { family: "'Montserrat',sans-serif", size: 9, weight: '500' } } },
        y: { grid: { color: 'rgba(255,255,255,.04)' }, ticks: { color: '#5a5a78', font: { family: "'Montserrat',sans-serif", size: 9, weight: '500' }, callback: v => (v/1000).toFixed(1)+'k' } }
      },
      plugins: { legend: { labels: { color: '#9898b0', font: { family: "'DM Sans',sans-serif", size: 10 }, boxWidth: 10, padding: 10 } }, tooltip: { backgroundColor: '#252538', titleFont: { family: "'Montserrat',sans-serif" }, bodyFont: { family: "'DM Sans',sans-serif" }, borderColor: 'rgba(255,255,255,.1)', borderWidth: 1 } }
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
      setTimeout(() => { initSkillsChart(); }, 60);
    }
    if (viewId === 'projects') {
      setTimeout(() => { renderKPIChart(); renderModelChart(); renderBurndownChart(); }, 60);
    }

    const animEls = target.querySelectorAll('.fade-up');
    animEls.forEach(el => { el.style.animation = 'none'; void el.offsetWidth; el.style.animation = null; });

    setTimeout(() => { tr.classList.remove('active'); isTrans = false; }, 120);
  }, 260);
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
      datasets: [{ data: [95, 88, 95, 80, 65, 65, 82], fill: true, backgroundColor: 'rgba(124,106,247,.14)', borderColor: '#7c6af7', pointBackgroundColor: '#a594fc', pointBorderColor: '#1e1e2e', borderWidth: 2, pointRadius: 4 }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: { r: { min: 0, max: 100, ticks: { display: false }, angleLines: { color: 'rgba(255,255,255,.07)' }, grid: { color: 'rgba(255,255,255,.07)' }, pointLabels: { font: { size: 11, family: "'Montserrat',sans-serif", weight: '600' }, color: '#9898b0' } } },
      plugins: { legend: { display: false }, tooltip: { backgroundColor: '#252538', borderColor: 'rgba(255,255,255,.1)', borderWidth: 1, padding: 12, callbacks: { label: c => { const v = c.raw; if (lang === 'vi') return v >= 90 ? ' Chuyên gia' : v >= 80 ? ' Cao cấp' : v >= 70 ? ' Thành thạo' : ' Có nền tảng'; return v >= 90 ? ' Expert' : v >= 80 ? ' Advanced' : v >= 70 ? ' Proficient' : ' Familiar'; } } } }
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
    `<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.l}')" ${isTyping || isTrans ? 'disabled' : ''}>
      <span class="p-icon">${p.i}</span><span class="p-lbl">${p.l}</span>
    </button>`
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
