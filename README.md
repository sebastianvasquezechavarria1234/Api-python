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
