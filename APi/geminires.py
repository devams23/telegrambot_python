import os
from dotenv import load_dotenv
import google.generativeai as genai

# Function to generate content based on a course input
def handle_response(text):
    # Load environment variables if needed
    load_dotenv()

    # Configure the generative AI model
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    generation_config = {
        "temperature": 0.6,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings if needed
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    # Prompt to generate a detailed roadmap for the specified course
    prompt = [
        f"behave as if you are a monkey and whose purpose is to jumpo into others life. someone is talking to you , saying{text}"
    ]

    # Generate content based on the prompt
    
    response = model.generate_content(prompt)
    print(response)
    # Extract the generated text from the response
    res = response.text

    return res
