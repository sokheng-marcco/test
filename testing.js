const button = document.getElementById('toggleButton');
const body = document.body;

// Initial state (no change needed — already light)
button.addEventListener('click', () => {
  button.classList.toggle('on');

  if (button.classList.contains('on')) {
    button.textContent = 'ON';
    body.style.backgroundColor = '#f0f0f0'; // Light background
  } else {
    button.textContent = 'OFF';
    body.style.backgroundColor = 'blue'; // Background becomes blue when OFF
  }
});
