from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained MLP model
mlp_model = joblib.load('model/xgb_best_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    entered_values = {}

    if request.method == 'POST':
        # Extract input values from form
        cgpa = float(request.form['CGPA'])
        internships = int(request.form['Internships'])
        projects = int(request.form['Projects'])
        workshops = int(request.form['Workshops'])
        aptitude_score = int(request.form['AptitudeTestScore'])
        soft_skills = float(request.form['SoftSkillsRating'])
        extracurricular = 1 if request.form['ExtracurricularActivities'] == 'Yes' else 0
        placement_training = 1 if request.form['PlacementTraining'] == 'Yes' else 0
        ssc_marks = int(request.form['SSC_Marks'])
        hsc_marks = int(request.form['HSC_Marks'])

        # Dictionary to store user input for displaying later
        entered_values = {
            "CGPA": cgpa,
            "Internships": internships,
            "Projects": projects,
            "Workshops": workshops,
            "Aptitude Test Score": aptitude_score,
            "Soft Skills Rating": soft_skills,
            "Extracurricular Activities": "Yes" if extracurricular else "No",
            "Placement Training": "Yes" if placement_training else "No",
            "SSC Marks": ssc_marks,
            "HSC Marks": hsc_marks
        }

        # Ensure only the **10 required features** are used for prediction
        input_data = np.array([[cgpa, internships, projects, workshops, aptitude_score, 
                                soft_skills, extracurricular, placement_training, ssc_marks, hsc_marks]])

        # Make the prediction
        prediction = mlp_model.predict(input_data)

        # Convert prediction to human-readable result
        result = 'Placed' if prediction[0] == 1 else 'Not Placed'

    return render_template('index.html', result=result, entered_values=entered_values)

if __name__ == '__main__':
    app.run(debug=True)
