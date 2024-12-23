# AI Script Generator

This project is an AI-powered script generator built with Django and Django REST Framework. It allows users to generate scripts based on prompts and optional file uploads.

## Features

- Generate scripts using AI based on user prompts.
- Optionally include file uploads to enhance script generation.
- Save generated scripts in the database.

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework
- OpenAI API

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/ai-script-generator.git
cd ai-script-generator

```
2. Create and activate a virtual environment:

```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

```
3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
Create a .env file in the root directory and add your OpenAI API key:
```sh
OPENAI_API_KEY=your_openai_api_key
```


5.Apply migrations:
```sh
python manage.py migrate
```
6.Run the development server:
```sh
python manage.py runserver
```

