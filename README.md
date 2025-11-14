# Heart Disease Prediction API  (MLOps)

## 📖 Descripción
API para predecir riesgo de enfermedad cardíaca usando un modelo de **Logistic Regression**.  
Este proyecto sigue buenas prácticas de **MLOps**, incluyendo:
- Entrenamiento reproducible en notebooks.
- Servición vía **FastAPI**.
- Contenerización con **Docker**.
- CI/CD automatizado con **GitHub Actions**.
- Despliegue opcional en **Kubernetes**.

---

##  Estructura del Proyecto

heart-disease-mlops/
├── app/
│ ├── api.py
│ └── model.joblib
├── docker/
│ ├── Dockerfile
│ └── requirements.txt
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
├── notebooks/
│ ├── 1_model_leakage_demo.ipynb
│ └── 2_model_pipeline_cv.ipynb
├── .github/
│ └── workflows/
│ └── ci.yml
├── drift_report.html
└── README.md

---

##  Instalación Local
pip install -r docker/requirements.txt
uvicorn app.api:app --reload


## Docker
docker build -t heart-disease-api -f docker/Dockerfile .
docker run -p 8000:8000 heart-disease-api


## Kubernets
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
