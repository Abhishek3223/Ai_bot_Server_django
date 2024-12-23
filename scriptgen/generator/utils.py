from PIL import Image
import pytesseract
from pdfminer.high_level import extract_text
from openai import OpenAI


# Get the API key and base URL from environment variables
api_key = "YOUR_API_KEY"


# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)


# Function to handle file uploads
def handle_file_upload(file):
    if file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    elif file.name.endswith('.pdf'):
        return extract_text(file)
    elif file.name.endswith(('png', 'jpg', 'jpeg')):
        # For images, use OCR to extract text
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text
    return ''


def generate_script_from_api(prompt, link=None):

    try:
        # Prepare messages for the API request
        messages = [
            {"role": "system", "content": "You are Grok, an AI designed to assist with script generation."},
            {"role": "user", "content": f"Prompt: {prompt}"},
        ]

        # Optionally include the link if provided
        if link:
            messages.append({"role": "user", "content": f"Consider this link: {link}"})

        # Make the API request x
        completion = client.chat.completions.create(
            model="grok-2-1212",  # Replace with your actual model name
            messages=messages,
        )

        # Extract and return the content from the response
        # print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    except Exception as e:
        # Handle exceptions and return a user-friendly error message
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

