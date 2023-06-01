document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission
  
      // Get input values
      var f1 = document.getElementById('F1').value;
      var f2 = document.getElementById('F2').value;
      var f3 = document.getElementById('F3').value;
      var f4 = document.getElementById('F4').value;
  
      // Create a new FormData object
      var formData = new FormData();
      formData.append('F1', f1);
      formData.append('F2', f2);
      formData.append('F3', f3);
      formData.append('F4', f4);
  
      // Send a POST request to the Flask app
      fetch('/', {
        method: 'POST',
        body: formData
      })
      .then(response => response.text())
      .then(prediction => {
        // Display prediction result
        var predictionElement = document.createElement('p');
        predictionElement.textContent = 'Prediction: ' + prediction;
        form.appendChild(predictionElement);
      })
      .catch(error => console.error('Error:', error));
    });
  });
  