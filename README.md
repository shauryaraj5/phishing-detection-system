# 🚨 Phishing Detection System — End-to-End Machine Learning & Deployment

A production-ready **phishing detection system** that classifies network requests as *phishing* or *legitimate* using machine learning.  
The system includes **automated training, experiment tracking, CI/CD, containerization, cloud deployment, and FastAPI-based inference**.

---

## 🔗 Table of Contents
- Overview
- Features
- Architecture
- Dataset
- Modeling & Training
- Experiment Tracking (MLflow + DAGsHub)
- Project Structure
- Setup & Installation
- Running the App
- Docker Support
- API Endpoints
- CI/CD & Deployment
- Future Improvements

---

## 🧾 Overview
This project implements a complete **MLOps pipeline** for phishing URL detection:

- Data ingestion from **MongoDB**
- Automated **training → evaluation → model selection**
- Inference served using **FastAPI** with a **web UI** for batch CSV uploads
- **MLflow + DAGsHub** for experiment tracking and comparison
- **Containerized with Docker**
- **CI/CD via GitHub Actions**, deployed to **AWS EC2**
- **AWS S3** used for trained model and artifact storage

---

## ⭐ Features
✔ FastAPI-based UI for CSV batch prediction  
✔ Custom dataset (~11k rows) of phishing/legitimate URLs  
✔ Multiple ML models trained & tuned using **GridSearchCV**  
✔ Best model achieves **~93% accuracy**  
✔ **MLflow + DAGsHub** experiment tracking and artifact storage  
✔ **MongoDB** as ingestion data source  
✔ **Dockerized** inference service  
✔ **CI/CD with GitHub Actions + AWS EC2, ECR, and S3**

---

## 🏗 Architecture
```
MongoDB → Data Ingestion → Data Validation → Data Transformation → Model Training (GridSearchCV)
                                      ↓
                         MLflow + DAGsHub (metrics + params + artifacts)
                                      ↓
Saved Preprocessor + Model → FastAPI Inference → HTML Results Table
                                                   ↓
                                       Deployment via Docker on AWS EC2
```

---

## 📊 Dataset
- Size: **~11,000 entries**
- Stored/loaded using **MongoDB**
- Target column: `Result`
- Dataset contains 30+ phishing-related features such as:

```
having_IP_Address, URL_Length, Shortening_Service, having_At_Symbol,
double_slash_redirecting, Prefix_Suffix, having_Sub_Domain, SSLfinal_State,
Domain_registeration_length, Favicon, port, HTTPS_token, Request_URL,
URL_of_Anchor, Links_in_tags, SFH, Submitting_to_email, Abnormal_URL,
Redirect, on_mouseover, RightClick, popUpWidnow, Iframe, age_of_domain,
DNSRecord, web_traffic, Page_Rank, Google_Index, Links_pointing_to_page,
Statistical_report, Result
```

---

## 🤖 Modeling & Training
- Models evaluated:
  - Logistic Regression  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
  - AdaBoost  
- **GridSearchCV** used for hyperparameter tuning  
- Best model achieved **~93% accuracy**  
- Trained artifacts saved to:
```
final_model/model.pkl  
final_model/preprocessor.pkl
```

---

## 🧪 Experiment Tracking (MLflow + DAGsHub)
Each training run logs:
- Accuracy, Precision, Recall, F1-score
- Parameters & hyperparameters
- Confusion matrix
- Model and Preprocessor artifacts

Benefits:
- Compare performance across runs
- Track reproducibility and model evolution
- Centralized artifact & metric storage

---

## 📂 Project Structure
```
phishing-detection-system/
├── app.py
├── data_schema
|    └── scehma.yaml
|── mlruns
├── networksecurity/
│   ├── pipeline/
│   ├── utils/
│   ├── logging/
│   ├── exception/
|   |── entity/
│   |── constant/
|   |── cloud/
|   └── components/
|
├── final_model/
│   ├── model.pkl
│   └── preprocessor.pkl
├── prediction_output/
│   └── batch_pred_output.csv
├── templates/
|   ├── base.html
│   ├── index.html
│   └── table.html
├── static/
|   └── styles.css
├── .github/workflows/
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```
git clone https://github.com/shauryaraj5/phishing-detection-system.git
cd phishing-detection-system
```

### 2️⃣ Install dependencies (using `uv`)
```
uv pip install -r requirements.txt
```

### 3️⃣ Configure environment variables
Create `.env`:
```
MONGODB_URL_KEY=<your_mongodb_connection_string>
```

---

## ▶️ Running the App
```
uv pip install -r requirements.txt
uvicorn app:app --reload
```

App URL → **http://127.0.0.1:8000**  
Swagger UI → **http://127.0.0.1:8000/docs**

---

## 🐳 Docker Support

### Build Image
```
docker build -t phishing-detection-system .
```

### Run Container
```
docker run -p 8000:8000 --env-file .env phishing-detection-system
```

---

## 📡 API Endpoints

| Method | Route       | Description |
|--------|-------------|-------------|
| GET    | `/`         | CSV upload UI |
| GET    | `/train`    | Triggers full ML training pipeline |
| POST   | `/predict`  | Upload CSV → returns prediction results |
| GET    | `/docs`     | Swagger documentation |

---

## 🚀 CI/CD & Deployment

### CI/CD — GitHub Actions
Automates:
- Dependency installation & validation
- Docker build
- Docker push to **AWS ECR**
- Deployment to **AWS EC2**
- Sync MLflow artifacts & logs to **DAGsHub**

### AWS Services Used
| Component | Service |
|----------|---------|
| Compute | **EC2** |
| Container Registry | **ECR** |
| Artifact Storage | **S3** |

---

## 🔮 Future Improvements
- Accept raw URL input (automated feature extraction)
- Auto-promote best model from DAGsHub to production
- Observability with Grafana / Prometheus
- Test suite + CI coverage dashboard

