# AI Agent for Social Media Marketing Content

This project is an AI-based content marketing assistant for LinkedIn and Medium posts. It combines text generation using GPT-4 and image generation using Stable Diffusion to help users create engaging content.

## Features

- **Text Generation**: Generate engaging and tailored text content for social media posts or blog articles using GPT-4.
- **Image Generation**: Create visually appealing images to accompany the text using Stable Diffusion.
- **User-Friendly Interface**: Accessible via a Gradio-based web interface, making it easy for non-technical users to interact with the assistant.

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd Creative-Writing-Assistant

   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv

   ```

3. **Activate the Virtual Environment**:

   ```bash
   .\venv\Scripts\activate

   ```

4. **Install Dependencies:**:

   ```bash
   pip install -r requirements.txt

   ```

5. **Run the Application:**:
   ```bash
   python app.py
   ```

## Usage

1. **Open the Google Colab Notebook**:

   - Open the provided Colab notebook - https://colab.research.google.com/drive/16Xgy90vY6vEfBL7U_55Vjnrwlo-SOeKq?authuser=4#scrollTo=9deP6mo5CPB- in Google Colab.

2. **Install Dependencies**:

   - Run the cell that installs necessary packages:
     ```python
     !pip install diffusers["torch"] transformers accelerate
     !pip install pyngrok Flask
     ```

3. **Set up ngrok**:

   - Add your ngrok authtoken:
     ```python
     !ngrok config add-authtoken YOUR_NGROK_AUTHTOKEN
     ```
     Replace `YOUR_NGROK_AUTHTOKEN` with your actual ngrok authtoken.

4. **Initialize the Stable Diffusion Model**:

   - Run the cell that sets up the Stable Diffusion pipeline:
     ```python
     pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
     pipe = pipe.to("cuda")
     ```

5. **Start the Flask App and ngrok Tunnel**:

   - Run the cells that set up the Flask app and start the ngrok tunnel.
   - Note the ngrok URL provided in the output. It will look like:
     ```
     ngrok tunnel available at: https://xxxx-xx-xxx-xxx-xx.ngrok-free.app
     ```

6. **Update `app.py`**:
   - Copy the ngrok URL from the Colab notebook.
   - In your local `app.py` file, update the `NGROK_URL` variable with this URL:
     ```python
     NGROK_URL = "https://xxxx-xx-xxx-xxx-xx.ngrok-free.app"
     ```

### Running the Local Application

1. **Launch the Gradio Interface**:

   - Run the `app.py` file:
     ```bash
     python app.py
     ```
   - A Gradio interface will open in your web browser.

2. **Using the Gradio UI**:

   - **Platform**: Choose between LinkedIn and Medium.
   - **Topic**: Enter the main topic or focus of your post.
   - **Tone**: Select the desired tone for your content.
   - **Word Count**: Adjust the slider to set the approximate word count.
   - **Generate**: Click to create both text and image content.

3. **Output**:
   - The generated text and image will be displayed for review.
   - You can copy the text and save the image for your use.

Note: Ensure that your Colab notebook remains running while using the local application, as it provides the image generation service through the ngrok tunnel.

## Acknowledgments

- [gpt4free by xtekky](https://github.com/xtekky/gpt4free): For enabling access to GPT-3.5-turbo capabilities.
- [Gradio](https://github.com/gradio-app/gradio): For providing an easy-to-use interface for AI-powered applications.
- [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5): The original model developed by Runway ML, now hosted as a legacy version on Hugging Face.
