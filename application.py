from flask import Flask, request, render_template
import pickle
import warnings
import os

warnings.filterwarnings("ignore")

application = Flask(__name__)
app = application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "Model")

scaler_path = os.path.join(MODEL_DIR, "standardScalar.pkl")
model_path = os.path.join(MODEL_DIR, "logReg.pkl")

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

with open(model_path, "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get("Glucose"))
        BloodPressure = float(request.form.get("BloodPressure"))
        SkinThickness = float(request.form.get("SkinThickness"))
        Insulin = float(request.form.get("Insulin"))
        BMI = float(request.form.get("BMI"))
        DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
        Age = float(request.form.get("Age"))

        new_data = scaler.transform([[
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        ]])

        prediction = model.predict(new_data)

        if prediction[0] == 1:
            result = "Diabetic"
        else:
            result = "Non-Diabetic"

        return render_template("single_prediction.html", result=result)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
