from flask import Flask, request, jsonify
from models.triangulo import calcular_triangulo

app = Flask(__name__)

@app.route("/api/triangulo", methods=["POST"])
def calcular_triangulo_endpoint():
    data = request.get_json()

    # Validar datos obligatorios y tipos
    required = ["base", "altura", "lado1", "lado2"]
    values = {}
    
    for field in required:
        if field not in data:
            return jsonify({"error": f"Missing required field: '{field}'"}), 400
        
        val = data[field]
        if not isinstance(val, (int, float)):
            return jsonify({"error": f"Field '{field}' must be a number"}), 400
        
        if val <= 0:
            return jsonify({"error": f"Field '{field}' must be greater than zero"}), 400
        
        values[field] = val

    base = values["base"]
    altura = values["altura"]
    lado1 = values["lado1"]
    lado2 = values["lado2"]

    # Validar desigualdad del triángulo (los lados deben ser base, lado1, lado2)
    if not (base + lado1 > lado2 and base + lado2 > lado1 and lado1 + lado2 > base):
        return jsonify({"error": "The provided sides (base, lado1, lado2) do not form a valid triangle"}), 400

    # Llamar al modelo
    area, perimetro = calcular_triangulo(base, altura, lado1, lado2)

    # Respuesta JSON
    return jsonify({
        "status": "success",
        "data": {
            "base": base,
            "altura": altura,
            "lado1": lado1,
            "lado2": lado2,
            "area": area,
            "perimetro": perimetro
        }
    }), 200

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request", "message": str(e.description)}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found", "message": "The requested URL was not found on the server"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed", "message": "The method is not allowed for the requested URL"}), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "message": "An unexpected error occurred on the server"}), 500

if __name__ == "__main__":
    app.run(debug=True)
