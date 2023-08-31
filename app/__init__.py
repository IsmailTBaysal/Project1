from flask import Flask


def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Configurations (e.g., secret keys, database URLs, etc.)

    # Register blueprints (route definitions)
    from . import routes
    app.register_blueprint(routes.bp)

    return app
