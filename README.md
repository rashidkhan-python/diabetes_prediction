# Diabetes Prediction Web App

Flask-based machine learning web application that predicts diabetes risk using a trained Logistic Regression model.

## Repository
https://github.com/rashidkhan-python/diabetes_prediction

## Key Features
- End-to-end prediction flow from form input to model inference
- Predicts output as `Diabetic` or `Non-Diabetic`
- Three-page user journey:
  - Landing page (`index.html`)
  - Input form page (`home.html`)
  - Prediction result page (`single_prediction.html`)
- Preprocessing + inference pipeline using saved scaler and model
- Deployment-ready for AWS Elastic Beanstalk
- CI/CD-ready structure for AWS CodePipeline

## Functional Details
- Accepts 8 medical features as input:
  1. Pregnancies
  2. Glucose
  3. BloodPressure
  4. SkinThickness
  5. Insulin
  6. BMI
  7. DiabetesPedigreeFunction
  8. Age
- Applies `standardScalar.pkl` for feature scaling
- Uses `logReg.pkl` for final prediction
- Maps model output:
  - `1` -> `Diabetic`
  - `0` -> `Non-Diabetic`

## Tech Stack
- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- HTML/CSS (Jinja templates)
- AWS Elastic Beanstalk
- AWS CodePipeline

## Project Structure
```text
.
|-- application.py
|-- requirements.txt
|-- README.md
|-- .ebextensions/
|   `-- python.config
|-- Model/
|   |-- logReg.pkl
|   `-- standardScalar.pkl
|-- templates/
|   |-- index.html
|   |-- home.html
|   `-- single_prediction.html
|-- Dataset/
|   `-- diabetes.csv
`-- Notebook/
    `-- diabetes_prediction.ipynb
```

## Routes
- `/` -> Landing page
- `/predictdata` (GET) -> Prediction form
- `/predictdata` (POST) -> Prediction result

## Local Setup
```bash
git clone https://github.com/rashidkhan-python/diabetes_prediction.git
cd diabetes_prediction
pip install -r requirements.txt
python application.py
```
App URL: `http://127.0.0.1:5000/`

## AWS Deployment
### Elastic Beanstalk
- WSGI mapping is configured in `.ebextensions/python.config`
- Deploy as a Python web application source bundle

### CodePipeline
Recommended pipeline flow:
1. Source: GitHub
2. Build: CodeBuild (optional)
3. Deploy: Elastic Beanstalk

## Author
Rashid Khan

## License
MIT License

