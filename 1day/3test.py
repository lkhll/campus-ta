from common import client, MODEL

messages = [{"role": "system", "content": "你是简洁的中文助手。"}]


def ask(text: str) -> str:
    messages.append({"role": "user", "content": text})
    resp = client.chat.completions.create(model=MODEL, messages=messages)
    answer = resp.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    return answer


print("A:", ask("我叫奶茶，记住我的名字。"))
print("B:", ask("我叫什么？"))
print("条数:", len(messages))