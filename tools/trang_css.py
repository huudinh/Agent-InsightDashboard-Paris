# -*- coding: utf-8 -*-
CSS = u"""
/* Bang mau rieng cua Nha khoa Paris - xanh #2a52be + vang #8a6f22 + nen xanh nhat.
   Khuon trang (steps - the tai - mbox - tab - file card - prompt card - toast)
   dung chung voi bo tai lieu huong dan agent, chi doi bang mau va phong. */
:root{
  --ground:#dce3ee; --surface:#ffffff; --surface-2:#eaf0fc; --surface-3:#f2f6fe;
  --ink:#131a2e; --ink-2:#3c4563; --ink-3:#6b7391;
  --line:#d7e2fa; --line-2:#e6edfb;
  --primary:#2a52be; --primary-ink:#152f73; --primary-wash:#eaf0fc; --on-primary:#ffffff;
  --accent:#8a6f22; --accent-soft:#a98a2d; --accent-wash:#f8f1d8;
  --band:#06101f; --band-ink:#eaf0fc; --band-accent:#8fb0f5; --on-band-accent:#06101f;
  --do:#c11b26;   --do-bg:#fdeaeb;
  --cam:#a85205;  --cam-bg:#fceeda;
  --vang:#8a6f22; --vang-bg:#f8f1d8;
  --ok:#2f6b46;   --ok-bg:#e4f1e9;
  --f:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  --f2:'Bricolage Grotesque','Be Vietnam Pro',system-ui,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --r:10px; --r-lg:14px;
  --sh:0 1px 2px rgba(19,26,46,.10),0 2px 6px rgba(19,26,46,.05);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#070c1c; --surface:#0e1527; --surface-2:#16203a; --surface-3:#16203a;
    --ink:#eef2fb; --ink-2:#c6cfe6; --ink-3:#8e9ab8;
    --line:#2c3a62; --line-2:#243150;
    --primary:#8fb0f5; --primary-ink:#b3c8f9; --primary-wash:#1c2a4e; --on-primary:#07102a;
    --accent:#ddc072; --accent-soft:#c0a254; --accent-wash:#2e2715;
    --band:#0c1d4d; --band-ink:#eaf0fc; --band-accent:#8fb0f5; --on-band-accent:#07102a;
    --do:#f9adb1;   --do-bg:#3a1b21;
    --cam:#efb478;  --cam-bg:#3e2612;
    --vang:#ddc072; --vang-bg:#2e2715;
    --ok:#8fd0a9;   --ok-bg:#17301f;
    --sh:0 1px 2px rgba(0,0,0,.45),0 3px 10px rgba(0,0,0,.30);
  }
}
:root[data-theme="dark"]{
  --ground:#070c1c; --surface:#0e1527; --surface-2:#16203a; --surface-3:#16203a;
  --ink:#eef2fb; --ink-2:#c6cfe6; --ink-3:#8e9ab8;
  --line:#2c3a62; --line-2:#243150;
  --primary:#8fb0f5; --primary-ink:#b3c8f9; --primary-wash:#1c2a4e; --on-primary:#07102a;
  --accent:#ddc072; --accent-soft:#c0a254; --accent-wash:#2e2715;
  --band:#0c1d4d; --band-ink:#eaf0fc; --band-accent:#8fb0f5; --on-band-accent:#07102a;
  --do:#f9adb1;   --do-bg:#3a1b21;
  --cam:#efb478;  --cam-bg:#3e2612;
  --vang:#ddc072; --vang-bg:#2e2715;
  --ok:#8fd0a9;   --ok-bg:#17301f;
  --sh:0 1px 2px rgba(0,0,0,.45),0 3px 10px rgba(0,0,0,.30);
}

*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font:400 15.5px/1.62 var(--f);-webkit-font-smoothing:antialiased}
.wrap{max-width:940px;margin:0 auto;padding-inline:20px}
@media(max-width:480px){.wrap{padding-inline:16px}}
h1,h2,h3{line-height:1.18;text-wrap:balance;margin:0;font-family:var(--f2);letter-spacing:-.01em}
p{margin:0 0 .8em}
a{color:var(--primary);text-decoration-thickness:1px;text-underline-offset:2px}
code{font-family:var(--mono);font-size:.88em;background:var(--surface-2);
  border:1px solid var(--line-2);border-radius:5px;padding:.08em .35em;overflow-wrap:anywhere}
:focus-visible{outline:2.5px solid var(--accent);outline-offset:2px;border-radius:6px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}

header.top{background:var(--band);color:var(--band-ink);border-bottom:4px solid var(--band-accent)}
.eyebrow{font:700 12px/1.4 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--band-accent);margin:0 0 9px}
.top h1{font-size:clamp(27px,5.2vw,39px);font-weight:800;letter-spacing:-.02em;color:#fff}
.lede{margin:12px 0 0;font-size:17px;color:rgba(255,255,255,.86);max-width:62ch}
.lede b{color:#fff}
.quick{margin:14px 0 0;font-size:14.5px;color:rgba(255,255,255,.80);max-width:68ch;
  padding-left:13px;border-left:3px solid var(--band-accent)}
.quick b{color:#fff}
.top .dim{color:rgba(255,255,255,.62);font-size:14px}
.top .dim a{color:var(--band-accent)}
.top .dim b{color:rgba(255,255,255,.90)}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px}
.chip{font-size:12.5px;font-weight:600;color:rgba(255,255,255,.80);
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22);
  border-radius:999px;padding:5px 11px}
.chip.on{color:var(--on-band-accent);background:var(--band-accent);border-color:var(--band-accent)}

nav.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;
  background:var(--band);border-bottom:1px solid rgba(255,255,255,.16)}
nav.bar .wrap{display:flex;gap:2px;align-items:center;overflow-x:auto;
  padding-block:9px;scrollbar-width:none}
nav.bar .wrap::-webkit-scrollbar{display:none}
nav.bar a{flex:0 0 auto;font-size:13px;font-weight:600;color:rgba(255,255,255,.74);
  text-decoration:none;padding:6px 11px;border-radius:7px}
nav.bar a:hover{background:rgba(255,255,255,.14);color:#fff}
.themebtn{flex:0 0 auto;margin-left:auto;font:600 12.5px var(--f);
  color:rgba(255,255,255,.74);background:transparent;cursor:pointer;
  border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:5px 12px}
.themebtn:hover{background:rgba(255,255,255,.14);color:#fff}

section.sec{padding-block:46px;border-top:1px solid var(--line);scroll-margin-top:62px}
section.sec:first-of-type{border-top:0}
.sec-h{margin-bottom:22px}
.sec-h .pre{font:700 11.5px/1.3 var(--mono);letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);display:block}
.sec-h h2{font-size:clamp(21px,3.4vw,27px);font-weight:800;color:var(--primary-ink);margin-top:5px}
.sec-h .bar{display:block;width:42px;height:3px;border-radius:3px;
  background:var(--accent-soft);margin-top:11px}
.sec-h p{margin:12px 0 0;color:var(--ink-2);max-width:66ch}
h3.sub{font-size:16px;font-weight:800;color:var(--primary-ink)}
h3.sub .pre2{font:700 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--accent);display:block;margin-bottom:4px}
.dim{color:var(--ink-3);font-size:13px}

.grid{display:grid;gap:14px}
.g2{grid-template-columns:repeat(2,1fr)}
@media(max-width:760px){.g2{grid-template-columns:1fr}}

.steps{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:var(--r-lg);overflow:hidden;margin:0 0 18px;grid-template-columns:repeat(3,1fr)}
@media(max-width:700px){.steps{grid-template-columns:1fr}}
.steps div{background:var(--surface);padding:15px 16px}
.steps b{display:block;font-size:13px;font-weight:800;color:var(--primary-ink);margin-bottom:3px}
.steps span{font-size:13.5px;color:var(--ink-2)}
.steps .n{display:inline-grid;place-content:center;width:21px;height:21px;border-radius:50%;
  background:var(--band);color:#fff;font:800 11.5px var(--f);margin-right:7px;vertical-align:1px}

.dl{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--accent-soft);
  border-radius:var(--r-lg);padding:22px 20px;text-align:center;box-shadow:var(--sh);margin:0 0 16px}
.dl h3{font-size:17px;font-weight:800;color:var(--primary-ink);margin:0 0 4px}
.dl p{margin:0;font-size:14px;color:var(--ink-2)}
a.dl-btn{display:inline-flex;align-items:center;gap:9px;margin:14px 0 0;background:var(--primary);
  color:var(--on-primary);font:800 16.5px var(--f);text-decoration:none;padding:14px 26px;
  border-radius:9px;box-shadow:0 2px 0 var(--accent-soft)}
a.dl-btn:hover{background:var(--primary-ink)}
.dl .alt{margin-top:13px;font-size:13px;color:var(--ink-3)}

.tabs{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 -1px;position:relative;z-index:1}
.tab{border:1px solid var(--line);border-bottom-color:transparent;background:var(--surface-2);
  color:var(--ink-3);font:700 13.5px var(--f);padding:9px 16px;
  border-radius:var(--r) var(--r) 0 0;cursor:pointer}
.tab:hover{color:var(--primary-ink)}
.tab[aria-selected="true"]{background:var(--surface);color:var(--primary-ink);
  border-top:3px solid var(--primary);border-bottom-color:var(--surface);padding-top:7px}
.tabpanel{background:var(--surface);border:1px solid var(--line);
  border-radius:0 var(--r-lg) var(--r-lg) var(--r-lg);padding:18px;box-shadow:var(--sh)}
ol.list{margin:0;padding-left:1.25em}
ol.list li{margin-bottom:9px}
ol.list li::marker{font-weight:800;color:var(--primary)}

.mbox{background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--primary);
  border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--sh);margin:0 0 16px}
.mrow{display:flex;gap:11px;align-items:flex-start;padding:13px 15px;
  border-bottom:1px solid var(--line-2);flex-wrap:wrap}
.mrow:last-child{border-bottom:0}
.mrow .lb{flex:none;width:112px;font-size:11.5px;font-weight:800;letter-spacing:.07em;
  text-transform:uppercase;color:var(--ink-3);padding-top:4px}
.mrow .vl{flex:1;min-width:210px;font-size:14.2px;color:var(--ink);line-height:1.55}
.mrow .vl.mono{font:700 13.6px/1.5 var(--mono)}
.mrow .copy{flex:none}
@media(max-width:600px){.mrow .lb{width:auto;padding-top:0}}
.st{display:flex;flex-direction:column;gap:8px;width:100%}
.st-i{display:flex;gap:9px;align-items:center;flex-wrap:wrap}
.st-i span{flex:1;min-width:170px;font:400 13.4px/1.5 var(--mono);color:var(--ink-2)}
.st-i .copy{padding:5px 11px;font-size:12px}

.cc{display:flex;flex-direction:column;gap:11px;background:var(--surface);
  border:1px solid var(--line);border-top:4px solid var(--accent-soft);
  border-radius:var(--r-lg);padding:17px;box-shadow:var(--sh)}
.cc .tag{font-size:11.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--ink-3)}
.cc h3{font-size:17px;font-weight:800;color:var(--primary-ink);margin:0}
.cc .meta{font-size:13px;color:var(--ink-2);margin:0;flex:1}
.cc .count{font-variant-numeric:tabular-nums;font-weight:700;color:var(--ink)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;width:100%;
  min-height:44px;border:0;border-radius:9px;background:var(--primary);color:var(--on-primary);
  font:800 14.5px var(--f);letter-spacing:.2px;cursor:pointer;
  box-shadow:0 2px 0 var(--accent-soft);transition:background-color .15s,transform .1s}
.btn:hover{background:var(--primary-ink)}
.btn:active{transform:translateY(1px);box-shadow:0 1px 0 var(--accent-soft)}
details.peek,details.fview{border-top:1px solid var(--line-2);padding-top:10px}
details.peek summary,details.fview summary{cursor:pointer;font-size:13px;font-weight:600;
  color:var(--primary);list-style:none}
details summary::-webkit-details-marker{display:none}
details.peek summary::before,details.fview summary::before{content:"\\25b8  ";color:var(--ink-3)}
details[open].peek summary::before,details[open].fview summary::before{content:"\\25be  "}
.filebody,pre.code{margin:10px 0 0;max-height:260px;overflow:auto;background:var(--surface-2);
  border:1px solid var(--line-2);border-radius:var(--r);padding:12px;
  font:400 12px/1.5 var(--mono);white-space:pre-wrap;word-break:break-word;color:var(--ink-2)}
pre.code{margin-top:0}
.codebar{display:flex;gap:10px;align-items:center;justify-content:space-between;
  flex-wrap:wrap;margin:15px 0 7px}
.codebar .cn{font:700 12.5px var(--mono);color:var(--primary-ink)}

.files{margin-top:8px}
.fcard{border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:var(--surface);
  margin:0 0 9px;box-shadow:var(--sh)}
.fcard.hi{border:2px solid var(--accent-soft)}
.fcard-h{display:flex;gap:10px;align-items:center;padding:11px 13px;flex-wrap:wrap}
.fname{font:700 13.4px var(--mono);color:var(--ink);overflow-wrap:anywhere}
.fbadge{font-size:10.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
  padding:3px 8px;border-radius:999px;background:var(--accent-wash);color:var(--accent);
  border:1px solid var(--accent-soft)}
.fsize{font-size:12.5px;color:var(--ink-3);font-variant-numeric:tabular-nums;margin-left:auto}
.fhow{margin:0;padding:0 13px 11px;font-size:13.8px;color:var(--ink-2)}
.fhow b{color:var(--ink)}
.fcard details.fview{margin:0 13px 11px}
@media(max-width:520px){.fsize{margin-left:0}}
.fgroup{font:800 11.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--ink-3);margin:18px 0 7px}

.copy{font:700 13px var(--f);padding:7px 14px;border-radius:7px;cursor:pointer;
  border:1px solid var(--primary);background:transparent;color:var(--primary);white-space:nowrap}
.copy:hover{background:var(--primary-wash)}
.copy.done{border-color:var(--ok);color:var(--ok);background:var(--ok-bg)}

.tw{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r-lg);
  background:var(--surface);margin:0 0 14px}
table{border-collapse:collapse;width:100%;min-width:620px;font-size:14px}
th,td{text-align:left;padding:11px 13px;border-bottom:1px solid var(--line-2);vertical-align:top}
thead th{font-size:11.5px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
  color:rgba(255,255,255,.94);background:var(--band);border-bottom:0;white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
td.num,th.num{font-variant-numeric:tabular-nums;text-align:right;white-space:nowrap;color:var(--ink-2)}
td.mono{font:600 13px var(--mono);white-space:nowrap}
tr.hl td{background:var(--accent-wash)}

.note{border-radius:0 var(--r) var(--r) 0;padding:13px 16px;font-size:14.5px;
  background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent-soft);
  box-shadow:var(--sh);color:var(--ink-2);margin:14px 0}
.note b{font-weight:800;color:var(--ink)}
.note.warn{border-left-color:var(--cam);background:var(--cam-bg)}
.note.ok{border-left-color:var(--ok);background:var(--ok-bg)}
.note.stop{background:var(--band);color:var(--band-ink);border:1px solid var(--band-accent);
  border-left:5px solid var(--band-accent);border-radius:var(--r)}
.note.stop b{color:#fff}
.note.stop code,header.top code,nav.bar code,thead th code{
  background:rgba(255,255,255,.10);border-color:rgba(255,255,255,.22);color:var(--band-ink)}
.note.stop i{color:var(--band-accent);font-style:normal}
.note.stop a{color:var(--band-accent)}
.note + .note{margin-top:10px}
.note p:last-child{margin-bottom:0}

/* hai luong - khoi rieng cua trang nay */
.vs{display:grid;gap:1px;background:var(--line);border:1px solid var(--line);
  border-radius:var(--r-lg);overflow:hidden;grid-template-columns:1fr 1fr;margin:0 0 4px}
@media(max-width:620px){.vs{grid-template-columns:1fr}}
.vs > div{background:var(--surface);padding:16px 18px}
.vs .h{font:800 11.5px var(--mono);letter-spacing:.09em;text-transform:uppercase;
  margin:0 0 7px;color:var(--ink-3)}
.vs .w{font-size:16px;font-weight:800;color:var(--primary-ink);margin:0 0 9px;
  font-family:var(--f2)}
.vs ul{margin:0;padding-left:1.1em;font-size:13.8px;color:var(--ink-2)}
.vs li{margin-bottom:4px}
.vs .i .h{color:var(--primary)}
.vs .q .h{color:var(--accent)}
.wall{grid-column:1/-1;background:var(--do-bg)!important;color:var(--do);
  font:800 11.5px var(--mono);letter-spacing:.1em;text-transform:uppercase;
  text-align:center;padding:11px 16px!important}

.qa-bar{display:flex;gap:7px;flex-wrap:wrap;align-items:center;margin:0 0 16px}
.qa-bar button{font:600 13px var(--f);padding:6px 13px;border:1px solid var(--line);
  background:var(--surface);color:var(--ink-3);border-radius:999px;cursor:pointer;white-space:nowrap}
.qa-bar button:hover{color:var(--primary-ink);border-color:var(--primary)}
.qa-bar button[aria-pressed="true"]{background:var(--primary);color:var(--on-primary);
  border-color:var(--primary)}
.prompt{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);
  margin:0 0 12px;overflow:hidden;box-shadow:var(--sh)}
.prompt-h{display:flex;gap:11px;align-items:center;padding:12px 15px;flex-wrap:wrap;
  background:var(--surface-2);border-bottom:1px solid var(--line-2)}
.prompt-h .n{flex:none;font:700 12.5px var(--mono);color:var(--primary-ink);
  font-variant-numeric:tabular-nums}
.prompt-h .t{font-size:14.8px;font-weight:700;flex:1;min-width:0;color:var(--ink)}
.prompt-h .k{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:var(--ink-3);border:1px solid var(--line);border-radius:999px;padding:3px 9px;white-space:nowrap}
.prompt-b{margin:0;padding:14px 15px;max-height:280px;overflow:auto;
  font:400 12.6px/1.66 var(--mono);color:var(--ink-2);white-space:pre-wrap;
  overflow-wrap:anywhere;background:var(--surface)}
.prompt-f{display:flex;gap:10px;align-items:center;justify-content:space-between;
  padding:11px 15px;flex-wrap:wrap;border-top:1px solid var(--line-2);background:var(--surface-2)}
.prompt-f .get{font-size:12.8px;color:var(--ink-3);flex:1;min-width:150px}
@media (max-width:420px){.prompt-h .k{display:none}}

footer{border-top:1px solid var(--line);background:var(--surface);
  padding-block:30px;font-size:13px;color:var(--ink-3)}
footer b{color:var(--ink-2)}
.toast{position:fixed;left:50%;transform:translateX(-50%);
  bottom:calc(20px + env(safe-area-inset-bottom,0px));
  background:var(--band);color:var(--band-ink);font:700 13.5px var(--f);padding:10px 18px;
  border-radius:999px;z-index:90;box-shadow:0 8px 24px rgba(0,0,0,.3);
  opacity:0;pointer-events:none;transition:opacity .18s ease}
.toast.on{opacity:1}
"""
