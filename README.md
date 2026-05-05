# Triangle API - Python

A robust Flask-based REST API designed to calculate geometric properties of triangles, such as area and perimeter. This project follows professional software engineering practices, including modular architecture, input validation, and automated testing.

## Tech Stack

- **Language:** Python 3.x
- **Framework:** Flask
- **Documentation:** Flasgger (Swagger/OpenAPI)
- **Testing:** Pytest
- **Environment Management:** python-dotenv
- **CORS Support:** Flask-CORS

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sebastianvasquezechavarria1234/Api-python.git
   cd Api-python
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   PORT=5000
   DEBUG=True
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

## API Documentation

### Calculate Triangle Properties

- **URL:** `/api/triangulo`
- **Method:** `POST`
- **Content-Type:** `application/json`

**Request Body Example:**
```json
{
  "base": 10,
  "altura": 5,
  "lado1": 10,
  "lado2": 10
}
```

**Success Response (200 OK):**
```json
{
  "status": "success",
  "data": {
    "base": 10,
    "altura": 5,
    "lado1": 10,
    "lado2": 10,
    "area": 25.0,
    "perimetro": 30.0
  }
}
```

**Error Response (400 Bad Request):**
```json
{
  "error": "Field 'base' must be a number",
  "message": "Specific details about the validation error"
}
```
