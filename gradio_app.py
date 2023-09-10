from models_util.translation_model import TranslationModel
import gradio as gr
import json

languages = ["en", "de", "ar", "da", "el", "es", "fa", "fi", "fr", "hi", "hu", "it", "ja", "ko", "nl", "no", "pl", "pt",
             "ru", 'cs', "sk", "sl", "sv", "tr", "zh"]

# Initialize the model
model = TranslationModel()


def translate_interface(text, target_language="en"):
    translation = model.translate_text(text, target_language)[0]
    return translation


def translate_json_interface(json_str, target_language="en"):
    try:
        data = json.loads(json_str)
        translated_data = {}

        for key, value in data.items():
            translated_value = model.translate_text(f"{value}", target_language)
            translated_data[key] = translated_value[0]

        # return json.dumps(translated_data, indent=4)
        sorted_translated_data = dict(sorted(translated_data.items()))
        return json.dumps(sorted_translated_data, indent=4)

    except:
        return json.dumps({"error": "Error in JSON or translation."}, indent=4)


# def multi_translate_interface(text, json_str, files, target_language="en"):
#     try:
#         # Handling text input
#         if text:
#             translation = model.translate_text(text, target_language)[0]
#             return translation, None, None
#
#         # Handling JSON string input
#         if json_str:
#             data = json.loads(json_str)
#             translated_data = {}
#             for key, value in data.items():
#                 translated_value = model.translate_text(f"{value}", target_language)
#                 translated_data[key] = translated_value[0]
#             return None, json.dumps(translated_data, indent=4), None
#
#         # Handling file input
#         if files:
#             results = []
#             for file_content in files:
#                 try:
#                     # Attempt to interpret file content as JSON
#                     data = json.loads(file_content)
#                     translated_data = {}
#                     for key, value in data.items():
#                         translated_value = model.translate_text(f"{value}", target_language)
#                         translated_data[key] = translated_value[0]
#                     results.append(json.dumps(translated_data, indent=4))
#                 except:
#                     # If not JSON, treat as text
#                     translation = model.translate_text(file_content, target_language)[0]
#                     results.append(translation)
#             return None, None, "\n\n".join(results)
#
#     except:
#         return "Error in JSON or translation.", None, None


iface1 = gr.Interface(
    title='JSON',
    fn=translate_json_interface,
    inputs=["textarea", gr.Dropdown(choices=languages, label="Target Language")],
    outputs="json"
)

iface2 = gr.Interface(
    title='Text',
    fn=translate_interface,
    inputs=[
        "textarea",
        gr.Dropdown(choices=languages, label="Target Language")
    ],
    outputs="textarea"
)

# iface3 = gr.Interface(
#     title='Multi-Translate',
#     fn=multi_translate_interface,
#     inputs=[
#         "textarea",
#         "textarea",
#         gr.File(label="Upload File(s)", type="file"),
#         gr.Dropdown(choices=languages, label="Target Language")
#     ],
#     outputs=[
#         "textarea",
#         "json",
#         gr.File(label="Download Translated Files")
#     ]
# )
# Group the interfaces
group = gr.TabbedInterface([iface1, iface2], tab_names=['JSON', 'Text'])
group.launch()
