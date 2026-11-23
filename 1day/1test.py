from common import client, MODEL

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "你叫什么，为什么有人叫你蓝色大肥鱼"}],
)
print(resp.choices[0].message.content)
