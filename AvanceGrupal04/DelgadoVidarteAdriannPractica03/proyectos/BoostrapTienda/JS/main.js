const checkbox = document.getElementById('checkbox');

checkbox.addEventListener('change', () => {
  // Cambiar el tema del sitio web
  document.body.classList.toggle('dark');
});