# 🔢 Number Property API

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgreSQL-15-blue)](https://www.postgresql.org/)
[![DRF](https://img.shields.io/badge/DRF-3.14-red)](https://www.django-rest-framework.org/)
[![Deploy](https://img.shields.io/badge/Hosted%20on-Render-purple)](https://hngi12-stage-one.onrender.com)

A simple RESTful API that classifies numbers by their mathematical properties. Whether it's an Armstrong number, perfect square, prime, or just a plain integer, the API processes it and returns interesting attributes and a fun fact.

---

## 📚 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)

---

## 🚀 Features

- Accepts integers as input via query parameters.
- Identifies mathematical properties:
  - Prime
  - Even/Odd
  - Perfect number
  - Armstrong number
  - Digit sum
- Provides a fun fact for valid inputs.
- Graceful handling of invalid or non-numeric inputs.

---

## ⚙️ Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/Maryam-20/HNGi12-stage-one.git
cd stageOne
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv  # Create virtual environment

# Activate it
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

---

## 📌 Usage

### Example: Classify a Valid Number

**Request**
```http
GET https://hngi12-stage-one.onrender.com/api/classify-number/?number=371
```

**Response**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
        "armstrong",
        "odd"
    ],
    "digit_sum": 11,
    "fun_fact": "371 is an unremarkable number."
}
```

### Example: Handle Invalid Input

**Request**
```http
GET https://hngi12-stage-one.onrender.com/api/classify-number/?number=a
```

**Response**
```json
{
    "error": "Invalid number format"
}
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/classify-number/?number=<value>` | Classifies a number and returns its properties and a fun fact |

---

## 🛠 Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Language:** Python
- **Hosting:** Render

---
