# 🚗 Vehicle Insurance Prediction – End-to-End MLOps Project

This project demonstrates a complete **End-to-End MLOps pipeline** for predicting whether a customer will purchase vehicle insurance.

It covers the full machine learning lifecycle including **data ingestion, validation, transformation, model training, evaluation, and deployment**, along with **CI/CD automation** using modern MLOps tools.

The objective is to build a **production-ready ML system** that is scalable, reproducible, and automated.

---

# 📌 Problem Statement

Insurance companies aim to predict whether customers who already have health insurance will also purchase vehicle insurance.

Using customer demographic and policy data, we build a Machine Learning model that predicts customer response.

---

# 🧠 Workflow

The project follows a structured MLOps pipeline:

1. Data Ingestion  
2. Data Validation  
3. Data Transformation  
4. Model Training  
5. Model Evaluation  
6. Model Deployment  
7. CI/CD Automation  

---

# 🏗️ Project Structure

```
MLOPs_1st_project_Vechical_insurance
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│
├── pipeline/
│   └── training_pipeline.py
│
├── config/
│   └── configuration files
│
├── artifacts/
│   └── trained models and outputs
│
├── app.py / main.py
├── requirements.txt
├── Dockerfile
├── .github/workflows/
│   └── CI/CD pipeline
└── README.md
```

---

# ⚙️ Tech Stack

### Programming Language
- Python

### Machine Learning Libraries
- Scikit-learn
- Pandas
- NumPy

### MLOps Tools
- GitHub Actions (CI/CD)
- Docker
- AWS Cloud
- Logging & Exception Handling

### Deployment
- FastAPI / Flask

---

# 🚀 Installation

Clone repository:

```bash
git clone https://github.com/dipta19062021/MLOPs_1st_project_Vechical_insurance.git
cd MLOPs_1st_project_Vechical_insurance
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Training Pipeline

```bash
python main.py
```

OR

```bash
python src/pipeline/training_pipeline.py
```

---

# 📊 Model Output

The pipeline generates:

- Trained model file
- Performance metrics
- Logs
- Artifacts folder containing outputs

Typical evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score

---

# 🔄 CI/CD Pipeline

GitHub Actions automates:

- Code integration
- Model training workflow
- Docker image build
- Deployment pipeline

This ensures reproducibility and reliability of the ML system.

---

# 🐳 Docker

Build docker image:

```bash
docker build -t vehicle-insurance-mlops .
```

Run container:

```bash
docker run -p 5000:5000 vehicle-insurance-mlops
```

---

# 📈 Future Improvements

- MLflow experiment tracking
- Model monitoring
- Data drift detection
- Kubernetes deployment
- Feature store integration

---

# 👨‍💻 Author

Archisman Ghosh  

Aspiring Data Scientist | ML Engineer | MLOps Enthusiast

Skills:
- Machine Learning
- Deep Learning
- MLOps
- TensorFlow
- Scikit-learn
- FastAPI
- Docker

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ If you like this project, consider giving it a star!
