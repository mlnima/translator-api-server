import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
BASE_URL = f"http://localhost:{os.environ.get('FLASK_PORT', 7860)}"
target_language = "fa"


def test_translate_text():
    url = f"{BASE_URL}/translate_text"
    data = {
        "text": "This website collects cookies to deliver better user experience",
        "target_language": target_language
    }
    response = requests.post(url, json=data)
    result = response.json()
    print("Translate Text Response:", result)


def test_translate_json():
    url = f"{BASE_URL}/translate_json"
    data = {
        "translationData": {
            "Home": "Home",
            "You Need To Log In": "You Need To Log In",
            "Categories": "Categories"
        },
        "target_language": target_language
    }
    response = requests.post(url, json=data)
    result = response.json()
    print("Translate JSON Response:", result)


def test_save_translated_json():
    url = f"{BASE_URL}/save_translated_json"
    data = {
        "translationData": {
            "Home": "Home",
            "You Need To Log In": "You Need To Log In",
            "Categories": "Categories",
            "Tags": "Tags"
        },
        "target_language": target_language
    }
    response = requests.post(url, json=data)

    # Print the raw response for debugging
    print(f"HTTP Status Code: {response.status_code}")
    print(f"Raw Response: {response.text}")

    # Attempt to decode as JSON only if response is OK and content type is application/json
    if response.status_code == 200 and response.headers.get('content-type') == 'application/json':
        result = response.json()
        print("Save Translated JSON Response:", result["message"])
    else:
        print("Server did not return a valid JSON response.")


def run_tests():
    test_translate_text()
    test_translate_json()
    test_save_translated_json()


if __name__ == '__main__':
    run_tests()
