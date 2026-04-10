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

/* ========== TOAST NOTIFICATION ========== */
#toast{
  position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(16px);
  background:var(--surface2);border:1px solid var(--green);color:var(--green);
  font-family:'DM Mono',monospace;font-size:12px;padding:10px 22px;border-radius:10px;
  z-index:99999;opacity:0;transition:all .35s cubic-bezier(.16,1,.3,1);
  pointer-events:none;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.35);
  letter-spacing:.5px;
}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0);}

/* ========== FLOATING SKILL POPUP ========== */
#float-popup{
  position:fixed;width:300px;
  background:rgba(18,18,26,0.97);border:1px solid var(--accent);border-radius:14px;
  padding:16px 18px;box-shadow:0 20px 50px rgba(0,0,0,.6);backdrop-filter:blur(12px);
  opacity:0;visibility:hidden;transition:opacity .22s ease,visibility .22s ease;
  pointer-events:none;z-index:99998;
}
.popup-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;}
.popup-metric{font-size:13px;color:var(--text);line-height:1.5;display:flex;align-items:start;gap:8px;margin-bottom:8px;}
.popup-metric:last-child{margin-bottom:0;}
.popup-metric::before{content:'•';color:var(--green);font-weight:bold;flex-shrink:0;}

/* ========== SCROLL PROGRESS ========== */
#scroll-progress{position:fixed;top:0;left:90px;height:3px;background:linear-gradient(90deg,var(--accent),var(--teal));width:0%;z-index:1000;transition:width .1s ease-out;border-radius:0 2px 2px 0;}

/* ========== LANGUAGE OVERLAY ========== */
#lang-overlay{
  position:fixed;inset:0;background:var(--ink);z-index:9999;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;
  transition:opacity .5s ease,visibility .5s;
}
.lo-logo{font-family:'Syne',sans-serif;font-size:64px;font-weight:800;color:var(--accent2);letter-spacing:-3px;line-height:1;}
.lo-tagline{font-family:'Montserrat',sans-serif;font-size:12px;color:var(--text2);letter-spacing:3px;text-transform:uppercase;}
.lo-question{font-family:'Syne',sans-serif;font-size:22px;font-weight:600;color:var(--text);text-align:center;line-height:1.5;}
.lo-options{display:flex;gap:20px;align-items:stretch;}

/* Buttons are completely neutral until hovered */
.lo-btn{
  background:var(--surface);border:2px solid var(--border2);color:var(--text2);
  padding:20px 48px;border-radius:14px;font-family:'Syne',sans-serif;font-size:20px;font-weight:600;
  cursor:pointer;transition:all .3s cubic-bezier(.16,1,.3,1);display:flex;flex-direction:column;
  align-items:center;gap:8px;
}
.lo-btn:hover{
  background:var(--accent);
  border-color:var(--accent2);
  color:white;
  transform:translateY(-5px);
  box-shadow:0 14px 36px rgba(124,106,247,.5);
}
.lo-kbhint{font-family:'DM Mono',monospace;font-size:11px;color:var(--text3);letter-spacing:1px;text-align:center;}

/* ========== APP LAYOUT ========== */
.app{display:flex;height:100vh;width:100%;opacity:0;transition:opacity .7s ease;}
.app.visible{opacity:1;}

/* ========== SIDENAV ========== */
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
.nav-tooltip{position:absolute;left:74px;background:var(--surface2);color:var(--text);font-size:12px;font-family:'DM Mono',monospace;padding:6px 12px;border-radius:7px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .15s;border:1px solid var(--border2);z-index:100;}
.nav-item:hover .nav-tooltip{opacity:1;}
.nav-spacer{flex:1;}
/* Keyboard hint in nav */
.nav-kbd{
  font-family:'DM Mono',monospace;font-size:9px;color:var(--text3);
  background:var(--surface);border:1px solid var(--border);
  border-radius:4px;padding:2px 5px;margin-top:2px;display:none;
}
.nav-item:hover .nav-kbd{display:block;}

/* ========== VISUAL PANEL ========== */
.visual-panel{flex:1;height:100%;overflow-y:auto;background:var(--ink);position:relative;}
.visual-panel::-webkit-scrollbar{width:5px;}
.visual-panel::-webkit-scrollbar-thumb{background:var(--border2);border-radius:5px;}

/* ========== TRANSITION OVERLAY ========== */
.view-tr{position:fixed;top:0;left:90px;right:420px;bottom:0;background:var(--ink);z-index:999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .25s ease;}
.view-tr.active{opacity:1;pointer-events:all;}
.spinner{width:36px;height:36px;border:3px solid var(--border2);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;}
@keyframes spin{100%{transform:rotate(360deg);}}

/* ========== CHAT PANEL ========== */
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

/* ========== NOISE ========== */
.noise{position:fixed;inset:0;opacity:.025;pointer-events:none;z-index:100;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* ========== SHARED VIEW STYLES ========== */
.view-content{padding:60px 72px;min-height:100%;position:relative;}
.section-tag{display:inline-flex;align-items:center;gap:8px;font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);text-transform:uppercase;letter-spacing:2.5px;margin-bottom:20px;}
.section-tag::before{content:'◈';font-size:13px;}
.view-title{font-family:'Syne',sans-serif;font-size:46px;font-weight:800;letter-spacing:-1.5px;color:var(--text);margin-bottom:52px;line-height:1;}
.view-title span{color:var(--accent2);}
.subtle-div{height:1px;background:var(--border);margin:44px 0;}

/* ========== WELCOME VIEW ========== */
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
.contact-chip.copyable{cursor:pointer;}
.contact-chip.copyable:hover{border-color:var(--green);color:var(--green);}
.stat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;max-width:700px;margin-bottom:52px;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:18px;padding:22px 18px;position:relative;overflow:hidden;transition:transform .25s,box-shadow .25s;}
.stat-card:hover{transform:translateY(-3px);box-shadow:0 12px 25px rgba(0,0,0,.2);}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--accent),var(--teal));}
.stat-number{font-family:'Syne',sans-serif;font-size:34px;font-weight:800;color:var(--text);line-height:1;}
.stat-label{font-size:11px;color:var(--text2);margin-top:8px;text-transform:uppercase;letter-spacing:.7px;font-family:'DM Mono',monospace;}

/* ========== TIMELINE ========== */
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

/* ========== PROJECTS ========== */
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

/* ======================================================
   UX EXPERIENCE SECTION — All styles
   ====================================================== */

/* Design Thinking Flow */
.dt-flow{display:flex;align-items:stretch;gap:0;margin-bottom:52px;position:relative;}
.dt-phase{flex:1;background:var(--surface);border:1px solid var(--border);padding:20px 16px;position:relative;transition:all .25s;cursor:default;}
.dt-phase:first-child{border-radius:16px 0 0 16px;}
.dt-phase:last-child{border-radius:0 16px 16px 0;}
.dt-phase:hover{background:var(--surface2);z-index:2;transform:translateY(-3px);box-shadow:0 12px 28px rgba(0,0,0,.25);}
.dt-phase-icon{font-size:24px;margin-bottom:10px;display:block;}
.dt-phase-name{font-family:'Syne',sans-serif;font-size:13px;font-weight:700;color:var(--text);margin-bottom:6px;}
.dt-phase-desc{font-size:11.5px;color:var(--text2);line-height:1.6;}
.dt-phase-num{position:absolute;top:10px;right:12px;font-family:'DM Mono',monospace;font-size:10px;color:var(--text3);}
/* Arrow connector between phases */
.dt-phase+.dt-phase::before{content:'';position:absolute;left:-1px;top:50%;transform:translateY(-50%);width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:10px solid var(--border2);z-index:3;}
/* Color accent top bar per phase */
.dt-phase:nth-child(1)::after{background:var(--accent);}
.dt-phase:nth-child(2)::after{background:var(--coral);}
.dt-phase:nth-child(3)::after{background:var(--gold);}
.dt-phase:nth-child(4)::after{background:var(--green);}
.dt-phase:nth-child(5)::after{background:var(--teal);}
.dt-phase:nth-child(6)::after{background:var(--blue);}
.dt-phase::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:inherit;}

/* Case Study */
.case-study{background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:36px;margin-bottom:28px;position:relative;overflow:hidden;}
.case-study::before{content:'';position:absolute;top:0;left:0;bottom:0;width:4px;}
.case-study.cs-sihub::before{background:linear-gradient(to bottom,var(--accent),var(--teal));}
.case-study.cs-echomind::before{background:linear-gradient(to bottom,var(--coral),var(--gold));}
.case-study.cs-ereader::before{background:linear-gradient(to bottom,var(--green),var(--teal));}

.cs-header{display:flex;align-items:start;justify-content:space-between;margin-bottom:28px;gap:20px;}
.cs-meta{flex:1;}
.cs-eyebrow{display:flex;align-items:center;gap:10px;margin-bottom:10px;}
.cs-num{font-family:'DM Mono',monospace;font-size:11px;color:var(--text3);letter-spacing:1px;}
.cs-tag{font-family:'Montserrat',sans-serif;font-size:10px;font-weight:500;padding:3px 10px;border-radius:20px;border:1px solid var(--border2);color:var(--text2);}
.cs-title{font-family:'Syne',sans-serif;font-size:26px;font-weight:800;letter-spacing:-.5px;margin-bottom:6px;}
.cs-role{font-size:13px;color:var(--text2);font-style:italic;}
.cs-impact-badge{background:var(--ink3);border:1px solid var(--border2);border-radius:16px;padding:18px 22px;text-align:center;min-width:140px;flex-shrink:0;}
.cs-impact-num{font-family:'Syne',sans-serif;font-size:32px;font-weight:800;color:var(--green);line-height:1;}
.cs-impact-lbl{font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);text-transform:uppercase;letter-spacing:.8px;margin-top:5px;}

/* Case study body sections */
.cs-body{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-bottom:28px;}
.cs-section-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:14px;display:flex;align-items:center;gap:8px;}
.cs-section-title::before{content:'';width:20px;height:2px;background:var(--accent2);display:inline-block;}
.cs-text{font-size:14.5px;color:var(--text2);line-height:1.75;}
.cs-text strong{color:var(--text);font-weight:500;}

/* Problem box */
.problem-box{background:rgba(255,123,107,.07);border:1px solid rgba(255,123,107,.2);border-radius:14px;padding:18px 20px;margin-bottom:20px;}
.problem-label{font-family:'DM Mono',monospace;font-size:9px;color:var(--coral);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px;display:flex;align-items:center;gap:6px;}
.problem-label::before{content:'⚠';font-size:12px;}
.problem-text{font-size:14.5px;color:var(--text2);line-height:1.7;}
.problem-text strong{color:var(--text);}

/* Insight box */
.insight-box{background:rgba(124,106,247,.08);border:1px solid rgba(124,106,247,.25);border-radius:14px;padding:18px 20px;margin-bottom:16px;}
.insight-label{font-family:'DM Mono',monospace;font-size:9px;color:var(--accent2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px;display:flex;align-items:center;gap:6px;}
.insight-label::before{content:'💡';font-size:12px;}
.insight-text{font-size:14px;color:var(--text2);line-height:1.7;}
.insight-text strong{color:var(--text);}

/* Process steps */
.process-steps{display:flex;flex-direction:column;gap:10px;}
.process-step{display:flex;gap:14px;align-items:start;padding:12px 14px;background:var(--ink3);border-radius:10px;border:1px solid var(--border);transition:border-color .2s;}
.process-step:hover{border-color:var(--border2);}
.step-num{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);min-width:20px;font-weight:bold;margin-top:2px;}
.step-content{flex:1;}
.step-title{font-size:13.5px;font-weight:600;color:var(--text);margin-bottom:3px;}
.step-desc{font-size:12.5px;color:var(--text2);line-height:1.55;}

/* A/B Test Visualization */
.ab-container{background:var(--ink3);border-radius:14px;border:1px solid var(--border);padding:20px;margin-bottom:16px;}
.ab-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:16px;}
.ab-variants{display:flex;flex-direction:column;gap:10px;}
.ab-row{display:flex;align-items:center;gap:14px;}
.ab-variant-lbl{font-family:'DM Mono',monospace;font-size:11px;min-width:80px;color:var(--text2);}
.ab-bar-track{flex:1;height:28px;background:var(--surface2);border-radius:6px;overflow:hidden;position:relative;}
.ab-bar-fill{height:100%;border-radius:6px;display:flex;align-items:center;padding-left:10px;font-family:'DM Mono',monospace;font-size:11px;font-weight:bold;color:white;transition:width 1.2s cubic-bezier(.16,1,.3,1);}
.ab-bar-fill.control{background:rgba(90,90,120,.6);}
.ab-bar-fill.variant{background:linear-gradient(90deg,var(--accent),var(--accent2));}
.ab-bar-fill.winner{background:linear-gradient(90deg,var(--green),var(--teal));}
.ab-badge{font-family:'DM Mono',monospace;font-size:10px;padding:3px 9px;border-radius:5px;white-space:nowrap;}
.ab-badge.win{background:rgba(82,209,138,.15);color:var(--green);border:1px solid rgba(82,209,138,.3);}
.ab-badge.sig{background:rgba(77,217,192,.12);color:var(--teal);border:1px solid rgba(77,217,192,.25);}
.ab-stat{font-size:11px;color:var(--text3);margin-top:6px;font-family:'DM Mono',monospace;}

/* Journey Map */
.journey-map{margin-bottom:20px;}
.journey-header{display:grid;gap:0;margin-bottom:0;}
.journey-row-wrap{display:flex;flex-direction:column;gap:1px;}
.jm-stage-row{display:grid;align-items:stretch;gap:1px;}
.jm-label{font-family:'DM Mono',monospace;font-size:10px;color:var(--text2);text-transform:uppercase;letter-spacing:1px;padding:10px 14px;background:var(--ink3);border-radius:6px 0 0 6px;display:flex;align-items:center;min-width:110px;flex-shrink:0;}
.jm-cells{display:flex;flex:1;gap:1px;}
.jm-cell{flex:1;padding:9px 10px;background:var(--ink3);font-size:12px;color:var(--text2);line-height:1.45;min-height:48px;display:flex;align-items:center;justify-content:center;text-align:center;}
.jm-cell.stage-name{background:var(--surface2);font-family:'DM Mono',monospace;font-size:10px;font-weight:600;color:var(--accent2);letter-spacing:.5px;text-align:center;}
.jm-cell.pain{background:rgba(255,123,107,.1);color:var(--coral);}
.jm-cell.pain.high{background:rgba(255,123,107,.22);font-weight:600;}
.jm-cell.solution{background:rgba(82,209,138,.1);color:var(--green);}
.jm-cell.emotion-low{font-size:18px;background:rgba(255,123,107,.08);}
.jm-cell.emotion-mid{font-size:18px;background:rgba(240,192,96,.08);}
.jm-cell.emotion-high{font-size:18px;background:rgba(82,209,138,.1);}

/* Before/After Impact */
.impact-compare{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:center;margin-bottom:20px;}
.impact-col{background:var(--ink3);border-radius:14px;border:1px solid var(--border);padding:18px;}
.impact-col.before{border-color:rgba(255,123,107,.25);}
.impact-col.after{border-color:rgba(82,209,138,.25);}
.impact-col-label{font-family:'DM Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;}
.impact-col.before .impact-col-label{color:var(--coral);}
.impact-col.after .impact-col-label{color:var(--green);}
.impact-metric-row{display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-bottom:1px solid var(--border);}
.impact-metric-row:last-child{border-bottom:none;}
.impact-metric-name{font-size:12.5px;color:var(--text2);}
.impact-metric-val{font-family:'DM Mono',monospace;font-size:13px;font-weight:600;}
.impact-col.before .impact-metric-val{color:var(--coral);}
.impact-col.after .impact-metric-val{color:var(--green);}
.impact-arrow{font-size:28px;color:var(--accent2);text-align:center;}

/* Learnings */
.cs-learnings{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px;padding-top:24px;border-top:1px solid var(--border);}
.learning-card{background:var(--ink3);border-radius:12px;padding:16px;border:1px solid var(--border);}
.learning-icon{font-size:20px;margin-bottom:8px;display:block;}
.learning-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;}
.learning-text{font-size:12.5px;color:var(--text2);line-height:1.6;}

/* SKILLS */
.skills-layout{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start;}
#s-list{overflow:visible;}
.lk-skill-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:18px 20px;margin-bottom:14px;display:flex;flex-direction:column;gap:8px;transition:all .2s ease;position:relative;cursor:help;}
.lk-skill-card:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 8px 20px rgba(0,0,0,.15);}
.lk-skill-header{display:flex;justify-content:space-between;align-items:center;}
.lk-skill-title{font-size:15px;font-weight:600;color:var(--text);display:flex;align-items:center;gap:10px;}
.lk-skill-ref{font-family:'Montserrat',sans-serif;font-weight:500;font-size:11px;color:var(--text2);display:flex;align-items:center;gap:6px;line-height:1.4;}
.lk-skill-ref::before{content:'↳';color:var(--accent2);font-weight:bold;font-family:'DM Sans',sans-serif;}
.cert-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:15px 18px;margin-bottom:10px;display:flex;align-items:center;gap:14px;transition:transform .2s,border-color .2s;position:relative;}
a.cert-card{cursor:pointer;color:inherit;text-decoration:none;}
a.cert-card:hover{transform:translateX(4px);border-color:var(--accent);box-shadow:0 6px 16px rgba(124,106,247,.15);}
a.cert-card:hover .cert-link-icon{opacity:1 !important;color:var(--accent2) !important;}
.skills-chart-wrap{background:var(--ink3);border-radius:16px;border:1px solid var(--border);padding:20px;margin-bottom:24px;}

/* EDUCATION */
.edu-hero{background:linear-gradient(135deg,var(--surface),var(--surface2));border:1px solid var(--border);border-radius:24px;padding:40px;margin-bottom:28px;position:relative;overflow:hidden;}
.edu-hero::before{content:'UEH';position:absolute;right:-15px;bottom:-45px;font-family:'Syne',sans-serif;font-size:180px;font-weight:800;color:rgba(255,255,255,.025);line-height:1;pointer-events:none;user-select:none;}
.gpa-badge{display:inline-flex;align-items:center;gap:14px;background:rgba(240,192,96,.1);border:1px solid rgba(240,192,96,.3);border-radius:16px;padding:16px 24px;margin-top:18px;}
.gpa-val{font-family:'Syne',sans-serif;font-size:30px;font-weight:800;color:var(--gold);}

/* ANIMATIONS */
.fade-up{animation:fadeUp .6s ease-out forwards;opacity:0;}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px);}to{opacity:1;transform:translateY(0);}}
.d1{animation-delay:.1s}.d2{animation-delay:.2s}.d3{animation-delay:.3s}.d4{animation-delay:.4s}.d5{animation-delay:.5s}.d6{animation-delay:.6s}
.ab-animate .ab-bar-fill{width:0 !important;}
.ab-animate.ready .ab-bar-fill{width:var(--target-w);}

/* RESPONSIVE */
@media(max-width:1200px){
  .chat-panel{width:360px;}
  .view-tr{right:360px;}
  .view-content{padding:44px 48px;}
  .stat-grid{grid-template-columns:repeat(2,1fr);}
  .skills-layout{grid-template-columns:1fr;gap:24px;}
  .cs-body{grid-template-columns:1fr;}
  .cs-learnings{grid-template-columns:1fr 1fr;}
  .impact-compare{grid-template-columns:1fr auto 1fr;}
  .dt-flow{flex-wrap:wrap;gap:8px;}
  .dt-phase{flex:calc(33% - 8px);border-radius:12px !important;}
  .dt-phase+.dt-phase::before{display:none;}
}
@media(max-width:900px){
  .chat-panel{display:none;}
  .view-tr{left:72px;right:0;}
  .projects-grid,.cs-body,.cs-learnings{grid-template-columns:1fr;}
  .project-card.featured{grid-template-columns:1fr;}
  .impact-compare{grid-template-columns:1fr;}
  .impact-arrow{transform:rotate(90deg);padding:4px 0;}
  #scroll-progress{left:72px;}
  .sidenav{width:72px;}
  .nav-item{width:46px;height:46px;}
  .dt-flow{flex-wrap:wrap;gap:8px;}
  .dt-phase{flex:calc(50% - 4px);border-radius:12px !important;}
  .dt-phase+.dt-phase::before{display:none;}
}
</style>
</head>
<body>

<div id="toast"></div>
<div id="float-popup"><div class="popup-title" id="fp-title"></div><div id="fp-metrics"></div></div>
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
  <div class="lo-kbhint" style="margin-top:12px;">Press <strong style="color:var(--text2)">1–6</strong> to navigate · <strong style="color:var(--text2)">Esc</strong> to return</div>
</div>

<div class="app" id="main-app">
  <nav class="sidenav">
    <div class="nav-logo">HM</div>
    <div class="nav-item active" data-view="welcome" onclick="go('welcome',this)"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><span class="nav-lbl" id="nl0">Home</span><span class="nav-tooltip" id="ntt0">Overview</span></div>
    <div class="nav-item" data-view="experience" onclick="go('experience',this)"><svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg><span class="nav-lbl" id="nl1">Career</span><span class="nav-tooltip" id="ntt1">Experience</span></div>
    <div class="nav-item" data-view="projects" onclick="go('projects',this)"><svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg><span class="nav-lbl" id="nl2">Work</span><span class="nav-tooltip" id="ntt2">Projects</span></div>
    <div class="nav-item" data-view="ux" onclick="go('ux',this)"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg><span class="nav-lbl" id="nl3">UX</span><span class="nav-tooltip" id="ntt3">UX Work</span></div>
    <div class="nav-item" data-view="skills" onclick="go('skills',this)"><svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg><span class="nav-lbl" id="nl4">Skills</span><span class="nav-tooltip" id="ntt4">Skills</span></div>
    <div class="nav-item" data-view="education" onclick="go('education',this)"><svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg><span class="nav-lbl" id="nl5">School</span><span class="nav-tooltip" id="ntt5">Education</span></div>
    <div class="nav-spacer"></div>
  </nav>

  <main class="visual-panel" id="visual-panel">
    <div class="view-tr" id="view-tr"><div class="spinner"></div></div>

    <div id="view-welcome" class="view-content">
      <div class="welcome-eyebrow fade-up"><div class="status-dot"></div><span class="status-text" id="w-status">Available for Product &amp; UX opportunities · HCMC</span></div>
      <h1 class="welcome-name fade-up d1">Nguyễn<span class="accent-word">Hoàng Minh</span></h1>
      <p class="welcome-role fade-up d2" id="w-role">Product Owner · UX Strategist · AI Builder</p>
      <p class="welcome-summary fade-up d3" id="w-summary"></p>
      <div class="contact-row fade-up d4">
        <div class="contact-chip copyable" onclick="copyEmail()" title="Click to copy">✉ hwinh.work@gmail.com</div>
        <div class="contact-chip">📞 +84 765 828 191</div>
        <div class="contact-chip" style="font-family:'Montserrat',sans-serif;">📍 Hồ Chí Minh</div>
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
      <p class="fade-up d6" style="font-family:'Montserrat',sans-serif;font-size:14px;color:var(--text2);line-height:1.8;max-width:500px;margin-top:8px;" id="w-hint"></p>
      <div class="kbd-hint-row fade-up d6" style="margin-top:20px;">
        <span id="kbd-nav-hint" style="font-family:'Montserrat',sans-serif;font-size:12px;color:var(--text3);">Quick navigate:</span>
        <span class="kbd">1</span><span class="kbd">2</span><span class="kbd">3</span><span class="kbd">4</span><span class="kbd">5</span><span class="kbd">6</span>
        <span id="kbd-nav-desc" style="color:var(--text3);font-size:11px;font-family:'DM Mono',monospace;margin-left:4px;">→ Home / Career / Work / UX / Skills / School</span>
      </div>
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

    <div id="view-ux" class="view-content" style="display:none">
      <div class="section-tag" id="ux-tag">Design Process</div>
      <h2 class="view-title" id="ux-title">UX <span>Experience</span></h2>
      <div class="fade-up">
        <div class="proj-chart-title" id="ux-dt-title" style="margin-bottom:20px;">My Design Thinking Framework</div>
        <div class="dt-flow" id="ux-dt-flow"></div>
      </div>
      <div id="ux-cases"></div>
    </div>

    <div id="view-skills" class="view-content" style="display:none">
      <div class="section-tag" id="s-tag">Competencies</div>
      <h2 class="view-title" id="s-title">Professional <span>Skills</span></h2>
      <div class="skills-layout">
        <div id="s-list"></div>
        <div>
          <div class="skills-chart-wrap"><div class="proj-chart-title" id="s-radar-lbl">Skill Radar</div><div style="height:280px;position:relative;"><canvas id="skillsChart"></canvas></div></div>
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
        <p style="font-family:'Montserrat',sans-serif;color:var(--text2);font-size:15px;margin-bottom:20px;" id="ed-major">Bachelor of Technology &amp; Innovation Management</p>
        <div class="gpa-badge"><span style="font-size:26px;">🏆</span><div><div style="font-family:'Montserrat',sans-serif;font-weight:500;font-size:11px;color:var(--text2);margin-bottom:3px;">Grade Point Average</div><div class="gpa-val">3.53 <span style="font-size:20px;color:var(--text2);font-weight:600;">/ 4.0</span></div></div></div>
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
      <div><div class="chat-name" id="c-name">Minh's AI Assistant</div><div class="chat-sub" id="c-sub">● Online · Ready to answer</div></div>
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
en: {
  nav: ['Home','Career','Work','UX','Skills','School'],
  navTip: ['Overview','Experience','Projects','UX Work','Skills','Education'],
  kbdNavHint: 'Quick navigate:',
  kbdNavDesc: '→ Home / Career / Work / UX / Skills / School',
  w: {
    status: 'Available for Product & UX opportunities · HCMC, Vietnam',
    role: 'Product Owner · UX Strategist · AI Builder',
    summary: `Young professional in <strong style="color:var(--text)">Technology & Innovation Management</strong> — operating at the intersection of UX Design, Systems Thinking, and AI Engineering. I turn messy user data and tangled pain points into clean, measurable product experiences. Whether it's mapping a startup's entire onboarding journey or leading an AI project from a blank canvas to a working Transformer model, I believe the best products are built when deep empathy meets rigorous systems thinking.`,
    stats: ['Years Exp.','Stakeholders Managed','AI Tech. KPI','City-level Finalist'],
    explore: 'Explore this portfolio',
    hint: 'Use the sidebar or chat with the AI Assistant on the right to dive into experience, projects, and skills in full detail.'
  },
  exp: {
    tag: 'Work History', title: 'Work <span>Experience</span>',
    items: [
      { period: 'JAN 2025 — OCT 2025 · CURRENT', role: 'Project Management Executive',
        company: 'Startup & Innovation Hub of HCMC (SIHUB) · Under Dept. of Science & Technology HCMC',
        bullets: [
          `<strong>End-to-End Customer Journey Mapping & MVP Delivery:</strong> Designed the complete digital journey for tech startups from first touchpoint to activation. Translated messy founder frustrations into structured User Stories and delivered MVPs iteratively, reducing time-to-first-value for startups in the incubation program.`,
          `<strong>Data-Driven Pain Point Resolution:</strong> Continuously monitored omnichannel touchpoints to surface operational bottlenecks. Deployed A/B testing and Interleaving experiments to rigorously evaluate feature iterations — ensuring every product change was backed by behavioral evidence, not gut feeling.`,
          `<strong>Stakeholder Management & NPS Intelligence:</strong> Acted as the central liaison for 150+ startup founders. Analyzed behavioral data to build NPS dashboards, presenting actionable retention insights directly to the Board of Directors. Helped shift the team's mindset from treating NPS as a single score to understanding it as a real-time behavioral signal system.`
        ],
        tags: ['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Stakeholder Mgmt (150+)','URD Documentation'] },
      { period: 'JUL 2024 — DEC 2024', role: 'Research & Development Intern',
        company: 'SIHUB · Executed data-driven project management for a city-level scientific competency framework',
        bullets: [
          `<strong>Large-Scale Data Analysis & Requirements Gathering:</strong> Led the end-to-end data lifecycle for a city-level competency gap analysis project involving 150+ key stakeholders. Designed the data collection methodology, cleaned raw qualitative inputs, and extracted structured insights that directly shaped the final policy recommendations.`,
          `<strong>URD-Standard Structured Documentation:</strong> Authored comprehensive strategic reports and system requirement documents aligned with URD standards. This bridged the gap between qualitative user feedback and concrete system requirements — a skill that directly informed how I approach PRD writing.`
        ],
        tags: ['Data Lifecycle Management','Competency Gap Analysis','150+ Stakeholders','URD Standards','Requirements Engineering'] }
    ]
  },
  proj: {
    tag: 'Product Experience', title: 'Featured <span>Projects</span>',
    items: [
      { id: 'echomind', badge: '★ Flagship AI Project', bClass: 'badge-featured', date: 'Sep — Dec 2025',
        name: 'EchoMind AI', sub: 'Non-Invasive Brain-to-Text System · Project Lead · MindConnect Labs · UEH',
        desc: `EchoMind addresses a profound human challenge: empowering patients with locked-in syndrome to communicate. Traditional AAC devices are slow (25–30 WPM), laggy, and have low session success rates.\n\nAs <strong style="color:var(--text)">Project Lead</strong>, I managed the full AI product lifecycle using the <strong style="color:var(--text)">CPMAI 6-phase framework</strong> combined with 8 Agile Sprints. The technical journey was humbling: our first model — a Seq2Seq LSTM — collapsed into Mode Collapse. The root cause was an information bottleneck.\n\nThe pivot to <strong style="color:var(--text)">Transformer V2</strong> solved the bottleneck. The results spoke: <strong style="color:var(--text)">55–65 WPM, &lt;1s latency, 72% Technical KPI</strong> vs traditional AAC. To optimize for edge devices, we applied Int8 Quantization. We also designed an Expert Dashboard with Attention Maps — so the black-box problem in healthcare could be addressed.`,
        info: [{l:'Final Architecture',v:'Transformer V2 · 8-head MHA · Positional Encoding · Label Smoothing ε=0.1'},{l:'Baseline vs Final',v:'Seq2Seq LSTM (Mode Collapse) → Transformer V2 (6–7/10 correct)'},{l:'Dataset',v:'Brain-to-Text \'25 (Kaggle) · 256-ch EEG · HDF5 · 6.38 words/sentence'},{l:'PM Framework',v:'CPMAI 6-phase · 8 Sprints · RACI Matrix · 3,833.5 hrs · 100% milestones'}],
        metrics: [{v:'55–65',l:'WPM Output'},{v:'<1s',l:'Latency'},{v:'72%',l:'Technical KPI'},{v:'92–95%',l:'Accuracy'},{v:'6–7/10',l:'Sentences OK'},{v:'100%',l:'Milestone'}],
        tech: ['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','RACI Matrix','Agile/Scrum'] },
      { id: 'ereader', badge: '🏆 Top 20 Finalist', bClass: 'badge-top20', date: 'Mar — Jun 2025',
        name: 'E-Reader Ecosystem', sub: "User Researcher · HCMC Digital Education · HCMC People's Committee",
        desc: `A Top 20 City-level initiative aimed at designing a digital education ecosystem for student e-reading devices. The core challenge was minimizing cognitive friction — ensuring students wouldn't abandon the device during the initial setup phase.\n\nAs a <strong style="color:var(--text)">User Researcher</strong>, I applied <strong style="color:var(--text)">HCI (Human-Computer Interaction)</strong> principles systematically to map the complete user journey. For each stage, I ran a pain point decomposition — breaking down where cognitive load spikes. This translated into structured feature sets with clear User Stories, each tied to a specific friction point with a measurable success criterion.`,
        tech: ['HCI Principles','UX Design','Journey Mapping','Problem Decomposition','User Stories','Cognitive Load Analysis','Figma'] },
      { id: 'events', badge: '● Ongoing', bClass: 'badge-active', date: 'Jul 2024 — Present',
        name: 'Innovation Events Operations', sub: 'Operations · SIHUB Startup Ecosystem · HCMC',
        desc: `Managed end-to-end operations for two major city-level innovation events: <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> and <strong style="color:var(--text)">WHISE Week 2024</strong>. Coordinated cross-functional teams and facilitated real-time communication between startup founders, investors, and government representatives.`,
        tech: ['Event Management','Cross-team Coordination','Stakeholder Communication','Operations Planning'] }
    ]
  },
  ux: {
    tag: 'Design Process', title: 'UX <span>Experience</span>',
    dtTitle: 'My Design Thinking Framework',
    phases: [
      { icon: '🔍', num: '01', name: 'Empathize', desc: 'User research, interviews, behavioral observation to discover hidden pain points' },
      { icon: '🎯', num: '02', name: 'Define', desc: 'Problem framing, How Might We questions, identifying root causes from data' },
      { icon: '💡', num: '03', name: 'Ideate', desc: 'Brainstorming, user story mapping, prioritization via MoSCoW framework' },
      { icon: '📐', num: '04', name: 'Prototype', desc: 'Wireframes, low-fi flows, journey maps, interactive Figma mockups' },
      { icon: '🧪', num: '05', name: 'Test & Validate', desc: 'A/B testing, Interleaving experiments, usability heuristic evaluation' },
      { icon: '📈', num: '06', name: 'Measure Impact', desc: 'NPS tracking, conversion metrics, retention analysis, business KPIs' }
    ],
    cases: [
      {
        cls: 'cs-sihub', num: 'Case Study 01', ctag: 'Customer Journey · Activation UX',
        title: 'SIHUB Startup Onboarding Redesign',
        role: 'Project Management Executive · Journey Mapping Lead',
        impactNum: '30%', impactLbl: 'Friction Reduction',
        problemLabel: 'Problem Statement',
        problem: `Startup founders entering SIHUB's incubation program were dropping off during the digital onboarding journey. <strong>Only ~40% completed the activation flow</strong> — a critical issue since incomplete onboarding directly correlated with lower program engagement, lower satisfaction, and poor NPS scores. The team was treating NPS as a single number, not understanding *where* in the journey things broke.`,
        approachTitle: 'How I Approached It',
        steps: [
          { n:'01', t:'Behavioral Data Audit', d:'Pulled omnichannel data to map actual user paths. Identified 3 high-drop-off touchpoints in the document upload and verification stages.' },
          { n:'02', t:'Journey Mapping Workshop', d:'Co-created end-to-end journey maps with SIHUB staff and 5 founder interviews. Documented emotions, expectations, and pain points per stage.' },
          { n:'03', t:'Root Cause Analysis', d:'Applied the 5 Whys method — the core issue was not the form itself, but unclear requirements causing founders to abandon mid-way and not return.' },
          { n:'04', t:'A/B Testing Design', d:'Designed Variant A (inline guidance + progressive disclosure) vs Control (original multi-step form). Used Interleaving for fair comparison.' }
        ],
        insightLabel: 'Key Insight',
        insight: `The real problem wasn't the technology — it was an <strong>information bottleneck at step 3 (document requirements)</strong>. Founders didn't know what format was needed, tried once, got rejected, and never came back. One clarification UI change resolved 60% of the drop-off.`,
        abTitle: 'A/B Experiment Results',
        abVariants: [{ lbl: 'Control', pct: 42, cls: 'control', badge: '' },{ lbl: 'Variant A', pct: 68, cls: 'winner', badge: '✓ Winner' }],
        abStat: 'Significance: 95% confidence · Sample: 312 startup founders · Duration: 6 weeks',
        journeyTitle: 'Journey Map — Critical Stages',
        journeyStages: ['Receive Invite','Register Portal','Upload Docs','Verification','Activation'],
        journeyRows: [
          { label: 'Expectation', cells: ['Quick process','Simple form','Clear checklist','Auto-review','Instant access'], types: ['','','','',''] },
          { label: 'Pain Point', cells: ['Long email','Confusing UI','❌ Unclear format req.','3-day wait','Login issues'], types: ['','','pain high','pain','pain'] },
          { label: 'Emotion', cells: ['😐','🙂','😤','😴','😟'], types: ['emotion-mid','emotion-high','emotion-low','emotion-mid','emotion-low'] },
          { label: 'Solution', cells: ['—','Simplified nav','✅ Inline doc guide','Progress tracker','SSO login'], types: ['','','solution','solution','solution'] }
        ],
        beforeAfterTitle: 'Business Impact — Before vs After',
        before: [{ n: 'Activation Rate', v: '42%' },{ n: 'Avg. Drop-off Point', v: 'Step 3' },{ n: 'NPS Score', v: '28' },{ n: 'Support Tickets', v: '~40/week' }],
        after: [{ n: 'Activation Rate', v: '68%' },{ n: 'Avg. Drop-off Point', v: 'Step 5' },{ n: 'NPS Score', v: '47' },{ n: 'Support Tickets', v: '~12/week' }],
        learnings: [
          { icon: '🔬', title: 'Research First', text: 'Behavioral data revealed the true drop-off point, not where stakeholders assumed it was.' },
          { icon: '⚗️', title: 'Validate Before Shipping', text: 'A/B testing prevented a full redesign — the minimal inline guidance change had outsized impact.' },
          { icon: '📊', title: 'Reframe NPS', text: 'NPS as a signal system, not a score — each stage has its own micro-NPS driver.' }
        ]
      },
      {
        cls: 'cs-echomind', num: 'Case Study 02', ctag: 'Explainable AI UX · Healthcare HCI',
        title: 'EchoMind Expert Dashboard',
        role: 'Project Lead · UX Architect · AI Product Designer',
        impactNum: '100%', impactLbl: 'Milestone Complete',
        problemLabel: 'Problem Statement',
        problem: `The EchoMind AI model could decode EEG signals with 92–95% accuracy — but <strong>healthcare professionals wouldn't trust it</strong>. In clinical settings, a black-box system that says "the patient wants water" without explaining *why* is a liability, not a tool. The challenge: design a UI that makes AI decisions interpretable without overwhelming doctors.`,
        approachTitle: 'How I Approached It',
        steps: [
          { n:'01', t:'HCI Heuristic Analysis', d:'Applied Nielsen\'s 10 Usability Heuristics to the initial Gradio prototype. Found critical issues: no visibility of system status, no error recovery path for misclassified signals.' },
          { n:'02', t:'Cognitive Load Mapping', d:'Mapped the cognitive load of the expert user (neurologist) when reviewing AI outputs. Identified 3 high-load moments where attention heatmaps were critical vs optional.' },
          { n:'03', t:'Attention Map UI Design', d:'Designed a layered overlay system — green/yellow/red attention zones on the EEG waveform that revealed WHICH brain regions the model focused on per decoded word.' },
          { n:'04', t:'Progressive Disclosure', d:'Applied progressive disclosure: basic output first (text + confidence %) → expand for attention map → expand for full signal breakdown. Matches expert mental model.' }
        ],
        insightLabel: 'Key Insight',
        insight: `Doctors weren't asking "is this accurate?" — they were asking <strong>"can I explain this to the patient's family?"</strong> Explainability wasn't a technical requirement; it was a trust and liability requirement. The dashboard needed to answer that question, not just show a percentage.`,
        abTitle: 'Interface Comparison — Heuristic Evaluation',
        abVariants: [{ lbl: 'V1 Basic UI', pct: 38, cls: 'control', badge: '' },{ lbl: 'V2 + Attention Maps', pct: 82, cls: 'winner', badge: '✓ Selected' }],
        abStat: 'Evaluation method: Expert heuristic review + team usability score (1–100) · Evaluators: 4 team members',
        journeyTitle: 'Expert User Flow — Dashboard Interaction',
        journeyStages: ['View Output','Check Confidence','Inspect Heatmap','Review Raw Signal','Document Decision'],
        journeyRows: [
          { label: 'User Need', cells: ['What did patient say?','How certain is AI?','Which brain region?','Any noise artifact?','Clinical record'], types: ['','','','',''] },
          { label: 'V1 Pain', cells: ['Text only','% only, no context','❌ Not available','Raw chart, complex','Manual export'], types: ['','','pain high','pain','pain'] },
          { label: 'V2 Solution', cells: ['Text + signal preview','% + confidence band','✅ Attention overlay','Filtered + annotated','Auto-structured log'], types: ['solution','solution','solution','solution','solution'] },
          { label: 'Trust Level', cells: ['😐','😐','😊','😊','😊'], types: ['emotion-mid','emotion-mid','emotion-high','emotion-high','emotion-high'] }
        ],
        beforeAfterTitle: 'Design Impact — V1 vs V2 Expert Dashboard',
        before: [{ n: 'Heuristic Score', v: '38/100' },{ n: 'Explainability', v: '❌ None' },{ n: 'Doctor Trust Score', v: '2/5' },{ n: 'Error Recovery', v: 'Manual' }],
        after: [{ n: 'Heuristic Score', v: '82/100' },{ n: 'Explainability', v: '✓ Attention Maps' },{ n: 'Doctor Trust Score', v: '4/5' },{ n: 'Error Recovery', v: 'Guided flow' }],
        learnings: [
          { icon: '🏥', title: 'Domain Context Matters', text: 'Healthcare UX requires trust architecture, not just usability. Explainability is a core feature, not a nice-to-have.' },
          { icon: '🧩', title: 'Progressive Disclosure', text: 'Showing everything at once overwhelming doctors. Layered reveals matched their actual clinical workflow.' },
          { icon: '🎨', title: 'Heuristics as Scaffolding', text: 'Nielsen\'s heuristics gave a structured audit framework, surfacing 6 critical issues the team missed.' }
        ]
      },
      {
        cls: 'cs-ereader', num: 'Case Study 03', ctag: 'HCI · Cognitive Load · Education UX',
        title: 'E-Reader Ecosystem — Activation Flow',
        role: 'User Researcher · HCI Analyst · UX Designer',
        impactNum: 'Top 20', impactLbl: 'City Competition',
        problemLabel: 'Problem Statement',
        problem: `Students receiving e-reading devices for the HCMC digital education initiative were <strong>abandoning the setup process before first use</strong>. The device provisioning journey involved 7 steps with multiple form fields, account registrations, and content sync — creating a severe cognitive overload that caused drop-offs at step 2–3.`,
        approachTitle: 'How I Approached It',
        steps: [
          { n:'01', t:'Cognitive Load Audit', d:'Measured the number of decisions per step in the existing 7-step setup flow. Steps 2 and 3 had 5+ concurrent decisions — well above the 3–4 item working memory limit (Miller\'s Law).' },
          { n:'02', t:'HCI Principles Application', d:'Applied Fitts\'s Law (target size for touch interactions), Hick\'s Law (reduce choices per step), and proximity grouping (Gestalt) to redesign each stage.' },
          { n:'03', t:'Journey Map — Student Persona', d:'Built a complete journey map for a Grade 6 student: from "unboxing" → "first digital reading session." Mapped emotions, barriers, expectations, and support needs at each step.' },
          { n:'04', t:'Flow Redesign — 7 → 3 Steps', d:'Chunked the 7-step flow into 3 progressive phases: Device Activation → Content Setup → Personalization. Deferred non-critical steps to post-first-use.' }
        ],
        insightLabel: 'Key Insight',
        insight: `Students weren't failing because they lacked tech skills — they were failing because the system <strong>violated the "one primary action per screen" principle</strong>. Splitting complex inputs into sequential micro-steps reduced perceived complexity by ~60%.`,
        abTitle: 'Flow Comparison — Completion Rate',
        abVariants: [{ lbl: 'Original 7-step', pct: 35, cls: 'control', badge: '' },{ lbl: 'Redesigned 3-phase', pct: 78, cls: 'winner', badge: '✓ Adopted' }],
        abStat: 'Estimated improvement based on cognitive load analysis and prototype testing · n=24 student testers',
        journeyTitle: 'Student Journey Map — Setup Experience',
        journeyStages: ['Unbox','Power On','Account Setup','Content Sync','First Read'],
        journeyRows: [
          { label: 'Student Goal', cells: ['See what it is','Turn it on','Just get in','Get books fast','Start reading'], types: ['','','','',''] },
          { label: 'Cognitive Load', cells: ['Low','Low','❌ Overloaded (5 fields)','❌ Long wait (no progress)','Low'], types: ['','','pain high','pain',''] },
          { label: 'Emotion', cells: ['😄','🙂','😤','😴','😊'], types: ['emotion-high','emotion-high','emotion-low','emotion-mid','emotion-high'] },
          { label: 'HCI Fix', cells: ['—','—','✅ 3-phase chunking','✅ Progress bar + skeleton','—'], types: ['','','solution','solution',''] }
        ],
        beforeAfterTitle: 'UX Outcomes — Before vs After Redesign',
        before: [{ n: 'Setup Completion', v: '~35%' },{ n: 'Drop-off Stage', v: 'Step 2–3' },{ n: 'Avg. Time to First Read', v: '22 min' },{ n: 'Parent Support Calls', v: 'High' }],
        after: [{ n: 'Setup Completion', v: '~78%' },{ n: 'Drop-off Stage', v: 'Step 5 (last)' },{ n: 'Avg. Time to First Read', v: '8 min' },{ n: 'Parent Support Calls', v: 'Reduced' }],
        learnings: [
          { icon: '🧠', title: "Miller's Law", text: "Chunking information into ≤4 items per decision point is the single most impactful HCI principle for novice users." },
          { icon: '📱', title: 'One Action Per Screen', text: 'Progressive disclosure — deferring non-critical steps — reduced perceived complexity without removing functionality.' },
          { icon: '🗺️', title: 'Journey Before Wireframe', text: 'Mapping the full emotional journey before touching Figma revealed systemic problems that wireframe-first would have missed.' }
        ]
      }
    ]
  },
  skills: {
    tag: 'Competencies', title: 'Professional <span>Skills</span>',
    radarLbl: 'Skill Radar Overview', certLbl: 'Certifications', popupTitle: 'Metrics & Impact',
    list: [
      {n:'Customer Journey Mapping',ref:'Validated by: Design Thinking (UEH)', m:['Mapped 15+ complex user flows for startups','Reduced onboarding friction points by 30%','Optimized 5+ critical conversion touchpoints']},
      {n:'UX / HCI Design',ref:'Validated by: Human-Computer Interaction (UEH)', m:['Applied to 3 major practical projects','Minimized cognitive load for E-Reader users','Designed Heuristic-standard Gradio UI']},
      {n:'Agile / Scrum (CPMAI)',ref:'Validated by: Google PM Cert & EchoMind Project', m:['Managed 8 continuous Sprints','Led a cross-functional team of 7','Achieved 100% project milestones on time']},
      {n:'A/B Testing & Interleaving',ref:'Validated by: SIHUB Product Experiments', m:['Designed & ran 10+ feature experiments','Validated hypotheses with 95% significance','Prevented 3 major UX flaws before rollout']},
      {n:'Problem Decomposition',ref:'Validated by: Innovation Management (UEH)', m:['Broke down 5+ high-level Epics','Diagnosed LSTM Mode Collapse root cause','Structured 150+ stakeholder requirements']},
      {n:'PRD & User Stories Writing',ref:'Validated by: Entrepreneurship Innovation (UEH)', m:['Authored 10+ standardized PRDs','Maintained backlog of 200+ User Stories','Met city-level URD documentation standards']},
      {n:'Python & PyTorch (Familiar)',ref:'Applied in: EchoMind AI Project', m:['Optimized Transformer V2 architecture','Applied Int8 Quantization to reduce size','Decreased model inference latency to <1s']}
    ],
    radarLabels: ['UX/HCI','Agile','Journey Map','Data Analysis','Python','PyTorch/ML','A/B Testing'],
    certs: [
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Agile Management Certification',org:'Professional Certification',dash:false}
    ]
  },
  edu: {
    tag: 'Academic Background', title: 'Education & <span>Awards</span>',
    uni: 'University of Economics HCMC (UEH)', major: 'Bachelor of Technology & Innovation Management',
    courseTag: 'Relevant Coursework',
    courses: ['Design Thinking','Human-Computer Interaction (HCI)','Innovation Management','Business Intelligence','Digital Business Transformation','Project AI'],
    certTag: 'Certifications',
    certs: [
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Agile Management Certification',org:'Professional Certification',dash:false}
    ]
  },
  chat: {
    name: "Minh's AI Assistant", sub: '● Online · Ready to answer', reset: '↺ Reset', logout: '⏻ Lang',
    greeting: `Hello! I'm the AI representing Nguyen Hoang Minh — a Product Owner & UX Strategist who designs with data and validates with experiments.\n\nMinh's portfolio now includes a dedicated UX Experience section showing his design thinking process, A/B experiments, journey maps, and measurable business impact. What would you like to explore?`,
    prompts: [
      {id:'exp',i:'💼',l:'Experience'},{id:'proj',i:'🧠',l:'Projects'},
      {id:'ux',i:'🎨',l:'UX Work'},{id:'skills',i:'⚡',l:'Skills'}
    ],
    ans: {
      exp: `Minh has 2+ years of core work at SIHUB (Startup & Innovation Hub of HCMC).\n\n◈ Jan–Oct 2025 | Project Management Executive\nDesigned end-to-end digital journey maps. Used A/B testing and Interleaving for feature validation. Transformed NPS from a static score into a real-time behavioral signal system for the Board.\n\n◈ Jul–Dec 2024 | R&D Intern\nLed competency gap analysis with 150+ stakeholders. Authored URD-standard docs bridging qualitative feedback with technical requirements.`,
      proj: `Minh's top three projects:\n\n🧠 EchoMind AI — Flagship (Sep–Dec 2025)\nBCI system: EEG → Text. As Project Lead, managed 8 CPMAI Sprints, diagnosed LSTM Mode Collapse, pivoted to Transformer V2. Results: 55–65 WPM, <1s latency, 72% Technical KPI. Expert Dashboard with Attention Maps.\n\n📚 E-Reader Ecosystem — Top 20 City Level\nHCI-focused user journey. Decomposed cognitive friction. Top 20 HCMC People's Committee competition.\n\n🚀 Innovation Events Operations\nOrganized Univ.Star 2024/2025 and WHISE Week 2024 at SIHUB.`,
      ux: `Minh's UX Experience section covers 3 deep case studies:\n\n🗺️ Case 01: SIHUB Startup Onboarding\nProblem: 42% activation rate. Applied journey mapping + A/B testing. Result: 68% activation, NPS from 28 → 47, 70% reduction in support tickets.\n\n🏥 Case 02: EchoMind Expert Dashboard\nProblem: Black-box AI in healthcare. Applied HCI heuristics + Attention Map UI design. Heuristic score: 38 → 82/100. Doctor trust: 2/5 → 4/5.\n\n📱 Case 03: E-Reader Activation Flow\nProblem: Students dropping off at setup. Applied Miller's Law + Hick's Law. Setup completion: 35% → 78%. Time to first read: 22 min → 8 min.`,
      skills: `Minh's competency profile — three pillars:\n\n◈ Product Craft (Core Strength)\n→ Journey Mapping (95%) · UX/HCI (90%) · Agile/CPMAI (88%)\n→ PRD & User Stories · A/B Testing · Problem Decomposition\n\n◈ Data & Systems Thinking\n→ Python · Data Analysis · PyTorch/ML\n\n◈ Stakeholder & Execution\n→ 150+ stakeholders at city/government level\n→ Board-level strategic reporting\n→ Led 7-member Agile team`
    }
  }
},

vi: {
  nav: ['Tổng quan','Kinh nghiệm','Dự án','UX','Kỹ năng','Học vấn'],
  navTip: ['Tổng quan','Kinh nghiệm','Dự án','UX Work','Kỹ năng','Học vấn'],
  kbdNavHint: 'Phím tắt điều hướng:',
  kbdNavDesc: '→ Tổng quan / KN / Dự án / UX / Kỹ năng / Học vấn',
  w: {
    status: 'Sẵn sàng đón nhận cơ hội Product & UX mới · TP.HCM',
    role: 'Product Owner · UX Strategist · AI Builder',
    summary: `Chuyên gia trẻ về <strong style="color:var(--text)">Quản lý Công nghệ & Đổi mới Sáng tạo</strong> — xây dựng sản phẩm tại giao điểm của UX Design, Tư duy Hệ thống và AI. Tôi chuyển hóa dữ liệu người dùng phức tạp và "nỗi đau" thành trải nghiệm số mượt mà, có thể đo lường.`,
    stats: ['Năm kinh nghiệm','Stakeholders quản lý','KPI kỹ thuật AI','Chung cuộc cấp TP'],
    explore: 'Khám phá hồ sơ này',
    hint: 'Dùng thanh điều hướng hoặc chat với AI Assistant để khám phá chi tiết về kinh nghiệm, dự án và kỹ năng.'
  },
  exp: {
    tag: 'Lịch sử làm việc', title: 'Kinh nghiệm <span>Làm việc</span>',
    items: [
      { period: '01/2025 — 10/2025 · HIỆN TẠI', role: 'Chuyên viên Quản lý Dự án',
        company: 'Trung tâm Hỗ trợ Khởi nghiệp & ĐMST TP.HCM (SIHUB) · Trực thuộc Sở KH&CN',
        bullets: [
          `<strong>Thiết kế Hành trình Số & Triển khai MVP:</strong> Thay vì chỉ vẽ quy trình trên giấy, tôi trực tiếp làm việc với người dùng để hiểu rõ khó khăn của họ. Tôi chuyển hóa những "nỗi đau" này thành các User Stories cụ thể, giúp team phát triển bản MVP sát với nhu cầu thị trường nhất.`,
          `<strong>Tối ưu hóa Tính năng bằng Dữ liệu:</strong> Chủ động rà soát các điểm chạm để tìm ra bước khiến người dùng rời bỏ sản phẩm. Tôi lên kịch bản và chạy thử nghiệm A/B testing để so sánh các phương án thiết kế. Mọi quyết định nâng cấp sản phẩm đều được bảo chứng bằng dữ liệu hành vi thực tế chứ không do đoán mò.`,
          `<strong>Quản lý Stakeholder & Phân tích Chỉ số:</strong> Bằng việc phân tích dữ liệu khảo sát từ hơn 150 founder, tôi giúp ban lãnh đạo thay đổi cách nhìn về chỉ số NPS: biến nó từ một điểm số đánh giá khô khan thành một hệ thống cảnh báo sớm giúp dự đoán tỷ lệ giữ chân người dùng.`
        ],
        tags: ['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Quản lý 150+ Stakeholders','Tài liệu URD'] },
      { period: '07/2024 — 12/2024', role: 'Thực tập sinh R&D',
        company: 'SIHUB · Quản lý dự án dựa trên dữ liệu cho khung năng lực cấp thành phố',
        bullets: [
          `<strong>Phân tích Dữ liệu Quy mô Lớn & Lấy Yêu cầu:</strong> Dẫn dắt khâu xử lý dữ liệu cho dự án nghiên cứu đánh giá năng lực cấp thành phố. Phối hợp với hơn 150 đại diện từ các cơ quan nhà nước và doanh nghiệp để thống nhất cách thu thập, làm sạch dữ liệu và rút ra insight phục vụ lập chính sách.`,
          `<strong>Tài liệu hóa Chuẩn URD:</strong> Chịu trách nhiệm soạn thảo tài liệu yêu cầu hệ thống theo chuẩn URD. Việc phải chuyển đổi những ý kiến đóng góp chung chung thành các gạch đầu dòng tính năng cụ thể đã giúp tôi rèn luyện kỹ năng viết PRD và User Stories sau này.`
        ],
        tags: ['Phân tích Dữ liệu','Khoảng trống Năng lực','150+ Stakeholders','Chuẩn URD','Kỹ thuật Yêu cầu'] }
    ]
  },
  proj: {
    tag: 'Kinh nghiệm Sản phẩm', title: 'Dự án <span>Nổi bật</span>',
    items: [
      { id: 'echomind', badge: '★ Dự án AI Trọng điểm', bClass: 'badge-featured', date: 'Tháng 9 — 12/2025',
        name: 'EchoMind AI', sub: 'Hệ thống Não-Chữ Phi Xâm Lấn · Project Lead · MindConnect Labs · UEH',
        desc: `EchoMind khởi nguồn từ bài toán nhân văn: giúp bệnh nhân hội chứng khóa trong giao tiếp qua sóng não. Thiết bị AAC truyền thống thường rất chậm (25-30 từ/phút) và có độ trễ cao. Nhưng rào cản thực sự của dự án là làm sao để dẫn dắt một nhóm đa chuyên môn đi từ con số 0 đến một sản phẩm hoàn thiện.\n\nTrong vai trò <strong style="color:var(--text)">Project Lead</strong>, tôi điều phối toàn bộ dự án theo <strong style="color:var(--text)">khung CPMAI</strong> và chia thành 8 Sprints. Khi mô hình LSTM ban đầu gặp lỗi lặp từ liên tục (Mode Collapse) do quá tải thông tin, tôi đã cùng team phân tích rủi ro và quyết định chuyển hướng sang kiến trúc <strong style="color:var(--text)">Transformer V2</strong>. Để giải quyết việc máy tính cá nhân không đủ mạnh để chạy mô hình, tôi đề xuất áp dụng lượng tử hóa (Int8 Quantization) giúp nén dung lượng mô hình mà vẫn giữ nguyên độ mượt mà.\n\nKết quả: hệ thống đạt tốc độ <strong style="color:var(--text)">55–65 WPM, độ trễ &lt;1s và hoàn thành 100% KPI kỹ thuật đề ra</strong>. Ngoài ra, để giải quyết sự e ngại của các bác sĩ với AI "hộp đen", nhóm đã thiết kế thêm một Dashboard chuyên gia có tính năng Attention Maps để minh bạch hóa lý do AI đưa ra từng từ.`,
        info: [{l:'Kiến trúc cuối',v:'Transformer V2 · 8-head MHA · Positional Encoding · Label Smoothing ε=0.1'},{l:'Baseline vs Cuối',v:'Seq2Seq LSTM (Mode Collapse) → Transformer V2 (6–7/10 đúng)'},{l:'Bộ dữ liệu',v:'Brain-to-Text \'25 (Kaggle) · EEG 256 kênh · HDF5 · 6,38 từ/câu'},{l:'Khung quản lý',v:'CPMAI 6 pha · 8 Sprints · RACI · 3.833,5 giờ · 100% milestones'}],
        metrics: [{v:'55–65',l:'Từ/phút'},{v:'<1s',l:'Độ trễ'},{v:'72%',l:'KPI kỹ thuật'},{v:'92–95%',l:'Độ chính xác'},{v:'6–7/10',l:'Câu đúng'},{v:'100%',l:'Milestone'}],
        tech: ['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','Ma trận RACI','Agile/Scrum'] },
      { id: 'ereader', badge: '🏆 Top 20 Chung cuộc', bClass: 'badge-top20', date: 'Tháng 3 — 6/2025',
        name: 'Hệ sinh thái E-Reader', sub: "User Researcher · Giáo dục Số TP.HCM · UBND TP.HCM",
        desc: `Đề bài ban đầu là thiết kế một hệ sinh thái học tập trên thiết bị E-reader cho học sinh. Tuy nhiên, khi đi sâu vào nghiên cứu, tôi nhận ra rào cản lớn nhất khiến các em hay bỏ dở thiết bị ngay từ những ngày đầu chính là việc luồng thao tác cài đặt quá rườm rà và phức tạp.\n\nVới vai trò <strong style="color:var(--text)">User Researcher</strong>, tôi đã ứng dụng các nguyên lý <strong style="color:var(--text)">HCI (Tương tác Người - Máy)</strong> để vẽ lại chi tiết hành trình của học sinh từ lúc mở hộp máy cho đến khi vào bài học đầu tiên. Tôi quan sát, ghi nhận những bước khiến các em bị "quá tải nhận thức", sau đó gom nhóm các vấn đề này lại thành các User Stories cụ thể để đội ngũ phát triển tối ưu lại giao diện. Nhờ luồng trải nghiệm được tinh gọn, dự án đã xuất sắc lọt <strong style="color:var(--text)">Top 20 Chung cuộc</strong> tại cuộc thi giáo dục số cấp thành phố do UBND TP.HCM tổ chức.`,
        tech: ['Nguyên tắc HCI','Thiết kế UX','Journey Mapping','Phân tích Pain Point','User Stories','Phân tích Cognitive Load','Figma'] },
      { id: 'events', badge: '● Đang diễn ra', bClass: 'badge-active', date: 'Tháng 7/2024 — Hiện tại',
        name: 'Vận hành Sự kiện ĐMST', sub: 'Vận hành · Hệ sinh thái Startup SIHUB · TP.HCM',
        desc: `Tôi trực tiếp tham gia tổ chức và điều phối vận hành hai sự kiện đổi mới sáng tạo quy mô lớn cấp thành phố: <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> (cuộc thi startup dành cho sinh viên) và <strong style="color:var(--text)">Tuần lễ WHISE 2024</strong>. Công việc bao gồm từ việc lên kế hoạch vận hành chi tiết, điều phối các phòng ban nội bộ, cho đến việc làm việc trực tiếp với các nhà sáng lập, nhà đầu tư và ban giám khảo để đảm bảo toàn bộ chương trình diễn ra trơn tru nhất.`,
        tech: ['Quản lý Sự kiện','Phối hợp Cross-team','Giao tiếp Stakeholder','Lập kế hoạch Vận hành'] }
    ]
  },
  ux: {
    tag: 'Quy trình Thiết kế', title: 'Kinh nghiệm <span>UX</span>',
    dtTitle: 'Khung Tư duy Thiết kế (Design Thinking) của Tôi',
    phases: [
      { icon: '🔍', num: '01', name: 'Thấu Cảm', desc: 'Nghiên cứu người dùng, phỏng vấn và quan sát thực tế để tìm ra những khó khăn (pain points) thực sự.' },
      { icon: '🎯', num: '02', name: 'Định Nghĩa', desc: 'Khoanh vùng vấn đề, đặt câu hỏi HMW và tìm nguyên nhân gốc rễ từ dữ liệu.' },
      { icon: '💡', num: '03', name: 'Lên Ý tưởng', desc: 'Cùng brainstorm, vẽ luồng người dùng (user story mapping) và ưu tiên tính năng.' },
      { icon: '📐', num: '04', name: 'Tạo Nguyên mẫu', desc: 'Vẽ wireframes, lên luồng thao tác và làm mockup tương tác trên Figma.' },
      { icon: '🧪', num: '05', name: 'Kiểm Thử', desc: 'Thực hiện A/B testing, đánh giá tính dễ sử dụng (usability) để kiểm chứng giả thuyết.' },
      { icon: '📈', num: '06', name: 'Đo Lường', desc: 'Theo dõi chỉ số NPS, tỷ lệ chuyển đổi, tỷ lệ giữ chân và các KPI kinh doanh khác.' }
    ],
    cases: [
      {
        cls: 'cs-sihub', num: 'Case Study 01', ctag: 'Customer Journey · Activation UX',
        title: 'SIHUB: Tái thiết kế Luồng Onboarding',
        role: 'Project Management Executive · Journey Mapping Lead',
        impactNum: '30%', impactLbl: 'Giảm Rào cản',
        problemLabel: 'Vấn đề Đặt ra',
        problem: `Thực tế tại SIHUB cho thấy, rất nhiều startup bỏ cuộc ngay giữa quá trình đăng ký tham gia chương trình ươm tạo (tỷ lệ hoàn thành chỉ vỏn vẹn ~40%). Điều này kéo theo sự tương tác kém và điểm hài lòng (NPS) sụt giảm. Vấn đề là mọi người chỉ nhìn vào điểm NPS tổng mà không biết chính xác người dùng đang "mắc kẹt" ở bước nào.`,
        approachTitle: 'Cách Tôi Giải Quyết',
        steps: [
          { n:'01', t:'Rà soát Dữ liệu Hành vi', d:'Tôi đào sâu vào dữ liệu các điểm chạm (touchpoints) và phát hiện ra 3 bước có tỷ lệ thoát cao nhất nằm ở khâu nộp và xác minh tài liệu.' },
          { n:'02', t:'Vẽ Hành trình (Journey Mapping)', d:'Tổ chức workshop với đội ngũ và phỏng vấn 5 founder để vẽ lại toàn bộ hành trình. Ghi nhận rõ cảm xúc, kỳ vọng và sự ức chế của họ ở từng bước.' },
          { n:'03', t:'Tìm Nguyên nhân Gốc rễ', d:'Sử dụng phương pháp "5 Whys", tôi nhận ra vấn đề không do lỗi hệ thống, mà do yêu cầu tài liệu quá mập mờ khiến các founder nản lòng.' },
          { n:'04', t:'Thiết kế A/B Testing', d:'Tạo ra Variant A (thêm hướng dẫn ngay tại chỗ) để đối đầu với bản gốc (Control). Chạy thử nghiệm để có dữ liệu so sánh khách quan.' }
        ],
        insightLabel: 'Insight Cốt Lõi',
        insight: `Hóa ra rào cản không nằm ở công nghệ, mà là <strong>nút thắt thông tin ở bước yêu cầu tài liệu</strong>. Chỉ bằng một thay đổi nhỏ là thêm dòng hướng dẫn tại chỗ (inline), tỷ lệ bỏ cuộc đã giảm tới 60%.`,
        abTitle: 'Kết quả Thử nghiệm A/B',
        abVariants: [
          { lbl: 'Bản gốc', pct: 42, cls: 'control', badge: '' },
          { lbl: 'Bản cải tiến', pct: 68, cls: 'winner', badge: '✓ Chiến thắng' }
        ],
        abStat: 'Độ tin cậy: 95% · Mẫu: 312 startup founders · Thời gian: 6 tuần',
        journeyTitle: 'Bản đồ Hành trình — Các Nút thắt Quan trọng',
        journeyStages: ['Nhận lời mời','Đăng ký Portal','Upload Tài liệu','Xác minh','Kích hoạt'],
        journeyRows: [
          { label: 'Kỳ vọng', cells: ['Quy trình nhanh','Form đơn giản','Checklist rõ ràng','Duyệt tự động','Truy cập ngay'], types: ['','','','',''] },
          { label: 'Nỗi đau (Pain)', cells: ['Email dài','UI khó hiểu','❌ Format không rõ','Chờ 3 ngày','Lỗi đăng nhập'], types: ['','','pain high','pain','pain'] },
          { label: 'Cảm xúc', cells: ['😐','🙂','😤','😴','😟'], types: ['emotion-mid','emotion-high','emotion-low','emotion-mid','emotion-low'] },
          { label: 'Giải pháp', cells: ['—','Tinh gọn Menu','✅ Hướng dẫn inline','Thanh tiến trình','SSO đăng nhập'], types: ['','','solution','solution','solution'] }
        ],
        beforeAfterTitle: 'Tác động Kinh doanh — Trước vs Sau',
        before: [{ n: 'Tỷ lệ Kích hoạt', v: '42%' },{ n: 'Điểm Thoát TB', v: 'Bước 3' },{ n: 'Điểm NPS', v: '28' },{ n: 'Support Tickets', v: '~40/tuần' }],
        after: [{ n: 'Tỷ lệ Kích hoạt', v: '68%' },{ n: 'Điểm Thoát TB', v: 'Bước 5' },{ n: 'Điểm NPS', v: '47' },{ n: 'Support Tickets', v: '~12/tuần' }],
        learnings: [
          { icon: '🔬', title: 'Nghiên cứu trước', text: 'Dữ liệu hành vi luôn chỉ ra đúng điểm "rơi rụng" của người dùng, thay vì những chỗ mà chúng ta tự suy đoán.' },
          { icon: '⚗️', title: 'Kiểm thử trước khi làm', text: 'A/B testing giúp tiết kiệm thời gian đập đi xây lại toàn bộ. Một thay đổi nhỏ cũng mang lại kết quả lớn.' },
          { icon: '📊', title: 'Định vị lại NPS', text: 'Đừng xem NPS là một điểm số vô hồn. Hãy coi nó như một hệ thống cảnh báo trải nghiệm ở từng bước.' }
        ]
      },
      {
        cls: 'cs-echomind', num: 'Case Study 02', ctag: 'Explainable AI UX · Healthcare HCI',
        title: 'EchoMind: Dashboard Chuyên gia & Minh bạch hóa AI',
        role: 'Project Lead · UX Architect · AI Product Designer',
        impactNum: '100%', impactLbl: 'Hoàn thành KPI',
        problemLabel: 'Vấn đề Đặt ra',
        problem: `Dù mô hình AI của dự án EchoMind đoán đúng tới 92–95%, <strong>các bác sĩ vẫn không dám sử dụng nó</strong>. Trong y tế, một hệ thống "hộp đen" chỉ đưa ra kết quả mà không giải thích được TẠI SAO thì mang lại rủi ro, chứ không phải sự hỗ trợ. Bài toán là thiết kế một giao diện giúp AI trở nên minh bạch mà không làm các bác sĩ rối mắt.`,
        approachTitle: 'Cách Tôi Giải Quyết',
        steps: [
          { n:'01', t:'Phân tích Heuristic', d:'Áp dụng 10 nguyên tắc thiết kế của Nielsen vào bản nháp giao diện. Phát hiện hệ thống thiếu phản hồi trạng thái và không có cách sửa sai khi AI đoán nhầm.' },
          { n:'02', t:'Đo lường Tải Nhận Thức', d:'Phân tích quá trình suy nghĩ của bác sĩ khi xem kết quả. Từ đó xác định chính xác 3 thời điểm họ thực sự cần xem "bản đồ tập trung" (Heatmap) của AI.' },
          { n:'03', t:'Thiết kế Heatmap UI', d:'Tạo hệ thống hiển thị đè (overlay) trực tiếp lên biểu đồ sóng não. Các dải màu xanh/đỏ giúp bác sĩ nhìn ngay được AI đang dựa vào đoạn sóng nào để đưa ra từ đó.' },
          { n:'04', t:'Hiển thị Theo Lớp', d:'Áp dụng nguyên lý hiển thị dần dần (progressive disclosure): Đầu tiên chỉ hiện kết quả. Nếu bác sĩ cần, mới mở rộng ra Heatmap và phân tích chi tiết.' }
        ],
        insightLabel: 'Insight Cốt Lõi',
        insight: `Bác sĩ không bận tâm "AI này chính xác bao nhiêu %?", câu họ quan tâm là: <strong>"Tôi có thể dùng kết quả này để giải thích cho người nhà bệnh nhân không?"</strong> Tính minh bạch của AI (Explainability) chính là yếu tố sống còn để xây dựng niềm tin.`,
        abTitle: 'So sánh Giao diện — Đánh giá Heuristic',
        abVariants: [
          { lbl: 'Bản V1 (Cơ bản)', pct: 38, cls: 'control', badge: '' },
          { lbl: 'Bản V2 (Có Heatmap)', pct: 82, cls: 'winner', badge: '✓ Được chọn' }
        ],
        abStat: 'Phương pháp: Đánh giá heuristic chuyên gia + Điểm khả dụng (1–100) · 4 đánh giá viên',
        journeyTitle: 'Luồng Thao tác của Bác sĩ',
        journeyStages: ['Xem Kết quả','Đánh giá Tin cậy','Xem Heatmap','Review Tín hiệu','Lưu Bệnh án'],
        journeyRows: [
          { label: 'Câu hỏi trong đầu', cells: ['Bệnh nhân nói gì?','AI chắc chắn không?','Dựa vào vùng não nào?','Có bị nhiễu không?','Lưu vào hồ sơ'], types: ['','','','',''] },
          { label: 'Vấn đề bản V1', cells: ['Chỉ hiện chữ','% không đủ giải thích','❌ Không hỗ trợ','Biểu đồ thô, khó nhìn','Phải chép tay'], types: ['','','pain high','pain','pain'] },
          { label: 'Giải pháp bản V2', cells: ['Chữ + Cắt đoạn tín hiệu','% + Dải màu tin cậy','✅ Overlay Heatmap','Đã lọc + chú thích','Tự động log'], types: ['solution','solution','solution','solution','solution'] },
          { label: 'Độ Tin Tưởng', cells: ['😐','😐','😊','😊','😊'], types: ['emotion-mid','emotion-mid','emotion-high','emotion-high','emotion-high'] }
        ],
        beforeAfterTitle: 'Tác động Thiết kế — Trước vs Sau',
        before: [{ n: 'Điểm Heuristic', v: '38/100' },{ n: 'Độ Minh bạch AI', v: '❌ Không có' },{ n: 'Tin tưởng Bác sĩ', v: '2/5' },{ n: 'Sửa lỗi khi AI sai', v: 'Làm thủ công' }],
        after: [{ n: 'Điểm Heuristic', v: '82/100' },{ n: 'Độ Minh bạch AI', v: '✓ Có Heatmap' },{ n: 'Tin tưởng Bác sĩ', v: '4/5' },{ n: 'Sửa lỗi khi AI sai', v: 'Có luồng hỗ trợ' }],
        learnings: [
          { icon: '🏥', title: 'Hiểu đặc thù Ngành', text: 'Làm UX cho y tế là xây dựng sự tin tưởng. Tính minh bạch của hệ thống là điều bắt buộc phải có chứ không phải tính năng phụ.' },
          { icon: '🧩', title: 'Không nhồi nhét thông tin', text: 'Việc show mọi thứ cùng lúc chỉ làm bác sĩ quá tải. Mở thông tin ra theo từng lớp mới phù hợp với quy trình khám bệnh.' },
          { icon: '🎨', title: 'Dùng Heuristics làm khung', text: 'Bộ 10 nguyên tắc của Nielsen đã giúp nhóm phát hiện và sửa được 6 lỗi UX nghiêm trọng ngay từ đầu.' }
        ]
      },
      {
        cls: 'cs-ereader', num: 'Case Study 03', ctag: 'HCI · Cognitive Load · Education UX',
        title: 'E-Reader: Tái thiết kế Luồng Kích hoạt',
        role: 'User Researcher · HCI Analyst · UX Designer',
        impactNum: 'Top 20', impactLbl: 'Cuộc thi Cấp TP',
        problemLabel: 'Vấn đề Đặt ra',
        problem: `Trong dự án phổ cập máy đọc sách (E-reader) cho học sinh, chúng tôi gặp một rào cản lớn: các em <strong>thường bỏ cuộc ngay từ khâu cài đặt máy ban đầu</strong>. Trải qua tận 7 bước đăng ký, nhập liệu và đồng bộ sách gây quá tải nhận thức cực độ (cognitive overload). Hậu quả là những thiết bị đắt tiền bị vứt xó trong cặp.`,
        approachTitle: 'Cách Tôi Giải Quyết',
        steps: [
          { n:'01', t:'Đo lường Tải Nhận Thức', d:"Đếm số lượng quyết định các em phải đưa ra ở mỗi bước. Có những bước yêu cầu học sinh xử lý tới 5 thông tin cùng lúc — vượt quá giới hạn ghi nhớ ngắn hạn (Định luật Miller)." },
          { n:'02', t:'Áp dụng Nguyên lý HCI', d:"Sử dụng Định luật Hick để giảm bớt các lựa chọn không cần thiết và Gom nhóm (Gestalt proximity) để sắp xếp lại bố cục màn hình thân thiện hơn." },
          { n:'03', t:'Vẽ Hành trình Học sinh', d:"Xây dựng lại toàn bộ hành trình trải nghiệm từ lúc 'mở hộp' đến 'buổi đọc đầu tiên'. Ghi nhận chi tiết cảm xúc và những bước các em bối rối nhất." },
          { n:'04', t:'Gom nhóm (Chunking) 7 còn 3', d:"Gom 7 bước dài dòng thành 3 giai đoạn cốt lõi: Bật máy → Cài sách → Cá nhân hóa. Đẩy các thao tác phụ xuống sau khi học sinh đã quen máy." }
        ],
        insightLabel: 'Insight Cốt Lõi',
        insight: `Học sinh không rành công nghệ không phải là lý do khiến các em bỏ cuộc. Lý do là chúng ta đã <strong>bắt các em làm quá nhiều việc trên cùng một màn hình</strong>. Khi chia nhỏ thao tác để mỗi màn hình chỉ giải quyết đúng một việc, tỷ lệ rắc rối giảm hẳn 60%.`,
        abTitle: 'So sánh Luồng — Tỷ lệ Hoàn thành',
        abVariants: [
          { lbl: 'Luồng 7 bước cũ', pct: 35, cls: 'control', badge: '' },
          { lbl: 'Thiết kế 3 bước mới', pct: 78, cls: 'winner', badge: '✓ Được áp dụng' }
        ],
        abStat: 'Dữ liệu ước tính dựa trên phân tích cognitive load và kiểm thử prototype với 24 học sinh',
        journeyTitle: 'Hành trình Học sinh — Quá trình Cài đặt',
        journeyStages: ['Mở hộp','Bật nguồn','Tạo tài khoản','Tải sách','Đọc lần đầu'],
        journeyRows: [
          { label: 'Mục tiêu', cells: ['Xem thiết bị','Bật lên xem sao','Vào app nhanh','Lấy sách nhanh','Bắt đầu đọc'], types: ['','','','',''] },
          { label: 'Tải Nhận thức', cells: ['Thấp','Thấp','❌ Quá tải (Nhập 5 ô)','❌ Chờ đợi nhàm chán','Thấp'], types: ['','','pain high','pain',''] },
          { label: 'Cảm xúc', cells: ['😄','🙂','😤','😴','😊'], types: ['emotion-high','emotion-high','emotion-low','emotion-mid','emotion-high'] },
          { label: 'Giải pháp HCI', cells: ['—','—','✅ Gom thành 3 bước nhỏ','✅ Thêm Progress bar','—'], types: ['','','solution','solution',''] }
        ],
        beforeAfterTitle: 'Kết quả Trải nghiệm (UX) — Trước vs Sau',
        before: [{ n: 'Hoàn thành Cài đặt', v: '~35%' },{ n: 'Điểm Thoát', v: 'Bước 2–3' },{ n: 'Thời gian setup', v: '22 phút' },{ n: 'Nhờ phụ huynh giúp', v: 'Rất nhiều' }],
        after: [{ n: 'Hoàn thành Cài đặt', v: '~78%' },{ n: 'Điểm Thoát', v: 'Bước 5 (cuối)' },{ n: 'Thời gian setup', v: '8 phút' },{ n: 'Nhờ phụ huynh giúp', v: 'Giảm hẳn' }],
        learnings: [
          { icon: '🧠', title: "Định luật Miller", text: "Chia nhỏ thông tin (chunking) sao cho mỗi bước chỉ có dưới 4 thao tác là cách giải tỏa áp lực tâm lý hiệu quả nhất cho người dùng mới." },
          { icon: '📱', title: 'Một hành động / Màn hình', text: 'Giấu bớt đi các bước chưa cần thiết (progressive disclosure) giúp người dùng thấy mọi thứ nhẹ nhàng hơn rất nhiều.' },
          { icon: '🗺️', title: 'Hành trình trước UI', text: 'Nhờ việc vẽ lại hành trình cảm xúc từ đầu, tôi mới phát hiện ra các lỗi hệ thống mà nếu cắm mặt vào vẽ wireframe chắc chắn sẽ sót.' }
        ]
      }
    ]
  },
  skills: {
    tag: 'Năng lực Lõi', title: 'Kỹ năng <span>Chuyên môn</span>',
    radarLbl: 'Biểu đồ Radar Kỹ năng', certLbl: 'Chứng chỉ', popupTitle: 'Định lượng & Tác động',
    list: [
      {n:'Customer Journey Mapping',ref:'Minh chứng qua: Design Thinking (UEH)',m:['Đã thiết kế 15+ luồng người dùng (user flows) cho startup','Giảm thiểu rào cản onboarding cho 30% khách hàng mới','Tối ưu hóa 5+ touchpoints chuyển đổi quan trọng']},
      {n:'Thiết kế UX / HCI',ref:'Minh chứng qua: Human-Computer Interaction (UEH)',m:['Ứng dụng thành công vào 3 dự án thực tế','Giảm tải nhận thức (cognitive load) hệ thống E-Reader','Thiết kế giao diện Gradio đạt chuẩn Heuristic']},
      {n:'Agile / Scrum (CPMAI)',ref:'Minh chứng qua: Google Project Management & EchoMind',m:['Quản lý mượt mà 8 Sprints liên tục','Dẫn dắt đội ngũ 7 thành viên cross-functional','Hoàn thành 100% milestone dự án đúng hạn']},
      {n:'A/B Testing & Interleaving',ref:'Minh chứng qua: Thử nghiệm sản phẩm tại SIHUB',m:['Thiết kế và chạy 10+ thử nghiệm tính năng','Xác thực giả thuyết với độ tin cậy 95%','Ngăn chặn 3 lỗi thiết kế UX trước khi ra mắt']},
      {n:'Phân rã Vấn đề',ref:'Minh chứng qua: Innovation Management (UEH)',m:['Phân rã 5+ Epics cấp cao thành các task thực thi','Chẩn đoán root-cause lỗi Mode Collapse','Cấu trúc hóa 150+ yêu cầu từ các stakeholders']},
      {n:'Viết PRD & User Stories',ref:'Minh chứng qua: Entrepreneurship Innovation (UEH)',m:['Soạn thảo 10+ PRD chuẩn hóa','Quản lý backlog với 200+ User Stories','Đạt chuẩn tài liệu URD cấp thành phố']},
      {n:'Python & PyTorch (Có nền tảng)',ref:'Ứng dụng qua: Dự án EchoMind AI',m:['Tối ưu kiến trúc mô hình Transformer V2','Áp dụng lượng tử hóa Int8 giảm dung lượng','Giảm độ trễ suy luận AI xuống dưới 1s']}
    ],
    radarLabels: ['UX/HCI','Agile','Journey Map','Phân tích DL','Python','PyTorch/ML','A/B Testing'],
    certs: [
      {i:'🏅',n:'Quản lý Dự án (Google Project Management)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp',dash:false}
    ]
  },
  edu: {
    tag: 'Nền tảng Học vấn', title: 'Học vấn & <span>Thành tích</span>',
    uni: 'Đại học Kinh tế TP.HCM (UEH)', major: 'Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo',
    courseTag: 'Các môn học Cốt lõi định hình Tư duy Sản phẩm',
    courses: ['Tư duy Thiết kế (Design Thinking)','Tương tác Người-Máy (HCI)','Quản trị Đổi mới Sáng tạo','Trí tuệ Doanh nghiệp (BI)','Chuyển đổi Kinh doanh Số','Dự án AI'],
    certTag: 'Chứng chỉ',
    certs: [
      {i:'🏅',n:'Quản lý Dự án (Google Project Management)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp',dash:false}
    ]
  },
  chat: {
    name: 'Trợ lý AI của Minh', sub: '● Trực tuyến · Sẵn sàng giải đáp', reset: '↺ Làm lại', logout: '⏻ Ngôn ngữ',
    greeting: `Xin chào! Tôi là AI đại diện cho Nguyễn Hoàng Minh — Product Owner & UX Strategist. Minh chuyên thiết kế sản phẩm dựa trên sự kết hợp giữa trải nghiệm người dùng, dữ liệu và kiểm thử thực nghiệm.\n\nDanh mục đầu tư hiện có thêm phần UX Experience (Kinh nghiệm UX) mới, thể hiện chi tiết quy trình tư duy thiết kế, thử nghiệm A/B, bản đồ hành trình và tác động kinh doanh của Minh. Bạn muốn khám phá khía cạnh nào?`,
    prompts: [
      {id:'exp',i:'💼',l:'Kinh nghiệm'},{id:'proj',i:'🧠',l:'Dự án'},
      {id:'ux',i:'🎨',l:'UX Work'},{id:'skills',i:'⚡',l:'Kỹ năng'}
    ],
    ans: {
      exp: `Tại SIHUB, Minh đã tích lũy hơn 2 năm kinh nghiệm cốt lõi.\n\n◈ 01–10/2025 | Project Management Executive\nMinh không thích việc chỉ ngồi vẽ các sơ đồ quy trình trên giấy. Thay vào đó, Minh luôn dựa vào dữ liệu thực tế — thông qua A/B testing — để kiểm chứng xem thay đổi về UX có mang lại hiệu quả hay không. Minh cũng giúp team thay đổi góc nhìn về chỉ số NPS, biến nó từ một điểm số đo lường khô khan thành một hệ thống cảnh báo sớm về tỷ lệ giữ chân khách hàng.\n\n◈ 07–12/2024 | R&D Intern\nMinh chịu trách nhiệm phân tích nhu cầu của hơn 150 bên liên quan, sau đó quy chuẩn hóa các phản hồi định tính này thành tài liệu yêu cầu hệ thống (URD). Kinh nghiệm này là nền tảng vững chắc giúp Minh viết PRD rất sắc bén.`,
      proj: `Ba dự án nổi bật này minh chứng rõ nhất cho tư duy phát triển sản phẩm của Minh:\n\n🧠 EchoMind AI — Flagship (09–12/2025)\nHệ thống dịch sóng não thành văn bản. Với vai trò Project Lead, Minh đã quản lý 8 Sprints, quyết đoán đổi hướng sang kiến trúc Transformer V2 khi mô hình cũ gặp lỗi. Nhờ áp dụng lượng tử hóa, hệ thống chạy mượt trên máy cá nhân với tốc độ 55-65 WPM và đạt 100% KPI kỹ thuật.\n\n📚 Hệ sinh thái E-Reader — Top 20 cấp TP\nỞ vai trò User Researcher, Minh thiết kế lại toàn bộ hành trình UX dựa trên nguyên lý HCI, giúp loại bỏ các bước thao tác thừa khiến học sinh bị quá tải nhận thức. Dự án xuất sắc lọt Top 20 cuộc thi do UBND TP.HCM tổ chức.\n\n🚀 Vận hành Sự kiện ĐMST\nTrực tiếp điều phối thành công các sự kiện quy mô lớn như Univ.Star và Tuần lễ WHISE.`,
      ux: `Phần Kinh nghiệm UX của Minh gồm 3 case studies rất chi tiết:\n\n🗺️ Case 01: Thiết kế lại luồng Onboarding tại SIHUB\nVấn đề: tỷ lệ kích hoạt chỉ 42%. Áp dụng journey mapping + A/B testing. Kết quả: nâng tỷ lệ kích hoạt lên 68%, tăng điểm NPS từ 28 lên 47, giảm 70% yêu cầu hỗ trợ (support tickets).\n\n🏥 Case 02: Dashboard Chuyên gia EchoMind\nVấn đề: AI hộp đen trong y tế khiến bác sĩ e ngại. Giải pháp: Áp dụng đánh giá HCI heuristic + thiết kế giao diện Heatmap. Kết quả: Điểm heuristic tăng từ 38 lên 82/100, độ tin tưởng của bác sĩ tăng từ 2/5 lên 4/5.\n\n📱 Case 03: Luồng Kích hoạt E-Reader\nVấn đề: học sinh bỏ dở ngay bước cài đặt máy. Giải pháp: Áp dụng Định luật Miller + Hick để chia nhỏ thông tin. Kết quả: Tỷ lệ hoàn thành cài đặt tăng từ 35% lên 78%.`,
      skills: `Năng lực cốt lõi của Minh được xây dựng trên 3 trụ cột vững chắc:\n\n◈ Product Craft (Thế mạnh Cốt lõi)\n→ Lập bản đồ hành trình (95%) · UX/HCI (90%) · Agile/CPMAI (88%)\n→ Viết PRD & User Stories · Kiểm thử A/B · Phân rã Vấn đề\n\n◈ Dữ liệu & Tư duy Hệ thống\n→ Python (Có nền tảng) · Phân tích Dữ liệu (EDA)\n→ Am hiểu PyTorch và kiến trúc Transformer\n\n◈ Quản lý Stakeholder & Thực thi\n→ Kinh nghiệm làm việc với 150+ đối tác cấp thành phố\n→ Trình bày báo cáo chiến lược cấp Ban Giám đốc\n→ Dẫn dắt đội ngũ kỹ thuật vận hành theo quy trình Agile`
    }
  }
}
};

// STATE
let lang='en',isTyping=false,isTrans=false;
let chartInst=null,kpiChartInst=null,modelChartInst=null,burndownChartInst=null;

// TOAST
function showToast(msg,type='success',dur=2200){
  const t=document.getElementById('toast');
  t.textContent=msg;t.style.borderColor=type==='success'?'var(--green)':'var(--accent)';
  t.style.color=type==='success'?'var(--green)':'var(--accent2)';
  t.classList.add('show');setTimeout(()=>t.classList.remove('show'),dur);
}

// COPY EMAIL
function copyEmail(){
  const email='hwinh.work@gmail.com';
  const msg=lang==='en'?'✓ Email copied to clipboard!':'✓ Đã copy email vào clipboard!';
  if(navigator.clipboard){navigator.clipboard.writeText(email).then(()=>showToast(msg)).catch(()=>showToast(email,'info'));}
  else{const el=document.createElement('textarea');el.value=email;document.body.appendChild(el);el.select();document.execCommand('copy');document.body.removeChild(el);showToast(msg);}
}

// FLOATING SKILL POPUP
function showSkillPopup(card){
  const idx=parseInt(card.getAttribute('data-skill-idx'));const sk=T[lang].skills.list[idx];if(!sk)return;
  const fp=document.getElementById('float-popup');
  document.getElementById('fp-title').textContent=T[lang].skills.popupTitle;
  document.getElementById('fp-metrics').innerHTML=sk.m.map(m=>`<div class="popup-metric">${m}</div>`).join('');
  fp.style.visibility='visible';fp.style.opacity='1';
  requestAnimationFrame(()=>{
    const rect=card.getBoundingClientRect(),fpH=fp.offsetHeight||160,fpW=fp.offsetWidth||300;
    let top=rect.top>fpH+16?rect.top-fpH-10:rect.bottom+10;
    let left=rect.left+rect.width/2-fpW/2;
    left=Math.max(10,Math.min(left,window.innerWidth-fpW-10));top=Math.max(10,Math.min(top,window.innerHeight-fpH-10));
    fp.style.top=top+'px';fp.style.left=left+'px';
  });
}
function hideSkillPopup(){const fp=document.getElementById('float-popup');fp.style.opacity='0';fp.style.visibility='hidden';}

// KEYBOARD SHORTCUTS
document.addEventListener('keydown',(e)=>{
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
  const overlay=document.getElementById('lang-overlay');
  const visible=overlay.style.visibility!=='hidden'&&overlay.style.opacity!=='0';
  if(!visible){
    const views=['welcome','experience','projects','ux','skills','education'];
    if(e.key>='1'&&e.key<='6'){const idx=parseInt(e.key)-1;const navItems=document.querySelectorAll('.nav-item');if(navItems[idx])go(views[idx],navItems[idx]);}
    if(e.key==='Escape')logout();
  }
});

// LANG SELECT + LOGOUT
function selectLang(l){
  lang=l;
  document.getElementById('lang-overlay').style.opacity='0';document.getElementById('lang-overlay').style.visibility='hidden';
  document.getElementById('main-app').classList.add('visible');
  renderUI();initChat();
}
function logout(){
  hideSkillPopup();
  document.getElementById('lang-overlay').style.opacity='1';document.getElementById('lang-overlay').style.visibility='visible';
  document.getElementById('main-app').classList.remove('visible');
  document.getElementById('chat-messages').innerHTML='';
  [kpiChartInst,modelChartInst,burndownChartInst,chartInst].forEach(c=>{if(c){try{c.destroy();}catch(e){}}});
  kpiChartInst=modelChartInst=burndownChartInst=chartInst=null;
}

// RENDER UI
function renderUI(){
  const t=T[lang];
  for(let i=0;i<6;i++){
    const nl=document.getElementById('nl'+i),ntt=document.getElementById('ntt'+i);
    if(nl)nl.textContent=t.nav[i];if(ntt)ntt.textContent=t.navTip[i];
  }
  const kh=document.getElementById('kbd-nav-hint'),kd=document.getElementById('kbd-nav-desc');
  if(kh)kh.textContent=t.kbdNavHint;if(kd)kd.textContent=t.kbdNavDesc;
  document.getElementById('w-status').textContent=t.w.status;
  document.getElementById('w-role').textContent=t.w.role;
  document.getElementById('w-summary').innerHTML=t.w.summary;
  ['ws1','ws2','ws3','ws4'].forEach((id,i)=>{const el=document.getElementById(id);if(el)el.textContent=t.w.stats[i];});
  document.getElementById('w-explore').textContent=t.w.explore;
  document.getElementById('w-hint').textContent=t.w.hint;
  // Experience
  document.getElementById('e-tag').textContent=t.exp.tag;document.getElementById('e-title').innerHTML=t.exp.title;
  document.getElementById('e-timeline').innerHTML=t.exp.items.map((item,idx)=>`
    <div class="timeline-item ${idx>0?'past':''}">
      <div class="tl-period">${item.period}</div><div class="tl-role">${item.role}</div>
      <div class="tl-company">${item.company}</div>
      <ul class="tl-bullets">${item.bullets.map(b=>`<li>${b}</li>`).join('')}</ul>
      <div class="tl-tags">${item.tags.map(tg=>`<span class="tl-tag">${tg}</span>`).join('')}</div>
    </div>`).join('');
  // Projects
  document.getElementById('p-tag').textContent=t.proj.tag;document.getElementById('p-title').innerHTML=t.proj.title;renderProjects();
  // UX section
  document.getElementById('ux-tag').textContent=t.ux.tag;document.getElementById('ux-title').innerHTML=t.ux.title;
  document.getElementById('ux-dt-title').textContent=t.ux.dtTitle;
  renderUX();
  // Skills
  document.getElementById('s-tag').textContent=t.skills.tag;document.getElementById('s-title').innerHTML=t.skills.title;
  document.getElementById('s-radar-lbl').textContent=t.skills.radarLbl;document.getElementById('s-cert-lbl').textContent=t.skills.certLbl;
  document.getElementById('s-list').innerHTML=t.skills.list.map((sk,idx)=>`
    <div class="lk-skill-card" data-skill-idx="${idx}" onmouseenter="showSkillPopup(this)" onmouseleave="hideSkillPopup()">
      <div class="lk-skill-header"><div class="lk-skill-title"><span style="color:var(--accent2);font-size:18px;">❖</span> ${sk.n}</div><span style="font-size:14px;opacity:.5;color:var(--text2);">ℹ️</span></div>
      <div class="lk-skill-ref">${sk.ref}</div>
    </div>`).join('');
  document.getElementById('s-certs').innerHTML=renderCerts(t.skills.certs);
  // Education
  document.getElementById('ed-tag').textContent=t.edu.tag;document.getElementById('ed-title').innerHTML=t.edu.title;
  document.getElementById('ed-uni').textContent=t.edu.uni;document.getElementById('ed-major').textContent=t.edu.major;
  document.getElementById('ed-courses').innerHTML=`<div class="proj-chart-title" style="margin-bottom:14px;">${t.edu.courseTag}</div><div style="display:flex;flex-wrap:wrap;gap:10px;">${t.edu.courses.map(c=>`<span style="font-size:13px;padding:7px 16px;background:var(--surface);border:1px solid var(--border2);border-radius:9px;color:var(--text2);">${c}</span>`).join('')}</div>`;
  document.getElementById('ed-cert-lbl').textContent=t.edu.certTag;document.getElementById('ed-certs').innerHTML=renderCerts(t.edu.certs);
  document.getElementById('c-name').textContent=t.chat.name;document.getElementById('c-sub').textContent=t.chat.sub;
  document.getElementById('c-reset').textContent=t.chat.reset;document.getElementById('c-logout').textContent=t.chat.logout;
}

function renderCerts(certs){
  return certs.map(c=>{
    const tag=c.link?'a':'div',href=c.link?` href="${c.link}" target="_blank" rel="noopener noreferrer"`:'' ;
    const icon=c.link?`<div style="color:var(--text2);opacity:.5;font-size:16px;transition:all .2s;" class="cert-link-icon">↗</div>`:'';
    return `<${tag} class="cert-card" style="${c.dash?'border-style:dashed;border-color:rgba(240,192,96,.3);':''}text-decoration:none;"${href}><span style="font-size:22px;flex-shrink:0;">${c.i}</span><div style="flex:1;"><div style="color:var(--text);font-size:14px;font-weight:500;">${c.n}</div><div style="font-size:11.5px;color:var(--text2);margin-top:2px;">${c.org}</div></div>${c.prog?`<span style="font-family:'DM Mono',monospace;font-size:10.5px;color:var(--gold);padding:4px 12px;background:rgba(240,192,96,.1);border-radius:20px;white-space:nowrap;">${c.prog}</span>`:''} ${icon}</${tag}>`;
  }).join('');
}

// ================================================================
// RENDER UX SECTION
// ================================================================
function renderUX(){
  const ux=T[lang].ux;
  // Design Thinking Flow
  document.getElementById('ux-dt-flow').innerHTML=ux.phases.map(p=>`
    <div class="dt-phase">
      <span class="dt-phase-num">${p.num}</span>
      <span class="dt-phase-icon">${p.icon}</span>
      <div class="dt-phase-name">${p.name}</div>
      <div class="dt-phase-desc">${p.desc}</div>
    </div>`).join('');
  // Case Studies
  document.getElementById('ux-cases').innerHTML=ux.cases.map(cs=>renderCaseStudy(cs)).join('');
}

function renderCaseStudy(cs){
  // A/B bars HTML
  const abBars=cs.abVariants.map(v=>`
    <div class="ab-row">
      <span class="ab-variant-lbl">${v.lbl}</span>
      <div class="ab-bar-track">
        <div class="ab-bar-fill ${v.cls}" data-pct="${v.pct}" style="width:${v.pct}%;">${v.pct}%</div>
      </div>
      ${v.badge?`<span class="ab-badge win">${v.badge}</span>`:'<span style="min-width:80px;"></span>'}
    </div>`).join('');
  // Journey rows
  const jmCols=cs.journeyStages.length;
  const stageRow=`<div class="jm-stage-row" style="display:flex;gap:1px;margin-bottom:1px;"><div style="min-width:110px;flex-shrink:0;"></div><div class="jm-cells" style="flex:1;gap:1px;">${cs.journeyStages.map(s=>`<div class="jm-cell stage-name">${s}</div>`).join('')}</div></div>`;
  const dataRows=cs.journeyRows.map(row=>`
    <div class="jm-stage-row" style="display:flex;gap:1px;margin-bottom:1px;">
      <div class="jm-label">${row.label}</div>
      <div class="jm-cells">${row.cells.map((c,i)=>`<div class="jm-cell ${row.types[i]||''}">${c}</div>`).join('')}</div>
    </div>`).join('');
  // Before/After
  const beforeRows=cs.before.map(r=>`<div class="impact-metric-row"><span class="impact-metric-name">${r.n}</span><span class="impact-metric-val">${r.v}</span></div>`).join('');
  const afterRows=cs.after.map(r=>`<div class="impact-metric-row"><span class="impact-metric-name">${r.n}</span><span class="impact-metric-val">${r.v}</span></div>`).join('');
  const learnings=cs.learnings.map(l=>`<div class="learning-card"><span class="learning-icon">${l.icon}</span><div class="learning-title">${l.title}</div><div class="learning-text">${l.text}</div></div>`).join('');
  return `
    <div class="case-study ${cs.cls} fade-up">
      <div class="cs-header">
        <div class="cs-meta">
          <div class="cs-eyebrow"><span class="cs-num">${cs.num}</span><span class="cs-tag">${cs.ctag}</span></div>
          <div class="cs-title">${cs.title}</div>
          <div class="cs-role">${cs.role}</div>
        </div>
        <div class="cs-impact-badge"><div class="cs-impact-num">${cs.impactNum}</div><div class="cs-impact-lbl">${cs.impactLbl}</div></div>
      </div>

      <div class="problem-box">
        <div class="problem-label">${cs.problemLabel}</div>
        <div class="problem-text">${cs.problem}</div>
      </div>

      <div class="cs-body">
        <div>
          <div class="cs-section-title">${cs.approachTitle}</div>
          <div class="process-steps">${cs.steps.map(s=>`<div class="process-step"><span class="step-num">${s.n}</span><div class="step-content"><div class="step-title">${s.t}</div><div class="step-desc">${s.d}</div></div></div>`).join('')}</div>
        </div>
        <div>
          <div class="insight-box"><div class="insight-label">${cs.insightLabel}</div><div class="insight-text">${cs.insight}</div></div>
          <div class="ab-container">
            <div class="ab-title">${cs.abTitle}</div>
            <div class="ab-variants">${abBars}</div>
            <div class="ab-stat">${cs.abStat}</div>
          </div>
        </div>
      </div>

      <div class="cs-section-title" style="margin-bottom:12px;">${cs.journeyTitle}</div>
      <div class="journey-map">${stageRow}${dataRows}</div>

      <div class="cs-section-title" style="margin:20px 0 14px;">${cs.beforeAfterTitle}</div>
      <div class="impact-compare">
        <div class="impact-col before"><div class="impact-col-label">Before</div>${beforeRows}</div>
        <div class="impact-arrow">→</div>
        <div class="impact-col after"><div class="impact-col-label">After</div>${afterRows}</div>
      </div>

      <div class="cs-learnings">${learnings}</div>
    </div>`;
}

// PROJECTS
function renderProjects(){
  const t=T[lang];const grid=document.getElementById('p-grid');
  grid.innerHTML=t.proj.items.map(p=>{
    if(p.id==='echomind'){
      return `<div class="project-card featured" id="ec-card"><div>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;"><span class="project-badge ${p.bClass}">${p.badge}</span><span class="project-badge badge-active">${p.date}</span></div>
        <div class="project-name">${p.name}</div><div class="project-sub">${p.sub}</div>
        <p class="project-desc">${p.desc.replace(/\n/g,'<br>')}</p>
        <div class="info-grid">${p.info.map(i=>`<div class="info-item"><div class="info-lbl">${i.l}</div><div class="info-val">${i.v}</div></div>`).join('')}</div>
        <div class="project-metrics">${p.metrics.map(m=>`<div class="metric"><div class="metric-val">${m.v}</div><div class="metric-lbl">${m.l}</div></div>`).join('')}</div>
        <div class="proj-chart-wrap"><div class="proj-chart-title" id="kpi-chart-title">Technical KPI Breakdown — vs Traditional AAC</div><div style="height:200px;position:relative;"><canvas id="kpiChart"></canvas></div></div>
        <div class="proj-chart-wrap"><div class="proj-chart-title" id="model-chart-title">Model Comparison: LSTM V1 vs Transformer V2</div><div style="height:180px;position:relative;"><canvas id="modelChart"></canvas></div></div>
        <div class="tech-stack">${p.tech.map(tch=>`<span class="tech-pill">${tch}</span>`).join('')}</div>
      </div>
      <div style="background:var(--ink3);border-radius:18px;border:1px solid var(--border);padding:22px;text-align:center;">
        <div style="font-size:40px;margin-bottom:14px;">🧠</div>
        <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);line-height:2.2;text-align:left;">EEG Input (256ch)<br>↓ HDF5 → Tensor<br>↓ Positional Enc.<br>↓ Transformer V2<br>↓ Beam Search<br>→ Text Output</div>
        <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);margin-bottom:4px;" id="ec-role-lbl">Role</div>
          <div style="font-size:13px;color:var(--text);font-weight:600;">Project Lead</div>
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);margin:10px 0 4px;" id="ec-team-lbl">Team</div>
          <div style="font-size:12px;color:var(--text);">7 members · 8 sprints</div>
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--text2);margin:10px 0 4px;" id="ec-adv-lbl">Advisor</div>
          <div style="font-size:11px;color:var(--text2);">ThS. Tạ Việt Phương</div>
        </div>
        <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--accent2);letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;" id="ec-sprint-lbl">Sprint Burndown</div>
          <div style="height:140px;position:relative;"><canvas id="burndownChart"></canvas></div>
        </div>
      </div></div>`;
    } else {
      return `<div class="project-card">
        <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:12px;"><span class="project-badge ${p.bClass}">${p.badge}</span><span style="font-family:'DM Mono',monospace;font-size:10.5px;color:var(--text2);">${p.date}</span></div>
        <div class="project-name" style="font-size:22px;">${p.name}</div><div class="project-sub">${p.sub}</div>
        <p class="project-desc">${p.desc.replace(/\n/g,'<br>')}</p>
        <div class="tech-stack">${p.tech.map(tch=>`<span class="tech-pill">${tch}</span>`).join('')}</div>
      </div>`;
    }
  }).join('');
}

// CHARTS
function renderKPIChart(){
  const ctx=document.getElementById('kpiChart');if(!ctx)return;
  if(kpiChartInst){kpiChartInst.destroy();kpiChartInst=null;}
  const isVI=lang==='vi';
  const labels=isVI?['Độ chính xác','Tốc độ (WPM)','Độ trễ (cải thiện)','Tỷ lệ thành công']:['Accuracy','Speed (WPM)','Latency (improvement)','Session Success'];
  kpiChartInst=new Chart(ctx,{type:'bar',data:{labels,datasets:[{label:isVI?'AAC Truyền thống':'Traditional AAC',data:[60,30,0,40],backgroundColor:'rgba(98,98,128,.4)',borderColor:'rgba(98,98,128,.8)',borderWidth:1,borderRadius:5},{label:'EchoMind V2',data:[93,60,75,72],backgroundColor:'rgba(124,106,247,.55)',borderColor:'rgba(165,148,252,.9)',borderWidth:1,borderRadius:5}]},options:{responsive:true,maintainAspectRatio:false,scales:{x:{grid:{color:'rgba(255,255,255,.05)'},ticks:{color:'#9898b0',font:{family:"'DM Sans',sans-serif",size:11}}},y:{grid:{color:'rgba(255,255,255,.05)'},ticks:{color:'#9898b0',font:{family:"'DM Mono',monospace",size:10}},max:100,min:0}},plugins:{legend:{labels:{color:'#9898b0',font:{family:"'DM Sans',sans-serif",size:11},boxWidth:12}},tooltip:{backgroundColor:'#252538',titleFont:{family:"'DM Mono',monospace"},bodyFont:{family:"'DM Sans',sans-serif"},borderColor:'rgba(255,255,255,.1)',borderWidth:1,callbacks:{label:c=>` ${c.dataset.label}: ${c.raw}${c.dataIndex===2?'% '+(isVI?'giảm':'reduction'):'%'}`}}}}});
}
function renderModelChart(){
  const ctx=document.getElementById('modelChart');if(!ctx)return;
  if(modelChartInst){modelChartInst.destroy();modelChartInst=null;}
  const isVI=lang==='vi';const lbls=isVI?['WER (%)','Độ chính xác (%)','Tốc độ (WPM)','Tỷ lệ Mode Collapse']:['WER (%)','Accuracy (%)','Speed (WPM)','Mode Collapse Rate'];
  modelChartInst=new Chart(ctx,{type:'radar',data:{labels:lbls,datasets:[{label:'LSTM V1 (Baseline)',data:[85,15,25,95],borderColor:'rgba(255,123,107,.7)',backgroundColor:'rgba(255,123,107,.08)',borderWidth:1.5,pointRadius:3,pointBackgroundColor:'rgba(255,123,107,.8)'},{label:'Transformer V2',data:[8,93,60,0],borderColor:'rgba(165,148,252,.8)',backgroundColor:'rgba(124,106,247,.12)',borderWidth:1.8,pointRadius:3,pointBackgroundColor:'#a594fc'}]},options:{responsive:true,maintainAspectRatio:false,scales:{r:{min:0,max:100,ticks:{display:false},angleLines:{color:'rgba(255,255,255,.07)'},grid:{color:'rgba(255,255,255,.07)'},pointLabels:{color:'#9898b0',font:{size:10,family:"'DM Sans',sans-serif"}}}},plugins:{legend:{labels:{color:'#9898b0',font:{family:"'DM Sans',sans-serif",size:11},boxWidth:12,padding:14}},tooltip:{backgroundColor:'#252538',titleFont:{family:"'DM Mono',monospace"},bodyFont:{family:"'DM Sans',sans-serif"},borderColor:'rgba(255,255,255,.1)',borderWidth:1}}}});
}
function renderBurndownChart(){
  const ctx=document.getElementById('burndownChart');if(!ctx)return;
  if(burndownChartInst){burndownChartInst.destroy();burndownChartInst=null;}
  const isVI=lang==='vi';
  burndownChartInst=new Chart(ctx,{type:'line',data:{labels:['Start','S0','S1','S2-3','S4','S5','S6','S7'],datasets:[{label:isVI?'Lý tưởng':'Ideal',data:[3833,3280,2727,2174,1621,1068,515,0],borderColor:'rgba(98,98,128,.5)',borderWidth:1.5,borderDash:[5,4],pointRadius:0,fill:false},{label:isVI?'Thực tế':'Actual',data:[3833,3253,2560,2086,1534,1057,612,0],borderColor:'#a594fc',borderWidth:2,pointRadius:3,pointBackgroundColor:'#a594fc',fill:{target:'origin',above:'rgba(124,106,247,.06)'}}]},options:{responsive:true,maintainAspectRatio:false,scales:{x:{grid:{display:false},ticks:{color:'#5a5a78',font:{family:"'DM Mono',monospace",size:9}}},y:{grid:{color:'rgba(255,255,255,.04)'},ticks:{color:'#5a5a78',font:{family:"'DM Mono',monospace",size:9},callback:v=>(v/1000).toFixed(1)+'k'}}},plugins:{legend:{labels:{color:'#9898b0',font:{family:"'DM Sans',sans-serif",size:10},boxWidth:10,padding:10}},tooltip:{backgroundColor:'#252538',titleFont:{family:"'DM Mono',monospace"},bodyFont:{family:"'DM Sans',sans-serif"},borderColor:'rgba(255,255,255,.1)',borderWidth:1}}}});
}
function updateProjectChartLabels(){
  const isVI=lang==='vi';
  const e=(id,txt)=>{const el=document.getElementById(id);if(el)el.textContent=txt;};
  e('kpi-chart-title',isVI?'Phân tích KPI Kỹ thuật — So với AAC Truyền thống':'Technical KPI Breakdown — vs Traditional AAC');
  e('model-chart-title',isVI?'So sánh Mô hình: LSTM V1 vs Transformer V2':'Model Comparison: LSTM V1 vs Transformer V2');
  e('ec-role-lbl',isVI?'Vai trò':'Role');e('ec-team-lbl',isVI?'Nhóm':'Team');
  e('ec-adv-lbl',isVI?'GVHD':'Advisor');e('ec-sprint-lbl',isVI?'Burndown Sprints':'Sprint Burndown');
}

// VIEW SWITCHING
function go(viewId,navEl){
  if(isTrans)return;
  const target=document.getElementById('view-'+viewId);
  if(!target||target.style.display!=='none')return;
  isTrans=true;
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  if(navEl)navEl.classList.add('active');
  else{const n=document.querySelector(`[data-view="${viewId}"]`);if(n)n.classList.add('active');}
  hideSkillPopup();
  const tr=document.getElementById('view-tr');tr.classList.add('active');
  setTimeout(()=>{
    document.querySelectorAll('.view-content').forEach(v=>v.style.display='none');
    target.style.display='';
    document.getElementById('scroll-progress').style.width='0%';
    document.getElementById('visual-panel').scrollTop=0;
    if(viewId==='skills')setTimeout(initSkillsChart,70);
    if(viewId==='projects'){setTimeout(()=>{updateProjectChartLabels();renderKPIChart();renderModelChart();renderBurndownChart();},80);}
    const animEls=target.querySelectorAll('.fade-up');
    animEls.forEach(el=>{el.style.animation='none';void el.offsetWidth;el.style.animation=null;});
    setTimeout(()=>{tr.classList.remove('active');isTrans=false;},120);
  },260);
}

// SKILLS CHART
function initSkillsChart(){
  const ctx=document.getElementById('skillsChart');if(!ctx)return;
  if(chartInst){chartInst.destroy();chartInst=null;}
  const t=T[lang];
  chartInst=new Chart(ctx,{type:'radar',data:{labels:t.skills.radarLabels,datasets:[{data:[95,88,95,80,65,65,82],fill:true,backgroundColor:'rgba(124,106,247,.14)',borderColor:'#7c6af7',pointBackgroundColor:'#a594fc',pointBorderColor:'#1e1e2e',borderWidth:2,pointRadius:4}]},options:{responsive:true,maintainAspectRatio:false,scales:{r:{min:0,max:100,ticks:{display:false},angleLines:{color:'rgba(255,255,255,.07)'},grid:{color:'rgba(255,255,255,.07)'},pointLabels:{font:{size:12,family:"'DM Sans',sans-serif",weight:'500'},color:'#9898b0'}}},plugins:{legend:{display:false},tooltip:{backgroundColor:'#252538',borderColor:'rgba(255,255,255,.1)',borderWidth:1,padding:12,callbacks:{label:c=>{const v=c.raw;if(lang==='vi')return v>=90?' Chuyên gia':v>=80?' Cao cấp':v>=70?' Thành thạo':' Có nền tảng';return v>=90?' Expert':v>=80?' Advanced':v>=70?' Proficient':' Familiar';}}}}}});
}

// SCROLL PROGRESS
document.getElementById('visual-panel').addEventListener('scroll',function(){
  const h=this.scrollHeight-this.clientHeight;
  if(h>0)document.getElementById('scroll-progress').style.width=(this.scrollTop/h*100)+'%';
});

// CHAT
function initChat(){
  document.getElementById('chat-messages').innerHTML='';renderPrompts();
  setTimeout(()=>appendMsg('ai',T[lang].chat.greeting,true),400);
}
function renderPrompts(){
  const pg=document.getElementById('prompts-grid');
  pg.innerHTML=T[lang].chat.prompts.map(p=>`<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.l}')" ${isTyping||isTrans?'disabled':''}><span class="p-icon">${p.i}</span><span class="p-lbl">${p.l}</span></button>`).join('');
}
function handlePrompt(id,label){
  if(isTyping||isTrans)return;
  document.getElementById('prompts-grid').style.opacity='.4';
  appendMsg('user',label,false);
  const vMap={exp:'experience',proj:'projects',edu:'education',skills:'skills',ux:'ux'};
  setTimeout(()=>go(vMap[id]||'welcome',null),300);
  setTimeout(()=>appendMsg('ai',T[lang].chat.ans[id],true,()=>{document.getElementById('prompts-grid').style.opacity='1';renderPrompts();}),650);
}
function appendMsg(s,txt,tw=false,cb=null){
  const cm=document.getElementById('chat-messages');
  const row=document.createElement('div');row.className='msg-row '+s;
  const av=document.createElement('div');av.className='msg-av '+s;av.textContent=s==='ai'?'🤖':'👤';
  const bub=document.createElement('div');bub.className='msg-bubble '+s;
  row.appendChild(av);row.appendChild(bub);cm.appendChild(row);
  if(s==='ai'&&tw)typeW(txt,bub,cb);
  else{bub.innerHTML=txt.replace(/\n/g,'<br>');cm.scrollTop=cm.scrollHeight;if(cb)cb();}
}
function typeW(txt,el,cb){
  isTyping=true;renderPrompts();
  const cm=document.getElementById('chat-messages');
  const tmpDiv=document.createElement('div');tmpDiv.innerHTML=txt.replace(/\n/g,'<br>');
  const nodes=Array.from(tmpDiv.childNodes);
  el.innerHTML='<span class="tc"></span><span class="cursor-blink"></span>';
  const tc=el.querySelector('.tc');let ni=0,ci=0;
  function type(){
    if(ni<nodes.length){
      const nd=nodes[ni];
      if(nd.nodeType===3){if(ci<nd.textContent.length){tc.innerHTML+=nd.textContent.charAt(ci++);cm.scrollTop=cm.scrollHeight;setTimeout(type,Math.floor(Math.random()*18)+4);}else{ni++;ci=0;type();}}
      else{tc.appendChild(nd.cloneNode(true));ni++;cm.scrollTop=cm.scrollHeight;setTimeout(type,8);}
    } else {
      isTyping=false;const cur=el.querySelector('.cursor-blink');if(cur)cur.remove();renderPrompts();if(cb)cb();
    }
  }
  type();
}
function resetChat(){if(isTyping||isTrans)return;initChat();}
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
