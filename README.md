# Student Management API using FastAPI

A simple REST API built using **FastAPI** to manage student records.

This project demonstrates basic CRUD operations:

* Create Student
* Read Student
* Update Student
* Partial Update
* Delete Student

---

## Features

* Get all students
* Get student by ID
* Add new student
* Update student details
* Update only age
* Delete student
* FastAPI automatic documentation

---

## Tech Stack

* Python
* FastAPI
* Uvicorn

---

## Project Structure

```text
project/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone YOUR_REPOSITORY_LINK
```

Open folder:

```bash
cd YOUR_PROJECT
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## Run Project

Start server:

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Get All Students

```http
GET /students
```

Response:

```json
{
 "Message":"All Students",
 "data":[]
}
```

---

### Get Student By ID

```http
GET /student/{student_id}
```

Example:

```http
GET /student/1
```

---

### Add Student

```http
POST /student
```

Parameters:

```text
id=3
name=Alex
age=20
```

Response:

```json
{
 "message":"Student Add"
}
```

---

### Update Student

```http
PUT /student/{student_id}
```

Example:

```text
name=Rahul
age=23
```

---

### Update Student Age

```http
PATCH /student/{student_id}
```

Example:

```text
age=25
```

---

### Delete Student

```http
DELETE /student/{student_id}
```

---

## Sample Data

```json
[
 {
  "id":1,
  "name":"Deepanshu",
  "age":22
 },
 {
  "id":2,
  "name":"Harshuuuu",
  "age":21
 }
]
```

---

## Future Improvements

* Database integration
* Validation using Pydantic
* Authentication
* Better error handling
* Store data permanently

---

## Author

Harsh Vardhan

