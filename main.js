
// Tab handling with keyboard controls
const tabs = Array.from(document.querySelectorAll('.tab'));
const panels = Array.from(document.querySelectorAll('.panel'));
function setActive(panelId){
  tabs.forEach(t=> t.classList.toggle('is-active', t.dataset.panel === panelId));
  panels.forEach(p=> p.classList.toggle('is-active', p.id === `panel-${panelId}`));
}
tabs.forEach(btn => {
  btn.addEventListener('click', () => setActive(btn.dataset.panel));
});

// Left/Right arrow to switch tabs
let idx = 0;
function focusTab(i){
  idx = (i + tabs.length) % tabs.length;
  setActive(tabs[idx].dataset.panel);
  tabs[idx].focus();
}
document.addEventListener('keydown', (e)=>{
  if(e.key === 'ArrowRight'){ focusTab(idx+1); }
  else if(e.key === 'ArrowLeft'){ focusTab(idx-1); }
});

// Knobs -> CSS variables
const root = document.documentElement;
const brightness = document.getElementById('brightness');
const glow = document.getElementById('glow');
const scan = document.getElementById('scan');

const setVar = (name, val) => root.style.setProperty(name, val);
brightness.addEventListener('input', ()=> setVar('--brightness', brightness.value));
glow.addEventListener('input', ()=> setVar('--glow', glow.value));
scan.addEventListener('input', ()=> setVar('--scan-alpha', scan.value));

// Initialize ARIA states
function syncAria(){
  tabs.forEach(t => {
    const isActive = t.classList.contains('is-active');
    t.setAttribute('aria-selected', String(isActive));
    const panel = document.getElementById(`panel-${t.dataset.panel}`);
    if(panel){ panel.hidden = !isActive ? true : false; }
  });
}
const observer = new MutationObserver(syncAria);
observer.observe(document.body, { attributes:true, subtree:true, attributeFilter:['class'] });
syncAria();
