# RAD Project: Simple Notes System  

A lightweight **notes management system** built with **FastAPI**.  

---

## 🚀 Features  
- OAuth2 Authentication for secure access  
- Manage notes (CRUD operations)  
- User management system  
- Cloud integrations (webhook handling and task initiation)  

---

## 📂 Folder Structure  

```plaintext
project_notes/
├── alembic/         # Database migrations
├── api/             # API routes and controllers
├── core/            # Core settings and utilities
├── db/              # Database models and interactions
├── service/         # Business logic services
├── .env             # Environment configuration file
├── .requirements    # Application dependencies
├── lambda_function.py
├── README.md


## 🛠️ Installation  

### Using Docker Compose  

1. Modify the `.env` file with the required configurations.  
2. Build and run the application:  
   ```bash
   docker-compose build  
   docker-compose up  

### Using Docker
1.Update environment variables in core/config.py and the Dockerfile.
2.Build the Docker image: