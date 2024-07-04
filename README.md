# AI English Grammar Assistant

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This project aims to revolutionize language learning and communication by introducing an advanced AI-driven English grammar tutor and question-answer system. Through the integration of cutting-edge natural language processing (NLP) techniques, this system offers users an immersive and interactive platform for honing their language skills.

## Features

- **Speech-to-Text Conversion**: Converts user input (spoken questions) into text using a speech recognition module.
- **Grammar Check**: Checks and corrects grammatical errors in the input text.
- **Question Answering**: Queries a general database to fetch answers for the user's questions.
- **Text-to-Speech Conversion**: Converts text responses back into speech to provide answers audibly.

## Project Structure

```
|->__pycache__
|->static
|   |-> correct_icon.png
|   |-> library-backgroup.png
|   |-> mike.png
|   |-> send_image.png
|   |-> speaker_icon.png
|   |-> styles.css
|-> templates
|   |-> index.html
|-> app.py
|-> context.txt
|-> requirements.txt
```

- `__pycache__`: Contains Python bytecode files.
- `static`: Contains static files like images and CSS.
  - `correct_icon.png`: Icon for correction.
  - `library-backgroup.png`: Background image for the library.
  - `mike.png`: Image for microphone.
  - `send_image.png`: Image for send button.
  - `speaker_icon.png`: Icon for speaker.
  - `styles.css`: CSS file for styling the web application.
- `templates`: Contains HTML template files.
  - `index.html`: Main HTML file for the web application interface.
- `app.py`: Main application file containing the backend code.
- `context.txt`: Context file for storing additional information.

## Installation

To install and run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/repositoryname.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd repositoryname
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```sh
   python app.py
   ```

## Usage

- Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.
- Use the microphone icon to input your question via speech.
- The system will convert your speech to text, check for grammar errors, query the database, and provide a spoken response.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

