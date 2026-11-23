import os

from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent/".env")
MODEL="deepseek-flash"
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
    timeout=60.0,
)
NO_THINK = {"thinking": {"type": "disabled"}}
NO_THINK_BODY = {"thinking": {"type": "disabled"}}
