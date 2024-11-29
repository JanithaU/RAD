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
some minor adjesments might need in .envs (refer core->config.py)

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


## API Overview

### Notes API

- **GET** `/notes/`  
  Retrieve all notes.

- **GET** `/notes/view/{note_id}`  
  Retrieve a note by ID.  
  **Path Parameters:**  
  - `note_id` (integer, required): ID of the note.

- **POST** `/notes/create`  
  Add a new note.  
  **Request Body:**  
  - `content` (string, minLength: 2): The content of the note.

- **PUT** `/notes/update/{note_id}`  
  Update an existing note.  
  **Path Parameters:**  
  - `note_id` (integer, required): ID of the note.  
  **Request Body:**  
  - `content` (string, minLength: 2): Updated content for the note.

- **DELETE** `/notes/delete/{note_id}`  
  Delete a note by ID.  
  **Path Parameters:**  
  - `note_id` (integer, required): ID of the note to delete.

### User Management API

- **GET** `/users/`  
  Retrieve all users.

- **POST** `/users/create`  
  Add a new user.  
  **Request Body:**  
  - `username` (string, maxLength: 50): Username of the user.  
  - `password` (string, minLength: 8, maxLength: 255): Password of the user.  
  - `role` (string, maxLength: 6, default: "user"): Role of the user.

- **POST** `/users/login`  
  Authenticate user and obtain an access token.  
  **Request Body:**  
  - `username` (string): Username of the user.  
  - `password` (string): Password of the user.

### Cloud API

- **POST** `/aws/webhook`  
  Handle webhook events.  
  **Request Body:**  
  - `task_data` (string): Data required for the task.  
  - `callback_url` (string): URL for callback.  

- **POST** `/aws/start-task`  
  Start a new task on AWS.  
  **Request Body:**  
  - `task_data` (string): Data required for the task.  
  - `callback_url` (string): URL for callback.

---

## Authentication

Authentication uses **OAuth2 Password Bearer**.  

To obtain an access token, make a **POST** request to `/auth/token`.  
**Request Body:**  
- `username` (string): The username of the user.  
- `password` (string): The password of the user.  

**Response:**  
- `200 OK`: Successfully authenticated. Returns the access token.  
- `422 Unprocessable Entity`: Invalid input or incorrect credentials.

Once authenticated, include the token in the `Authorization` header as a **Bearer token** when making requests to protected routes:
```bash
Authorization: Bearer <your_access_token>
