#!/bin/bash
python app.py &
cd ui && python gradio_app.py &