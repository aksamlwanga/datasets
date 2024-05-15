function sendReview() {
    var reviewsText = document.getElementById('reviewInput').value.trim();
    var reviews = reviewsText.split('\n').filter(r => r.trim() !== ''); // Split by newline and filter out empty lines
    console.log(APP_URL);
    $.ajax({
        url: API_URL, // URL of the Flask API
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ reviews: reviews }),
        success: function(response) {
            displayResults(response);
        },
        error: function(err) {
            console.log(err);
            document.getElementById('predictionResult').innerHTML = '<p>Error fetching prediction. Make sure the API is running.</p>';
        }
    });
}

function displayResults(results) {
    var resultDiv = document.getElementById('predictionResult');
    resultDiv.innerHTML = ''; // Clear previous results
    results.forEach(function(result) {
        var icon = result.predicted_quality === 'High Quality' ? '<span style="color: green;">✓</span>' 
                                                               : '<span style="color: red;">🙁</span>';
        var content = `<p>Review: "${result.review}"<br>Predicted Quality: ${icon} ${result.predicted_quality}</p>`;
        resultDiv.innerHTML += content;
    });
}

