# GetFit 🚧

> A robust fitness API designed to streamline workout tracking, nutrition management, and long-term fitness goal planning.

## 📌 Overview

GetFit is a fitness and nutrition tracking platform that enables users to:

* Track daily food intake and nutritional values
* Create customizable macro goals
* Maintain diet and nutrition logs
* Build personalized workout plans
* Track workout history and progress
* Set and monitor short-term and long-term fitness goals

```text
The project aims to provide a centralized solution for managing both fitness and nutrition data through a scalable API-driven architecture.
---
```
## 🚀 Features

### 🔐 Authentication

* User registration and login
* Password hashing for secure credential storage
* JWT-based authentication for protected API endpoints
* Persistent user sessions through frontend state management

### 🥗 Nutrition Tracking *(Planned)*

* Daily food logging
* Custom macro targets
* Nutrient tracking and reporting
* Historical nutrition data

### 🏋️ Workout Management *(Planned)*

* Create and manage workout plans
* Exercise tracking
* Workout history and analytics
* Goal-based training programs
---
## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* MySQL

### Frontend

* React
* JSX
* HTML5
* CSS3

### Architecture

* Decoupled React Frontend + FastAPI Backend
* Layered Architecture
  - API Routers
  - DTO/Schema Layer
  - Service Layer
  - Repository Layer
  - Data Model Layer
* Domain-Based Modular Design
* RESTful API Architecture
* JWT Authentication
* Microservice-Ready Structure

### Tools
* Git
* GitHub
---

## 📦 Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/joemuldowney/getfit.git
cd getfit
```

### Backend Setup
for local dev without docker:
  - create a mysql db and update variables in getfit/db/connection.py
  - run "poetry run uvicorn getfit.main:app --host 0.0.0.0 --port 8000" in root
for production
  - 

# Coming soon

### Frontend Setup

# Coming soon

---
## 📖 API Documentation

FastAPI automatically generates API documentation.

Once the server is running, visit:

```text
http://localhost:8000/docs
```

For ReDoc documentation:

```text
http://localhost:8000/redoc
```
---
## 📅 Project Status

### Current Progress

* [x] Project planning
* [x] Technology stack selected
* [x] Authentication system
* [ ] User profiles
* [ ] Nutrition tracking
* [ ] Workout management
* [ ] Goal tracking
* [ ] Analytics dashboard
* [ ] Production deployment

> **Note:** This project is currently under active development. Features and API endpoints may change as development progresses.

---
## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---
