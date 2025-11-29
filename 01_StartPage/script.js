// script.js - small UI enhancements and graceful transitions
document.addEventListener('DOMContentLoaded', () => {
  // small micro-interactions (button ripple-like)
  document.querySelectorAll('.btn').forEach(b => {
    b.addEventListener('mousedown', () => { b.style.transform = 'translateY(1px) scale(.997)'; });
    b.addEventListener('mouseup', () => { b.style.transform = ''; });
    b.addEventListener('mouseleave', () => { b.style.transform = ''; });
  });
});
