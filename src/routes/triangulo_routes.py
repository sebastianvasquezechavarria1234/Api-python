from flask import Blueprint, request, jsonify
import logging
from src.services.triangulo_service import calcular_triangulo

logger = logging.getLogger(__name__)
triangulo_bp = Blueprint('triangulo', __name__)

@triangulo_bp.route("/triangulo", methods=["POST"])
def calcular_triangulo_endpoint():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

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

    # Validar desigualdad del triángulo
    if not (base + lado1 > lado2 and base + lado2 > lado1 and lado1 + lado2 > base):
        logger.warning(f"Invalid triangle inequality: base={base}, lado1={lado1}, lado2={lado2}")
        return jsonify({"error": "The provided sides (base, lado1, lado2) do not form a valid triangle"}), 400

    # Llamar al servicio
    logger.info(f"Calculating triangle for base={base}, altura={altura}")
    area, perimetro = calcular_triangulo(base, altura, lado1, lado2)

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
