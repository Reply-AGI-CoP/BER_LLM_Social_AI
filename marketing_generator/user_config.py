import os
import openai
from dotenv import load_dotenv


def setup_api_keys():
    """
    Set up and retrieve API keys for OpenAI and Stable Diffusion.
    
    Function loads environment variables containing API keys and initializes the necessary configurations for OpenAI and Stable Diffusion.
    """
    
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve and set the OpenAI API key from the environment variable
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Retrieve Stable Diffusion API key, Host and Engine
    engine_id = "stable-diffusion-xl-1024-v1-0" # The older Model is: "stable-diffusion-v1-5" -> Cheaper for Testing purposes
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    sd_api_key = os.getenv("STABILITY_API_KEY")

    return engine_id, api_host, sd_api_key