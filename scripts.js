document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const length = document.getElementById('length').value;
    const height = document.getElementById('height').value;
    const width = document.getElementById('width').value;
  
    fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ length, height, width })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').style.display = 'block';
      document.getElementById('predictionOutput').textContent = data.prediction;
    })
    .catch(error => console.error('Error:', error));
  });
  