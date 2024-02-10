# Language Translator

This is a simple language translator application built in Python using the MarianMT model from Hugging Face.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

### Clone the Repository

Clone the repository to your local machine using the following command:


	git clone https://github.com/kmparks60/translator.git


### Install Dependencies

Navigate to the project directory and install the required dependencies:

	cd translator
	pip install -r required.txt 

### Run the Application

	python translator.py
		or 
	python3 translator.py

The GUI window will appear, allowing you to select source and target languages, input text, and click the "Translate" button.

### Usage

1. Select the source language from the dropdown menu.
2. Select the target language from the dropdown menu.
3. Enter the text you want to translate in the provided text box.
4. Click the "Translate" button.
5. The translated text will appear in the output box.

### Language List
This is a list of every language offered by Hugging Face and the corresponding language code.

	https://huggingface.co/languages

### Dependencies

Ensure you have the follwing dependencies installed. You can install them using the provided `required.txt` file:

	pip install -r required.txt

- sacremoses
- sentencepiece
- tensorflow
- torch
- transformers

### If you'd like to contribute, please fork the repository, create a new branch, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.