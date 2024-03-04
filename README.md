# PresentSmart

PresentSmart is a Python-based tool that utilizes AI to create on-point and in-depth PowerPoint presentations by generating notes. It is designed for both teachers and students, making it a versatile tool for educational purposes. The tool leverages the powerful GPT-3.5 Turbo engine for text generation, the Google Cloud Storage (GCS) for attaching related images, and the pptx library to generate PowerPoint files and add slides. Additionally, PresentSmart provides a user-friendly graphical user interface (GUI) implemented using the Tkinter library.

## Demo Video



https://github.com/parthgupta1208/PresentSmart/assets/114602309/dc8a0ded-af9f-4ce3-a284-746798a917b2

## Features

- Automatically generates notes-based PowerPoint presentations using AI technology.
- Makes use of the advanced GPT-3.5 Turbo engine for accurate and relevant text generation.
- Integrates with Google Cloud Storage (GCS) to attach related images to the presentations.
- Utilizes the `pptx` library to create and manipulate PowerPoint files, adding slides dynamically.
- Offers a user-friendly GUI powered by the Tkinter library, allowing for an intuitive user experience.

## Installation

1. Clone this repo.

2. Install the required dependencies using pip (NOTE: use conda env and python 3.11).
    - ```pip install python_pptx```
    - ```pip install openai```
    - ```pip install google_images_search```

3. Setup a `.envrc` file as below (you can use direnv to load these env vars):
    - OPENAI_KEY="user-value"
    - GCS_DEVELOPER_KEY=user-value
    - GCS_CX=user-value

## Usage

1. Add keyword in main.py

2. Run code and see generated powerpoint


## License

[MIT License](LICENSE)


