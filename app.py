<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nguyễn Hoàng Minh · Product & UX</title>
<meta name="description" content="Nguyễn Hoàng Minh — Product Owner, UX Strategist & AI Builder. Portfolio.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<style>
:root{
  /* refined dark surfaces */
  --bg:#07070b; --bg1:#0c0c13; --bg2:#11111a;
  --surface:#15151f; --surface2:#1c1c29; --surface3:#24243400;
  --ink3:#13131c;
  --line:rgba(255,255,255,.065); --line2:rgba(255,255,255,.12);
  /* text — tuned for AA contrast on --bg */
  --txt:#f3f3f8; --txt2:#aeaec6; --txt3:#71718e;
  /* brand */
  --violet:#7c6af7; --violet2:#a594fc; --violet3:#cbbffe;
  --teal:#4dd9c0; --gold:#f0c060; --green:#52d18a; --coral:#ff7b6b; --blue:#5b9bd5;
  --glow:124,106,247;
  /* motion tokens */
  --e-out:cubic-bezier(.16,1,.3,1);
  --e-soft:cubic-bezier(.22,.61,.36,1);
  --d-fast:.18s; --d:.34s; --d-slow:.6s;
  --shadow-card:0 24px 60px -24px rgba(0,0,0,.7);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
button{font-family:inherit;font-size:inherit;color:inherit;background:none;border:none;cursor:pointer;-webkit-appearance:none;appearance:none;}
html{scroll-behavior:smooth;}
body{
  font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--txt);
  height:100vh;overflow:hidden;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
}
::selection{background:rgba(var(--glow),.35);color:#fff;}

/* ===== ambient depth field (3D parallax orbs) ===== */
.depth-field{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;perspective:1200px;}
.orb{position:absolute;border-radius:50%;filter:blur(70px);opacity:.5;will-change:transform;mix-blend-mode:screen;transition:transform .6s var(--e-soft);}
.orb.o1{width:520px;height:520px;top:-140px;left:6%;background:radial-gradient(circle,rgba(124,106,247,.55),transparent 70%);}
.orb.o2{width:460px;height:460px;bottom:-120px;left:30%;background:radial-gradient(circle,rgba(77,217,192,.32),transparent 70%);}
.orb.o3{width:380px;height:380px;top:18%;right:24%;background:radial-gradient(circle,rgba(240,192,96,.18),transparent 70%);}
.grid-floor{position:fixed;inset:auto 0 0 0;height:42vh;z-index:0;pointer-events:none;opacity:.5;
  background-image:linear-gradient(rgba(124,106,247,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(124,106,247,.07) 1px,transparent 1px);
  background-size:48px 48px;transform-origin:bottom;transform:perspective(420px) rotateX(62deg);
  -webkit-mask-image:linear-gradient(to top,#000,transparent);mask-image:linear-gradient(to top,#000,transparent);}

/* noise grain */
.noise{position:fixed;inset:0;opacity:.03;pointer-events:none;z-index:101;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* toast */
#toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%) translateY(16px);background:rgba(28,28,41,.96);border:1px solid var(--green);color:var(--green);font-family:'DM Mono',monospace;font-size:12px;padding:11px 22px;border-radius:12px;z-index:99999;opacity:0;transition:all .4s var(--e-out);pointer-events:none;white-space:nowrap;box-shadow:0 14px 40px rgba(0,0,0,.5);letter-spacing:.4px;backdrop-filter:blur(10px);}
#toast.show{opacity:1;transform:translateX(-50%) translateY(0);}

/* float popup */
#float-popup{position:fixed;width:308px;background:rgba(17,17,26,.97);border:1px solid rgba(var(--glow),.6);border-radius:16px;padding:18px;box-shadow:0 24px 60px rgba(0,0,0,.65);backdrop-filter:blur(14px);opacity:0;visibility:hidden;transition:opacity .22s,visibility .22s,transform .22s var(--e-out);transform:translateY(6px);pointer-events:none;z-index:99998;}
#float-popup.on{transform:translateY(0);}
.popup-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);text-transform:uppercase;letter-spacing:1.4px;margin-bottom:12px;}
.popup-metric{font-size:13px;color:var(--txt);line-height:1.55;display:flex;align-items:flex-start;gap:9px;margin-bottom:9px;}
.popup-metric:last-child{margin-bottom:0;}
.popup-metric::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--green);margin-top:6px;flex-shrink:0;box-shadow:0 0 8px var(--green);}

/* scroll progress */
#scroll-progress{position:fixed;top:0;left:96px;height:2px;background:linear-gradient(90deg,var(--violet),var(--teal));width:0%;z-index:1000;transition:width .12s linear;box-shadow:0 0 12px rgba(var(--glow),.6);}

/* ============ LANGUAGE GATE ============ */
#lang-overlay{position:fixed;inset:0;background:radial-gradient(ellipse at 50% 30%,#15131f,#07070b 70%);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:42px;transition:opacity .6s var(--e-out),visibility .6s;perspective:1000px;}
#lang-overlay.hide{opacity:0;visibility:hidden;}
.lo-stack{text-align:center;transform-style:preserve-3d;}
.lo-logo{font-family:'Syne',sans-serif;font-size:74px;font-weight:800;letter-spacing:-4px;line-height:1;
  background:linear-gradient(135deg,var(--violet3),var(--violet) 60%,var(--teal));-webkit-background-clip:text;background-clip:text;color:transparent;
  animation:loFloat 6s ease-in-out infinite;}
@keyframes loFloat{0%,100%{transform:translateZ(0) translateY(0);}50%{transform:translateZ(40px) translateY(-6px);}}
.lo-tagline{font-family:'DM Mono',monospace;font-size:11px;color:var(--txt2);letter-spacing:4px;text-transform:uppercase;margin-top:14px;}
.lo-question{font-family:'Syne',sans-serif;font-size:22px;font-weight:600;color:var(--txt);text-align:center;line-height:1.5;}
.lo-options{display:flex;gap:22px;}
.lo-btn{position:relative;background:rgba(21,21,31,.8);border:1px solid var(--line2);color:var(--txt2);padding:22px 52px;border-radius:18px;font-family:'Syne',sans-serif;font-size:20px;font-weight:600;cursor:pointer;transition:all .4s var(--e-out);display:flex;flex-direction:column;align-items:center;gap:8px;overflow:hidden;}
.lo-btn::after{content:'';position:absolute;inset:0;background:radial-gradient(circle at 50% 120%,rgba(var(--glow),.4),transparent 70%);opacity:0;transition:opacity .4s;}
.lo-btn:hover{border-color:rgba(var(--glow),.7);transform:translateY(-6px) rotateX(8deg);box-shadow:0 24px 50px rgba(var(--glow),.25);color:var(--txt);}
.lo-btn:hover::after{opacity:1;}
.lo-btn:focus-visible{outline:2px solid var(--violet2);outline-offset:3px;}
.lo-btn span{font-family:'DM Mono',monospace;font-size:11px;color:var(--txt3);}
.lo-kbhint{font-family:'DM Mono',monospace;font-size:11px;color:var(--txt3);letter-spacing:1px;text-align:center;}
.lo-kbhint strong{color:var(--txt2);}

/* ============ APP SHELL ============ */
.app{display:flex;height:100vh;width:100%;position:relative;z-index:2;opacity:0;transition:opacity .8s var(--e-out);}
.app.visible{opacity:1;}

/* sidebar */
.sidenav{width:96px;height:100%;background:rgba(10,10,16,.72);backdrop-filter:blur(16px);border-right:1px solid var(--line);display:flex;flex-direction:column;align-items:center;padding:28px 0 24px;gap:8px;flex-shrink:0;z-index:10;}
.nav-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:19px;margin-bottom:18px;letter-spacing:-1px;background:linear-gradient(135deg,var(--violet3),var(--teal));-webkit-background-clip:text;background-clip:text;color:transparent;}
.nav-item{width:60px;height:56px;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;transition:transform .3s var(--e-out),background .25s,color .25s,border-color .25s;color:var(--txt2);border:1px solid transparent;position:relative;gap:4px;}
.nav-item svg{width:20px;height:20px;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0;transition:transform .3s var(--e-out);}
.nav-item .nav-lbl{font-family:'DM Mono',monospace;font-size:8px;letter-spacing:.3px;text-transform:uppercase;opacity:.75;white-space:nowrap;}
.nav-item:hover{background:var(--surface);color:var(--txt);transform:translateX(3px);}
.nav-item:hover svg{transform:scale(1.12);}
.nav-item:focus-visible{outline:2px solid var(--violet2);outline-offset:2px;}
.nav-item.active{background:linear-gradient(135deg,rgba(var(--glow),.32),rgba(var(--glow),.1));color:var(--violet2);border-color:rgba(var(--glow),.4);box-shadow:0 0 22px rgba(var(--glow),.22);}
.nav-item.active::before{content:'';position:absolute;left:-1px;top:50%;transform:translateY(-50%);width:3px;height:24px;background:linear-gradient(var(--violet2),var(--teal));border-radius:0 3px 3px 0;}
.nav-tooltip{position:absolute;left:78px;background:var(--surface2);color:var(--txt);font-size:12px;font-family:'DM Mono',monospace;padding:6px 12px;border-radius:8px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .15s,transform .2s var(--e-out);transform:translateX(-4px);border:1px solid var(--line2);z-index:100;}
.nav-item:hover .nav-tooltip{opacity:1;transform:translateX(0);}
.nav-spacer{flex:1;}
.nav-foot{display:flex;flex-direction:column;gap:8px;align-items:center;}
.nav-mini{width:44px;height:44px;border-radius:13px;border:1px solid var(--line2);background:var(--surface);color:var(--txt2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-family:'DM Mono',monospace;font-size:11px;transition:all .25s var(--e-out);}
.nav-mini:hover{border-color:rgba(var(--glow),.6);color:var(--txt);transform:translateY(-2px);}
.nav-mini:focus-visible{outline:2px solid var(--violet2);outline-offset:2px;}
.nav-mini svg{width:17px;height:17px;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;}

/* visual panel */
.visual-panel{flex:1;height:100%;overflow-y:auto;overflow-x:hidden;position:relative;scroll-behavior:smooth;perspective:1400px;}
.visual-panel::-webkit-scrollbar{width:6px;}
.visual-panel::-webkit-scrollbar-thumb{background:var(--line2);border-radius:6px;}
.visual-panel::-webkit-scrollbar-thumb:hover{background:rgba(var(--glow),.5);}

/* view transition curtain (3D depth push) */
.view-content{padding:64px 76px 96px;min-height:100%;position:relative;transform-origin:center top;}
.view-content.swapping{animation:viewOut .26s var(--e-soft) forwards;}
@keyframes viewOut{to{opacity:0;transform:translateZ(-60px) translateY(8px);filter:blur(4px);}}
.view-content.swapin{animation:viewIn .5s var(--e-out);}
@keyframes viewIn{from{opacity:0;transform:translateZ(-80px) translateY(22px);filter:blur(6px);}to{opacity:1;transform:none;filter:none;}}

/* shared section atoms */
.section-tag{display:inline-flex;align-items:center;gap:9px;font-family:'DM Mono',monospace;font-size:11px;color:var(--violet2);text-transform:uppercase;letter-spacing:2.6px;margin-bottom:22px;}
.section-tag::before{content:'';width:22px;height:1px;background:linear-gradient(90deg,var(--violet2),transparent);}
.view-title{font-family:'Syne',sans-serif;font-size:clamp(34px,4vw,50px);font-weight:800;letter-spacing:-1.8px;color:var(--txt);margin-bottom:54px;line-height:1.02;}
.view-title span{background:linear-gradient(120deg,var(--violet2),var(--teal));-webkit-background-clip:text;background-clip:text;color:transparent;}
.subtle-div{height:1px;background:linear-gradient(90deg,var(--line2),transparent);margin:48px 0;}

/* reveal-on-scroll (Apple-style) */
.reveal{opacity:0;transform:translateY(42px) rotateX(7deg);transform-origin:center bottom;filter:blur(6px);transition:opacity .8s var(--e-out),transform .9s var(--e-out),filter .8s var(--e-out);will-change:opacity,transform,filter;}
.reveal.in{opacity:1;transform:none;filter:none;}

/* magnetic lift — hover brings the card FORWARD (lift + scale) so it invites reading,
   never recede/shrink. Lift+shadow via CSS (reliable); cursor glow + subtle inner 3D tilt via JS. */
.tilt{perspective:1000px;transition:transform .5s var(--e-out),box-shadow .5s var(--e-out),border-color .35s;will-change:transform;}
.tilt .tilt-lift{position:relative;z-index:1;transition:transform .25s var(--e-out);transform-style:preserve-3d;}
.tilt-glow{position:absolute;inset:0;border-radius:inherit;opacity:0;background:radial-gradient(480px circle at var(--mx,50%) var(--my,50%),rgba(var(--glow),.18),transparent 60%);transition:opacity .35s;pointer-events:none;z-index:0;}
.tilt:hover{transform:translateY(-9px) scale(1.02);border-color:rgba(var(--glow),.5);box-shadow:0 34px 84px -30px rgba(0,0,0,.85),0 0 52px -16px rgba(var(--glow),.34);}
.tilt.featured:hover{transform:translateY(-6px) scale(1.006);}
.tilt:hover .tilt-glow{opacity:1;}
@media(prefers-reduced-motion:reduce){.tilt:hover{transform:none;}}

/* ===== WELCOME ===== */
.hero-3d{position:relative;transform-style:preserve-3d;margin-bottom:8px;}
.welcome-eyebrow{display:flex;align-items:center;gap:11px;margin-bottom:26px;}
.status-dot{width:9px;height:9px;background:var(--green);border-radius:50%;box-shadow:0 0 10px var(--green);animation:pg 2s infinite;}
@keyframes pg{0%,100%{box-shadow:0 0 6px var(--green);}50%{box-shadow:0 0 18px var(--green);}}
.status-text{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--green);letter-spacing:1px;text-transform:uppercase;}
.welcome-name{font-family:'Syne',sans-serif;font-size:clamp(50px,6.2vw,96px);font-weight:800;line-height:.92;letter-spacing:-3px;margin-bottom:16px;transform:translateZ(60px);}
.welcome-name .accent-word{display:block;background:linear-gradient(120deg,var(--violet3),var(--violet) 55%,var(--teal));-webkit-background-clip:text;background-clip:text;color:transparent;}
.welcome-role{font-size:19px;color:var(--txt2);font-weight:300;margin-bottom:36px;font-style:italic;transform:translateZ(34px);}
.welcome-summary{font-size:16px;line-height:1.85;color:var(--txt2);max-width:600px;margin-bottom:44px;border-left:2px solid var(--violet);padding-left:26px;transform:translateZ(20px);}
.welcome-summary strong{color:var(--txt);font-weight:500;}
.contact-row{display:flex;flex-wrap:wrap;gap:11px;margin-bottom:50px;}
.contact-chip{display:flex;align-items:center;gap:9px;padding:10px 18px;background:var(--surface);border:1px solid var(--line2);border-radius:12px;font-size:12.5px;font-family:'DM Mono',monospace;color:var(--txt2);transition:all .25s var(--e-out);cursor:default;}
.contact-chip svg{width:15px;height:15px;stroke:currentColor;stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.contact-chip:hover{border-color:rgba(var(--glow),.5);color:var(--txt);transform:translateY(-3px);}
.contact-chip.copyable{cursor:pointer;}
.contact-chip.copyable:hover{border-color:var(--green);color:var(--green);}
.contact-chip.copyable:focus-visible{outline:2px solid var(--green);outline-offset:2px;}
.stat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;max-width:760px;margin-bottom:56px;perspective:900px;}
.stat-card{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:24px 20px;overflow:hidden;cursor:default;}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--violet),var(--teal));opacity:.85;}
.stat-number{font-family:'Syne',sans-serif;font-size:36px;font-weight:800;color:var(--txt);line-height:1;}
.stat-label{font-size:11px;color:var(--txt2);margin-top:9px;text-transform:uppercase;letter-spacing:.7px;font-family:'DM Mono',monospace;}
.kbd-hint-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.kbd{font-family:'DM Mono',monospace;font-size:10px;padding:4px 9px;background:var(--surface);border:1px solid var(--line2);border-radius:6px;color:var(--txt2);box-shadow:0 2px 0 rgba(0,0,0,.4);}

/* scroll cue */
.scroll-cue{position:absolute;right:0;top:6px;display:flex;flex-direction:column;align-items:center;gap:8px;color:var(--txt3);font-family:'DM Mono',monospace;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;}
.scroll-cue .mouse{width:22px;height:34px;border:1.5px solid var(--line2);border-radius:12px;position:relative;}
.scroll-cue .mouse::after{content:'';position:absolute;top:6px;left:50%;transform:translateX(-50%);width:3px;height:6px;background:var(--violet2);border-radius:2px;animation:scrolly 1.6s infinite;}
@keyframes scrolly{0%{opacity:0;transform:translate(-50%,0);}40%{opacity:1;}80%{opacity:0;transform:translate(-50%,10px);}100%{opacity:0;}}

/* ===== TIMELINE ===== */
.timeline{position:relative;padding-left:36px;}
.timeline::before{content:'';position:absolute;left:0;top:8px;bottom:8px;width:2px;background:linear-gradient(to bottom,var(--violet),rgba(var(--glow),.05));}
.timeline-item{position:relative;margin-bottom:54px;}
.timeline-item::before{content:'';position:absolute;left:-42px;top:6px;width:13px;height:13px;border-radius:50%;background:var(--violet2);box-shadow:0 0 16px rgba(var(--glow),.6);border:2px solid var(--bg);}
.timeline-item.past::before{background:var(--txt3);box-shadow:none;}
.tl-period{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--violet2);letter-spacing:1px;margin-bottom:11px;text-transform:uppercase;}
.tl-role{font-family:'Syne',sans-serif;font-size:23px;font-weight:700;margin-bottom:6px;}
.tl-company{font-size:14px;color:var(--txt2);font-style:italic;margin-bottom:22px;}
.tl-bullets{list-style:none;display:flex;flex-direction:column;gap:14px;}
.tl-bullets li{font-size:14.5px;color:var(--txt2);line-height:1.74;padding-left:24px;position:relative;}
.tl-bullets li::before{content:'';position:absolute;left:0;top:9px;width:8px;height:8px;border-right:1.5px solid var(--violet);border-bottom:1.5px solid var(--violet);transform:rotate(-45deg);}
.tl-bullets li strong{color:var(--txt);font-weight:500;}
.tl-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px;}
.tl-tag{font-family:'DM Mono',monospace;font-size:10.5px;padding:5px 13px;border-radius:7px;background:rgba(var(--glow),.1);border:1px solid rgba(var(--glow),.25);color:var(--violet3);}

/* ===== PROJECTS ===== */
.projects-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px;perspective:1200px;}
.project-card{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:24px;padding:32px;overflow:hidden;}
.project-card:hover{border-color:rgba(var(--glow),.45);box-shadow:var(--shadow-card);}
.project-card.featured{grid-column:1/-1;display:grid;grid-template-columns:1fr 240px;gap:34px;align-items:start;}
.project-card.featured>div{min-width:0;}
.project-desc,.info-val,.tl-bullets li,.cs-text,.problem-text,.insight-text{overflow-wrap:anywhere;}
.project-badge{font-family:'DM Mono',monospace;font-size:10.5px;padding:5px 13px;border-radius:20px;text-transform:uppercase;letter-spacing:.5px;}
.badge-featured{background:rgba(240,192,96,.14);color:var(--gold);border:1px solid rgba(240,192,96,.3);}
.badge-active{background:rgba(82,209,138,.12);color:var(--green);border:1px solid rgba(82,209,138,.3);}
.badge-top20{background:rgba(255,123,107,.14);color:var(--coral);border:1px solid rgba(255,123,107,.3);}
.project-name{font-family:'Syne',sans-serif;font-size:27px;font-weight:700;margin:14px 0 8px;letter-spacing:-.6px;}
.project-sub{font-size:13px;color:var(--txt2);font-style:italic;margin-bottom:18px;}
.project-desc{font-size:14.5px;color:var(--txt2);line-height:1.76;margin-bottom:22px;}
.project-desc strong{color:var(--txt);}
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:16px 0;}
.info-item{background:var(--ink3);border-radius:12px;padding:12px 16px;border:1px solid var(--line);}
.info-lbl{font-family:'DM Mono',monospace;font-size:9px;color:var(--txt2);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:6px;}
.info-val{font-size:12.5px;color:var(--txt);font-weight:500;line-height:1.45;}
.project-metrics{display:flex;flex-wrap:wrap;gap:24px;margin:18px 0;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
.metric-val{font-family:'Syne',sans-serif;font-size:25px;font-weight:700;background:linear-gradient(120deg,var(--violet2),var(--teal));-webkit-background-clip:text;background-clip:text;color:transparent;}
.metric-lbl{font-size:9.5px;color:var(--txt2);text-transform:uppercase;letter-spacing:.6px;margin-top:5px;font-family:'DM Mono',monospace;}
.tech-stack{display:flex;flex-wrap:wrap;gap:8px;}
.tech-pill{font-family:'DM Mono',monospace;font-size:10.5px;padding:5px 13px;border-radius:7px;background:var(--ink3);border:1px solid var(--line2);color:var(--txt2);transition:all .2s;}
.tech-pill:hover{border-color:rgba(var(--glow),.4);color:var(--txt);}
.proj-chart-wrap{background:var(--ink3);border-radius:18px;border:1px solid var(--line);padding:22px;margin:18px 0;}
.proj-chart-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:16px;}
.echo-side{background:var(--ink3);border-radius:20px;border:1px solid var(--line);padding:24px;}
.echo-pipeline{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);line-height:2.3;}
.echo-pipeline b{color:var(--txt);font-weight:500;}

/* ===== UX SECTION ===== */
.dt-flow{display:flex;gap:0;margin-bottom:56px;position:relative;perspective:1000px;}
.dt-phase{flex:1;background:var(--surface);border:1px solid var(--line);padding:22px 16px;position:relative;transition:transform .35s var(--e-out),background .25s,box-shadow .35s,z-index 0s;cursor:default;}
.dt-phase:first-child{border-radius:18px 0 0 18px;}
.dt-phase:last-child{border-radius:0 18px 18px 0;}
.dt-phase:hover{background:var(--surface2);z-index:2;transform:translateY(-6px) translateZ(20px);box-shadow:var(--shadow-card);}
.dt-phase-icon{width:30px;height:30px;margin-bottom:12px;stroke:var(--violet2);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.dt-phase-name{font-family:'Syne',sans-serif;font-size:14px;font-weight:700;color:var(--txt);margin-bottom:7px;}
.dt-phase-desc{font-size:11.5px;color:var(--txt2);line-height:1.6;}
.dt-phase-num{position:absolute;top:12px;right:14px;font-family:'DM Mono',monospace;font-size:10px;color:var(--txt3);}
.dt-phase::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:inherit;}
.dt-phase:nth-child(1)::after{background:var(--violet);}
.dt-phase:nth-child(2)::after{background:var(--coral);}
.dt-phase:nth-child(3)::after{background:var(--gold);}
.dt-phase:nth-child(4)::after{background:var(--green);}
.dt-phase:nth-child(5)::after{background:var(--teal);}
.dt-phase:nth-child(6)::after{background:var(--blue);}

.case-study{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:26px;padding:40px;margin-bottom:30px;overflow:hidden;}
.case-study::before{content:'';position:absolute;top:0;left:0;bottom:0;width:4px;}
.case-study.cs-sihub::before{background:linear-gradient(to bottom,var(--violet),var(--teal));}
.case-study.cs-echomind::before{background:linear-gradient(to bottom,var(--coral),var(--gold));}
.cs-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:30px;gap:22px;}
.cs-meta{flex:1;}
.cs-eyebrow{display:flex;align-items:center;gap:11px;margin-bottom:12px;flex-wrap:wrap;}
.cs-num{font-family:'DM Mono',monospace;font-size:11px;color:var(--txt3);letter-spacing:1px;}
.cs-tag{font-family:'DM Mono',monospace;font-size:10px;padding:4px 11px;border-radius:20px;border:1px solid var(--line2);color:var(--txt2);}
.cs-title{font-family:'Syne',sans-serif;font-size:27px;font-weight:800;letter-spacing:-.6px;margin-bottom:7px;}
.cs-role{font-size:13px;color:var(--txt2);font-style:italic;}
.cs-impact-badge{background:var(--ink3);border:1px solid var(--line2);border-radius:18px;padding:20px 24px;text-align:center;min-width:148px;flex-shrink:0;}
.cs-impact-num{font-family:'Syne',sans-serif;font-size:34px;font-weight:800;color:var(--green);line-height:1;}
.cs-impact-lbl{font-family:'DM Mono',monospace;font-size:9px;color:var(--txt2);text-transform:uppercase;letter-spacing:.8px;margin-top:6px;}
.cs-body{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:30px;}
.cs-section-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:16px;display:flex;align-items:center;gap:9px;}
.cs-section-title::before{content:'';width:22px;height:2px;background:var(--violet2);}
.problem-box{background:rgba(255,123,107,.07);border:1px solid rgba(255,123,107,.2);border-radius:16px;padding:20px 22px;margin-bottom:22px;}
.problem-label{font-family:'DM Mono',monospace;font-size:9px;color:var(--coral);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:9px;display:flex;align-items:center;gap:7px;}
.problem-label svg,.insight-label svg{width:13px;height:13px;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.problem-text{font-size:14.5px;color:var(--txt2);line-height:1.72;}
.problem-text strong{color:var(--txt);}
.insight-box{background:rgba(var(--glow),.08);border:1px solid rgba(var(--glow),.25);border-radius:16px;padding:20px 22px;margin-bottom:18px;}
.insight-label{font-family:'DM Mono',monospace;font-size:9px;color:var(--violet2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:9px;display:flex;align-items:center;gap:7px;}
.insight-text{font-size:14px;color:var(--txt2);line-height:1.7;}
.insight-text strong{color:var(--txt);}
.process-steps{display:flex;flex-direction:column;gap:11px;}
.process-step{display:flex;gap:15px;align-items:flex-start;padding:13px 15px;background:var(--ink3);border-radius:12px;border:1px solid var(--line);transition:border-color .2s,transform .25s var(--e-out);}
.process-step:hover{border-color:var(--line2);transform:translateX(4px);}
.step-num{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);min-width:20px;font-weight:bold;margin-top:2px;}
.step-title{font-size:13.5px;font-weight:600;color:var(--txt);margin-bottom:4px;}
.step-desc{font-size:12.5px;color:var(--txt2);line-height:1.55;}
.ab-container{background:var(--ink3);border-radius:16px;border:1px solid var(--line);padding:22px;margin-bottom:18px;}
.ab-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:18px;}
.ab-variants{display:flex;flex-direction:column;gap:12px;}
.ab-row{display:flex;align-items:center;gap:14px;}
.ab-variant-lbl{font-family:'DM Mono',monospace;font-size:11px;min-width:96px;color:var(--txt2);}
.ab-bar-track{flex:1;height:30px;background:var(--surface2);border-radius:8px;overflow:hidden;}
.ab-bar-fill{height:100%;border-radius:8px;display:flex;align-items:center;padding-left:12px;font-family:'DM Mono',monospace;font-size:11px;font-weight:bold;color:#fff;width:0;transition:width 1.3s var(--e-out);}
.ab-bar-fill.control{background:rgba(110,110,140,.6);}
.ab-bar-fill.winner{background:linear-gradient(90deg,var(--green),var(--teal));}
.ab-badge{font-family:'DM Mono',monospace;font-size:10px;padding:4px 10px;border-radius:6px;white-space:nowrap;background:rgba(82,209,138,.15);color:var(--green);border:1px solid rgba(82,209,138,.3);}
.ab-stat{font-size:11px;color:var(--txt3);margin-top:10px;font-family:'DM Mono',monospace;line-height:1.5;}
.journey-map{margin-bottom:8px;overflow-x:auto;}
.jm-stage-row{display:flex;gap:2px;margin-bottom:2px;min-width:560px;}
.jm-label{font-family:'DM Mono',monospace;font-size:10px;color:var(--txt2);text-transform:uppercase;letter-spacing:.8px;padding:10px 14px;background:var(--ink3);border-radius:7px 0 0 7px;display:flex;align-items:center;min-width:118px;flex-shrink:0;}
.jm-cells{display:flex;flex:1;gap:2px;}
.jm-cell{flex:1;padding:10px;background:var(--ink3);font-size:12px;color:var(--txt2);line-height:1.45;min-height:50px;display:flex;align-items:center;justify-content:center;text-align:center;}
.jm-cell.stage-name{background:var(--surface2);font-family:'DM Mono',monospace;font-size:10px;font-weight:600;color:var(--violet2);letter-spacing:.4px;}
.jm-cell.pain{background:rgba(255,123,107,.1);color:var(--coral);}
.jm-cell.pain.high{background:rgba(255,123,107,.22);font-weight:600;}
.jm-cell.solution{background:rgba(82,209,138,.1);color:var(--green);}
.jm-cell.emotion-low,.jm-cell.emotion-mid,.jm-cell.emotion-high{font-size:18px;}
.jm-cell.emotion-low{background:rgba(255,123,107,.08);}
.jm-cell.emotion-mid{background:rgba(240,192,96,.08);}
.jm-cell.emotion-high{background:rgba(82,209,138,.1);}
.impact-compare{display:grid;grid-template-columns:1fr auto 1fr;gap:18px;align-items:center;margin-bottom:8px;}
.impact-col{background:var(--ink3);border-radius:16px;border:1px solid var(--line);padding:20px;}
.impact-col.before{border-color:rgba(255,123,107,.25);}
.impact-col.after{border-color:rgba(82,209,138,.25);}
.impact-col-label{font-family:'DM Mono',monospace;font-size:10px;text-transform:uppercase;letter-spacing:1px;margin-bottom:15px;}
.impact-col.before .impact-col-label{color:var(--coral);}
.impact-col.after .impact-col-label{color:var(--green);}
.impact-metric-row{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--line);}
.impact-metric-row:last-child{border-bottom:none;}
.impact-metric-name{font-size:12.5px;color:var(--txt2);}
.impact-metric-val{font-family:'DM Mono',monospace;font-size:13px;font-weight:600;}
.impact-col.before .impact-metric-val{color:var(--coral);}
.impact-col.after .impact-metric-val{color:var(--green);}
.impact-arrow{color:var(--violet2);text-align:center;}
.impact-arrow svg{width:26px;height:26px;stroke:currentColor;stroke-width:2;fill:none;}
.cs-learnings{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px;padding-top:26px;border-top:1px solid var(--line);}
.learning-card{background:var(--ink3);border-radius:14px;padding:18px;border:1px solid var(--line);transition:transform .3s var(--e-out),border-color .25s;}
.learning-card:hover{transform:translateY(-4px);border-color:var(--line2);}
.learning-icon{width:24px;height:24px;margin-bottom:10px;stroke:var(--violet2);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.learning-title{font-family:'DM Mono',monospace;font-size:10px;color:var(--violet2);text-transform:uppercase;letter-spacing:1px;margin-bottom:7px;}
.learning-text{font-size:12.5px;color:var(--txt2);line-height:1.6;}

/* ===== SKILLS ===== */
.skills-layout{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:start;}
.lk-skill-card{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:20px 22px;margin-bottom:14px;display:flex;flex-direction:column;gap:9px;transition:transform .3s var(--e-out),border-color .25s,box-shadow .3s;cursor:help;}
.lk-skill-card:hover{border-color:rgba(var(--glow),.45);transform:translateY(-3px);box-shadow:0 14px 30px -16px rgba(0,0,0,.6);}
.lk-skill-card:focus-visible{outline:2px solid var(--violet2);outline-offset:2px;}
.lk-skill-header{display:flex;justify-content:space-between;align-items:center;}
.lk-skill-title{font-size:15px;font-weight:600;color:var(--txt);display:flex;align-items:center;gap:11px;}
.lk-skill-title .dot{width:8px;height:8px;border-radius:2px;background:linear-gradient(135deg,var(--violet2),var(--teal));transform:rotate(45deg);flex-shrink:0;}
.lk-info svg{width:15px;height:15px;stroke:var(--txt3);stroke-width:1.8;fill:none;}
.lk-skill-ref{font-family:'DM Mono',monospace;font-size:11px;color:var(--txt2);display:flex;align-items:center;gap:7px;line-height:1.4;}
.lk-skill-ref::before{content:'↳';color:var(--violet2);font-weight:bold;}
.cert-card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:16px 18px;margin-bottom:11px;display:flex;align-items:center;gap:15px;transition:transform .25s var(--e-out),border-color .25s,box-shadow .25s;}
a.cert-card{cursor:pointer;color:inherit;text-decoration:none;}
a.cert-card:hover{transform:translateX(5px);border-color:rgba(var(--glow),.5);box-shadow:0 8px 20px rgba(var(--glow),.14);}
a.cert-card:focus-visible{outline:2px solid var(--violet2);outline-offset:2px;}
a.cert-card:hover .cert-link-icon{opacity:1;color:var(--violet2);}
.cert-ico{width:26px;height:26px;flex-shrink:0;stroke:var(--gold);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.skills-chart-wrap{background:var(--ink3);border-radius:18px;border:1px solid var(--line);padding:22px;margin-bottom:26px;}

/* ===== EDUCATION ===== */
.edu-hero{position:relative;background:linear-gradient(135deg,var(--surface),var(--surface2));border:1px solid var(--line);border-radius:26px;padding:42px;margin-bottom:30px;overflow:hidden;}
.edu-hero::before{content:'UEH';position:absolute;right:-15px;bottom:-50px;font-family:'Syne',sans-serif;font-size:190px;font-weight:800;color:rgba(255,255,255,.025);line-height:1;pointer-events:none;}
.gpa-badge{display:inline-flex;align-items:center;gap:15px;background:rgba(240,192,96,.1);border:1px solid rgba(240,192,96,.3);border-radius:18px;padding:18px 26px;margin-top:20px;}
.gpa-ico{width:30px;height:30px;stroke:var(--gold);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.gpa-val{font-family:'Syne',sans-serif;font-size:30px;font-weight:800;color:var(--gold);}
.course-pill{font-size:13px;padding:8px 17px;background:var(--surface);border:1px solid var(--line2);border-radius:10px;color:var(--txt2);transition:all .2s var(--e-out);}
.course-pill:hover{border-color:rgba(var(--glow),.4);color:var(--txt);transform:translateY(-2px);}

/* ===== CHAT ===== */
.chat-panel{width:420px;height:100%;flex-shrink:0;background:rgba(10,10,16,.72);backdrop-filter:blur(16px);border-left:1px solid var(--line);display:flex;flex-direction:column;}
.chat-header{padding:22px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:14px;flex-shrink:0;}
.chat-avatar{position:relative;width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,var(--violet),var(--teal));display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(var(--glow),.35);}
.chat-avatar svg{width:22px;height:22px;stroke:#fff;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.chat-name{font-family:'Syne',sans-serif;font-size:15px;font-weight:700;}
.chat-sub{font-size:11px;color:var(--green);font-family:'DM Mono',monospace;margin-top:3px;display:flex;align-items:center;gap:6px;}
.chat-sub .live{width:6px;height:6px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green);animation:pg 2s infinite;}
.chat-actions{margin-left:auto;display:flex;gap:8px;}
.chat-btn{background:none;border:1px solid var(--line2);color:var(--txt2);font-size:11px;padding:8px 12px;border-radius:9px;cursor:pointer;font-family:'DM Mono',monospace;transition:all .2s var(--e-out);white-space:nowrap;display:flex;align-items:center;gap:5px;}
.chat-btn svg{width:13px;height:13px;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.chat-btn:hover{border-color:rgba(var(--glow),.6);background:var(--surface2);color:var(--txt);}
.chat-btn:focus-visible{outline:2px solid var(--violet2);outline-offset:2px;}
.chat-btn.danger:hover{border-color:var(--coral);color:var(--coral);}
.chat-messages{flex:1;overflow-y:auto;padding:22px;display:flex;flex-direction:column;gap:18px;scroll-behavior:smooth;}
.chat-messages::-webkit-scrollbar{width:4px;}
.chat-messages::-webkit-scrollbar-thumb{background:var(--line2);border-radius:4px;}
.msg-row{display:flex;gap:10px;align-items:flex-end;animation:msgIn .4s var(--e-out);}
@keyframes msgIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
.msg-row.user{flex-direction:row-reverse;}
.msg-av{width:30px;height:30px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.msg-av svg{width:16px;height:16px;stroke:#fff;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.msg-av.ai{background:linear-gradient(135deg,var(--violet),var(--teal));}
.msg-av.user{background:var(--surface2);border:1px solid var(--line2);}
.msg-av.user svg{stroke:var(--txt2);}
.msg-bubble{max-width:82%;padding:14px 18px;border-radius:18px;font-size:13.5px;line-height:1.66;}
.msg-bubble.ai{background:var(--surface);border:1px solid var(--line2);color:var(--txt);border-bottom-left-radius:5px;}
.msg-bubble.user{background:var(--violet);color:#fff;border-bottom-right-radius:5px;}
.cursor-blink{display:inline-block;width:7px;height:15px;background:var(--violet2);margin-left:3px;animation:blink 1s step-end infinite;vertical-align:middle;border-radius:1px;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}
.chat-footer{padding:16px;border-top:1px solid var(--line);flex-shrink:0;}
.prompts-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.prompt-btn{position:relative;background:linear-gradient(145deg,var(--surface),var(--surface2));border:1px solid var(--line2);border-radius:16px;padding:16px 14px;color:var(--txt);cursor:pointer;transition:transform .3s var(--e-out),box-shadow .3s,border-color .25s;display:flex;flex-direction:column;align-items:flex-start;gap:9px;overflow:hidden;text-align:left;}
.prompt-btn::before{content:'';position:absolute;top:0;left:0;width:3px;height:100%;background:linear-gradient(var(--violet),var(--teal));transform:scaleY(0);transition:transform .3s var(--e-out);transform-origin:bottom;}
.prompt-btn:hover{transform:translateY(-4px);box-shadow:0 10px 24px rgba(var(--glow),.2);border-color:rgba(var(--glow),.45);}
.prompt-btn:hover::before{transform:scaleY(1);}
.prompt-btn:focus-visible{outline:2px solid var(--violet2);outline-offset:2px;}
.p-icon{display:flex;align-items:center;justify-content:center;padding:9px;background:rgba(var(--glow),.1);border-radius:11px;border:1px solid rgba(var(--glow),.2);}
.p-icon svg{width:20px;height:20px;stroke:var(--violet2);stroke-width:1.7;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.p-lbl{font-family:'Syne',sans-serif;font-size:15px;letter-spacing:-.2px;font-weight:700;color:var(--txt);}
.prompt-btn:disabled{opacity:.4;cursor:not-allowed;transform:none;box-shadow:none;}
.prompt-btn:disabled::before{display:none;}

/* ===== RESPONSIVE ===== */
@media(max-width:1240px){
  .chat-panel{width:360px;}
  .view-content{padding:48px 52px 80px;}
  .stat-grid{grid-template-columns:repeat(2,1fr);}
  .skills-layout{grid-template-columns:1fr;gap:28px;}
  .cs-body{grid-template-columns:1fr;}
  .cs-learnings{grid-template-columns:1fr 1fr;}
}
@media(max-width:920px){
  .chat-panel{display:none;}
  .projects-grid,.cs-body,.cs-learnings{grid-template-columns:1fr;}
  .project-card.featured{grid-template-columns:1fr;}
  .impact-compare{grid-template-columns:1fr;}
  .impact-arrow{transform:rotate(90deg);}
  #scroll-progress{left:72px;}
  .sidenav{width:72px;}
  .nav-item{width:48px;height:48px;}
  .dt-flow{flex-wrap:wrap;gap:10px;}
  .dt-phase{flex:calc(50% - 5px);border-radius:14px !important;}
  .scroll-cue{display:none;}
}
@media(max-width:600px){
  .view-content{padding:30px 18px 64px;}
  .welcome-name{font-size:clamp(34px,11vw,52px);letter-spacing:-1.5px;word-break:break-word;}
  .welcome-name .accent-word{word-break:break-word;}
  .welcome-summary{font-size:15px;padding-left:18px;max-width:none;}
  .welcome-role{font-size:16px;}
  .view-title{font-size:clamp(28px,9vw,38px);margin-bottom:36px;}
  .stat-grid{gap:12px;}
  .stat-number{font-size:30px;}
  .contact-row{gap:8px;}
  .contact-chip{font-size:11.5px;padding:9px 13px;}
  .case-study{padding:24px 18px;}
  .cs-header{flex-direction:column;}
  .cs-impact-badge{align-self:flex-start;}
  .cs-learnings{grid-template-columns:1fr;}
  .project-card{padding:24px 20px;}
  .project-metrics{gap:14px 18px;}
  .info-grid{grid-template-columns:1fr;}
  .timeline{padding-left:26px;}
  .timeline-item::before{left:-32px;}
  .edu-hero{padding:28px 22px;}
  .nav-item .nav-lbl{display:none;}
  .nav-item{height:44px;}
}
@media(prefers-reduced-motion:reduce){
  *{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important;scroll-behavior:auto !important;}
  .reveal{opacity:1;transform:none;filter:none;}
  .orb,.grid-floor{display:none;}
}
</style>
</head>
<body>

<div class="depth-field" id="depth"><div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div></div>
<div class="grid-floor" id="floor"></div>
<div class="noise"></div>
<div id="toast" role="status" aria-live="polite"></div>
<div id="float-popup"><div class="popup-title" id="fp-title"></div><div id="fp-metrics"></div></div>
<div id="scroll-progress"></div>

<!-- LANGUAGE GATE -->
<div id="lang-overlay">
  <div class="lo-stack">
    <div class="lo-logo">hwinh</div>
    <div class="lo-tagline">AI Portfolio · Product &amp; UX</div>
  </div>
  <div class="lo-question">Choose your language<br><span style="font-size:18px;color:var(--txt2);font-weight:400;">Chọn ngôn ngữ hiển thị</span></div>
  <div class="lo-options">
    <button class="lo-btn" onclick="selectLang('en')">English<span>EN</span></button>
    <button class="lo-btn" onclick="selectLang('vi')">Tiếng Việt<span>VI</span></button>
  </div>
  <div class="lo-kbhint">Press <strong>1–6</strong> to navigate · <strong>Esc</strong> to return · <strong>L</strong> toggle language</div>
</div>

<!-- APP -->
<div class="app" id="main-app">
  <nav class="sidenav" aria-label="Section navigation">
    <div class="nav-logo">HM</div>
    <button class="nav-item active" data-view="welcome" onclick="go('welcome',this)" aria-label="Home"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><span class="nav-lbl" id="nl0">Home</span><span class="nav-tooltip" id="ntt0">Overview</span></button>
    <button class="nav-item" data-view="experience" onclick="go('experience',this)" aria-label="Experience"><svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg><span class="nav-lbl" id="nl1">Career</span><span class="nav-tooltip" id="ntt1">Experience</span></button>
    <button class="nav-item" data-view="projects" onclick="go('projects',this)" aria-label="Projects"><svg viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg><span class="nav-lbl" id="nl2">Work</span><span class="nav-tooltip" id="ntt2">Projects</span></button>
    <button class="nav-item" data-view="ux" onclick="go('ux',this)" aria-label="UX work"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg><span class="nav-lbl" id="nl3">UX</span><span class="nav-tooltip" id="ntt3">UX Work</span></button>
    <button class="nav-item" data-view="skills" onclick="go('skills',this)" aria-label="Skills"><svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg><span class="nav-lbl" id="nl4">Skills</span><span class="nav-tooltip" id="ntt4">Skills</span></button>
    <button class="nav-item" data-view="education" onclick="go('education',this)" aria-label="Education"><svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg><span class="nav-lbl" id="nl5">School</span><span class="nav-tooltip" id="ntt5">Education</span></button>
    <div class="nav-spacer"></div>
    <div class="nav-foot">
      <button class="nav-mini" id="lang-mini" onclick="toggleLang()" aria-label="Toggle language">EN</button>
      <button class="nav-mini" onclick="logout()" aria-label="Back to language gate"><svg viewBox="0 0 24 24"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"/><line x1="12" y1="2" x2="12" y2="12"/></svg></button>
    </div>
  </nav>

  <main class="visual-panel" id="visual-panel">
    <div id="view-welcome" class="view-content">
      <div class="hero-3d" id="hero3d">
        <div class="welcome-eyebrow reveal"><div class="status-dot"></div><span class="status-text" id="w-status"></span></div>
        <h1 class="welcome-name reveal" style="transition-delay:.05s">Nguyễn<span class="accent-word">Hoàng Minh</span></h1>
        <p class="welcome-role reveal" id="w-role" style="transition-delay:.12s"></p>
        <p class="welcome-summary reveal" id="w-summary" style="transition-delay:.18s"></p>
        <div class="scroll-cue reveal" style="transition-delay:.3s"><div class="mouse"></div><span>scroll</span></div>
      </div>
      <div class="contact-row reveal" style="transition-delay:.22s">
        <button class="contact-chip copyable" onclick="copyEmail()" title="Copy email"><svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/></svg> hwinh.work@gmail.com</button>
        <span class="contact-chip"><svg viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg> +84 765 828 191</span>
        <span class="contact-chip"><svg viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg> Hồ Chí Minh</span>
        <span class="contact-chip"><svg viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg> UEH · GPA 3.57/4.0</span>
      </div>
      <div class="stat-grid" id="stat-grid"></div>
      <div class="subtle-div reveal"></div>
      <div class="section-tag reveal" id="w-explore"></div>
      <p class="reveal" style="font-size:14.5px;color:var(--txt2);line-height:1.8;max-width:520px;margin-top:6px;" id="w-hint"></p>
      <div class="kbd-hint-row reveal" style="margin-top:22px;">
        <span id="kbd-nav-hint" style="font-size:12px;font-family:'DM Mono',monospace;color:var(--txt3);"></span>
        <span class="kbd">1</span><span class="kbd">2</span><span class="kbd">3</span><span class="kbd">4</span><span class="kbd">5</span><span class="kbd">6</span>
        <span id="kbd-nav-desc" style="color:var(--txt3);font-size:11px;font-family:'DM Mono',monospace;margin-left:4px;"></span>
      </div>
    </div>

    <div id="view-experience" class="view-content" style="display:none">
      <div class="section-tag reveal" id="e-tag"></div>
      <h2 class="view-title reveal" id="e-title"></h2>
      <div class="timeline" id="e-timeline"></div>
    </div>

    <div id="view-projects" class="view-content" style="display:none">
      <div class="section-tag reveal" id="p-tag"></div>
      <h2 class="view-title reveal" id="p-title"></h2>
      <div class="projects-grid" id="p-grid"></div>
    </div>

    <div id="view-ux" class="view-content" style="display:none">
      <div class="section-tag reveal" id="ux-tag"></div>
      <h2 class="view-title reveal" id="ux-title"></h2>
      <div class="reveal"><div class="proj-chart-title" id="ux-dt-title" style="margin-bottom:22px;"></div><div class="dt-flow" id="ux-dt-flow"></div></div>
      <div id="ux-cases"></div>
    </div>

    <div id="view-skills" class="view-content" style="display:none">
      <div class="section-tag reveal" id="s-tag"></div>
      <h2 class="view-title reveal" id="s-title"></h2>
      <div class="skills-layout">
        <div id="s-list" class="reveal"></div>
        <div class="reveal" style="transition-delay:.1s">
          <div class="skills-chart-wrap"><div class="proj-chart-title" id="s-radar-lbl"></div><div style="height:290px;position:relative;"><canvas id="skillsChart"></canvas></div></div>
          <div class="proj-chart-title" id="s-cert-lbl"></div>
          <div id="s-certs"></div>
        </div>
      </div>
    </div>

    <div id="view-education" class="view-content" style="display:none">
      <div class="section-tag reveal" id="ed-tag"></div>
      <h2 class="view-title reveal" id="ed-title"></h2>
      <div class="edu-hero reveal">
        <div style="font-family:'DM Mono',monospace;font-size:11px;color:var(--violet2);letter-spacing:1px;margin-bottom:15px;">AUG 2022 — AUG 2026</div>
        <h3 style="font-family:'Syne',sans-serif;font-size:27px;font-weight:800;color:var(--txt);margin-bottom:7px;" id="ed-uni"></h3>
        <p style="color:var(--txt2);font-size:15px;margin-bottom:20px;" id="ed-major"></p>
        <div class="gpa-badge"><svg class="gpa-ico" viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg><div><div style="font-size:11px;color:var(--txt2);margin-bottom:3px;">Grade Point Average</div><div class="gpa-val">3.57 / 4.0</div></div></div>
      </div>
      <div id="ed-courses" class="reveal"></div>
      <div class="subtle-div reveal"></div>
      <div class="proj-chart-title reveal" id="ed-cert-lbl"></div>
      <div id="ed-certs" class="reveal"></div>
    </div>
  </main>

  <aside class="chat-panel" aria-label="AI assistant">
    <div class="chat-header">
      <div class="chat-avatar"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg></div>
      <div><div class="chat-name" id="c-name"></div><div class="chat-sub" id="c-sub"><span class="live"></span><span id="c-sub-txt"></span></div></div>
      <div class="chat-actions">
        <button class="chat-btn" onclick="resetChat()" id="c-reset"><svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg><span id="c-reset-txt"></span></button>
      </div>
    </div>
    <div class="chat-messages" id="chat-messages"></div>
    <div class="chat-footer"><div class="prompts-grid" id="prompts-grid"></div></div>
  </aside>
</div>

<script>
/* ICON SET (inline SVG, consistent stroke) */
const IC={
  search:'<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
  target:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
  bulb:'<svg viewBox="0 0 24 24"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V18h6v-1.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2z"/></svg>',
  ruler:'<svg viewBox="0 0 24 24"><path d="M3 17 17 3l4 4L7 21z"/><path d="m7.5 12.5 2 2M11 9l2 2M14.5 5.5l2 2"/></svg>',
  flask:'<svg viewBox="0 0 24 24"><path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7 15h10"/></svg>',
  trend:'<svg viewBox="0 0 24 24"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',
  micro:'<svg viewBox="0 0 24 24"><path d="M3 11v2a9 9 0 0 0 18 0v-2"/><path d="M12 19v3"/><rect x="9" y="2" width="6" height="13" rx="3"/></svg>',
  scope:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/></svg>',
  puzzle:'<svg viewBox="0 0 24 24"><path d="M4 7h3a1.5 1.5 0 1 0 3 0h4v3a1.5 1.5 0 1 0 0 3v4h-4a1.5 1.5 0 1 0-3 0H4v-4a1.5 1.5 0 1 0 0-3z"/></svg>',
  map:'<svg viewBox="0 0 24 24"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg>',
  briefcase:'<svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
  brain:'<svg viewBox="0 0 24 24"><path d="M9 3a3 3 0 0 0-3 3 3 3 0 0 0-1 5.8A3 3 0 0 0 7 17a3 3 0 0 0 5 1 3 3 0 0 0 5-1 3 3 0 0 0 2-5.2A3 3 0 0 0 18 6a3 3 0 0 0-3-3 3 3 0 0 0-3 1.5A3 3 0 0 0 9 3z"/></svg>',
  palette:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="9.5" r="1"/><circle cx="15.5" cy="9.5" r="1"/><circle cx="9" cy="15" r="1"/></svg>',
  bolt:'<svg viewBox="0 0 24 24"><polygon points="13 2 4 14 11 14 10 22 20 9 13 9 13 2"/></svg>',
  arrow:'<svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/></svg>',
  warn:'<svg viewBox="0 0 24 24"><path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12" y2="17"/></svg>'
};
const CERTIC=IC.target; // placeholder not used

// ================= DATA =================
const T = {
en: {
  nav: ['Home','Career','Work','UX','Skills','School'],
  navTip: ['Overview','Experience','Projects','UX Work','Skills','Education'],
  kbdNavHint: 'Quick navigate:',
  kbdNavDesc: '→ Home / Career / Work / UX / Skills / School',
  w: {
    status: 'Available for Product & UX opportunities · HCMC, Vietnam',
    role: 'Product Owner · UX Strategist · AI Builder',
    summary: `Young professional in <strong>Technology &amp; Innovation Management</strong> — operating at the intersection of UX Design, Systems Thinking, and AI. I specialize in turning complex user data and behavioral pain points into seamless, measurable digital experiences. I believe the best products emerge when deep empathy meets rigorous execution.`,
    stats: ['Years Exp.','Stakeholders Managed','AI Tech. KPI','City-level Finalist'],
    statVals:['+1','150+','72%','Top 20'],
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
      { id: 'echomind', badge: 'Flagship AI Project', bClass: 'badge-featured', date: 'Sep — Dec 2025',
        name: 'EchoMind AI', sub: 'Non-Invasive Brain-to-Text System · Project Lead · MindConnect Labs · UEH',
        desc: `EchoMind addresses a profound human challenge: empowering patients with locked-in syndrome to communicate. Traditional AAC devices are slow (25–30 WPM), laggy, and have low session success rates.\n\nAs <strong>Project Lead</strong>, I managed the full AI lifecycle via <strong>CPMAI 6-phase framework</strong> across 8 Agile Sprints. When our baseline LSTM suffered Mode Collapse, I pivoted to <strong>Transformer V2</strong>. We applied Int8 Quantization for CPU inference, and built an Expert Dashboard with Attention Maps for Explainable AI.\n\nFinal results: <strong>55–65 WPM, &lt;1s latency, 72% Technical KPI</strong> vs traditional AAC.`,
        info: [{l:'Final Architecture',v:'Transformer V2 · 8-head MHA · Positional Encoding · Label Smoothing ε=0.1'},{l:'Baseline vs Final',v:'Seq2Seq LSTM (Mode Collapse, WER ~85–90%) → Transformer V2 (6–7/10 correct)'},{l:'Dataset',v:'Brain-to-Text \'25 (Kaggle) · 256-ch EEG · HDF5 · 6.38 words/sentence'},{l:'PM Framework',v:'CPMAI 6-phase · 8 Sprints · RACI Matrix · 3,833.5 hrs · 100% milestones'}],
        metrics: [{v:'55–65',l:'WPM Output'},{v:'<1s',l:'Latency'},{v:'72%',l:'Technical KPI'},{v:'92–95%',l:'Accuracy'},{v:'6–7/10',l:'Sentences OK'},{v:'100%',l:'Milestone'}],
        tech: ['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','RACI Matrix','Agile/Scrum'] },
      { id: 'ereader', badge: 'Top 20 Finalist', bClass: 'badge-top20', date: 'Mar — Jun 2025',
        name: 'E-Reader Ecosystem', sub: "User Researcher · HCMC Digital Education · HCMC People's Committee",
        desc: `A Top 20 City-level initiative to design a digital education ecosystem for student e-reading devices. Applied <strong>HCI principles</strong> to map the complete user journey, decomposed pain points causing cognitive overload, and translated observations into actionable User Stories with clear success criteria.`,
        tech: ['HCI Principles','UX Design','Journey Mapping','Problem Decomposition','User Stories','Cognitive Load Analysis','Figma'] },
      { id: 'events', badge: 'Ongoing', bClass: 'badge-active', date: 'Jul 2024 — Present',
        name: 'Innovation Events Operations', sub: 'Operations · SIHUB Startup Ecosystem · HCMC',
        desc: `Managed end-to-end operations for <strong>Univ.Star 2024 & 2025</strong> and <strong>WHISE Week 2024</strong>. Coordinated cross-functional teams and facilitated real-time communication between startup founders, investors, and government representatives.`,
        tech: ['Event Management','Cross-team Coordination','Stakeholder Communication','Operations Planning'] }
    ]
  },
  ux: {
    tag: 'Design Process', title: 'UX <span>Experience</span>',
    dtTitle: 'My Design Thinking Framework',
    phases: [
      { ic:'search', num: '01', name: 'Empathize', desc: 'User research, interviews, behavioral observation to discover hidden pain points' },
      { ic:'target', num: '02', name: 'Define', desc: 'Problem framing, How Might We questions, identifying root causes from data' },
      { ic:'bulb', num: '03', name: 'Ideate', desc: 'Brainstorming, user story mapping, prioritization via MoSCoW framework' },
      { ic:'ruler', num: '04', name: 'Prototype', desc: 'Wireframes, low-fi flows, journey maps, interactive Figma mockups' },
      { ic:'flask', num: '05', name: 'Test & Validate', desc: 'A/B testing, Interleaving experiments, usability heuristic evaluation' },
      { ic:'trend', num: '06', name: 'Measure Impact', desc: 'NPS tracking, conversion metrics, retention analysis, business KPIs' }
    ],
    cases: [
      { cls: 'cs-sihub', num: 'Case Study 01', ctag: 'Customer Journey · Activation UX',
        title: 'SIHUB Startup Onboarding Redesign', role: 'Project Management Executive · Journey Mapping Lead',
        impactNum: '30%', impactLbl: 'Friction Reduction', problemLabel: 'Problem Statement',
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
        abVariants: [{ lbl: 'Control', pct: 42, cls: 'control', badge: '' },{ lbl: 'Variant A', pct: 68, cls: 'winner', badge: 'Winner' }],
        abStat: 'Significance: 95% confidence · Sample: 312 startup founders · Duration: 6 weeks',
        journeyTitle: 'Journey Map — Critical Stages',
        journeyStages: ['Receive Invite','Register Portal','Upload Docs','Verification','Activation'],
        journeyRows: [
          { label: 'Expectation', cells: ['Quick process','Simple form','Clear checklist','Auto-review','Instant access'], types: ['','','','',''] },
          { label: 'Pain Point', cells: ['Long email','Confusing UI','Unclear format req.','3-day wait','Login issues'], types: ['','','pain high','pain','pain'] },
          { label: 'Emotion', cells: ['Neutral','Calm','Frustrated','Bored','Worried'], types: ['emotion-mid','emotion-high','emotion-low','emotion-mid','emotion-low'] },
          { label: 'Solution', cells: ['—','Simplified nav','Inline doc guide','Progress tracker','SSO login'], types: ['','','solution','solution','solution'] }
        ],
        beforeAfterTitle: 'Business Impact — Before vs After',
        before: [{ n: 'Activation Rate', v: '42%' },{ n: 'Avg. Drop-off Point', v: 'Step 3' },{ n: 'NPS Score', v: '28' },{ n: 'Support Tickets', v: '~40/week' }],
        after: [{ n: 'Activation Rate', v: '68%' },{ n: 'Avg. Drop-off Point', v: 'Step 5' },{ n: 'NPS Score', v: '47' },{ n: 'Support Tickets', v: '~12/week' }],
        learnings: [
          { ic:'flask', title: 'Research First', text: 'Behavioral data revealed the true drop-off point, not where stakeholders assumed it was.' },
          { ic:'flask', title: 'Validate Before Shipping', text: 'A/B testing prevented a full redesign — the minimal inline guidance change had outsized impact.' },
          { ic:'trend', title: 'Reframe NPS', text: 'NPS as a signal system, not a score — each stage has its own micro-NPS driver.' }
        ]
      },
      { cls: 'cs-echomind', num: 'Case Study 02', ctag: 'AI Product UX · Expert Dashboard Design',
        title: 'EchoMind: Designing the Output Interface', role: 'Project Lead · UI/UX Thinker · Gradio Demo Designer',
        impactNum: '100%', impactLbl: 'Milestones Done', problemLabel: 'Context & Challenge',
        problem: `EchoMind is a university AI project built on the <strong>Brain-to-Text 2025 dataset (Kaggle)</strong> — we trained a model to decode non-invasive EEG signals into text. Once the model was working, we faced a UX question: <strong>how do we show the output in a way that actually makes sense to someone reviewing it?</strong> A raw text output with no context tells you nothing — you can't tell if the model was confident, which part of the brain it read, or whether the signal was clean.`,
        approachTitle: 'How We Thought About It',
        steps: [
          { n:'01', t:'Start with the demo interface', d:"We built the first version in Gradio — just the model output as plain text plus a confidence score. When we reviewed it ourselves, we realised it felt like a black box. If we couldn't trust it, nobody else would." },
          { n:'02', t:'Apply HCI heuristics to the prototype', d:"I ran Nielsen's 10 Usability Heuristics against our V1 Gradio demo. Found two real problems: the interface gave no indication it was processing, and there was no way to flag when the signal quality was low." },
          { n:'03', t:'Think through what an expert would need', d:"If this model were used by a clinician in future, what would they actually need to see? We mapped out the questions: What did the model decode? How sure is it? Which brain region did it focus on? That framing drove the V2 design." },
          { n:'04', t:'Design the Attention Map layer', d:"The most meaningful addition was showing WHICH part of the EEG waveform the model paid attention to for each decoded word — visualised as a colour overlay. This turns a black box into something you can reason about." }
        ],
        insightLabel: 'Key Realisation',
        insight: `The model result alone means almost nothing without context. <strong>A 93% accuracy number tells you it works — the attention map shows you WHY it works.</strong> Designing for explainability from the start, even in a prototype, forces you to think about the output from the user's perspective, not just the engineer's.`,
        abTitle: 'Interface Comparison — Team Heuristic Review',
        abVariants: [{ lbl: 'V1 — Plain output', pct: 38, cls: 'control', badge: '' },{ lbl: 'V2 — Attention Map', pct: 82, cls: 'winner', badge: 'Final version' }],
        abStat: "Scored using Nielsen's 10 Heuristics by 4 team members · Scale 0–100 · Not a clinical study",
        journeyTitle: 'Thinking Through the User Flow',
        journeyStages: ['See output','Check confidence','Understand why','Review signal','Draw conclusion'],
        journeyRows: [
          { label: 'What user wants', cells: ['What was decoded?','Is it reliable?','How did it decide?','Was signal clean?','Can I trust this?'], types: ['','','','',''] },
          { label: 'V1 gap', cells: ['Text only','% no context','Nothing shown','Raw chart','Unclear'], types: ['','','pain high','pain','pain'] },
          { label: 'V2 added', cells: ['Text + waveform','% + signal quality','Attention overlay','Highlighted region','Much clearer'], types: ['solution','solution','solution','solution','solution'] },
          { label: 'Clarity', cells: ['Neutral','Neutral','Clear','Clear','Clear'], types: ['emotion-mid','emotion-mid','emotion-high','emotion-high','emotion-high'] }
        ],
        beforeAfterTitle: 'V1 vs V2 — What Changed',
        before: [{ n: 'Heuristic Score', v: '38/100' },{ n: 'Shows reasoning', v: 'No' },{ n: 'Signal quality info', v: 'None' },{ n: 'Error feedback', v: 'None' }],
        after: [{ n: 'Heuristic Score', v: '82/100' },{ n: 'Shows reasoning', v: 'Attention map' },{ n: 'Signal quality info', v: 'Visible' },{ n: 'Error feedback', v: 'Shown clearly' }],
        learnings: [
          { ic:'scope', title: 'Design the output', text: 'Even for a research project, how you present the result matters. A well-designed output is what makes the model feel trustworthy, not just accurate.' },
          { ic:'puzzle', title: 'Heuristics on prototypes', text: 'Running a quick heuristic review on our own Gradio demo caught problems we had completely normalised. Takes 30 minutes, saves a lot of confusion.' },
          { ic:'map', title: 'Think about the user', text: "This was a student project — no real users. But thinking through who would use this and what they would need shaped better design decisions throughout." }
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
      {n:'Google Project Management',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {n:'Google Business Intelligence',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {n:'Agile Management Certification',org:'Professional Certification'}
    ]
  },
  edu: {
    tag: 'Academic Background', title: 'Education & <span>Awards</span>',
    uni: 'University of Economics HCMC (UEH)', major: 'Bachelor of Technology & Innovation Management',
    courseTag: 'Relevant Coursework',
    courses: ['Design Thinking','Human-Computer Interaction (HCI)','Innovation Management','Business Intelligence','Digital Business Transformation','Project AI'],
    certTag: 'Certifications',
    certs: [
      {n:'Google Project Management',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {n:'Google Business Intelligence',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {n:'Agile Management Certification',org:'Professional Certification'}
    ]
  },
  chat: {
    name: "Minh's AI Assistant", sub: 'Online · Ready to answer', reset: 'Reset',
    greeting: `Hey there! I'm an AI assistant here to tell you about Nguyen Hoang Minh — he's a final-year student at UEH who's been doing real product and UX work at SIHUB, one of Ho Chi Minh City's main startup hubs, for the past couple of years.\n\nHe's the kind of person who doesn't just map user journeys on paper — he actually runs A/B tests, tracks NPS stage by stage, and led a 7-person AI project from scratch. What do you want to know about him?`,
    prompts: [{id:'exp',ic:'briefcase',l:'Experience'},{id:'proj',ic:'brain',l:'Projects'},{id:'ux',ic:'palette',l:'UX Work'},{id:'skills',ic:'bolt',l:'Skills'}],
    ans: {
      exp: `Minh has been at SIHUB — that's the Startup & Innovation Hub under the HCMC Department of Science & Technology — since mid-2024.\n\nIn his most recent role as Project Management Executive (Jan–Oct 2025), he was the main point of contact for 150+ startup founders going through the incubation program. He designed their onboarding journeys end-to-end and ran A/B tests to validate every change. One of the things he's proud of: he helped the team stop treating NPS as just a number and start treating it as a signal — something that tells you exactly where in the journey things are going wrong.\n\nBefore that, as an R&D Intern, he handled a large-scale competency gap analysis — gathering data from government officials, research institutes, and companies — and turned all that qualitative mess into structured URD documentation.`,
      proj: `Sure! Minh has three projects worth knowing about:\n\nEchoMind AI — his flagship project (Sep–Dec 2025). This was a university AI project where his team trained a model to decode brainwave signals into text, using the Brain-to-Text 2025 dataset from Kaggle. Minh was the Project Lead — he ran 8 Agile sprints, and when their first model (an LSTM) kept breaking down, he diagnosed the problem and made the call to switch to a Transformer architecture. The model ended up hitting 55–65 words per minute with under 1 second of latency. He also designed the output interface so people could actually understand what the model was doing.\n\nE-Reader Ecosystem — a city-level project (Mar–Jun 2025) where he did user research for a student e-reading platform. He mapped the setup journey, found where students were dropping off, and used HCI principles to simplify it. The project made it to the Top 20 at an HCMC People's Committee competition.\n\nInnovation Events — ongoing work organizing major startup events like Univ.Star 2024/2025 and WHISE Week 2024 at SIHUB.`,
      ux: `The UX section has two case studies that show how Minh thinks through design problems — not just the output, but the whole process.\n\nCase 01 is about the SIHUB onboarding flow. Only 42% of startup founders were completing the activation journey. He dug into the data, ran a journey mapping workshop, found the real drop-off point (it was a document upload step with unclear requirements), and tested a fix via A/B experiment. Result: 68% activation, NPS jumped from 28 to 47, support tickets dropped by about 70%.\n\nCase 02 is the EchoMind dashboard — how do you show AI output in a way that actually makes sense? His team built a demo in Gradio and it felt like a black box. He used Nielsen's heuristics to audit it, then added an attention map layer so you could see which part of the brainwave the model was reading. Heuristic score went from 38 to 82 out of 100.`,
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
    summary: `Chuyên gia trẻ về <strong>Quản lý Công nghệ &amp; Đổi mới Sáng tạo</strong> — xây dựng sản phẩm tại giao điểm của UX Design, Tư duy Hệ thống và AI. Tôi chuyển hóa dữ liệu người dùng phức tạp và "nỗi đau" thành các sản phẩm liền mạch, đo lường được và đáp ứng đúng nhu cầu người dùng.`,
    stats: ['Năm kinh nghiệm','Stakeholders quản lý','KPI kỹ thuật AI','Chung cuộc cấp TP'],
    statVals:['+1','150+','72%','Top 20'],
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
      { id: 'echomind', badge: 'Dự án AI Trọng điểm', bClass: 'badge-featured', date: 'Tháng 9 — 12/2025',
        name: 'EchoMind AI', sub: 'Hệ thống Não-Chữ Phi Xâm Lấn · Project Lead · MindConnect Labs · UEH',
        desc: `Khởi nguồn từ bài toán nhân văn: giúp bệnh nhân hội chứng khóa trong giao tiếp qua sóng não. Thiết bị AAC truyền thống chậm (25–30 WPM), độ trễ cao.\n\nVới vai trò <strong>Project Lead</strong>, tôi quản lý theo <strong>khung CPMAI 6 pha</strong> và 8 Agile Sprints. Khi LSTM gặp Mode Collapse, tôi pivot sang <strong>Transformer V2</strong>. Áp dụng Int8 Quantization, thiết kế Expert Dashboard với Attention Maps cho Explainable AI y tế.\n\nKết quả: <strong>55–65 WPM, &lt;1s, KPI kỹ thuật 72%</strong>.`,
        info: [{l:'Kiến trúc cuối',v:'Transformer V2 · 8-head MHA · Positional Encoding · Label Smoothing ε=0.1'},{l:'Baseline vs Cuối',v:'Seq2Seq LSTM (Mode Collapse) → Transformer V2 (6–7/10 đúng)'},{l:'Bộ dữ liệu',v:'Brain-to-Text \'25 (Kaggle) · EEG 256 kênh · HDF5 · 6,38 từ/câu'},{l:'Khung quản lý',v:'CPMAI 6 pha · 8 Sprints · RACI · 3.833,5 giờ · 100% milestones'}],
        metrics: [{v:'55–65',l:'Từ/phút'},{v:'<1s',l:'Độ trễ'},{v:'72%',l:'KPI kỹ thuật'},{v:'92–95%',l:'Độ chính xác'},{v:'6–7/10',l:'Câu đúng'},{v:'100%',l:'Milestone'}],
        tech: ['Python','PyTorch','Transformer','Multi-Head Attention','Label Smoothing','WER Metric','Google Colab','Gradio Demo','Figma UI','CPMAI','Ma trận RACI','Agile/Scrum'] },
      { id: 'ereader', badge: 'Top 20 Chung cuộc', bClass: 'badge-top20', date: 'Tháng 3 — 6/2025',
        name: 'Hệ sinh thái E-Reader', sub: "User Researcher · Giáo dục Số TP.HCM · UBND TP.HCM",
        desc: `Dự án hệ sinh thái giáo dục số. Áp dụng <strong>nguyên lý HCI</strong> lập bản đồ hành trình đầy đủ, phân tích cognitive overload, chuyển thành User Stories có tiêu chí đo lường. Lọt <strong>Top 20 Chung cuộc</strong> cuộc thi UBND TP.HCM.`,
        tech: ['Nguyên tắc HCI','Thiết kế UX','Journey Mapping','Phân tích Pain Point','User Stories','Phân tích Cognitive Load','Figma'] },
      { id: 'events', badge: 'Đang diễn ra', bClass: 'badge-active', date: 'Tháng 7/2024 — Hiện tại',
        name: 'Vận hành Sự kiện ĐMST', sub: 'Vận hành · Hệ sinh thái Startup SIHUB · TP.HCM',
        desc: `Tổ chức và điều phối <strong>Univ.Star 2024 & 2025</strong> và <strong>Tuần lễ WHISE 2024</strong>. Phối hợp cross-team, giao tiếp liên tục với founders, nhà đầu tư và chính quyền.`,
        tech: ['Quản lý Sự kiện','Phối hợp Cross-team','Giao tiếp Stakeholder','Lập kế hoạch Vận hành'] }
    ]
  },
  ux: {
    tag: 'Quy trình Thiết kế', title: 'Kinh nghiệm <span>UX</span>',
    dtTitle: 'Khung Tư duy Thiết kế của Tôi',
    phases: [
      { ic:'search', num: '01', name: 'Thấu Cảm', desc: 'Tìm hiểu người dùng qua phỏng vấn, quan sát hành vi và dữ liệu thực tế — để khám phá những gì họ thực sự đang gặp khó.' },
      { ic:'target', num: '02', name: 'Định Nghĩa', desc: 'Đặt lại vấn đề theo góc nhìn người dùng. Dùng "How Might We" và tìm nguyên nhân gốc rễ thay vì chữa triệu chứng.' },
      { ic:'bulb', num: '03', name: 'Lên Ý tưởng', desc: 'Brainstorm không giới hạn, lọc qua user story mapping và khung MoSCoW để chọn giải pháp đáng thử nghiệm nhất.' },
      { ic:'ruler', num: '04', name: 'Tạo Nguyên mẫu', desc: 'Hiện thực hóa ý tưởng thành wireframes, luồng low-fi và journey maps — đủ cụ thể để kiểm thử.' },
      { ic:'flask', num: '05', name: 'Kiểm Thử', desc: 'Dùng A/B testing, Interleaving và đánh giá heuristic để kiểm chứng. Mọi thay đổi phải có dữ liệu.' },
      { ic:'trend', num: '06', name: 'Đo Tác Động', desc: 'Theo dõi NPS theo từng bước hành trình, tỷ lệ chuyển đổi và chỉ số giữ chân để biết giải pháp có hiệu quả thật.' }
    ],
    cases: [
      { cls: 'cs-sihub', num: 'Case Study 01', ctag: 'Customer Journey · Activation UX',
        title: 'SIHUB: Tái thiết kế Onboarding Startup', role: 'Project Management Executive · Journey Mapping Lead',
        impactNum: '30%', impactLbl: 'Giảm Friction', problemLabel: 'Vấn đề Đặt ra',
        problem: `Trong giai đoạn đầu của chương trình ươm tạo SIHUB, nhiều startup bỏ cuộc ngay từ bước kích hoạt tài khoản. <strong>Chỉ khoảng 40% hoàn tất được luồng onboarding</strong> — kéo theo tỷ lệ tham gia thấp, người dùng không hài lòng và điểm NPS sụt giảm. Vấn đề là đội ngũ lúc đó chỉ nhìn vào một con số NPS chung chung, chứ không biết cụ thể chỗ nào trong hành trình đang làm người dùng bỏ cuộc.`,
        approachTitle: 'Cách Tiếp Cận',
        steps: [
          { n:'01', t:'Audit dữ liệu hành vi', d:'Tôi thu thập dữ liệu từ nhiều kênh để lập lại hành trình thực tế. Kết quả cho thấy 3 điểm thoát chính, tập trung ở bước upload tài liệu và xác minh.' },
          { n:'02', t:'Workshop Journey Mapping', d:'Tổ chức workshop cùng nhân viên SIHUB và phỏng vấn trực tiếp 5 founder. Ghi lại cảm xúc, kỳ vọng và điểm đau ở từng bước.' },
          { n:'03', t:'Phân tích nguyên nhân gốc', d:'Áp dụng 5 Whys. Vấn đề không phải form phức tạp — mà là yêu cầu tài liệu không rõ, khiến người dùng thử một lần, bị từ chối, rồi không quay lại.' },
          { n:'04', t:'Thiết kế thử nghiệm A/B', d:'Thiết kế Variant A bổ sung hướng dẫn inline (progressive disclosure) so với Control là form gốc. Dùng Interleaving để so sánh công bằng.' }
        ],
        insightLabel: 'Insight Cốt Lõi',
        insight: `Vấn đề không nằm ở công nghệ. <strong>Điểm nghẽn nằm đúng ở bước 3 — yêu cầu định dạng tài liệu</strong>. Founder không biết cần nộp file gì, thử một lần bị từ chối, rồi bỏ luôn. Chỉ thêm một dòng hướng dẫn ngay tại chỗ đã xử lý được 60% tỷ lệ rời bỏ.`,
        abTitle: 'Kết quả Thử nghiệm A/B',
        abVariants: [{ lbl: 'Control', pct: 42, cls: 'control', badge: '' },{ lbl: 'Variant A', pct: 68, cls: 'winner', badge: 'Chiến thắng' }],
        abStat: 'Độ tin cậy: 95% · Mẫu: 312 startup founders · Thời gian: 6 tuần',
        journeyTitle: 'Journey Map — Các Giai đoạn Quan trọng',
        journeyStages: ['Nhận lời mời','Đăng ký Portal','Upload Tài liệu','Xác minh','Kích hoạt'],
        journeyRows: [
          { label: 'Kỳ vọng', cells: ['Quy trình nhanh','Form đơn giản','Checklist rõ ràng','Auto-review','Truy cập ngay'], types: ['','','','',''] },
          { label: 'Pain Point', cells: ['Email dài','UI khó hiểu','Format không rõ','Chờ 3 ngày','Lỗi đăng nhập'], types: ['','','pain high','pain','pain'] },
          { label: 'Cảm xúc', cells: ['Bình thường','Tạm ổn','Bực bội','Chán','Lo lắng'], types: ['emotion-mid','emotion-high','emotion-low','emotion-mid','emotion-low'] },
          { label: 'Giải pháp', cells: ['—','Nav đơn giản hóa','Hướng dẫn inline','Thanh tiến trình','SSO đăng nhập'], types: ['','','solution','solution','solution'] }
        ],
        beforeAfterTitle: 'Tác động Kinh doanh — Trước vs Sau',
        before: [{ n: 'Tỷ lệ Kích hoạt', v: '42%' },{ n: 'Điểm Thoát TB', v: 'Bước 3' },{ n: 'Điểm NPS', v: '28' },{ n: 'Support Tickets', v: '~40/tuần' }],
        after: [{ n: 'Tỷ lệ Kích hoạt', v: '68%' },{ n: 'Điểm Thoát TB', v: 'Bước 5' },{ n: 'Điểm NPS', v: '47' },{ n: 'Support Tickets', v: '~12/tuần' }],
        learnings: [
          { ic:'flask', title: 'Research trước', text: 'Dữ liệu hành vi chỉ ra điểm thoát thực sự là bước 3 — trong khi các bên đều đoán bước 1 hoặc 2.' },
          { ic:'flask', title: 'Kiểm thử trước khi triển khai', text: 'Nhờ A/B testing, không phải làm lại toàn bộ giao diện. Một thay đổi nhỏ tạo tác động lớn.' },
          { ic:'trend', title: 'NPS không phải một con số', text: 'Mỗi bước có điểm đau riêng và NPS driver riêng. Đọc NPS theo từng giai đoạn mới thấy gốc vấn đề.' }
        ]
      },
      { cls: 'cs-echomind', num: 'Case Study 02', ctag: 'AI Project UX · Thiết kế Giao diện Đầu ra',
        title: 'EchoMind: Thiết kế Giao diện Hiển thị Kết quả AI', role: 'Project Lead · Người thiết kế giao diện Gradio Demo',
        impactNum: '100%', impactLbl: 'Milestone Hoàn thành', problemLabel: 'Bối cảnh & Vấn đề',
        problem: `EchoMind là dự án AI của nhóm sinh viên, xây dựng trên <strong>bộ dữ liệu Brain-to-Text 2025 (Kaggle)</strong> — nhóm huấn luyện mô hình giải mã tín hiệu sóng não EEG phi xâm lấn thành văn bản. Khi mô hình đã chạy, câu hỏi tiếp theo là: <strong>hiển thị kết quả như thế nào để người xem thực sự hiểu được?</strong> Chỉ in ra một dòng văn bản với một con số phần trăm là không đủ.`,
        approachTitle: 'Nhóm Tiếp Cận Thế Nào',
        steps: [
          { n:'01', t:'Xây bản demo V1 bằng Gradio', d:"Phiên bản đầu chỉ hiển thị văn bản giải mã và con số độ tin cậy. Khi cả nhóm tự dùng thử, ai cũng thấy nó như một hộp đen." },
          { n:'02', t:'Đánh giá bằng 10 Heuristics Nielsen', d:"Tôi chạy đánh giá heuristic trên chính prototype V1. Phát hiện hai vấn đề: giao diện không cho biết đang xử lý, và không phát hiện được khi tín hiệu kém." },
          { n:'03', t:'Người dùng cần biết gì?', d:"Nếu công cụ được dùng thực tế, người review cần biết: mô hình giải mã ra gì, tự tin tới đâu, dựa vào phần nào của EEG. Ba câu hỏi đó định hướng V2." },
          { n:'04', t:'Thiết kế lớp Attention Map', d:"Thay đổi ý nghĩa nhất là thêm lớp highlight lên dạng sóng EEG — cho thấy phần nào tín hiệu mà mô hình chú ý khi giải mã từng từ. Biến hộp đen thành thứ lý giải được." }
        ],
        insightLabel: 'Điều Nhóm Nhận Ra',
        insight: `Kết quả mô hình đứng một mình thì ít giá trị. <strong>Con số 93% accuracy cho biết nó hoạt động — attention map cho thấy vì sao nó hoạt động.</strong> Nghĩ đến cách trình bày đầu ra từ góc độ người xem làm cả sản phẩm thuyết phục hơn hẳn.`,
        abTitle: 'So sánh V1 vs V2 — Đánh giá của nhóm',
        abVariants: [{ lbl: 'V1 — Chỉ text + %', pct: 38, cls: 'control', badge: '' },{ lbl: 'V2 — Attention Map', pct: 82, cls: 'winner', badge: 'Phiên bản cuối' }],
        abStat: "Đánh giá theo 10 Heuristics Nielsen · 4 thành viên cho điểm · Thang 0–100 · Không phải nghiên cứu lâm sàng",
        journeyTitle: 'Luồng suy nghĩ khi thiết kế giao diện',
        journeyStages: ['Xem kết quả','Kiểm tra độ tin cậy','Hiểu lý do','Đọc tín hiệu','Kết luận'],
        journeyRows: [
          { label: 'Người dùng cần', cells: ['Đọc được gì?','Có chắc không?','Dựa vào đâu?','Tín hiệu sạch?','Tin được không?'], types: ['','','','',''] },
          { label: 'V1 thiếu', cells: ['Chỉ có text','% không ngữ cảnh','Không hiển thị','Biểu đồ thô','Không rõ'], types: ['','','pain high','pain','pain'] },
          { label: 'V2 bổ sung', cells: ['Text + waveform','% + chất lượng','Attention overlay','Vùng highlight','Rõ hơn nhiều'], types: ['solution','solution','solution','solution','solution'] },
          { label: 'Độ rõ ràng', cells: ['Bình thường','Bình thường','Rõ','Rõ','Rõ'], types: ['emotion-mid','emotion-mid','emotion-high','emotion-high','emotion-high'] }
        ],
        beforeAfterTitle: 'V1 vs V2 — Điều thay đổi',
        before: [{ n: 'Điểm Heuristic', v: '38/100' },{ n: 'Giải thích được', v: 'Không' },{ n: 'Thông tin tín hiệu', v: 'Không có' },{ n: 'Phản hồi lỗi', v: 'Không có' }],
        after: [{ n: 'Điểm Heuristic', v: '82/100' },{ n: 'Giải thích được', v: 'Attention map' },{ n: 'Thông tin tín hiệu', v: 'Hiển thị rõ' },{ n: 'Phản hồi lỗi', v: 'Có thông báo' }],
        learnings: [
          { ic:'scope', title: 'Thiết kế đầu ra', text: 'Ngay cả trong dự án nghiên cứu, cách trình bày kết quả quan trọng không kém độ chính xác. Giao diện tốt làm mô hình đáng tin.' },
          { ic:'puzzle', title: 'Heuristics trên prototype', text: 'Chạy heuristic trên chính demo của nhóm mất 30 phút nhưng phát hiện vấn đề mà cả nhóm đã quen mắt.' },
          { ic:'map', title: 'Nghĩ về người dùng', text: "Dự án sinh viên không có người dùng thật. Nhưng hỏi ai sẽ dùng và họ cần gì giúp ra quyết định thiết kế tốt hơn." }
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
      {n:'Quản lý Dự án (Google PM)',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp'}
    ]
  },
  edu: {
    tag: 'Nền tảng Học vấn', title: 'Học vấn & <span>Thành tích</span>',
    uni: 'Đại học Kinh tế TP.HCM (UEH)', major: 'Cử nhân Quản lý Công nghệ và Đổi mới Sáng tạo',
    courseTag: 'Các môn học Cốt lõi định hình Tư duy Sản phẩm',
    courses: ['Tư duy Thiết kế','Tương tác Người-Máy (HCI)','Quản trị ĐMST','Trí tuệ Doanh nghiệp','Chuyển đổi Kinh doanh Số','Dự án AI'],
    certTag: 'Chứng chỉ',
    certs: [
      {n:'Quản lý Dự án (Google PM)',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/certificate/695T8LGAXCX2'},
      {n:'Trí tuệ Doanh nghiệp (Google BI)',org:'Coursera · Google',link:'https://www.coursera.org/account/accomplishments/specialization/certificate/BD9KAWKMEKXD'},
      {n:'Quản trị Agile',org:'Chứng nhận Chuyên nghiệp'}
    ]
  },
  chat: {
    name: 'Trợ lý AI của Minh', sub: 'Trực tuyến · Sẵn sàng', reset: 'Làm lại',
    greeting: `Xin chào! Tôi là AI assistant ở đây để giới thiệu về Nguyễn Hoàng Minh — sinh viên năm cuối UEH, đang làm Product & UX thực chiến tại SIHUB, một trong những trung tâm hỗ trợ startup lớn nhất TP.HCM, từ giữa năm 2024.\n\nMinh không chỉ vẽ journey map trên giấy — anh ấy chạy A/B test thực tế, theo dõi NPS từng bước, và vừa dẫn dắt nhóm 7 người xây dựng dự án AI từ đầu. Bạn muốn tìm hiểu phần nào?`,
    prompts: [{id:'exp',ic:'briefcase',l:'Kinh nghiệm'},{id:'proj',ic:'brain',l:'Dự án'},{id:'ux',ic:'palette',l:'UX Work'},{id:'skills',ic:'bolt',l:'Kỹ năng'}],
    ans: {
      exp: `Minh làm việc tại SIHUB — Trung tâm Hỗ trợ Khởi nghiệp & ĐMST trực thuộc Sở KH&CN TP.HCM — từ giữa năm 2024.\n\nVị trí gần nhất là Chuyên viên Quản lý Dự án (01–10/2025). Minh là đầu mối làm việc trực tiếp với hơn 150 startup founder trong chương trình ươm tạo — thiết kế hành trình onboarding từ đầu đến cuối, rồi chạy A/B test để kiểm chứng từng thay đổi. Một điều Minh tự hào: thuyết phục được đội ngũ không nhìn NPS như một con số, mà như một tín hiệu — để biết chính xác chỗ nào trong hành trình đang có vấn đề.\n\nTrước đó, khi còn là Thực tập sinh R&D (07–12/2024), Minh xử lý dự án phân tích khoảng trống năng lực quy mô lớn, rồi tổng hợp tất cả thành tài liệu yêu cầu hệ thống theo chuẩn URD.`,
      proj: `Minh có ba dự án đáng chú ý:\n\nEchoMind AI là dự án lớn nhất (09–12/2025). Đây là dự án AI của nhóm sinh viên, train mô hình giải mã tín hiệu sóng não thành văn bản bằng bộ dữ liệu Brain-to-Text 2025 từ Kaggle. Minh là Project Lead — chạy 8 Agile sprint, khi mô hình LSTM đầu tiên sập vào Mode Collapse thì Minh chẩn đoán và quyết định chuyển sang kiến trúc Transformer. Cuối cùng mô hình đạt 55–65 từ/phút, độ trễ dưới 1 giây. Minh còn thiết kế giao diện Gradio demo để kết quả AI hiển thị dễ hiểu.\n\nHệ sinh thái E-Reader (03–06/2025) là dự án nghiên cứu người dùng cho nền tảng đọc sách điện tử cho học sinh. Minh lập bản đồ hành trình cài đặt, tìm ra chỗ học sinh bỏ cuộc, rồi dùng HCI để đơn giản hóa luồng. Dự án vào Top 20 cuộc thi UBND TP.HCM.\n\nVận hành Sự kiện ĐMST — công việc đang diễn ra, tổ chức Univ.Star 2024/2025 và WHISE Week 2024 tại SIHUB.`,
      ux: `Phần UX có 2 case study, mỗi cái kể lại một câu chuyện thiết kế thực tế.\n\nCase 01 là hành trình onboarding của startup tại SIHUB. Chỉ 42% founder hoàn tất luồng kích hoạt. Minh đào vào dữ liệu, tổ chức workshop journey mapping, tìm ra điểm thoát thực sự là bước upload tài liệu (yêu cầu không rõ), rồi test một cách sửa nhỏ qua A/B. Kết quả: kích hoạt lên 68%, NPS tăng 28 lên 47, support tickets giảm ~70%.\n\nCase 02 là giao diện demo của EchoMind. Khi xây xong mô hình, nhóm làm demo bằng Gradio — và nó như hộp đen. Minh đánh giá lại bằng 10 Heuristics Nielsen rồi thêm lớp attention map để người xem thấy mô hình đang đọc phần nào của sóng não. Điểm heuristic tăng từ 38 lên 82/100.`,
      skills: `Thế mạnh lõi của Minh là product và UX — lập bản đồ hành trình, chạy A/B test, viết PRD, phân tích vấn đề thành những thứ một nhóm có thể thực thi. Minh cũng quen Agile và khung CPMAI, dùng trực tiếp qua 8 sprint trong EchoMind.\n\nVề kỹ thuật, Minh biết Python và đã làm việc thực tế với PyTorch và phân tích dữ liệu — không ở mức kỹ sư, nhưng đủ để cộng tác chặt với đội AI.\n\nVề con người — anh ấy đã quản lý hơn 150 startup founder với tư cách đầu mối chính tại một trung tâm do chính quyền thành phố hỗ trợ, và trình bày insight chiến lược trực tiếp lên Ban Giám đốc.`
    }
  }
}
};

// ================= STATE =================
let lang='en',isTyping=false,isTrans=false,curView='welcome';
let chartInst=null,kpiChartInst=null,modelChartInst=null,burndownChartInst=null;
const RM=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
const $=id=>document.getElementById(id);
if(!window.gsap)document.body.classList.add('no-gsap');

// ================= TOAST =================
function showToast(msg,type='success',dur=2200){
  const t=$('toast');t.textContent=msg;
  t.style.borderColor=type==='success'?'var(--green)':'var(--violet)';
  t.style.color=type==='success'?'var(--green)':'var(--violet2)';
  t.classList.add('show');setTimeout(()=>t.classList.remove('show'),dur);
}
function copyEmail(){
  const email='hwinh.work@gmail.com';
  const msg=lang==='en'?'Email copied to clipboard':'Đã copy email vào clipboard';
  if(navigator.clipboard){navigator.clipboard.writeText(email).then(()=>showToast(msg)).catch(()=>showToast(email,'info'));}
  else{const el=document.createElement('textarea');el.value=email;document.body.appendChild(el);el.select();document.execCommand('copy');document.body.removeChild(el);showToast(msg);}
}

// ================= SKILL POPUP =================
function showSkillPopup(card){
  const idx=parseInt(card.getAttribute('data-skill-idx'));const sk=T[lang].skills.list[idx];if(!sk)return;
  const fp=$('float-popup');
  $('fp-title').textContent=T[lang].skills.popupTitle;
  $('fp-metrics').innerHTML=sk.m.map(m=>`<div class="popup-metric">${m}</div>`).join('');
  fp.style.visibility='visible';fp.style.opacity='1';fp.classList.add('on');
  requestAnimationFrame(()=>{
    const rect=card.getBoundingClientRect(),fpH=fp.offsetHeight||160,fpW=fp.offsetWidth||308;
    let top=rect.top>fpH+16?rect.top-fpH-10:rect.bottom+10;
    let left=rect.left+rect.width/2-fpW/2;
    left=Math.max(10,Math.min(left,window.innerWidth-fpW-10));top=Math.max(10,Math.min(top,window.innerHeight-fpH-10));
    fp.style.top=top+'px';fp.style.left=left+'px';
  });
}
function hideSkillPopup(){const fp=$('float-popup');fp.style.opacity='0';fp.style.visibility='hidden';fp.classList.remove('on');}

// ================= KEYBOARD =================
document.addEventListener('keydown',(e)=>{
  if(e.target.tagName==='INPUT'||e.target.tagName==='TEXTAREA')return;
  const overlay=$('lang-overlay');
  const gateVisible=!overlay.classList.contains('hide');
  if(gateVisible){
    if(e.key==='1'){selectLang('en');}if(e.key==='2'){selectLang('vi');}
    return;
  }
  const views=['welcome','experience','projects','ux','skills','education'];
  if(e.key>='1'&&e.key<='6'){const idx=parseInt(e.key)-1;const nav=document.querySelectorAll('.nav-item');if(nav[idx])go(views[idx],nav[idx]);}
  if(e.key==='Escape')logout();
  if(e.key==='l'||e.key==='L')toggleLang();
});

// ================= LANG =================
function selectLang(l){
  lang=l;isTrans=false;isTyping=false;curView='welcome';
  $('lang-overlay').classList.add('hide');
  $('main-app').classList.add('visible');
  $('lang-mini').textContent=l.toUpperCase();
  // reset to Home view
  document.querySelectorAll('.view-content').forEach(v=>{v.style.display=v.id==='view-welcome'?'':'none';v.classList.remove('swapin','swapping');});
  document.querySelectorAll('.nav-item').forEach((n,i)=>n.classList.toggle('active',i===0));
  $('visual-panel').scrollTop=0;
  renderUI();initChat();
  bindMagnetic('.nav-item',.2);bindMagnetic('.nav-mini',.22);
  setTimeout(()=>observeReveals($('view-welcome')),120);
}
function toggleLang(){
  lang=lang==='en'?'vi':'en';
  $('lang-mini').textContent=lang.toUpperCase();
  renderUI();initChat();
  // re-render active view side effects
  if(curView==='projects'){updateProjectChartLabels();renderKPIChart();renderModelChart();renderBurndownChart();}
  if(curView==='skills')initSkillsChart();
  observeReveals($('view-'+curView));
  showToast(lang==='en'?'Language: English':'Ngôn ngữ: Tiếng Việt','info',1500);
}
function logout(){
  hideSkillPopup();
  $('lang-overlay').classList.remove('hide');
  $('main-app').classList.remove('visible');
  $('chat-messages').innerHTML='';
  [kpiChartInst,modelChartInst,burndownChartInst,chartInst].forEach(c=>{if(c){try{c.destroy();}catch(e){}}});
  kpiChartInst=modelChartInst=burndownChartInst=chartInst=null;
}

// ================= RENDER UI =================
function renderUI(){
  const t=T[lang];
  for(let i=0;i<6;i++){const nl=$('nl'+i),ntt=$('ntt'+i);if(nl)nl.textContent=t.nav[i];if(ntt)ntt.textContent=t.navTip[i];}
  $('kbd-nav-hint').textContent=t.kbdNavHint;$('kbd-nav-desc').textContent=t.kbdNavDesc;
  $('w-status').textContent=t.w.status;$('w-role').textContent=t.w.role;$('w-summary').innerHTML=t.w.summary;
  $('stat-grid').innerHTML=t.w.statVals.map((v,i)=>`<div class="stat-card tilt"><div class="tilt-glow"></div><div class="tilt-lift"><div class="stat-number">${v}</div><div class="stat-label">${t.w.stats[i]}</div></div></div>`).join('');
  $('w-explore').textContent=t.w.explore;$('w-hint').textContent=t.w.hint;
  // experience
  $('e-tag').textContent=t.exp.tag;$('e-title').innerHTML=t.exp.title;
  $('e-timeline').innerHTML=t.exp.items.map((item,idx)=>`
    <div class="timeline-item reveal ${idx>0?'past':''}" style="transition-delay:${idx*.08}s">
      <div class="tl-period">${item.period}</div><div class="tl-role">${item.role}</div>
      <div class="tl-company">${item.company}</div>
      <ul class="tl-bullets">${item.bullets.map(b=>`<li>${b}</li>`).join('')}</ul>
      <div class="tl-tags">${item.tags.map(tg=>`<span class="tl-tag">${tg}</span>`).join('')}</div>
    </div>`).join('');
  // projects
  $('p-tag').textContent=t.proj.tag;$('p-title').innerHTML=t.proj.title;renderProjects();
  // ux
  $('ux-tag').textContent=t.ux.tag;$('ux-title').innerHTML=t.ux.title;$('ux-dt-title').textContent=t.ux.dtTitle;renderUX();
  // skills
  $('s-tag').textContent=t.skills.tag;$('s-title').innerHTML=t.skills.title;
  $('s-radar-lbl').textContent=t.skills.radarLbl;$('s-cert-lbl').textContent=t.skills.certLbl;
  $('s-list').innerHTML=t.skills.list.map((sk,idx)=>`
    <div class="lk-skill-card" tabindex="0" data-skill-idx="${idx}" onmouseenter="showSkillPopup(this)" onmouseleave="hideSkillPopup()" onfocus="showSkillPopup(this)" onblur="hideSkillPopup()">
      <div class="lk-skill-header"><div class="lk-skill-title"><span class="dot"></span>${sk.n}</div><span class="lk-info">${IC.scope}</span></div>
      <div class="lk-skill-ref">${sk.ref}</div>
    </div>`).join('');
  $('s-certs').innerHTML=renderCerts(t.skills.certs);
  // education
  $('ed-tag').textContent=t.edu.tag;$('ed-title').innerHTML=t.edu.title;
  $('ed-uni').textContent=t.edu.uni;$('ed-major').textContent=t.edu.major;
  $('ed-courses').innerHTML=`<div class="proj-chart-title" style="margin-bottom:16px;">${t.edu.courseTag}</div><div style="display:flex;flex-wrap:wrap;gap:11px;">${t.edu.courses.map(c=>`<span class="course-pill">${c}</span>`).join('')}</div>`;
  $('ed-cert-lbl').textContent=t.edu.certTag;$('ed-certs').innerHTML=renderCerts(t.edu.certs);
  // chat labels
  $('c-name').textContent=t.chat.name;$('c-sub-txt').textContent=t.chat.sub;$('c-reset-txt').textContent=t.chat.reset;
  bindLift();
}

function renderCerts(certs){
  return certs.map(c=>{
    const tag=c.link?'a':'div',href=c.link?` href="${c.link}" target="_blank" rel="noopener noreferrer"`:'';
    const icon=c.link?`<div class="cert-link-icon" style="color:var(--txt3);opacity:.5;font-size:16px;transition:all .2s;">↗</div>`:'';
    return `<${tag} class="cert-card"${href}><svg class="cert-ico" viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg><div style="flex:1;"><div style="color:var(--txt);font-size:14px;font-weight:500;">${c.n}</div><div style="font-size:11.5px;color:var(--txt2);margin-top:2px;">${c.org}</div></div>${icon}</${tag}>`;
  }).join('');
}

// ================= UX =================
function renderUX(){
  const ux=T[lang].ux;
  $('ux-dt-flow').innerHTML=ux.phases.map(p=>`
    <div class="dt-phase"><span class="dt-phase-num">${p.num}</span>
      <svg class="dt-phase-icon" viewBox="0 0 24 24">${IC[p.ic].replace(/<\/?svg[^>]*>/g,'')}</svg>
      <div class="dt-phase-name">${p.name}</div><div class="dt-phase-desc">${p.desc}</div></div>`).join('');
  $('ux-cases').innerHTML=ux.cases.map(cs=>renderCaseStudy(cs)).join('');
}
function renderCaseStudy(cs){
  const abBars=cs.abVariants.map(v=>`
    <div class="ab-row"><span class="ab-variant-lbl">${v.lbl}</span>
      <div class="ab-bar-track"><div class="ab-bar-fill ${v.cls}" data-pct="${v.pct}">${v.pct}%</div></div>
      ${v.badge?`<span class="ab-badge">${v.badge}</span>`:'<span style="min-width:84px;"></span>'}</div>`).join('');
  const stageRow=`<div class="jm-stage-row"><div style="min-width:118px;flex-shrink:0;"></div><div class="jm-cells">${cs.journeyStages.map(s=>`<div class="jm-cell stage-name">${s}</div>`).join('')}</div></div>`;
  const dataRows=cs.journeyRows.map(row=>`
    <div class="jm-stage-row"><div class="jm-label">${row.label}</div>
      <div class="jm-cells">${row.cells.map((c,i)=>`<div class="jm-cell ${row.types[i]||''}">${c}</div>`).join('')}</div></div>`).join('');
  const beforeRows=cs.before.map(r=>`<div class="impact-metric-row"><span class="impact-metric-name">${r.n}</span><span class="impact-metric-val">${r.v}</span></div>`).join('');
  const afterRows=cs.after.map(r=>`<div class="impact-metric-row"><span class="impact-metric-name">${r.n}</span><span class="impact-metric-val">${r.v}</span></div>`).join('');
  const learnings=cs.learnings.map(l=>`<div class="learning-card"><svg class="learning-icon" viewBox="0 0 24 24">${IC[l.ic].replace(/<\/?svg[^>]*>/g,'')}</svg><div class="learning-title">${l.title}</div><div class="learning-text">${l.text}</div></div>`).join('');
  return `
    <div class="case-study ${cs.cls} reveal">
      <div class="cs-header"><div class="cs-meta">
        <div class="cs-eyebrow"><span class="cs-num">${cs.num}</span><span class="cs-tag">${cs.ctag}</span></div>
        <div class="cs-title">${cs.title}</div><div class="cs-role">${cs.role}</div></div>
        <div class="cs-impact-badge"><div class="cs-impact-num">${cs.impactNum}</div><div class="cs-impact-lbl">${cs.impactLbl}</div></div>
      </div>
      <div class="problem-box"><div class="problem-label">${IC.warn} ${cs.problemLabel}</div><div class="problem-text">${cs.problem}</div></div>
      <div class="cs-body">
        <div><div class="cs-section-title">${cs.approachTitle}</div>
          <div class="process-steps">${cs.steps.map(s=>`<div class="process-step"><span class="step-num">${s.n}</span><div><div class="step-title">${s.t}</div><div class="step-desc">${s.d}</div></div></div>`).join('')}</div></div>
        <div><div class="insight-box"><div class="insight-label">${IC.bulb} ${cs.insightLabel}</div><div class="insight-text">${cs.insight}</div></div>
          <div class="ab-container"><div class="ab-title">${cs.abTitle}</div><div class="ab-variants">${abBars}</div><div class="ab-stat">${cs.abStat}</div></div></div>
      </div>
      <div class="cs-section-title" style="margin-bottom:12px;">${cs.journeyTitle}</div>
      <div class="journey-map">${stageRow}${dataRows}</div>
      <div class="cs-section-title" style="margin:22px 0 14px;">${cs.beforeAfterTitle}</div>
      <div class="impact-compare">
        <div class="impact-col before"><div class="impact-col-label">Before</div>${beforeRows}</div>
        <div class="impact-arrow">${IC.arrow}</div>
        <div class="impact-col after"><div class="impact-col-label">After</div>${afterRows}</div></div>
      <div class="cs-learnings">${learnings}</div>
    </div>`;
}

// ================= PROJECTS =================
function renderProjects(){
  const t=T[lang];const grid=$('p-grid');
  grid.innerHTML=t.proj.items.map(p=>{
    if(p.id==='echomind'){
      return `<div class="project-card featured tilt"><div class="tilt-glow"></div><div>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;flex-wrap:wrap;"><span class="project-badge ${p.bClass}">${p.badge}</span><span class="project-badge badge-active">${p.date}</span></div>
        <div class="project-name">${p.name}</div><div class="project-sub">${p.sub}</div>
        <p class="project-desc">${p.desc.replace(/\n/g,'<br>')}</p>
        <div class="info-grid">${p.info.map(i=>`<div class="info-item"><div class="info-lbl">${i.l}</div><div class="info-val">${i.v}</div></div>`).join('')}</div>
        <div class="project-metrics">${p.metrics.map(m=>`<div><div class="metric-val">${m.v}</div><div class="metric-lbl">${m.l}</div></div>`).join('')}</div>
        <div class="proj-chart-wrap"><div class="proj-chart-title" id="kpi-chart-title">Technical KPI Breakdown — vs Traditional AAC</div><div style="height:210px;position:relative;"><canvas id="kpiChart"></canvas></div></div>
        <div class="proj-chart-wrap"><div class="proj-chart-title" id="model-chart-title">Model Comparison: LSTM V1 vs Transformer V2</div><div style="height:190px;position:relative;"><canvas id="modelChart"></canvas></div></div>
        <div class="tech-stack">${p.tech.map(tch=>`<span class="tech-pill">${tch}</span>`).join('')}</div>
      </div>
      <div class="echo-side">
        <div style="display:flex;align-items:center;justify-content:center;margin-bottom:16px;color:var(--violet2);">${IC.brain.replace('<svg viewBox="0 0 24 24">','<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" style="display:block;">')}</div>
        <div class="echo-pipeline">EEG Input (256ch)<br>↓ <b>HDF5 → Tensor</b><br>↓ Positional Enc.<br>↓ <b>Transformer V2</b><br>↓ Int8 Quantization<br>↓ <b>Gradio Expert UI</b><br>→ Text Output</div>
        <div style="margin-top:18px;padding-top:18px;border-top:1px solid var(--line);">
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--txt2);margin-bottom:4px;" id="ec-role-lbl">Role</div><div style="font-size:13px;color:var(--txt);font-weight:600;">Project Lead</div>
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--txt2);margin:10px 0 4px;" id="ec-team-lbl">Team</div><div style="font-size:12px;color:var(--txt);">7 members · 8 sprints</div>
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--txt2);margin:10px 0 4px;" id="ec-adv-lbl">Advisor</div><div style="font-size:11px;color:var(--txt2);">ThS. Tạ Việt Phương</div>
        </div>
        <div style="margin-top:18px;padding-top:18px;border-top:1px solid var(--line);">
          <div style="font-family:'DM Mono',monospace;font-size:9px;color:var(--violet2);letter-spacing:1px;text-transform:uppercase;margin-bottom:12px;" id="ec-sprint-lbl">Sprint Burndown</div>
          <div style="height:140px;position:relative;"><canvas id="burndownChart"></canvas></div>
        </div></div></div>`;
    }
    return `<div class="project-card tilt"><div class="tilt-glow"></div><div class="tilt-lift">
        <div style="display:flex;justify-content:space-between;align-items:start;margin-bottom:12px;gap:10px;"><span class="project-badge ${p.bClass}">${p.badge}</span><span style="font-family:'DM Mono',monospace;font-size:10.5px;color:var(--txt2);">${p.date}</span></div>
        <div class="project-name" style="font-size:22px;">${p.name}</div><div class="project-sub">${p.sub}</div>
        <p class="project-desc">${p.desc.replace(/\n/g,'<br>')}</p>
        <div class="tech-stack">${p.tech.map(tch=>`<span class="tech-pill">${tch}</span>`).join('')}</div></div></div>`;
  }).join('');
}

// ================= CHARTS =================
const CHART_FONT="'DM Sans',sans-serif",MONO="'DM Mono',monospace";
function renderKPIChart(){
  const ctx=$('kpiChart');if(!ctx)return;if(kpiChartInst){kpiChartInst.destroy();kpiChartInst=null;}
  const isVI=lang==='vi';
  const labels=isVI?['Độ chính xác','Tốc độ (WPM)','Độ trễ (cải thiện)','Tỷ lệ thành công']:['Accuracy','Speed (WPM)','Latency (improvement)','Session Success'];
  kpiChartInst=new Chart(ctx,{type:'bar',data:{labels,datasets:[{label:isVI?'AAC Truyền thống':'Traditional AAC',data:[60,30,0,40],backgroundColor:'rgba(110,110,140,.4)',borderColor:'rgba(110,110,140,.8)',borderWidth:1,borderRadius:6},{label:'EchoMind V2',data:[93,60,75,72],backgroundColor:'rgba(124,106,247,.55)',borderColor:'rgba(165,148,252,.9)',borderWidth:1,borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,animation:{duration:RM?0:900},scales:{x:{grid:{color:'rgba(255,255,255,.05)'},ticks:{color:'#aeaec6',font:{family:CHART_FONT,size:11}}},y:{grid:{color:'rgba(255,255,255,.05)'},ticks:{color:'#aeaec6',font:{family:MONO,size:10}},max:100,min:0}},plugins:{legend:{labels:{color:'#aeaec6',font:{family:CHART_FONT,size:11},boxWidth:12}},tooltip:{backgroundColor:'#1c1c29',titleFont:{family:MONO},bodyFont:{family:CHART_FONT},borderColor:'rgba(255,255,255,.1)',borderWidth:1,callbacks:{label:c=>` ${c.dataset.label}: ${c.raw}${c.dataIndex===2?'% '+(isVI?'giảm':'reduction'):'%'}`}}}}});
}
function renderModelChart(){
  const ctx=$('modelChart');if(!ctx)return;if(modelChartInst){modelChartInst.destroy();modelChartInst=null;}
  const isVI=lang==='vi';const lbls=isVI?['WER (%)','Độ chính xác (%)','Tốc độ (WPM)','Tỷ lệ Mode Collapse']:['WER (%)','Accuracy (%)','Speed (WPM)','Mode Collapse Rate'];
  modelChartInst=new Chart(ctx,{type:'radar',data:{labels:lbls,datasets:[{label:'LSTM V1 (Baseline)',data:[85,15,25,95],borderColor:'rgba(255,123,107,.7)',backgroundColor:'rgba(255,123,107,.08)',borderWidth:1.5,pointRadius:3,pointBackgroundColor:'rgba(255,123,107,.8)'},{label:'Transformer V2',data:[8,93,60,0],borderColor:'rgba(165,148,252,.8)',backgroundColor:'rgba(124,106,247,.12)',borderWidth:1.8,pointRadius:3,pointBackgroundColor:'#a594fc'}]},options:{responsive:true,maintainAspectRatio:false,animation:{duration:RM?0:900},scales:{r:{min:0,max:100,ticks:{display:false},angleLines:{color:'rgba(255,255,255,.07)'},grid:{color:'rgba(255,255,255,.07)'},pointLabels:{color:'#aeaec6',font:{size:10,family:CHART_FONT}}}},plugins:{legend:{labels:{color:'#aeaec6',font:{family:CHART_FONT,size:11},boxWidth:12,padding:14}},tooltip:{backgroundColor:'#1c1c29',titleFont:{family:MONO},bodyFont:{family:CHART_FONT},borderColor:'rgba(255,255,255,.1)',borderWidth:1}}}});
}
function renderBurndownChart(){
  const ctx=$('burndownChart');if(!ctx)return;if(burndownChartInst){burndownChartInst.destroy();burndownChartInst=null;}
  const isVI=lang==='vi';
  burndownChartInst=new Chart(ctx,{type:'line',data:{labels:['Start','S0','S1','S2-3','S4','S5','S6','S7'],datasets:[{label:isVI?'Lý tưởng':'Ideal',data:[3833,3280,2727,2174,1621,1068,515,0],borderColor:'rgba(110,110,140,.5)',borderWidth:1.5,borderDash:[5,4],pointRadius:0,fill:false},{label:isVI?'Thực tế':'Actual',data:[3833,3253,2560,2086,1534,1057,612,0],borderColor:'#a594fc',borderWidth:2,pointRadius:3,pointBackgroundColor:'#a594fc',fill:{target:'origin',above:'rgba(124,106,247,.06)'}}]},options:{responsive:true,maintainAspectRatio:false,animation:{duration:RM?0:900},scales:{x:{grid:{display:false},ticks:{color:'#71718e',font:{family:MONO,size:9}}},y:{grid:{color:'rgba(255,255,255,.04)'},ticks:{color:'#71718e',font:{family:MONO,size:9},callback:v=>(v/1000).toFixed(1)+'k'}}},plugins:{legend:{labels:{color:'#aeaec6',font:{family:CHART_FONT,size:10},boxWidth:10,padding:10}},tooltip:{backgroundColor:'#1c1c29',titleFont:{family:MONO},bodyFont:{family:CHART_FONT},borderColor:'rgba(255,255,255,.1)',borderWidth:1}}}});
}
function updateProjectChartLabels(){
  const isVI=lang==='vi';const e=(id,txt)=>{const el=$(id);if(el)el.textContent=txt;};
  e('kpi-chart-title',isVI?'Phân tích KPI Kỹ thuật — So với AAC Truyền thống':'Technical KPI Breakdown — vs Traditional AAC');
  e('model-chart-title',isVI?'So sánh Mô hình: LSTM V1 vs Transformer V2':'Model Comparison: LSTM V1 vs Transformer V2');
  e('ec-role-lbl',isVI?'Vai trò':'Role');e('ec-team-lbl',isVI?'Nhóm':'Team');e('ec-adv-lbl',isVI?'GVHD':'Advisor');e('ec-sprint-lbl',isVI?'Burndown Sprints':'Sprint Burndown');
}
function initSkillsChart(){
  const ctx=$('skillsChart');if(!ctx)return;if(chartInst){chartInst.destroy();chartInst=null;}
  const t=T[lang];
  chartInst=new Chart(ctx,{type:'radar',data:{labels:t.skills.radarLabels,datasets:[{data:[95,88,95,80,65,65,82],fill:true,backgroundColor:'rgba(124,106,247,.14)',borderColor:'#7c6af7',pointBackgroundColor:'#a594fc',pointBorderColor:'#15151f',borderWidth:2,pointRadius:4}]},options:{responsive:true,maintainAspectRatio:false,animation:{duration:RM?0:900},scales:{r:{min:0,max:100,ticks:{display:false},angleLines:{color:'rgba(255,255,255,.07)'},grid:{color:'rgba(255,255,255,.07)'},pointLabels:{font:{size:12,family:CHART_FONT,weight:'500'},color:'#aeaec6'}}},plugins:{legend:{display:false},tooltip:{backgroundColor:'#1c1c29',borderColor:'rgba(255,255,255,.1)',borderWidth:1,padding:12,callbacks:{label:c=>{const v=c.raw;if(lang==='vi')return v>=90?' Chuyên gia':v>=80?' Cao cấp':v>=70?' Thành thạo':' Có nền tảng';return v>=90?' Expert':v>=80?' Advanced':v>=70?' Proficient':' Familiar';}}}}}});
}

// ================= VIEW SWITCHING (3D push) =================
function go(viewId,navEl){
  if(isTrans)return;
  const target=$('view-'+viewId);
  if(!target||target.style.display!=='none')return;
  isTrans=true;curView=viewId;
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  if(navEl)navEl.classList.add('active');else{const n=document.querySelector(`[data-view="${viewId}"]`);if(n)n.classList.add('active');}
  hideSkillPopup();
  const cur=document.querySelector('.view-content:not([style*="display: none"])');
  const finish=()=>{
    document.querySelectorAll('.view-content').forEach(v=>{v.style.display='none';v.classList.remove('swapin','swapping');});
    target.style.display='';target.classList.add('swapin');
    $('scroll-progress').style.width='0%';$('visual-panel').scrollTop=0;
    if(viewId==='skills')setTimeout(initSkillsChart,80);
    if(viewId==='projects')setTimeout(()=>{updateProjectChartLabels();renderKPIChart();renderModelChart();renderBurndownChart();bindLift();},90);
    observeReveals(target);bindLift();
    setTimeout(()=>{isTrans=false;},RM?0:420);
  };
  if(RM||!cur){finish();}
  else{cur.classList.add('swapping');setTimeout(finish,240);}
}

// ================= REVEAL ON SCROLL =================
let io=null;
function observeReveals(scope){
  const els=(scope||document).querySelectorAll('.reveal');
  if(RM){els.forEach(e=>e.classList.add('in'));return;}
  if(!io){
    io=new IntersectionObserver((entries)=>{
      entries.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');animateAB(en.target);io.unobserve(en.target);}});
    },{root:$('visual-panel'),threshold:.12,rootMargin:'0px 0px -8% 0px'});
  }
  els.forEach(e=>{e.classList.remove('in');io.observe(e);});
}
function animateAB(node){
  const fills=node.querySelectorAll?node.querySelectorAll('.ab-bar-fill'):[];
  fills.forEach(f=>{const pct=f.getAttribute('data-pct');f.style.width='0';requestAnimationFrame(()=>{setTimeout(()=>f.style.width=pct+'%',60);});});
}

// ================= MAGNETIC LIFT (GSAP) =================
// Hover brings the card FORWARD (lift + subtle scale + cursor-follow glow) so it
// invites reading — never recede/shrink. Falls back to CSS under body.no-gsap.
function bindLift(){
  if(RM)return;
  const G=window.gsap;
  document.querySelectorAll('.tilt').forEach(card=>{
    if(card._lift)return;card._lift=true;
    // cursor-follow glow only; the forward lift (translateY+scale) is CSS :hover —
    // reading-friendly, never twists/recedes the content under the cursor.
    card.addEventListener('pointermove',e=>{
      const r=card.getBoundingClientRect();
      card.style.setProperty('--mx',((e.clientX-r.left)/r.width*100)+'%');
      card.style.setProperty('--my',((e.clientY-r.top)/r.height*100)+'%');
    });
  });
}

// magnetic pull for icon buttons (awwwards-style) — inline transform + CSS transition smoothing
function bindMagnetic(sel,strength){
  if(RM)return;
  document.querySelectorAll(sel).forEach(el=>{
    if(el._mag)return;el._mag=true;
    el.addEventListener('pointermove',e=>{
      const r=el.getBoundingClientRect();
      const x=(e.clientX-r.left-r.width/2)*strength,y=(e.clientY-r.top-r.height/2)*strength;
      el.style.transform=`translate(${x.toFixed(2)}px,${y.toFixed(2)}px)`;
    });
    el.addEventListener('pointerleave',()=>{el.style.transform='';});
  });
}

// ================= AMBIENT PARALLAX =================
const depth=$('depth'),floor=$('floor'),hero=()=>$('hero3d');
let mx=0,my=0,tx=0,ty=0;
if(!RM){
  window.addEventListener('pointermove',e=>{mx=(e.clientX/window.innerWidth-.5);my=(e.clientY/window.innerHeight-.5);});
  (function loop(){
    tx+=(mx-tx)*.06;ty+=(my-ty)*.06;
    const orbs=depth.querySelectorAll('.orb');
    orbs.forEach((o,i)=>{const f=(i+1)*16;o.style.transform=`translate3d(${tx*f}px,${ty*f}px,0)`;});
    if(floor)floor.style.transform=`perspective(420px) rotateX(62deg) translateX(${tx*20}px)`;
    const h=hero();if(h&&curView==='welcome'){h.style.transform=`rotateX(${ -ty*4}deg) rotateY(${tx*5}deg)`;}
    requestAnimationFrame(loop);
  })();
}
// scroll-driven hero fade + parallax depth
$('visual-panel').addEventListener('scroll',function(){
  const h=this.scrollHeight-this.clientHeight;
  if(h>0)$('scroll-progress').style.width=(this.scrollTop/h*100)+'%';
  if(curView==='welcome'&&!RM){
    const s=this.scrollTop;const hd=hero();
    if(hd){hd.style.opacity=Math.max(0,1-s/420);hd.style.filter=`blur(${Math.min(6,s/120)}px)`;}
  }
},{passive:true});

// ================= CHAT =================
function initChat(){$('chat-messages').innerHTML='';renderPrompts();setTimeout(()=>appendMsg('ai',T[lang].chat.greeting,true),400);}
function renderPrompts(){
  $('prompts-grid').innerHTML=T[lang].chat.prompts.map(p=>`<button class="prompt-btn" onclick="handlePrompt('${p.id}','${p.l}')" ${isTyping||isTrans?'disabled':''}><span class="p-icon">${IC[p.ic]}</span><span class="p-lbl">${p.l}</span></button>`).join('');
}
function handlePrompt(id,label){
  if(isTyping||isTrans)return;
  $('prompts-grid').style.opacity='.4';
  appendMsg('user',label,false);
  const vMap={exp:'experience',proj:'projects',ux:'ux',skills:'skills'};
  setTimeout(()=>go(vMap[id]||'welcome',null),300);
  setTimeout(()=>appendMsg('ai',T[lang].chat.ans[id],true,()=>{$('prompts-grid').style.opacity='1';renderPrompts();}),650);
}
function appendMsg(s,txt,tw=false,cb=null){
  const cm=$('chat-messages');
  const row=document.createElement('div');row.className='msg-row '+s;
  const av=document.createElement('div');av.className='msg-av '+s;
  av.innerHTML=s==='ai'?'<svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/></svg>':'<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>';
  const bub=document.createElement('div');bub.className='msg-bubble '+s;
  row.appendChild(av);row.appendChild(bub);cm.appendChild(row);
  if(s==='ai'&&tw&&!RM)typeW(txt,bub,cb);
  else{bub.innerHTML=txt.replace(/\n/g,'<br>');cm.scrollTop=cm.scrollHeight;if(cb)cb();}
}
function typeW(txt,el,cb){
  isTyping=true;renderPrompts();
  const cm=$('chat-messages');
  const tmp=document.createElement('div');tmp.innerHTML=txt.replace(/\n/g,'<br>');
  const nodes=Array.from(tmp.childNodes);
  el.innerHTML='<span class="tc"></span><span class="cursor-blink"></span>';
  const tc=el.querySelector('.tc');let ni=0,ci=0;
  function type(){
    if(ni<nodes.length){
      const nd=nodes[ni];
      if(nd.nodeType===3){if(ci<nd.textContent.length){tc.innerHTML+=nd.textContent.charAt(ci++);cm.scrollTop=cm.scrollHeight;setTimeout(type,Math.floor(Math.random()*16)+4);}else{ni++;ci=0;type();}}
      else{tc.appendChild(nd.cloneNode(true));ni++;cm.scrollTop=cm.scrollHeight;setTimeout(type,8);}
    }else{isTyping=false;const cur=el.querySelector('.cursor-blink');if(cur)cur.remove();renderPrompts();if(cb)cb();}
  }
  type();
}
function resetChat(){if(isTyping||isTrans)return;initChat();}
</script>
</body>
</html>
