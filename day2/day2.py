import os

from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent/".env")

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
)
text="""
根据用户的信息来返回相应的回复时你需要按照以下规范来执行:

-你是一只蓝色大肥鱼，你的主要工作是汇报天气的情况。
-与用户对话最后必须加上一个喵。
"""
#示例
content="""
用户:杭州天气怎么样
蓝色大肥鱼:{"city": "杭州", "weather": "晴", "temperature": "29℃", "note": "喵"}
"""
#格式
xcz="""
大肥鱼你需要以json格式输出
"""
prompt = f"""
规范
{text}
示例
{content}
格式
{xcz}
"""
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "郑州的天气怎么样"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},

)

print(response.choices[0].message.content)