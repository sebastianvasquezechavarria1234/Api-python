from flask import Flask, request, jsonify
from models.triangulo import calcular_triangulo

app = Flask(__name__)

@app.route("/api/triangulo", methods=["POST"])
def calcular_triangulo_endpoint():
    data = request.get_json()

    # Validar datos obligatorios
    required = ["base", "altura", "lado1", "lado2"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"Falta el campo '{field}'"}), 400

    base = data["base"]
    altura = data["altura"]
    lado1 = data["lado1"]
    lado2 = data["lado2"]

    # Llamar al modelo
    area, perimetro = calcular_triangulo(base, altura, lado1, lado2)

    # Respuesta JSON
    return jsonify({
        "base": base,
        "altura": altura,
        "lado1": lado1,
        "lado2": lado2,
        "area": area,
        "perimetro": perimetro
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
