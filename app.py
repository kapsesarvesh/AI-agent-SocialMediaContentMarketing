from g4f.client import Client
import gradio as gr
import requests
from PIL import Image
from io import BytesIO

# Initialize the G4F client
client = Client()

# ngrok tunnel URL (use the one generated from your Colab notebook)
NGROK_URL = "#paste the URL generated in Google Colab here"

# Define the function for generating marketing content
def generate_marketing_content(platform, topic, tone, length):
    # Generate text using G4F
    prompt = f"Create a {platform} post about {topic}. The tone should be {tone} and the length should be approximately {length} words."
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    text_content = response.choices[0].message.content
    
    # Generate an image based on the topic using the Stable Diffusion model via the ngrok tunnel
    image_prompt = f"Create an image related to this prompt: {topic}."
    image_url = f"{NGROK_URL}/generate_image"
    
    # Send a POST request to the ngrok image generation API
    try:
        image_response = requests.post(image_url, json={"prompt": image_prompt})
        image = Image.open(BytesIO(image_response.content))
    except Exception as e:
        # In case of any error, use a placeholder image
        image = Image.open("path/to/placeholder_image.png")  # Use an actual placeholder image file

    return text_content, image

# Gradio user interface
interface = gr.Interface(
    fn=generate_marketing_content,
    inputs=[
        gr.Dropdown(["LinkedIn", "Medium"], label="Platform"),
        gr.Textbox(lines=2, placeholder="Enter the main topic or focus of your post...", label="Topic"),
        gr.Dropdown(["Professional", "Casual", "Inspirational", "Educational"], label="Tone"),
        gr.Slider(100, 1000, step=50, label="Approximate word count")
    ],
    outputs=[
        gr.Textbox(label="Generated Content"),
        gr.Image(label="Generated Image")
    ],
    title="Marketing Content Assistant for LinkedIn and Medium 📝",
    description="Generate engaging marketing content for your LinkedIn and Medium posts.",
    theme="huggingface",
    examples=[
        ["LinkedIn", "The impact of AI on digital marketing", "Professional", 300],
        ["Medium", "5 effective social media strategies for small businesses", "Educational", 500],
        ["LinkedIn", "How our company achieved 50% growth in Q2", "Inspirational", 200],
    ]
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()