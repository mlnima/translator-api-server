from flask import Flask
from views.endpoints import endpoints_bp
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.register_blueprint(endpoints_bp)

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5000))  # Default to 5000 if not found
    app.run(host='0.0.0.0', port=port, debug=True)
