# Multilingual Translator Flask Server

A Flask-based server that provides endpoints for multilingual translations using Hugging Face's 🤗 Transformers.

## Features

- **Multilingual Support**: Translates across multiple languages including English, German, Arabic, and many others.
- **Auto Language Detection**: Automatically detects the source language if not provided.
- **Flexible Input**: Translates raw texts and JSON payloads, retaining the structure of the JSON input.
- **File Generation**: Generates a translated JSON file in the `/output/date/` directory.
- **Modularity**: Uses the MVC pattern for organized and maintainable code.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Pip

### Setup & Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/translator_server.git
   cd translator_server

### Setup Virtual Environment:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies:

```
pip install -r requirements.txt
```

### IEnvironment Variables:
1. Ensure your .env file is in the root directory and contains:

```
FLASK_PORT=8000
```

### Run the Server::


```
python app.py
```

This will start the Flask server on the port specified in the .env file (default to 8000).

API Endpoints
Translate Text:

Endpoint: /translate_text
Method: POST
Data Params: input_text (required), target_language (optional)
Translate JSON Payload:

Endpoint: /translate_json
Method: POST
Data Params: input_json (required), input_language (optional), target_language (required)
Translate and Save to File:

Endpoint: /translate_save
Method: POST
Data Params: input_json (required), input_language (optional), target_language (required)


###Testing
To run tests:

```
python test_server.py
```

Contributing
Fork the project.
Create your feature branch: git checkout -b feature/AmazingFeature
Commit your changes: git commit -m 'Add some AmazingFeature'
Push to the branch: git push origin feature/AmazingFeature
Open a pull request.

License
Distributed under the MIT License. See LICENSE for more information.