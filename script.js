function handleUpload() {
  const input = document.getElementById('dataUpload');
  const output = document.getElementById('output');

  if (!input.files.length) {
    output.textContent = 'No file selected.';
    return;
  }

  const file = input.files[0];
  const formData = new FormData();
  formData.append('file', file);

  output.textContent = 'Sending file for analysis...';

  fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        output.textContent = `Error: ${data.error}`;
      } else {
        output.textContent = 'Meta Predictions:\n';
        data.prediction.forEach(([archetype, prob]) => {
          output.textContent += `- ${archetype}: ${prob * 100}%\n`;
        });
      }
    })
    .catch(err => {
      output.textContent = `Request failed: ${err.message}`;
    });
}
