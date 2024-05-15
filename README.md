### Review Quality Predictor

---

#### Project Overview

The Review Quality Predictor is a Flask-based application designed to predict the quality of textual reviews using machine learning. This application uses several trained models and natural language processing (NLP) techniques to analyze textual data and return predictions.

#### Features

- Predict review quality as High or Low based on the content of the review.
- Utilizes pre-trained machine learning models using Scikit-Learn and NLP processing.
- Easy-to-use web interface.

#### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or above
- pip (Python package installer)

#### Installation

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/aksamlwanga/datasets.git
   ```

   Navigate to the cloned directory:
   ```
   cd datasets
   ```

2. **Set Up a Virtual Environment**

   It's recommended to create a virtual environment for Python projects. Use the following commands:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   Install all required packages using the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

#### Configuration

- Ensure all configurations are correct in `config.py` or within environment variables (refer to `.env.example` for template).

#### Running the Application

To run the application locally:
```
export FLASK_APP=app.py
FLASK_DEBUG=1   # Set to 0 in a production environment
flask run
```

This will start the Flask server on `http://127.0.0.1:5000/`, where you can access the web interface.

#### Using the Application

- Navigate to `http://127.0.0.1:5000/` in your web browser.
- Enter a review or multiple reviews into the text area, separated by new lines.
- Click the "Predict Quality" button to see the predictions.

#### API Usage

You can also interact with the predictor directly through the API:

**Endpoint:**
```
POST /predict
```
**Payload:**
```json
{
  "reviews": ["Sample review text here", "Another sample review"]
}
```
**Response:**
```json
[
  {
    "review": "Sample review text here",
    "predicted_quality": "High Quality"
  },
  {
    "review": "Another sample review",
    "predicted_quality": "Low Quality"
  }
]
```





.
