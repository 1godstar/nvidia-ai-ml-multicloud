# nvidia-ai-ml-multicloud
AI/ML Product Deployment Pipeline in a Multi-Cloud Environment
# Repo Structure
/ai-model-deployment
├── model/
│   ├── train.py         # Script to train the model
│   ├── simple_model.h5  # Saved TensorFlow model
│   ├── model.pkl        # Pickled model
│   ├── preprocess.py    # Preprocessing functions
│   ├── inference.py     # Inference class
├── deployment/
│   ├── deploy_lambda.py
│   ├── ansible_deploy.yml
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml
├── README.md
