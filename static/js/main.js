const tabs=[...document.querySelectorAll('.tab')];
const panels=[...document.querySelectorAll('.panel')];
function setActive(id){
  tabs.forEach(t=>t.classList.toggle('is-active',t.dataset.panel===id));
  panels.forEach(p=>p.classList.toggle('is-active',p.id===`panel-${id}`));
}
tabs.forEach(b=>b.addEventListener('click',()=>setActive(b.dataset.panel)));

let idx=0;
function focusTab(i){ idx=(i+tabs.length)%tabs.length; setActive(tabs[idx].dataset.panel); tabs[idx].focus(); }
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight') focusTab(idx+1);
  else if(e.key==='ArrowLeft') focusTab(idx-1);
});

// Scanline knob
const root=document.documentElement, scan=document.getElementById('scan');
const setVar=(n,v)=>root.style.setProperty(n,v);
scan && scan.addEventListener('input',()=>setVar('--scan-alpha',scan.value));

// Swap image when a stat/skill is clicked
const vaultImg=document.getElementById('vaultboy-img');
document.querySelectorAll('.stat-btn').forEach(btn=>{
  btn.addEventListener('click',()=>{
    const src=btn.getAttribute('data-image');
    if(src && vaultImg){ vaultImg.src=src; }
  });
});
