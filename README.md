## **Project Status** ✅ Operational
- Automated model deployments via GitHub Actions
- Serverless inference via AWS Lambda
- Local deployment via Ansible

## **Usage**
```bash
# Manual deployment
ansible-playbook deployment/ansible_deploy.yml

# Automated deployment (push to main branch)
git push origin main


## **Testing the Full Pipeline**

### **1. Make a Change and Observe**
1. Modify your `model.pkl` (or create a dummy change)
   ```bash
   touch model/model.pkl
