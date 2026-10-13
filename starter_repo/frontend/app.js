document.getElementById('load').addEventListener('click', async () => {
  const out = document.getElementById('output');
  out.textContent = 'Loading...';
  try {
    const res = await fetch('/api/interviews');
    const data = await res.json();
    out.textContent = JSON.stringify(data.slice(0, 10), null, 2);
  } catch (err) {
    out.textContent = 'Failed to load interviews';
  }
});
