import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src.routes.triangulo_routes import triangulo_bp

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(triangulo_bp, url_prefix='/api')

    # Global Error Handlers
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

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "True") == "True"
    app.run(host="0.0.0.0", port=port, debug=debug)
