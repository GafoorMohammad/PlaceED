## **📌 Placement Prediction Web App**
A Flask-based web application that predicts whether a student will be **placed** or **not placed** based on academic and extracurricular factors using **Machine Learning**.

---

## **📖 Features**
✅ Predicts **student placement status** based on CGPA, internships, projects, etc.  
✅ Uses a trained **XGBoost Classifier** for prediction  
✅ **User-friendly web interface** with Flask  
✅ Can be **deployed on Render, PythonAnywhere, or AWS**  

---

## **🛠 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/placement-prediction.git
cd placement-prediction
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Flask App**
```bash
python app.py
```
The app will be running at **`http://127.0.0.1:5000/`** 🚀  

---
📂 Dataset
The dataset used for training the model can be found on Kaggle:
🔗 Placement Prediction Dataset

📊 Dataset Features
| Feature                 | Description |
|-------------------------|------------|
| CGPA                    | Cumulative Grade Point Average |
| Internships             | Number of internships completed |
| Projects                | Number of projects completed |
| Workshops/Certifications | Number of workshops attended |
| Aptitude Test Score     | Score in aptitude test |
| Soft Skills Rating      | Rating (0-5) on soft skills |
| Extracurricular Activities | Yes/No |
| Placement Training      | Yes/No |
| SSC Marks              | 10th-grade percentage |
| HSC Marks              | 12th-grade percentage |
🔹 Note: You may need a Kaggle account to download the dataset.
---

## **📡 Deployment**
### **🔹 Deploy on Render**
1. **Push your code to GitHub**
2. Create a **`requirements.txt`** and **`Procfile`**:
   ```
   web: gunicorn app:app
   ```
3. Sign up at **[Render](https://render.com/)** → Create a new **Web Service**  
4. Connect your GitHub repo and deploy 🚀  

### **🔹 Deploy on PythonAnywhere**
1. Upload your project to **PythonAnywhere**  
2. Modify `wsgi.py` to point to `app.py`  
3. Restart the web app ✅  

### **🔹 Deploy on AWS EC2**
1. Launch an **EC2 instance** (Ubuntu)  
2. SSH into the instance and install dependencies  
3. Run the app using **Gunicorn**  
4. Open port **5000** in security settings  

---

## **🤝 Contributing**
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a **Pull Request** 🎉  

---

## **📜 License**
This project is **open-source** under the **MIT License**.  

---

## **📞 Contact**
📧 Email: your.email@example.com  
🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)  

---

### ⭐ If you found this useful, **star** this repo! 🌟  
Would you like me to customize anything further? 😊
