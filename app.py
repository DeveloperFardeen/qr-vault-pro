from flask import Flask, render_template
from config import Config
from models import db
from routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()

    return app

# Create app here
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
