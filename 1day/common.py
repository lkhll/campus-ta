"""D1 习题共用客户端。"""
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

HERE = Path(__file__).resolve().parent

# 优先读当前目录的 .env，其次读上一级的 .env
for candidate in (HERE / ".env", HERE.parent / ".env"):
    if candidate.exists():
        load_dotenv(candidate)
        break

MODEL = "deepseek-flash"
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    timeout=60.0,
)
