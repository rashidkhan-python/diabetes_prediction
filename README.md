# Diabetes Prediction Web App

A Flask-based machine learning web application that predicts whether a person is likely to be **Diabetic** or **Non-Diabetic** using a trained Logistic Regression model.

## Overview
This project demonstrates an end-to-end ML deployment workflow:
- Data preprocessing and model training
- Model and scaler serialization (`.pkl`)
- Flask backend with Jinja templates
- Multi-page web interface for prediction
- Deployment-ready setup for AWS Elastic Beanstalk
- CI/CD compatibility with AWS CodePipeline

## Features
- User-friendly landing page
- Input form for health metrics
- Real-time prediction result page
- Responsive and clean UI templates
- Elastic Beanstalk WSGI configuration

## Tech Stack
- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- HTML/CSS (Jinja2 templates)
- AWS Elastic Beanstalk
- AWS CodePipeline

## Project Structure
```text
.
+-- application.py
+-- requirements.txt
+-- README.md
+-- .ebextensions/
¦   +-- python.config
+-- Model/
¦   +-- logReg.pkl
¦   +-- standardScalar.pkl
+-- Dataset/
¦   +-- diabetes.csv
+-- templates/
¦   +-- index.html
¦   +-- home.html
¦   +-- single_prediction.html
+-- Notebook/
    +-- diabetes_prediction.ipynb
```

## Application Routes
- `/` -> Landing page
- `/predictdata` (GET) -> Input form page
- `/predictdata` (POST) -> Prediction result page

## Input Features
1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

## Prediction Output
- `Diabetic` (model output `1`)
- `Non-Diabetic` (model output `0`)

## Local Setup
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-project-folder>
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python application.py
   ```
5. Open:
   `http://127.0.0.1:5000/`

## Deployment (AWS Elastic Beanstalk)
This project is structured for Elastic Beanstalk deployment with:
- `application.py` as app entry point
- `.ebextensions/python.config` for WSGI path
- `requirements.txt` for package installation

Basic deployment flow:
1. Create Elastic Beanstalk application and Python environment
2. Upload project source bundle (zip root contents)
3. Deploy and verify application health

## CI/CD (AWS CodePipeline)
Recommended pipeline stages:
1. **Source**: GitHub or CodeCommit
2. **Build**: CodeBuild (optional checks/package)
3. **Deploy**: Elastic Beanstalk

## Security & Privacy Notes
- Avoid hardcoded machine-specific/local absolute paths
- Use relative paths for model loading
- Do not commit secrets, credentials, or private keys
- Keep `.gitignore` updated (`.venv`, cache, temporary files)

## Future Improvements
- Add input validation and detailed error handling
- Show model probability/confidence on result page
- Add automated tests for Flask routes
- Add logging and monitoring for production

## License
Add your preferred license (for example, MIT).
