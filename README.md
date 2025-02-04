**Number Property API - Stage 1 Task**

**Overview**
The **Number Property API** is a simple RESTful API that takes a number as input and returns interesting mathematical properties about it, along with a fun fact. The API is designed to process both integers and special cases like alphabets or non-numeric inputs.

** Features**
- Accepts a number as input.
- Returns mathematical properties (e.g., prime, even/odd, perfect square, armstrong, digit sum).
- Provides a fun fact related to the number.
- Handles invalid inputs gracefully.

**Tech Stack**
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: Postgress
- **Hosting**:Render

**Project Setup**
Clone the Repository
```sh
 git clone https://github.com/Maryam-20/HNGi12-stage-one.git
 cd stageOne
```

Create a Virtual Environment & Install Dependencies
```sh
 python -m venv venv  # Create virtual environment
 source venv/bin/activate  # Activate on macOS/Linux
 venv\Scripts\activate  # Activate on Windows

 pip install -r requirements.txt  # Install dependencies
```

Run Migrations
```sh
 python manage.py migrate
```

Start the Django Server
```sh
 python manage.py runserver
```

**API Endpoints**
 Get Number Properties
Request
```sh
GET /number-api/{number}/
```
Response (Example for `371`)
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

Handle Invalid Inputs
Request
```sh
GET /number-api/a/
```
Response
```json
{
  "number": "alphabet",
  "error": true
}
```

 Contributors
Maryam Anileleye - Backend Developer

