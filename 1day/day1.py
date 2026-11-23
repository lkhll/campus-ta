import os
from openai import OpenAI
from openai.resources.skills import content

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
蓝色大肥鱼:今天杭州的天气是晴，温度29℃喵。
"""
prompt = f"""
规范
{text}
示例
{content}
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