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
  --gold:#f0c060;--green:#52d18a;--coral:#ff7b6b;--teal:#4dd9c0;--blue:#5b9bd5;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'DM Sans',sans-serif;background:var(--ink);color:var(--text);height:100vh;overflow:hidden;-webkit-font-smoothing:antialiased;}

/* TOAST */
#toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(16px);background:var(--surface2);border:1px solid var(--green);color:var(--green);font-family:'DM Mono',monospace;font-size:12px;padding:10px 22px;border-radius:10px;z-index:99999;opacity:0;transition:all .35s cubic-bezier(.16,1,.3,1);pointer-events:none;white-space:nowrap;box-shadow:0 8px 24px rgba(0,0,0,.35);letter-spacing:.5px;}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0);}

/* FLOAT POPUP */
#float-popup{position:fixed;width:300px;background:rgba(18,18,26,0.97);border:1px solid var(--accent);border-radius:14px;padding:16px 18px;box-shadow:0 20px 50px rgba(0,0,0,.6);backdrop-filter:blur(12px);opacity:0;visibility:hidden;transition:opacity .22s ease,visibility .22s ease;pointer-events:none;z-index:99998;}
.popup-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);text-transform:uppercase;letter-spacing:1px;margin-bottom:10px;}
.popup-metric{font-size:13px;color:var(--text);line-height:1.5;display:flex;align-items:start;gap:8px;margin-bottom:8px;}
.popup-metric:last-child{margin-bottom:0;}
.popup-metric::before{content:'•';color:var(--green);font-weight:bold;flex-shrink:0;}

/* SCROLL PROGRESS */
#scroll-progress{position:fixed;top:0;left:90px;height:3px;background:linear-gradient(90deg,var(--accent),var(--teal));width:0%;z-index:1000;transition:width .1s ease-out;border-radius:0 2px 2px 0;}

/* LANG OVERLAY */
#lang-overlay{position:fixed;inset:0;background:var(--ink);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;transition:opacity .5s ease,visibility .5s;}
.lo-logo{font-family:'Syne',sans-serif;font-size:64px;font-weight:800;color:var(--accent2);letter-spacing:-3px;line-height:1;}
.lo-tagline{font-family:'DM Mono',monospace;font-size:12px;color:var(--text2);letter-spacing:3px;text-transform:uppercase;}
.lo-question{font-family:'Syne',sans-serif;font-size:22px;font-weight:600;color:var(--text);text-align:center;line-height:1.5;}
.lo-options{display:flex;gap:20px;align-items:stretch;}
.lo-btn{background:var(--surface);border:2px solid var(--border2);color:var(--text2);padding:20px 48px;border-radius:14px;font-family:'Syne',sans-serif;font-size:20px;font-weight:600;cursor:pointer;transition:all .3s cubic-bezier(.16,1,.3,1);display:flex;flex-direction:column;align-items:center;gap:8px;}
.lo-btn:hover{border-color:var(--accent);background:var(--surface2);transform:translateY(-4px);box-shadow:0 12px 30px rgba(124,106,247,.2);color:var(--text);}
.lo-btn span{font-family:'DM Mono',monospace;font-size:11px;color:var(--text2);}
.lo-kbhint{font-family:'DM Mono',monospace;font-size:11px;color:var(--text3);letter-spacing:1px;text-align:center;}

/* LAYOUT */
.app{display:flex;height:100vh;width:100%;opacity:0;transition:opacity .7s ease;}
.app.visible{opacity:1;}

/* SIDENAV */
.sidenav{width:90px;height:100%;background:var(--ink2);border-right:1px solid var(--border);display:flex;flex-direction:column;align-items:center;padding:28px 0 24px;gap:10px;flex-shrink:0;z-index:10;}
.nav-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:18px;color:var(--accent2);margin-bottom:16px;letter-spacing:-.5px;}
.nav-item{width:58px;height:54px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;color:var(--text2);border:1px solid transparent;position:relative;gap:3px;}
.nav-item svg{width:20px;height:20px;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0;}
.nav-item .nav-lbl{font-family:'DM Mono',monospace;font-size:8px;letter-spacing:.3px;text-transform:uppercase;opacity:.7;white-space:nowrap;}
.nav-item:hover{background:var(--surface);color:var(--text);}
.nav-item.active{background:linear-gradient(135deg,rgba(124,106,247,.3),rgba(124,106,247,.12));color:var(--accent2);border-color:rgba(124,106,247,.35);box-shadow:0 0 18px rgba(124,106,247,.2);}
.nav-tooltip{position:absolute;left:74px;background:var(--surface2);color:var(--text);font-size:12px;font-family:'DM Mono',monospace;padding:6px 12px;border-radius:7px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .15s;border:1px solid var(--border2);z-index:100;}
.nav-item:hover .nav-tooltip{opacity:1;}
.nav-spacer{flex:1;}

/* VISUAL PANEL */
.visual-panel{flex:1;height:100%;overflow-y:auto;background:var(--ink);position:relative;}
.visual-panel::-webkit-scrollbar{width:5px;}
.visual-panel::-webkit-scrollbar-thumb{background:var(--border2);border-radius:5px;}

/* TRANSITION */
.view-tr{position:fixed;top:0;left:90px;right:420px;bottom:0;background:var(--ink);z-index:999;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .25s ease;}
.view-tr.active{opacity:1;pointer-events:all;}
.spinner{width:36px;height:36px;border:3px solid var(--border2);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;}
@keyframes spin{100%{transform:rotate(360deg);}}

/* CHAT PANEL */
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
.msg-bubble{max-width:82%;padding:14px 18px;border-radius:18px;font-size:13.5px;line-height:1.65;}
.msg-bubble.ai{background:var(--surface);border:1px solid var(--border2);color:var(--text);border-bottom-left-radius:4px;}
.msg-bubble.user{background:var(--accent);color:white;border-bottom-right-radius:4px;}
.cursor-blink{display:inline-block;width:8px;height:15px;background:var(--accent2);margin-left:3px;animation:blink 1s step-end infinite;vertical-align:middle;border-radius:1px;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}
.chat-footer{padding:16px;border-top:1px solid var(--border);flex-shrink:0;background:var(--ink2);}
.prompts-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.prompt-btn{background:linear-gradient(145deg,var(--surface) 0%,var(--surface2) 100%);border:1px solid var(--border2);border-radius:16px;padding:16px 14px;font-size:13px;color:var(--text);font-weight:500;cursor:pointer;transition:all .3s cubic-bezier(.16,1,.3,1);display:flex;flex-direction:column;align-items:flex-start;gap:8px;box-shadow:0 4px 12px rgba(0,0,0,.1);position:relative;overflow:hidden;text-align:left;}
.prompt-btn::before{content:'';position:absolute;top:0;left:0;width:4px;height:100%;background:var(--accent);transform:scaleY(0);transition:transform .3s;transform-origin:bottom;}
.prompt-btn:hover{transform:translateY(-4px);box-shadow:0 8px 20px rgba(124,106,247,.2);border-color:rgba(124,106,247,.4);background:var(--surface2);}
.prompt-btn:hover::before{transform:scaleY(1);}
.p-icon{font-size:22px;padding:8px;background:rgba(124,106,247,.1);border-radius:10px;line-height:1;margin-bottom:2px;border:1px solid rgba(124,106,247,.2);}
.p-lbl{font-family:'Syne',sans-serif;font-size:15px;letter-spacing:-.2px;font-weight:700;color:var(--text);}
.prompt-btn:disabled{opacity:.4;cursor:not-allowed;transform:none;box-shadow:none;}
.prompt-btn:disabled::before{display:none;}

/* NOISE */
.noise{position:fixed;inset:0;opacity:.025;pointer-events:none;z-index:100;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* SHARED */
.view-content{padding:60px 72px;min-height:100%;position:relative;}
.section-tag{display:inline-flex;align-items:center;gap:8px;font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);text-transform:uppercase;letter-spacing:2.5px;margin-bottom:20px;}
.section-tag::before{content:'◈';font-size:13px;}
.view-title{font-family:'Syne',sans-serif;font-size:46px;font-weight:800;letter-spacing:-1.5px;color:var(--text);margin-bottom:52px;line-height:1;}
.view-title span{color:var(--accent2);}
.subtle-div{height:1px;background:var(--border);margin:44px 0;}

/* WELCOME */
.welcome-eyebrow{display:flex;align-items:center;gap:10px;margin-bottom:28px;}
.status-dot{width:10px;height:10px;background:var(--green);border-radius:50%;box-shadow:0 0 10px var(--green);animation:pg 2s infinite;}
@keyframes pg{0%,100%{box-shadow:0 0 6px var(--green);}50%{box-shadow:0 0 20px var(--green);}}
.status-text{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--green);letter-spacing:1px;text-transform:uppercase;}
.welcome-name{font-family:'Syne',sans-serif;font-size:clamp(46px,5vw,80px);font-weight:800;line-height:.95;letter-spacing:-2.5px;margin-bottom:14px;}
.welcome-name .accent-word{color:var(--accent2);display:block;}
.welcome-role{font-size:18px;color:var(--text2);font-weight:300;margin-bottom:36px;font-style:italic;}
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
.kbd-hint-row{display:flex;align-items:center;gap:8px;margin-top:8px;flex-wrap:wrap;}
.kbd{font-family:'DM Mono',monospace;font-size:10px;padding:3px 8px;background:var(--surface);border:1px solid var(--border2);border-radius:5px;color:var(--text2);}

/* TIMELINE */
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

/* PROJECTS */
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
.cs-tag{font-family:'DM Mono',monospace;font-size:10px;padding:3px 10px;border-radius:20px;border:1px solid var(--border2);color:var(--text2);}
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
.lk-skill-ref{font-family:'DM Mono',monospace;font-size:11px;color:var(--text2);display:flex;align-items:center;gap:6px;line-height:1.4;}
.lk-skill-ref::before{content:'↳';color:var(--accent2);font-weight:bold;}
.cert-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:15px 18px;margin-bottom:10px;display:flex;align-items:center;gap:14px;transition:transform .2s,border-color .2s;position:relative;}
a.cert-card{cursor:pointer;color:inherit;text-decoration:none;}
a.cert-card:hover{transform:translateX(4px);border-color:var(--accent);box-shadow:0 6px 16px rgba(124,106,247,.15);}
a.cert-card:hover .cert-link-icon{opacity:1 !important;color:var(--accent2) !important;}
.skills-chart-wrap{background:var(--ink3);border-radius:16px;border:1px solid var(--border);padding:20px;margin-bottom:24px;}

/* EDUCATION */
.edu-hero{background:linear-gradient(135deg,var(--surface),var(--surface2));border:1px solid var(--border);border-radius:24px;padding:40px;margin-bottom:28px;position:relative;overflow:hidden;}
.edu-hero::before{content:'UEH';position:absolute;right:-15px;bottom:-45px;font-family:'Syne',sans-serif;font-size:180px;font-weight:800;color:rgba(255,255,255,.025);line-height:1;pointer-events:none;}
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
  .nav-item{width:44px;height:44px;}
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

<!-- LANG OVERLAY -->
<div id="lang-overlay">
  <div style="text-align:center;">
    <div class="lo-logo">hwinh</div>
    <div class="lo-tagline" style="margin-top:10px;">AI Portfolio · Product &amp; UX</div>
  </div>
  <div class="lo-question">Choose your language<br><span style="font-size:18px;color:var(--text2);font-weight:400;">Chọn ngôn ngữ hiển thị</span></div>
  <div class="lo-options">
    <button class="lo-btn" onclick="selectLang('en')">English</button>
    <button class="lo-btn" onclick="selectLang('vi')">Tiếng Việt</button>
  </div>
  <div class="lo-kbhint">Press <strong style="color:var(--text2)">1–6</strong> to navigate · <strong style="color:var(--text2)">Esc</strong> to return</div>
</div>

<!-- APP -->
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

    <!-- WELCOME -->
    <div id="view-welcome" class="view-content">
      <div class="welcome-eyebrow fade-up"><div class="status-dot"></div><span class="status-text" id="w-status">Available for Product &amp; UX opportunities · HCMC</span></div>
      <h1 class="welcome-name fade-up d1">Nguyễn<span class="accent-word">Hoàng Minh</span></h1>
      <p class="welcome-role fade-up d2" id="w-role">Product Owner · UX Strategist · AI Builder</p>
      <p class="welcome-summary fade-up d3" id="w-summary"></p>
      <div class="contact-row fade-up d4">
        <div class="contact-chip copyable" onclick="copyEmail()" title="Click to copy">✉ hwinh.work@gmail.com</div>
        <div class="contact-chip">📞 +84 765 828 191</div>
        <div class="contact-chip">📍 Hồ Chí Minh</div>
        <div class="contact-chip">🎓 UEH · GPA 3.53/4.0</div>
      </div>
      <div class="stat-grid fade-up d5">
        <div class="stat-card"><div class="stat-number">3+</div><div class="stat-label" id="ws1">Years Exp.</div></div>
        <div class="stat-card"><div class="stat-number">150+</div><div class="stat-label" id="ws2">Stakeholders</div></div>
        <div class="stat-card"><div class="stat-number">72%</div><div class="stat-label" id="ws3">AI Tech. KPI</div></div>
        <div class="stat-card"><div class="stat-number">Top 20</div><div class="stat-label" id="ws4">City Finalist</div></div>
      </div>
      <div class="subtle-div fade-up"></div>
      <div class="section-tag fade-up d6" id="w-explore">Explore this portfolio</div>
      <p class="fade-up d6" style="font-size:14px;color:var(--text2);line-height:1.8;max-width:500px;margin-top:8px;" id="w-hint"></p>
      <div class="kbd-hint-row fade-up d6" style="margin-top:20px;">
        <span id="kbd-nav-hint" style="font-size:12px;font-family:'DM Mono',monospace;color:var(--text3);">Quick navigate:</span>
        <span class="kbd">1</span><span class="kbd">2</span><span class="kbd">3</span><span class="kbd">4</span><span class="kbd">5</span><span class="kbd">6</span>
        <span id="kbd-nav-desc" style="color:var(--text3);font-size:11px;font-family:'DM Mono',monospace;margin-left:4px;">→ Home / Career / Work / UX / Skills / School</span>
      </div>
    </div>

    <!-- EXPERIENCE -->
    <div id="view-experience" class="view-content" style="display:none">
      <div class="section-tag" id="e-tag">Work History</div>
      <h2 class="view-title" id="e-title">Work <span>Experience</span></h2>
      <div class="timeline" id="e-timeline"></div>
    </div>

    <!-- PROJECTS -->
    <div id="view-projects" class="view-content" style="display:none">
      <div class="section-tag" id="p-tag">Product Experience</div>
      <h2 class="view-title" id="p-title">Featured <span>Projects</span></h2>
      <div class="projects-grid" id="p-grid"></div>
    </div>

    <!-- UX EXPERIENCE — NEW SECTION -->
    <div id="view-ux" class="view-content" style="display:none">
      <div class="section-tag" id="ux-tag">Design Process</div>
      <h2 class="view-title" id="ux-title">UX <span>Experience</span></h2>

      <!-- Design Thinking Framework Visual -->
      <div class="fade-up">
        <div class="proj-chart-title" id="ux-dt-title" style="margin-bottom:20px;">My Design Thinking Framework</div>
        <div class="dt-flow" id="ux-dt-flow"></div>
      </div>

      <!-- Case Studies -->
      <div id="ux-cases"></div>
    </div>

    <!-- SKILLS -->
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

    <!-- EDUCATION -->
    <div id="view-education" class="view-content" style="display:none">
      <div class="section-tag" id="ed-tag">Academic Background</div>
      <h2 class="view-title" id="ed-title">Education &amp; <span>Awards</span></h2>
      <div class="edu-hero">
        <div style="font-family:'DM Mono',monospace;font-size:11px;color:var(--accent2);letter-spacing:1px;margin-bottom:14px;">AUG 2022 — AUG 2026</div>
        <h3 style="font-family:'Syne',sans-serif;font-size:26px;font-weight:800;color:var(--text);margin-bottom:6px;" id="ed-uni">University of Economics HCMC (UEH)</h3>
        <p style="color:var(--text2);font-size:15px;margin-bottom:20px;" id="ed-major">Bachelor of Technology &amp; Innovation Management</p>
        <div class="gpa-badge"><span style="font-size:26px;">🏆</span><div><div style="font-size:11px;color:var(--text2);margin-bottom:3px;">Grade Point Average</div><div class="gpa-val">3.53 / 4.0</div></div></div>
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
// ================================================================
// DATA
// ================================================================
const T = {
en: {
  nav: ['Home','Career','Work','UX','Skills','School'],
  navTip: ['Overview','Experience','Projects','UX Work','Skills','Education'],
  kbdNavHint: 'Quick navigate:',
  kbdNavDesc: '→ Home / Career / Work / UX / Skills / School',
  w: {
    status: 'Available for Product & UX opportunities · HCMC, Vietnam',
    role: 'Product Owner · UX Strategist · AI Builder',
    summary: `Young professional in <strong style="color:var(--text)">Technology & Innovation Management</strong> — operating at the intersection of UX Design, Systems Thinking, and AI. I specialize in turning complex user data and behavioral pain points into seamless, measurable digital experiences. I believe the best products emerge when deep empathy meets rigorous execution.`,
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
          `<strong>End-to-End Customer Journey Mapping & MVP Delivery:</strong> Designed complete digital user journeys for tech startups. Instead of just creating flowcharts, I focused on identifying core user frustrations, translating them into structured User Stories, and driving rapid, iterative MVP development to reduce time-to-first-value.`,
          `<strong>Data-Driven Product Validation:</strong> Monitored omnichannel touchpoints to identify operational bottlenecks. I implemented A/B testing and Interleaving experiments to rigorously evaluate feature changes, ensuring that every product decision was backed by behavioral evidence rather than assumptions.`,
          `<strong>Stakeholder Management & NPS Analytics:</strong> Served as the primary liaison for 150+ startup founders. By analyzing behavioral data, I transformed NPS from a static metric into a real-time behavioral signal system, presenting actionable retention insights directly to the Board of Directors.`
        ],
        tags: ['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Stakeholder Mgmt (150+)','URD Documentation'] },
      { period: 'JUL 2024 — DEC 2024', role: 'Research & Development Intern',
        company: 'SIHUB · Executed data-driven project management for a city-level scientific competency framework',
        bullets: [
          `<strong>Large-Scale Data Analysis & Requirements Gathering:</strong> Directed the full data lifecycle for a city-level competency gap analysis. I successfully managed conflicting requirements from over 150 key stakeholders, extracting structured insights that shaped final policy recommendations.`,
          `<strong>URD-Standard Structured Documentation:</strong> Authored comprehensive strategic reports and system requirement documents aligned with URD standards. This experience refined my ability to bridge the gap between qualitative user feedback and concrete technical requirements.`
        ],
        tags: ['Data Lifecycle Management','Competency Gap Analysis','150+ Stakeholders','URD Standards','Requirements Engineering'] }
    ]
  },
  proj: {
    tag: 'Product Experience', title: 'Featured <span>Projects</span>',
    items: [
      { id: 'echomind', badge: '★ Flagship AI Project', bClass: 'badge-featured', date: 'Sep — Dec 2025',
        name: 'EchoMind AI', sub: 'Non-Invasive Brain-to-Text System · Project Lead · MindConnect Labs · UEH',
        desc: `EchoMind addresses a profound human challenge: empowering patients with locked-in syndrome to communicate. Traditional AAC devices are slow (25–30 WPM), laggy, and have low session success rates.\n\nAs <strong style="color:var(--text)">Project Lead</strong>, I managed the full AI lifecycle via <strong style="color:var(--text)">CPMAI 6-phase framework</strong> across 8 Agile Sprints. When our baseline LSTM suffered Mode Collapse, I pivoted to <strong style="color:var(--text)">Transformer V2</strong>. We applied Int8 Quantization for CPU inference, and built an Expert Dashboard with Attention Maps for Explainable AI.\n\nFinal results: <strong style="color:var(--text)">55–65 WPM, &lt;1s latency, 72% Technical KPI</strong> vs traditional AAC.`,
        info: [{l:'Final Architecture',v:'Transformer V2 · 8-head MHA · Positional Encoding · Label Smoothing ε=0.1'},{l:'Baseline vs Final',v:'Seq2Seq LSTM (Mode Collapse, WER ~85–90%) → Transformer V2 (6–7/10 correct)'},{l:'Dataset',v:'Brain-to-Text \'25 (Kaggle) · 256-ch EEG · HDF5 · 6.38 words/sentence'},{l:'PM Framework',v:'CPMAI 6-phase · 8 Sprints · RACI Matrix · 3,833.5 hrs · 100% milestones'}],
        metrics: [{v:'55–65',l:'WPM Output'},{v:'<1s',l:'Latency'},{v:'72%',l:'Technical KPI'},{v:'92–95%',l:'Accuracy'},{v:'6–7/10',l:'Sentences OK'},{v:'100%',l:'Milestone'}],
        tech: ['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','RACI Matrix','Agile/Scrum'] },
      { id: 'ereader', badge: '🏆 Top 20 Finalist', bClass: 'badge-top20', date: 'Mar — Jun 2025',
        name: 'E-Reader Ecosystem', sub: "User Researcher · HCMC Digital Education · HCMC People's Committee",
        desc: `A Top 20 City-level initiative to design a digital education ecosystem for student e-reading devices. Applied <strong style="color:var(--text)">HCI principles</strong> to map the complete user journey, decomposed pain points causing cognitive overload, and translated observations into actionable User Stories with clear success criteria.`,
        tech: ['HCI Principles','UX Design','Journey Mapping','Problem Decomposition','User Stories','Cognitive Load Analysis','Figma'] },
      { id: 'events', badge: '● Ongoing', bClass: 'badge-active', date: 'Jul 2024 — Present',
        name: 'Innovation Events Operations', sub: 'Operations · SIHUB Startup Ecosystem · HCMC',
        desc: `Managed end-to-end operations for <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> and <strong style="color:var(--text)">WHISE Week 2024</strong>. Coordinated cross-functional teams and facilitated real-time communication between startup founders, investors, and government representatives.`,
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
        cls: 'cs-sihub',
        num: 'Case Study 01',
        ctag: 'Customer Journey · Activation UX',
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
        abVariants: [
          { lbl: 'Control', pct: 42, cls: 'control', badge: '' },
          { lbl: 'Variant A', pct: 68, cls: 'winner', badge: '✓ Winner' }
        ],
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
        cls: 'cs-echomind',
        num: 'Case Study 02',
        ctag: 'AI Product UX · Expert Dashboard Design',
        title: 'EchoMind: Designing the Output Interface',
        role: 'Project Lead · UI/UX Thinker · Gradio Demo Designer',
        impactNum: '100%', impactLbl: 'Milestones Done',
        problemLabel: 'Context & Challenge',
        problem: `EchoMind is a university AI project built on the <strong>Brain-to-Text 2025 dataset (Kaggle)</strong> — we trained a model to decode non-invasive EEG signals into text. Once the model was working, we faced a UX question: <strong>how do we show the output in a way that actually makes sense to someone reviewing it?</strong> A raw text output with no context tells you nothing — you can't tell if the model was confident, which part of the brain it read, or whether the signal was clean.`,
        approachTitle: 'How We Thought About It',
        steps: [
          { n:'01', t:'Start with the demo interface', d:'We built the first version in Gradio — just the model output as plain text plus a confidence score. When we reviewed it ourselves, we realised it felt like a black box. If we couldn't trust it, nobody else would.' },
          { n:'02', t:'Apply HCI heuristics to the prototype', d:'I ran Nielsen's 10 Usability Heuristics against our V1 Gradio demo. Found two real problems: the interface gave no indication it was processing, and there was no way to flag when the signal quality was low.' },
          { n:'03', t:'Think through what an expert would need', d:'If this model were used by a clinician in future, what would they actually need to see? We mapped out the questions: What did the model decode? How sure is it? Which brain region did it focus on? That framing drove the V2 design.' },
          { n:'04', t:'Design the Attention Map layer', d:'The most meaningful addition was showing WHICH part of the EEG waveform the model paid attention to for each decoded word — visualised as a colour overlay. This turns a black box into something you can reason about.' }
        ],
        insightLabel: 'Key Realisation',
        insight: `The model result alone means almost nothing without context. <strong>A 93% accuracy number tells you it works — the attention map shows you WHY it works.</strong> Designing for explainability from the start, even in a prototype, forces you to think about the output from the user's perspective, not just the engineer's.`,
        abTitle: 'Interface Comparison — Team Heuristic Review',
        abVariants: [
          { lbl: 'V1 — Plain output', pct: 38, cls: 'control', badge: '' },
          { lbl: 'V2 — With Attention Map', pct: 82, cls: 'winner', badge: '✓ Final version' }
        ],
        abStat: 'Scored using Nielsen's 10 Heuristics by 4 team members · Scale 0–100 · Not a clinical study',
        journeyTitle: 'Thinking Through the User Flow',
        journeyStages: ['See output','Check confidence','Understand why','Review signal','Draw conclusion'],
        journeyRows: [
          { label: 'What user wants', cells: ['What was decoded?','Is it reliable?','How did it decide?','Was signal clean?','Can I trust this?'], types: ['','','','',''] },
          { label: 'V1 gap', cells: ['Text only','% with no context','❌ Nothing shown','Raw chart','Unclear'], types: ['','','pain high','pain','pain'] },
          { label: 'V2 added', cells: ['Text + waveform','% + signal quality','✅ Attention overlay','Highlighted region','Much clearer'], types: ['solution','solution','solution','solution','solution'] },
          { label: 'Clarity', cells: ['😐','😐','😊','😊','😊'], types: ['emotion-mid','emotion-mid','emotion-high','emotion-high','emotion-high'] }
        ],
        beforeAfterTitle: 'V1 vs V2 — What Changed',
        before: [{ n: 'Heuristic Score', v: '38/100' },{ n: 'Shows reasoning', v: '❌ No' },{ n: 'Signal quality info', v: '❌ None' },{ n: 'Error feedback', v: 'None' }],
        after: [{ n: 'Heuristic Score', v: '82/100' },{ n: 'Shows reasoning', v: '✓ Attention map' },{ n: 'Signal quality info', v: '✓ Visible' },{ n: 'Error feedback', v: 'Shown clearly' }],
        learnings: [
          { icon: '🔭', title: 'Design the output, not just the model', text: 'Even for a research project, how you present the result matters. A well-designed output is what makes the model feel trustworthy, not just accurate.' },
          { icon: '🧩', title: 'Heuristics work on prototypes too', text: 'Running a quick heuristic review on our own Gradio demo caught problems we had completely normalised. Takes 30 minutes, saves a lot of confusion.' },
          { icon: '🗺️', title: 'Think about the user, even when there isn't one yet', text: 'This was a student project — no real users. But thinking through "who would use this and what would they need" shaped better design decisions throughout.' }
        ]
      },
      {
        cls: 'cs-ereader',
        num: 'Case Study 03',
        ctag: 'HCI · Cognitive Load · Education UX',
        title: 'E-Reader Ecosystem — Activation Flow',
        role: 'User Researcher · HCI Analyst · UX Designer',
        impactNum: 'Top 20', impactLbl: 'City Competition',
        problemLabel: 'Problem Statement',
        problem: `Students receiving e-reading devices for the HCMC digital education initiative were <strong>abandoning the setup process before first use</strong>. The device provisioning journey involved 7 steps with multiple form fields, account registrations, and content sync — creating a severe cognitive overload that caused drop-offs at step 2–3. The result: expensive devices sitting unused in school bags.`,
        approachTitle: 'How I Approached It',
        steps: [
          { n:'01', t:'Cognitive Load Audit', d:'Measured the number of decisions per step in the existing 7-step setup flow. Steps 2 and 3 had 5+ concurrent decisions — well above the 3–4 item working memory limit (Miller\'s Law).' },
          { n:'02', t:'HCI Principles Application', d:'Applied Fitts\'s Law (target size for touch interactions), Hick\'s Law (reduce choices per step), and proximity grouping (Gestalt) to redesign each stage.' },
          { n:'03', t:'Journey Map — Student Persona', d:'Built a complete journey map for a Grade 6 student: from "unboxing" → "first digital reading session." Mapped emotions, barriers, expectations, and support needs at each step.' },
          { n:'04', t:'Flow Redesign — 7 → 3 Steps', d:'Chunked the 7-step flow into 3 progressive phases: Device Activation → Content Setup → Personalization. Deferred non-critical steps to post-first-use.' }
        ],
        insightLabel: 'Key Insight',
        insight: `Students weren't failing because they lacked tech skills — they were failing because the system <strong>violated the "one primary action per screen" principle</strong>. Step 2 asked for school code, parent phone, grade level, and preferred language all at once. Splitting this into sequential micro-steps reduced perceived complexity by ~60%.`,
        abTitle: 'Flow Comparison — Completion Rate',
        abVariants: [
          { lbl: 'Original 7-step', pct: 35, cls: 'control', badge: '' },
          { lbl: 'Redesigned 3-phase', pct: 78, cls: 'winner', badge: '✓ Adopted' }
        ],
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
      {n:'Customer Journey Mapping',ref:'Validated by: Design Thinking (UEH)',m:['Mapped 15+ complex user flows for startups','Reduced onboarding friction points by 30%','Optimized 5+ critical conversion touchpoints']},
      {n:'UX / HCI Design',ref:'Validated by: Human-Computer Interaction (UEH)',m:['Applied to 3 major practical projects','Minimized cognitive load for E-Reader users','Designed Heuristic-standard Gradio UI']},
      {n:'Agile / Scrum (CPMAI)',ref:'Validated by: Google PM Cert & EchoMind Project',m:['Managed 8 continuous Sprints','Led a cross-functional team of 7','Achieved 100% project milestones on time']},
      {n:'A/B Testing & Interleaving',ref:'Validated by: SIHUB Product Experiments',m:['Designed & ran 10+ feature experiments','Validated hypotheses with 95% significance','Prevented 3 major UX flaws before rollout']},
      {n:'Problem Decomposition',ref:'Validated by: Innovation Management (UEH)',m:['Broke down 5+ high-level Epics','Diagnosed LSTM Mode Collapse root cause','Structured 150+ stakeholder requirements']},
      {n:'PRD & User Stories Writing',ref:'Validated by: Entrepreneurship Innovation (UEH)',m:['Authored 10+ standardized PRDs','Maintained backlog of 200+ User Stories','Met city-level URD documentation standards']},
      {n:'Python & PyTorch (Familiar)',ref:'Applied in: EchoMind AI Project',m:['Optimized Transformer V2 architecture','Applied Int8 Quantization to reduce size','Decreased model inference latency to <1s']}
    ],
    radarLabels: ['UX/HCI','Agile','Journey Map','Data Analysis','Python','PyTorch/ML','A/B Testing'],
    certs: [
      {i:'🏅',n:'Google Project Management',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Google Business Intelligence',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Agile Management Certification',org:'Professional Certification',dash:false},
      {i:'🗣️',n:'TOEIC — English Proficiency',org:'Preparing for certification exam',dash:true,prog:'In Progress'}
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
      {i:'🔄',n:'Agile Management Certification',org:'Professional Certification',dash:false},
      {i:'🗣️',n:'TOEIC — English Proficiency',org:'Preparing for certification exam',dash:true,prog:'In Progress'}
    ]
  },
  chat: {
    name: "Minh's AI Assistant", sub: '● Online · Ready to answer', reset: '↺ Reset', logout: '⏻ Lang',
    greeting: `Hey there! I'm an AI assistant here to tell you about Nguyen Hoang Minh — he's a final-year student at UEH who's been doing real product and UX work at SIHUB, one of Ho Chi Minh City's main startup hubs, for the past couple of years.\n\nHe's the kind of person who doesn't just map user journeys on paper — he actually runs A/B tests, tracks NPS stage by stage, and led a 7-person AI project from scratch. What do you want to know about him?`,
    prompts: [
      {id:'exp',i:'💼',l:'Experience'},{id:'proj',i:'🧠',l:'Projects'},
      {id:'ux',i:'🎨',l:'UX Work'},{id:'skills',i:'⚡',l:'Skills'}
    ],
    ans: {
      exp: `Minh has been at SIHUB — that's the Startup & Innovation Hub under the HCMC Department of Science & Technology — since mid-2024.\n\nIn his most recent role as Project Management Executive (Jan–Oct 2025), he was the main point of contact for 150+ startup founders going through the incubation program. He designed their onboarding journeys end-to-end and ran A/B tests to validate every change. One of the things he's proud of: he helped the team stop treating NPS as just a number and start treating it as a signal — something that tells you exactly where in the journey things are going wrong.\n\nBefore that, as an R&D Intern, he handled a large-scale competency gap analysis — gathering data from government officials, research institutes, and companies — and turned all that qualitative mess into structured URD documentation.`,
      proj: `Sure! Minh has three projects worth knowing about:\n\n🧠 EchoMind AI — his flagship project (Sep–Dec 2025). This was a university AI project where his team trained a model to decode brainwave signals into text, using the Brain-to-Text 2025 dataset from Kaggle. Minh was the Project Lead — he ran 8 Agile sprints, and when their first model (an LSTM) kept breaking down, he diagnosed the problem and made the call to switch to a Transformer architecture. The model ended up hitting 55–65 words per minute with under 1 second of latency. He also designed the output interface so people could actually understand what the model was doing.\n\n📚 E-Reader Ecosystem — a city-level project (Mar–Jun 2025) where he did user research for a student e-reading platform. He mapped the setup journey, found where students were dropping off, and used HCI principles to simplify it. The project made it to the Top 20 at an HCMC People's Committee competition.\n\n🚀 Innovation Events — ongoing work organizing major startup events like Univ.Star 2024/2025 and WHISE Week 2024 at SIHUB.`,
      ux: `The UX section has three case studies that show how Minh thinks through design problems — not just the output, but the whole process.\n\n🗺️ Case 01 is about the SIHUB onboarding flow. Only 42% of startup founders were completing the activation journey. He dug into the data, ran a journey mapping workshop, found the real drop-off point (it was a document upload step with unclear requirements), and tested a fix via A/B experiment. Result: 68% activation, NPS jumped from 28 to 47, support tickets dropped by about 70%.\n\n🧠 Case 02 is the EchoMind dashboard — how do you show AI output in a way that actually makes sense? His team built a demo in Gradio and it felt like a black box. He used Nielsen's heuristics to audit it, then added an attention map layer so you could see which part of the brainwave the model was reading. Heuristic score went from 38 to 82 out of 100.\n\n📱 Case 03 is the E-Reader setup flow. Students were abandoning the 7-step setup process at step 2 or 3 — way too many things to fill in at once. He applied Miller's Law to chunk it down to 3 phases. Setup completion went from 35% to 78%, and first-read time dropped from 22 minutes to 8.`,
      skills: `Minh's strongest area is product and UX work — we're talking journey mapping, running A/B tests, writing PRDs, breaking down complex problems into things a team can actually build. He's also comfortable with Agile and the CPMAI framework, which he ran across 8 sprints on the EchoMind project.\n\nOn the technical side, he knows Python and has hands-on experience with PyTorch and data analysis — not at an engineer level, but enough to work closely with AI teams and understand what's happening under the hood.\n\nAnd in terms of working with people — he's managed 150+ startup founders as the main point of contact at a city government-backed hub, and presented strategic insights directly to the Board. That's not a small thing.`
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
          `<strong>Thiết kế Hành trình Số & Triển khai MVP:</strong> Thiết kế hành trình người dùng end-to-end cho startup. Xác định vấn đề cốt lõi, chuyển thành User Stories, thúc đẩy MVP nhanh để rút ngắn time-to-first-value.`,
          `<strong>Giải quyết Pain Point dựa trên Dữ liệu:</strong> Theo dõi touchpoints đa kênh, triển khai A/B testing và Interleaving đảm bảo mọi thay đổi được chứng minh bởi dữ liệu hành vi thực tế.`,
          `<strong>Quản lý Stakeholder & NPS:</strong> Làm đầu mối với 150+ startup founders. Chuyển NPS thành hệ thống tín hiệu hành vi real-time báo cáo lên Ban Giám đốc.`
        ],
        tags: ['Customer Journey Mapping','A/B Testing','Interleaving','MVP Delivery','NPS Analytics','Quản lý 150+ Stakeholders','Tài liệu URD'] },
      { period: '07/2024 — 12/2024', role: 'Thực tập sinh R&D',
        company: 'SIHUB · Quản lý dự án dựa trên dữ liệu cho khung năng lực cấp thành phố',
        bullets: [
          `<strong>Phân tích Dữ liệu & Lấy Yêu cầu:</strong> Dẫn dắt end-to-end data lifecycle cho dự án phân tích khoảng trống năng lực, phối hợp 150+ stakeholders, trích xuất insights định hình chính sách.`,
          `<strong>Tài liệu hóa Chuẩn URD:</strong> Soạn thảo báo cáo chiến lược và tài liệu yêu cầu hệ thống, kết nối phản hồi định tính với yêu cầu kỹ thuật cụ thể.`
        ],
        tags: ['Phân tích Dữ liệu','Khoảng trống Năng lực','150+ Stakeholders','Chuẩn URD','Kỹ thuật Yêu cầu'] }
    ]
  },
  proj: {
    tag: 'Kinh nghiệm Sản phẩm', title: 'Dự án <span>Nổi bật</span>',
    items: [
      { id: 'echomind', badge: '★ Dự án AI Trọng điểm', bClass: 'badge-featured', date: 'Tháng 9 — 12/2025',
        name: 'EchoMind AI', sub: 'Hệ thống Não-Chữ Phi Xâm Lấn · Project Lead · MindConnect Labs · UEH',
        desc: `Khởi nguồn từ bài toán nhân văn: giúp bệnh nhân hội chứng khóa trong giao tiếp qua sóng não. Thiết bị AAC truyền thống chậm (25–30 WPM), độ trễ cao.\n\nVới vai trò <strong style="color:var(--text)">Project Lead</strong>, tôi quản lý theo <strong style="color:var(--text)">khung CPMAI 6 pha</strong> và 8 Agile Sprints. Khi LSTM gặp Mode Collapse, tôi pivot sang <strong style="color:var(--text)">Transformer V2</strong>. Áp dụng Int8 Quantization, thiết kế Expert Dashboard với Attention Maps cho Explainable AI y tế.\n\nKết quả: <strong style="color:var(--text)">55–65 WPM, &lt;1s, KPI kỹ thuật 72%</strong>.`,
        info: [{l:'Kiến trúc cuối',v:'Transformer V2 · 8-head MHA · Positional Encoding · Label Smoothing ε=0.1'},{l:'Baseline vs Cuối',v:'Seq2Seq LSTM (Mode Collapse) → Transformer V2 (6–7/10 đúng)'},{l:'Bộ dữ liệu',v:'Brain-to-Text \'25 (Kaggle) · EEG 256 kênh · HDF5 · 6,38 từ/câu'},{l:'Khung quản lý',v:'CPMAI 6 pha · 8 Sprints · RACI · 3.833,5 giờ · 100% milestones'}],
        metrics: [{v:'55–65',l:'Từ/phút'},{v:'<1s',l:'Độ trễ'},{v:'72%',l:'KPI kỹ thuật'},{v:'92–95%',l:'Độ chính xác'},{v:'6–7/10',l:'Câu đúng'},{v:'100%',l:'Milestone'}],
        tech: ['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','Ma trận RACI','Agile/Scrum'] },
      { id: 'ereader', badge: '🏆 Top 20 Chung cuộc', bClass: 'badge-top20', date: 'Tháng 3 — 6/2025',
        name: 'Hệ sinh thái E-Reader', sub: "User Researcher · Giáo dục Số TP.HCM · UBND TP.HCM",
        desc: `Dự án hệ sinh thái giáo dục số. Áp dụng <strong style="color:var(--text)">nguyên lý HCI</strong> lập bản đồ hành trình đầy đủ, phân tích cognitive overload, chuyển thành User Stories có tiêu chí đo lường. Lọt <strong style="color:var(--text)">Top 20 Chung cuộc</strong> cuộc thi UBND TP.HCM.`,
        tech: ['Nguyên tắc HCI','Thiết kế UX','Journey Mapping','Phân tích Pain Point','User Stories','Phân tích Cognitive Load','Figma'] },
      { id: 'events', badge: '● Đang diễn ra', bClass: 'badge-active', date: 'Tháng 7/2024 — Hiện tại',
        name: 'Vận hành Sự kiện ĐMST', sub: 'Vận hành · Hệ sinh thái Startup SIHUB · TP.HCM',
        desc: `Tổ chức và điều phối <strong style="color:var(--text)">Univ.Star 2024 & 2025</strong> và <strong style="color:var(--text)">Tuần lễ WHISE 2024</strong>. Phối hợp cross-team, giao tiếp liên tục với founders, nhà đầu tư và chính quyền.`,
        tech: ['Quản lý Sự kiện','Phối hợp Cross-team','Giao tiếp Stakeholder','Lập kế hoạch Vận hành'] }
    ]
  },
  ux: {
    tag: 'Quy trình Thiết kế', title: 'Kinh nghiệm <span>UX</span>',
    dtTitle: 'Khung Tư duy Thiết kế của Tôi',
    phases: [
      { icon: '🔍', num: '01', name: 'Thấu Cảm', desc: 'Tìm hiểu người dùng qua phỏng vấn, quan sát hành vi và dữ liệu thực tế — để khám phá những gì họ thực sự đang gặp khó, không chỉ những gì họ nói ra.' },
      { icon: '🎯', num: '02', name: 'Định Nghĩa', desc: 'Đặt lại vấn đề theo góc nhìn người dùng. Dùng câu hỏi "How Might We" để chuyển từ vấn đề sang hướng giải quyết, và tìm nguyên nhân gốc rễ thay vì chữa triệu chứng.' },
      { icon: '💡', num: '03', name: 'Lên Ý tưởng', desc: 'Brainstorm không giới hạn, sau đó lọc qua user story mapping và khung MoSCoW để chọn giải pháp đáng thử nghiệm nhất.' },
      { icon: '📐', num: '04', name: 'Tạo Nguyên mẫu', desc: 'Hiện thực hóa ý tưởng thành wireframes, luồng low-fi và journey maps — đủ cụ thể để kiểm thử, đủ linh hoạt để thay đổi.' },
      { icon: '🧪', num: '05', name: 'Kiểm Thử', desc: 'Dùng A/B testing, Interleaving và đánh giá heuristic để kiểm chứng giả thuyết. Mọi thay đổi phải có dữ liệu, không phải cảm tính.' },
      { icon: '📈', num: '06', name: 'Đo Tác Động', desc: 'Theo dõi NPS theo từng bước hành trình, tỷ lệ chuyển đổi và chỉ số giữ chân — để biết giải pháp có tạo ra thay đổi thực sự hay không.' }
    ],
    cases: [
      {
        cls: 'cs-sihub', num: 'Case Study 01', ctag: 'Customer Journey · Activation UX',
        title: 'SIHUB: Tái thiết kế Onboarding Startup',
        role: 'Project Management Executive · Journey Mapping Lead',
        impactNum: '30%', impactLbl: 'Giảm Friction',
        problemLabel: 'Vấn đề Đặt ra',
        problem: `Trong giai đoạn đầu của chương trình ươm tạo SIHUB, nhiều startup bỏ cuộc ngay từ bước kích hoạt tài khoản. <strong>Chỉ khoảng 40% hoàn tất được luồng onboarding</strong> — kéo theo tỷ lệ tham gia thấp, người dùng không hài lòng và điểm NPS sụt giảm. Vấn đề là đội ngũ lúc đó chỉ nhìn vào một con số NPS chung chung, chứ không biết cụ thể chỗ nào trong hành trình đang làm người dùng bỏ cuộc.`,
        approachTitle: 'Cách Tiếp Cận',
        steps: [
          { n:'01', t:'Audit dữ liệu hành vi', d:'Tôi bắt đầu bằng cách thu thập dữ liệu từ nhiều kênh khác nhau để lập lại hành trình thực tế của người dùng. Kết quả cho thấy có 3 điểm thoát chính, tập trung ở bước upload tài liệu và xác minh thông tin.' },
          { n:'02', t:'Workshop Journey Mapping', d:'Sau khi có dữ liệu định lượng, tôi tổ chức workshop cùng nhân viên SIHUB và phỏng vấn trực tiếp 5 founder. Mục tiêu là ghi lại cảm xúc, kỳ vọng và điểm đau cụ thể ở từng bước trong hành trình.' },
          { n:'03', t:'Phân tích nguyên nhân gốc', d:'Áp dụng phương pháp 5 Whys để đào sâu. Câu trả lời không phải là form quá phức tạp — mà là yêu cầu tài liệu không được giải thích rõ, khiến người dùng thử một lần, bị từ chối, rồi không quay lại nữa.' },
          { n:'04', t:'Thiết kế thử nghiệm A/B', d:'Tôi thiết kế Variant A bổ sung hướng dẫn inline ngay tại chỗ cần nhập liệu (progressive disclosure) và so sánh với Control là form gốc. Dùng Interleaving để đảm bảo so sánh công bằng giữa hai nhóm.' }
        ],
        insightLabel: 'Insight Cốt Lõi',
        insight: `Vấn đề không nằm ở công nghệ. <strong>Điểm nghẽn nằm đúng ở bước 3 — yêu cầu định dạng tài liệu</strong>. Founder không biết cần nộp file gì, thử một lần bị hệ thống từ chối, rồi bỏ luôn và không quay lại. Chỉ cần thêm một dòng hướng dẫn ngay tại chỗ là đã xử lý được 60% tỷ lệ rời bỏ — mà không cần redesign gì thêm.`,
        abTitle: 'Kết quả Thử nghiệm A/B',
        abVariants: [
          { lbl: 'Control', pct: 42, cls: 'control', badge: '' },
          { lbl: 'Variant A', pct: 68, cls: 'winner', badge: '✓ Chiến thắng' }
        ],
        abStat: 'Độ tin cậy: 95% · Mẫu: 312 startup founders · Thời gian: 6 tuần',
        journeyTitle: 'Journey Map — Các Giai đoạn Quan trọng',
        journeyStages: ['Nhận lời mời','Đăng ký Portal','Upload Tài liệu','Xác minh','Kích hoạt'],
        journeyRows: [
          { label: 'Kỳ vọng', cells: ['Quy trình nhanh','Form đơn giản','Checklist rõ ràng','Auto-review','Truy cập ngay'], types: ['','','','',''] },
          { label: 'Pain Point', cells: ['Email dài','UI khó hiểu','❌ Format không rõ','Chờ 3 ngày','Lỗi đăng nhập'], types: ['','','pain high','pain','pain'] },
          { label: 'Cảm xúc', cells: ['😐','🙂','😤','😴','😟'], types: ['emotion-mid','emotion-high','emotion-low','emotion-mid','emotion-low'] },
          { label: 'Giải pháp', cells: ['—','Nav đơn giản hóa','✅ Hướng dẫn inline','Thanh tiến trình','SSO đăng nhập'], types: ['','','solution','solution','solution'] }
        ],
        beforeAfterTitle: 'Tác động Kinh doanh — Trước vs Sau',
        before: [{ n: 'Tỷ lệ Kích hoạt', v: '42%' },{ n: 'Điểm Thoát TB', v: 'Bước 3' },{ n: 'Điểm NPS', v: '28' },{ n: 'Support Tickets', v: '~40/tuần' }],
        after: [{ n: 'Tỷ lệ Kích hoạt', v: '68%' },{ n: 'Điểm Thoát TB', v: 'Bước 5' },{ n: 'Điểm NPS', v: '47' },{ n: 'Support Tickets', v: '~12/tuần' }],
        learnings: [
          { icon: '🔬', title: 'Research trước', text: 'Dữ liệu hành vi chỉ ra điểm thoát thực sự là bước 3 — trong khi các bên liên quan đều đoán là bước 1 hoặc 2. Đây là lý do phải đi từ dữ liệu, không phải từ giả định.' },
          { icon: '⚗️', title: 'Kiểm thử trước khi triển khai', text: 'Nhờ A/B testing, tôi không phải làm lại toàn bộ giao diện. Một thay đổi nhỏ về hướng dẫn inline tạo ra tác động lớn hơn nhiều so với redesign tổng thể.' },
          { icon: '📊', title: 'NPS không phải một con số', text: 'Mỗi bước trong hành trình có điểm đau riêng và NPS driver riêng. Đọc NPS theo từng giai đoạn mới thấy được gốc vấn đề — đọc tổng thì chỉ thấy kết quả.' }
        ]
      },
      {
        cls: 'cs-echomind', num: 'Case Study 02', ctag: 'AI Project UX · Thiết kế Giao diện Đầu ra',
        title: 'EchoMind: Thiết kế Giao diện Hiển thị Kết quả AI',
        role: 'Project Lead · Người thiết kế giao diện Gradio Demo',
        impactNum: '100%', impactLbl: 'Milestone Hoàn thành',
        problemLabel: 'Bối cảnh & Vấn đề',
        problem: `EchoMind là dự án AI của nhóm sinh viên, được xây dựng trên <strong>bộ dữ liệu Brain-to-Text 2025 (Kaggle)</strong> — nhóm huấn luyện mô hình để giải mã tín hiệu sóng não EEG phi xâm lấn thành văn bản. Khi mô hình đã chạy được, câu hỏi tiếp theo xuất hiện: <strong>hiển thị kết quả như thế nào để người xem thực sự hiểu được?</strong> Chỉ in ra một dòng văn bản với một con số phần trăm không đủ — bạn không biết mô hình có chắc không, nó đọc vùng não nào, hay tín hiệu đầu vào có sạch không.`,
        approachTitle: 'Nhóm Tiếp Cận Thế Nào',
        steps: [
          { n:'01', t:'Xây bản demo V1 bằng Gradio', d:'Phiên bản đầu tiên chỉ hiển thị văn bản giải mã và một con số độ tin cậy. Khi cả nhóm tự ngồi dùng thử, ai cũng cảm thấy nó như một hộp đen — không hiểu mô hình đang làm gì bên trong.' },
          { n:'02', t:'Đánh giá bằng 10 Heuristics của Nielsen', d:'Tôi chạy đánh giá heuristic trên chính prototype V1 của nhóm. Phát hiện được hai vấn đề: giao diện không cho biết hệ thống đang xử lý, và không có cách nào phát hiện khi chất lượng tín hiệu đầu vào kém.' },
          { n:'03', t:'Đặt câu hỏi: người dùng cần biết gì?', d:'Nếu công cụ này được dùng trong thực tế, người review kết quả cần trả lời được: mô hình giải mã ra cái gì, nó tự tin tới đâu, và nó dựa vào phần nào của tín hiệu EEG. Ba câu hỏi đó định hướng thiết kế V2.' },
          { n:'04', t:'Thiết kế lớp Attention Map', d:'Thay đổi có ý nghĩa nhất là thêm lớp highlight trực tiếp lên dạng sóng EEG — cho thấy phần nào của tín hiệu mà mô hình chú ý khi giải mã từng từ. Cái này biến hộp đen thành thứ có thể quan sát và lý giải được.' }
        ],
        insightLabel: 'Điều Nhóm Nhận Ra',
        insight: `Kết quả mô hình đứng một mình thì ít có giá trị. <strong>Con số 93% accuracy cho biết nó hoạt động được — attention map cho thấy vì sao nó hoạt động.</strong> Dù đây chỉ là dự án sinh viên, việc nghĩ đến cách trình bày đầu ra từ góc độ người xem — thay vì chỉ từ góc độ kỹ thuật — làm cho cả sản phẩm thuyết phục hơn hẳn.`,
        abTitle: 'So sánh V1 vs V2 — Đánh giá của nhóm',
        abVariants: [
          { lbl: 'V1 — Chỉ text + %', pct: 38, cls: 'control', badge: '' },
          { lbl: 'V2 — Có Attention Map', pct: 82, cls: 'winner', badge: '✓ Phiên bản cuối' }
        ],
        abStat: 'Đánh giá theo 10 Heuristics Nielsen · 4 thành viên nhóm cho điểm · Thang 0–100 · Không phải nghiên cứu lâm sàng',
        journeyTitle: 'Luồng suy nghĩ khi thiết kế giao diện',
        journeyStages: ['Xem kết quả','Kiểm tra độ tin cậy','Hiểu lý do','Đọc tín hiệu','Kết luận'],
        journeyRows: [
          { label: 'Người dùng cần', cells: ['Mô hình đọc được gì?','Có chắc không?','Dựa vào đâu?','Tín hiệu sạch không?','Có tin được không?'], types: ['','','','',''] },
          { label: 'V1 thiếu', cells: ['Chỉ có text','% không ngữ cảnh','❌ Không hiển thị','Biểu đồ thô','Không rõ'], types: ['','','pain high','pain','pain'] },
          { label: 'V2 bổ sung', cells: ['Text + waveform preview','% + chất lượng tín hiệu','✅ Attention overlay','Vùng được highlight','Rõ hơn nhiều'], types: ['solution','solution','solution','solution','solution'] },
          { label: 'Mức độ rõ ràng', cells: ['😐','😐','😊','😊','😊'], types: ['emotion-mid','emotion-mid','emotion-high','emotion-high','emotion-high'] }
        ],
        beforeAfterTitle: 'V1 vs V2 — Điều thay đổi',
        before: [{ n: 'Điểm Heuristic', v: '38/100' },{ n: 'Giải thích được', v: '❌ Không' },{ n: 'Thông tin tín hiệu', v: '❌ Không có' },{ n: 'Phản hồi lỗi', v: 'Không có' }],
        after: [{ n: 'Điểm Heuristic', v: '82/100' },{ n: 'Giải thích được', v: '✓ Attention map' },{ n: 'Thông tin tín hiệu', v: '✓ Hiển thị rõ' },{ n: 'Phản hồi lỗi', v: 'Có thông báo' }],
        learnings: [
          { icon: '🔭', title: 'Thiết kế đầu ra, không chỉ mô hình', text: 'Ngay cả trong dự án nghiên cứu, cách bạn trình bày kết quả quan trọng không kém việc kết quả đó có chính xác không. Giao diện tốt là thứ làm cho mô hình cảm thấy đáng tin, không chỉ là con số accuracy.' },
          { icon: '🧩', title: 'Heuristics hiệu quả ngay cả trên prototype', text: 'Chạy đánh giá heuristic trên chính demo của nhóm mất chừng 30 phút nhưng giúp phát hiện những vấn đề mà cả nhóm đã quen mắt và không còn nhận ra nữa.' },
          { icon: '🗺️', title: 'Nghĩ về người dùng, dù chưa có người dùng thật', text: 'Đây là dự án sinh viên, không có người dùng thực tế. Nhưng việc đặt câu hỏi "ai sẽ dùng và họ cần gì" giúp đưa ra những quyết định thiết kế tốt hơn ngay từ đầu.' }
        ]
      },
      {
        cls: 'cs-ereader', num: 'Case Study 03', ctag: 'HCI · Cognitive Load · Education UX',
        title: 'E-Reader: Tái thiết kế Luồng Kích hoạt',
        role: 'User Researcher · HCI Analyst · UX Designer',
        impactNum: 'Top 20', impactLbl: 'Cuộc thi Cấp TP',
        problemLabel: 'Vấn đề Đặt ra',
        problem: `Học sinh nhận thiết bị về nhà nhưng phần lớn <strong>bỏ cuộc ngay ở khâu cài đặt, trước khi dùng lần đầu</strong>. Luồng setup ban đầu có 7 bước với nhiều trường thông tin, đăng ký tài khoản và đồng bộ nội dung — gây quá tải nhận thức nghiêm trọng ở bước 2 và 3. Hậu quả thực tế rất rõ: thiết bị vài triệu đồng nằm im trong cặp sách, không được dùng lần nào.`,
        approachTitle: 'Cách Tiếp Cận',
        steps: [
          { n:'01', t:'Đo tải nhận thức từng bước', d:"Tôi đếm số quyết định mà người dùng cần đưa ra ở từng bước trong luồng 7-bước. Kết quả: bước 2 và 3 yêu cầu xử lý hơn 5 thông tin cùng lúc — vượt quá giới hạn bộ nhớ làm việc 3–4 mục của não người theo Định luật Miller." },
          { n:'02', t:'Áp dụng nguyên lý HCI', d:"Tôi sử dụng Định luật Fitts để tối ưu kích thước vùng chạm, Định luật Hick để giảm số lựa chọn trên mỗi màn hình, và nguyên tắc gần kề của Gestalt để nhóm thông tin liên quan lại với nhau." },
          { n:'03', t:'Journey map học sinh lớp 6', d:"Tôi xây dựng journey map theo góc nhìn của một học sinh lớp 6: từ lúc mở hộp cho đến buổi đọc sách kỹ thuật số đầu tiên. Ghi lại cảm xúc, rào cản, kỳ vọng và nhu cầu hỗ trợ ở từng bước." },
          { n:'04', t:'Tái thiết kế từ 7 bước xuống 3 giai đoạn', d:"Tôi dồn 7 bước lại thành 3 giai đoạn: Kích hoạt thiết bị → Cài đặt nội dung → Cá nhân hóa. Những bước không cần thiết ở lần đầu dùng được chuyển sang sau — khi học sinh đã quen với thiết bị." }
        ],
        insightLabel: 'Insight Cốt Lõi',
        insight: `Học sinh bỏ cuộc không phải vì thiếu kỹ năng công nghệ. Luồng cũ yêu cầu nhập mã trường, số điện thoại phụ huynh, lớp học và ngôn ngữ trên <strong>cùng một màn hình</strong> — vi phạm thẳng nguyên tắc "một hành động chính mỗi màn hình". Chỉ cần tách ra thành các bước nhỏ tuần tự là độ phức tạp nhận thức giảm ngay khoảng 60%.`,
        abTitle: 'So sánh Luồng — Tỷ lệ Hoàn thành',
        abVariants: [
          { lbl: 'Luồng 7-bước gốc', pct: 35, cls: 'control', badge: '' },
          { lbl: 'Thiết kế 3-giai đoạn', pct: 78, cls: 'winner', badge: '✓ Được áp dụng' }
        ],
        abStat: 'Ước tính dựa trên phân tích cognitive load và kiểm thử prototype · n=24 học sinh',
        journeyTitle: 'Journey Map Học sinh — Trải nghiệm Cài đặt',
        journeyStages: ['Mở hộp','Bật nguồn','Tạo tài khoản','Đồng bộ nội dung','Đọc lần đầu'],
        journeyRows: [
          { label: 'Mục tiêu', cells: ['Xem thiết bị','Bật lên','Vào app nhanh','Lấy sách nhanh','Đọc bài'], types: ['','','','',''] },
          { label: 'Cognitive Load', cells: ['Thấp','Thấp','❌ Quá tải (5 trường)','❌ Chờ lâu','Thấp'], types: ['','','pain high','pain',''] },
          { label: 'Cảm xúc', cells: ['😄','🙂','😤','😴','😊'], types: ['emotion-high','emotion-high','emotion-low','emotion-mid','emotion-high'] },
          { label: 'Giải pháp HCI', cells: ['—','—','✅ 3-giai đoạn','✅ Progress bar','—'], types: ['','','solution','solution',''] }
        ],
        beforeAfterTitle: 'Kết quả UX — Trước vs Sau Tái thiết kế',
        before: [{ n: 'Hoàn thành Cài đặt', v: '~35%' },{ n: 'Điểm Thoát', v: 'Bước 2–3' },{ n: 'Thời gian đến Lần đọc 1', v: '22 phút' },{ n: 'Hỗ trợ Phụ huynh', v: 'Cao' }],
        after: [{ n: 'Hoàn thành Cài đặt', v: '~78%' },{ n: 'Điểm Thoát', v: 'Bước 5 (cuối)' },{ n: 'Thời gian đến Lần đọc 1', v: '8 phút' },{ n: 'Hỗ trợ Phụ huynh', v: 'Giảm đáng kể' }],
        learnings: [
          { icon: '🧠', title: "Định luật Miller trong thực tế", text: "Giới hạn bộ nhớ làm việc của não người là 3–4 mục. Vượt ngưỡng đó, người dùng không phải khó tính — họ đơn giản là không thể xử lý thêm được nữa." },
          { icon: '📱', title: 'Một hành động mỗi màn hình', text: 'Progressive disclosure không có nghĩa là ẩn thông tin. Nó có nghĩa là chỉ hiện những gì người dùng cần ở thời điểm đó — còn lại để đến khi họ thực sự cần.' },
          { icon: '🗺️', title: 'Journey map trước khi mở Figma', text: 'Nếu tôi mở Figma trước khi lập journey map, tôi sẽ chỉ làm lại giao diện mà không chạm được vào vấn đề thật. Journey map là thứ cho thấy vấn đề hệ thống, không phải vấn đề giao diện.' }
        ]
      }
    ]
  },
  skills: {
    tag: 'Năng lực Lõi', title: 'Kỹ năng <span>Chuyên môn</span>',
    radarLbl: 'Biểu đồ Radar Kỹ năng', certLbl: 'Chứng chỉ', popupTitle: 'Định lượng & Tác động',
    list: [
      {n:'Customer Journey Mapping',ref:'Minh chứng qua: Design Thinking (UEH)',m:['Thiết kế 15+ user flows cho startup','Giảm onboarding friction 30%','Tối ưu 5+ touchpoints chuyển đổi']},
      {n:'Thiết kế UX / HCI',ref:'Minh chứng qua: Human-Computer Interaction (UEH)',m:['Ứng dụng vào 3 dự án thực tế','Giảm cognitive load E-Reader','Thiết kế Gradio UI chuẩn Heuristic']},
      {n:'Agile / Scrum (CPMAI)',ref:'Minh chứng qua: Google PM Cert & EchoMind',m:['Quản lý 8 Sprints liên tục','Dẫn nhóm 7 thành viên','100% milestone đúng hạn']},
      {n:'A/B Testing & Interleaving',ref:'Minh chứng qua: Thử nghiệm sản phẩm SIHUB',m:['Chạy 10+ thử nghiệm tính năng','Xác thực độ tin cậy 95%','Ngăn 3 lỗi UX trước khi ra mắt']},
      {n:'Phân rã Vấn đề',ref:'Minh chứng qua: Innovation Management (UEH)',m:['Phân rã 5+ Epics cấp cao','Chẩn đoán root-cause Mode Collapse','Cấu trúc 150+ yêu cầu stakeholders']},
      {n:'Viết PRD & User Stories',ref:'Minh chứng qua: Entrepreneurship Innovation (UEH)',m:['Soạn 10+ PRD chuẩn hóa','Quản lý backlog 200+ User Stories','Đạt chuẩn URD cấp thành phố']},
      {n:'Python & PyTorch (Có nền tảng)',ref:'Ứng dụng qua: Dự án EchoMind AI',m:['Tối ưu kiến trúc Transformer V2','Áp dụng Int8 Quantization','Giảm độ trễ AI xuống <1s']}
    ],
    radarLabels: ['UX/HCI','Agile','Journey Map','Phân tích DL','Python','PyTorch/ML','A/B Testing'],
    certs: [
      {i:'🏅',n:'Quản lý Dự án (Google PM)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp',dash:false},
      {i:'🗣️',n:'TOEIC — Năng lực Tiếng Anh',org:'Đang chuẩn bị thi',dash:true,prog:'Đang học'}
    ]
  },
  edu: {
    tag: 'Nền tảng Học vấn', title: 'Học vấn & <span>Thành tích</span>',
    uni: 'Đại học Kinh tế TP.HCM (UEH)', major: 'Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo',
    courseTag: 'Các môn học Cốt lõi định hình Tư duy Sản phẩm',
    courses: ['Tư duy Thiết kế','Tương tác Người-Máy (HCI)','Quản trị ĐMST','Trí tuệ Doanh nghiệp','Chuyển đổi Kinh doanh Số','Dự án AI'],
    certTag: 'Chứng chỉ',
    certs: [
      {i:'🏅',n:'Quản lý Dự án (Google PM)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {i:'📊',n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',dash:false,link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {i:'🔄',n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp',dash:false},
      {i:'🗣️',n:'TOEIC — Năng lực Tiếng Anh',org:'Đang chuẩn bị thi',dash:true,prog:'Đang học'}
    ]
  },
  chat: {
    name: 'Trợ lý AI của Minh', sub: '● Trực tuyến · Sẵn sàng', reset: '↺ Làm lại', logout: '⏻ Ngôn ngữ',
    greeting: `Xin chào! Tôi là AI assistant ở đây để giới thiệu với bạn về Nguyễn Hoàng Minh — sinh viên năm cuối UEH, đang làm Product & UX thực chiến tại SIHUB, một trong những trung tâm hỗ trợ startup lớn nhất ở TP.HCM, từ giữa năm 2024 đến nay.\n\nMinh không chỉ vẽ journey map trên giấy — anh ấy chạy A/B test thực tế, theo dõi NPS từng bước trong hành trình, và vừa dẫn dắt một nhóm 7 người xây dựng dự án AI từ đầu. Bạn muốn tìm hiểu về phần nào?`,
    prompts: [
      {id:'exp',i:'💼',l:'Kinh nghiệm'},{id:'proj',i:'🧠',l:'Dự án'},
      {id:'ux',i:'🎨',l:'UX Work'},{id:'skills',i:'⚡',l:'Kỹ năng'}
    ],
    ans: {
      exp: `Minh làm việc tại SIHUB — Trung tâm Hỗ trợ Khởi nghiệp & ĐMST trực thuộc Sở KH&CN TP.HCM — từ giữa năm 2024.\n\nVị trí gần nhất là Chuyên viên Quản lý Dự án (01–10/2025). Minh là đầu mối làm việc trực tiếp với hơn 150 startup founder trong chương trình ươm tạo — thiết kế hành trình onboarding của họ từ đầu đến cuối, rồi chạy A/B test để kiểm chứng từng thay đổi. Một trong những điều Minh tự hào: thuyết phục được đội ngũ không nhìn NPS như một con số nữa, mà như một tín hiệu — để biết chính xác chỗ nào trong hành trình đang có vấn đề.\n\nTrước đó, hồi còn là Thực tập sinh R&D (07–12/2024), Minh xử lý một dự án phân tích khoảng trống năng lực quy mô lớn — làm việc với cơ quan nhà nước, viện nghiên cứu và doanh nghiệp, rồi tổng hợp tất cả thành tài liệu yêu cầu hệ thống theo chuẩn URD.`,
      proj: `Minh có ba dự án đáng chú ý:\n\n🧠 EchoMind AI là dự án lớn nhất (09–12/2025). Đây là dự án AI của nhóm sinh viên, train mô hình giải mã tín hiệu sóng não thành văn bản bằng bộ dữ liệu Brain-to-Text 2025 từ Kaggle. Minh là Project Lead — chạy 8 Agile sprint, khi mô hình LSTM đầu tiên sập vào Mode Collapse thì Minh chẩn đoán vấn đề và quyết định chuyển sang kiến trúc Transformer. Cuối cùng mô hình đạt 55–65 từ/phút, độ trễ dưới 1 giây. Minh còn thiết kế giao diện Gradio demo để kết quả AI hiển thị theo cách người ta có thể hiểu được.\n\n📚 Hệ sinh thái E-Reader (03–06/2025) là dự án nghiên cứu người dùng cho nền tảng đọc sách điện tử dành cho học sinh. Minh lập bản đồ hành trình cài đặt, tìm ra chỗ học sinh bỏ cuộc, rồi dùng nguyên lý HCI để đơn giản hóa luồng. Dự án vào Top 20 cuộc thi do UBND TP.HCM tổ chức.\n\n🚀 Vận hành Sự kiện ĐMST — công việc đang diễn ra, tổ chức các sự kiện startup lớn như Univ.Star 2024/2025 và WHISE Week 2024 tại SIHUB.`,
      ux: `Phần UX Experience có 3 case study, mỗi cái kể lại một câu chuyện thiết kế thực tế — không phải lý thuyết.\n\n🗺️ Case 01 là hành trình onboarding của startup tại SIHUB. Chỉ 42% founder hoàn tất được luồng kích hoạt. Minh đào vào dữ liệu, tổ chức workshop journey mapping, tìm ra điểm thoát thực sự là bước upload tài liệu (yêu cầu không rõ ràng), rồi test một cách sửa nhỏ qua A/B experiment. Kết quả: tỷ lệ kích hoạt lên 68%, NPS tăng từ 28 lên 47, support tickets giảm khoảng 70%.\n\n🧠 Case 02 là giao diện demo của EchoMind. Khi nhóm xây xong mô hình, họ làm demo bằng Gradio — và nó trông như một hộp đen. Minh đánh giá lại bằng 10 Heuristics của Nielsen rồi thêm lớp attention map để người xem thấy được mô hình đang "đọc" phần nào của sóng não. Điểm heuristic tăng từ 38 lên 82 trên 100.\n\n📱 Case 03 là luồng cài đặt cho thiết bị E-Reader của học sinh. Học sinh bỏ cuộc ở bước 2–3 vì phải điền quá nhiều thứ cùng lúc. Minh áp dụng Định luật Miller để chia nhỏ thành 3 giai đoạn. Tỷ lệ hoàn thành cài đặt tăng từ 35% lên 78%, thời gian đến lần đọc đầu tiên giảm từ 22 phút xuống còn 8 phút.`,
      skills: `Thế mạnh lõi của Minh là product và UX — lập bản đồ hành trình người dùng, chạy A/B test, viết PRD, phân tích vấn đề thành những thứ một nhóm có thể thực thi được. Minh cũng quen với Agile và khung CPMAI, thứ mà anh ấy dùng trực tiếp qua 8 sprint trong dự án EchoMind.\n\nVề kỹ thuật, Minh biết Python và đã làm việc thực tế với PyTorch và phân tích dữ liệu — không ở mức kỹ sư, nhưng đủ để cộng tác chặt với đội AI và hiểu chuyện gì đang xảy ra bên trong.\n\nVề con người và thực thi — anh ấy đã quản lý hơn 150 startup founder với tư cách đầu mối chính tại một trung tâm do chính quyền thành phố hỗ trợ, và trình bày insight chiến lược trực tiếp lên Ban Giám đốc. Đó không phải chuyện nhỏ.`
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
      return `<div class="project-card featured"><div>
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
        <div style="font-family:'DM Mono',monospace;font-size:10px;color:var(--accent2);line-height:2.2;text-align:left;">EEG Input (256ch)<br>↓ HDF5 → Tensor<br>↓ Positional Enc.<br>↓ Transformer V2<br>↓ Int8 Quantization<br>↓ Gradio Expert UI<br>→ Text Output</div>
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
