from common import MODEL,client,NO_THINK
LABELS=["闲聊","多步任务","查数据","知识问答"]

FEW_SHOT="""

示例:
用户:帮我查询一下灭建国的成绩，如果不及格给它打电话→多步任务
用户:今天天气不错→闲聊
用户:杭州的GDP怎么样→查数据
用户:rag是什么→知识问答
用户:你叫什么名字 → 闲聊
用户:embedding 和向量库有什么关系 → 知识问答
用户:张三高数多少分 → 查数据
用户:先看课表，再告诉我明天几节课 → 多步任务

"""
PROMPT="""
你是意图分析器，你只能输出下面4个标签中的其中一个，不要解释，不要标点
标签:
{labels}
{few_shot}
用户:{text}
标签:
"""
def classify(text: str) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT.format(
            labels="/".join(LABELS), few_shot=FEW_SHOT, text=text)}],
        temperature=0,
        max_tokens=10,
        extra_body=NO_THINK,
    )
    out = (resp.choices[0].message.content or "").strip()
    for label in LABELS:
        if label in out:
            return label
    return "未知"


TESTS = [
    ("你好呀", "闲聊"),
    ("今天心情不太好", "闲聊"),
    ("RAG 和微调有什么区别", "知识问答"),
    ("什么是向量数据库", "知识问答"),
    ("王五的数据库考了多少", "查数据"),
    ("李四的英语成绩是多少", "查数据"),
    ("查一下我的课表，再推荐两门选修", "多步任务"),
    ("先看张三的成绩，再根据天气建议他去哪自习", "多步任务"),
    ("帮我查一下", "查数据"),      # 边界：信息不全
    ("嗯", "闲聊"),                # 边界：无意义输入
]

if __name__ == "__main__":
    correct = 0
    for text, expected in TESTS:
        got = classify(text)
        ok = got == expected
        correct += ok
        print(f"{'OK ' if ok else 'ERR'}  {text} -> {got}（期望 {expected}）")
    print(f"\n准确率：{correct}/{len(TESTS)}")