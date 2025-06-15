
function toggleDarkMode() {
  const body = document.body;
  const toggle = document.getElementById('toggle-btn');
  body.classList.toggle('dark');
  toggle.classList.toggle('active');
}
