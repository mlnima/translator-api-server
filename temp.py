import json
from models_util.translation_model import TranslationModel

model = TranslationModel()

json_str = '''{
    "Home": "Home",
    "You Need To Log In": "You Need To Log In",
    "Categories": "Categories",
    "Tags": "Tags",
    "Actors": "Actors",
    "Email": "Email",
    "Login": "Login"
}'''

data = json.loads(json_str)

translated_data = {}

for key, value in data.items():
    translated_value = model.translate_text(f"{value}", 'de')
    translated_data[key] = translated_value[0]

print(json.dumps(translated_data, indent=4))
