from flask import jsonify, make_response
from models_util.translation_model import TranslationModel
import os
import json
from datetime import datetime

model = TranslationModel()


def translate_single_text(req_data):
    data = req_data.json
    text = data.get('text', '')
    target_language = data.get('target_language', 'en')
    translation = model.translate_text(text, target_language)[0]
    return jsonify({"translated_text": translation})


def translate_json_text(req_data):
    data = req_data.json
    translation_data = data.get('translationData', {})
    target_language = data.get('target_language', 'en')
    translated_data = {}

    for key, value in translation_data.items():
        translated_data[key] = model.translate_text(value, target_language)[0]

    return jsonify(translated_data)


def save_translated_json(req_data):
    try:
        data = req_data.get_json()
        translation_data = data.get('translationData', {})
        target_language = data.get('target_language', 'en')
        translated_data = {}

        for key, value in translation_data.items():
            translated_data[key] = model.translate_text(value, target_language)[0]

        if not os.path.exists('output'):
            os.makedirs('output')

        filename = f"translated_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        filepath = os.path.join('output', filename)
        with open(filepath, 'w', encoding='utf-8') as outfile:
            json.dump(translated_data, outfile, ensure_ascii=False, indent=4, sort_keys=True)

        return jsonify({"message": f"Translation saved to {filepath}"})

    except json.JSONDecodeError:
        # Return an error response
        return make_response(jsonify(error="Invalid JSON provided"), 400)
