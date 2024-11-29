---
title: 'Simple Notes System'
shortTitle: 'Simple Notes'
intro: 'Learn about the Simple Notes System, a lightweight notes management system built with FastAPI.'
product: "FastAPI"
type: overview
topics:
  - notes management
  - FastAPI
  - OAuth2
versions:
  - 1.0.0
---

## Introduction

The Simple Notes System is a lightweight application developed with FastAPI. It allows users to securely manage notes, handle user accounts, and integrate with cloud services for advanced functionality.

## Features

- Secure user authentication with OAuth2.
- Notes management (CRUD operations).
- User account management.
- Cloud service integration for webhook handling and task initiation.

## Installation

### Using Docker Compose

1. Update the `.env` file with your configuration.
2. Build and run the application:
   ```bash
   docker-compose build
   docker-compose up

### Using Docker

1. Update environment variables in core/config.py and the Dockerfile.
2. Build the Docker image:
  ```bash
   docker build -t fastapi-app .
   docker run -p 8000:8000 fastapi-app

### Running the Application
Access the application at:
👉 http://localhost:8000/

API documentation is available at:
👉 http://localhost:8000/docs

### 📂 Folder Structure

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