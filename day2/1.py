"""练习 1：模糊版 vs 四件套对照，并写入 notes_d2.md。"""
from pathlib import Path

from common import client, MODEL, NO_THINK

VAGUE = "介绍一下 RAG"

STRUCTURED = """你是给大四学生讲课的助教。
任务：解释 RAG 是什么、为什么需要它。
约束：
1. 不超过 200 字
2. 不用学术术语
3. 必须举一个生活例子
输出格式：三行，分别是“是什么 / 为什么 / 例子”。
"""

NOTES = Path(__file__).resolve().parent / "notes_d2.md"


def ask(prompt: str):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        extra_body=NO_THINK,
    )
    return resp.choices[0].message.content, resp.usage.completion_tokens


def main():
    rows = ["# D2 练习 1 记录\n"]
    for name, prompt in [("模糊版", VAGUE), ("四件套", STRUCTURED)]:
        text, tokens = ask(prompt)
        print(f"\n===== {name}（{tokens} tokens）=====")
        print(text)
        rows.append(f"## {name}（{tokens} tokens）\n\n```\n{text}\n```\n")
    NOTES.write_text("\n".join(rows), encoding="utf-8")
    print(f"\n已写入 {NOTES}")


if __name__ == "__main__":
    main()