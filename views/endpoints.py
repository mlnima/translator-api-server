from flask import Blueprint, request, jsonify, send_from_directory
from controllers.translation_controller import translate_single_text, translate_json_text, save_translated_json

endpoints_bp = Blueprint('endpoints', __name__)


@endpoints_bp.route('/translate_text', methods=['POST'])
def translate_text_endpoint():
    return translate_single_text(request)


@endpoints_bp.route('/translate_json', methods=['POST'])
def translate_json_endpoint():
    return translate_json_text(request)


@endpoints_bp.route('/save_translated_json', methods=['POST'])
def save_translated_json_endpoint():
    return save_translated_json(request)


@endpoints_bp.route('/output/<path:filename>', methods=['GET'])
def get_output(filename):
    return send_from_directory('output', filename, as_attachment=True)


@endpoints_bp.errorhandler(Exception)
def handle_server_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500