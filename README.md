# DevOps Assessment: CI/CD Pipeline with GitHub Actions, Ansible, and EC2

This project demonstrates a simple Flask app deployed on an EC2 instance using:
- GitHub Actions for CI/CD
- Ansible for configuration management
- NGINX as a reverse proxy
## Project

- `.github/workflows/deploy.yml` – GitHub Actions pipeline
- `ansible/playbook.yml` – Automates Flask + NGINX setup on EC2
- `nginx/default.conf` – Reverse proxy config for Flask app
- `app/app.py` – Simple Python Flask app
- `requirements.txt` – Flask dependency

## Deployment Flow

1. Push to `main` branch
2. GitHub Actions triggers `deploy.yml`
3. Ansible connects to EC2 and:
   - Installs dependencies
   - Deploys the Flask app
   - Configures and restarts NGINX

## Author

*Shaik Rahoof*
