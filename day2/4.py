"""练习 3：直接回答 / 显式 CoT / 思考模式 三组对照。"""
import csv
import time
from pathlib import Path

from common import client, MODEL, NO_THINK

QUESTIONS = [
    "一个班 40 人，60% 是女生，女生里 25% 戴眼镜。戴眼镜的女生有多少人？",
    "今天是 2026 年 11 月 18 日星期三，从今天算起第 100 天是星期几？",
    "小明比小红高，小红比小刚高，小刚比小丽高。四个人里谁最矮？",
]

COT_SUFFIX = "\n请一步一步推理，最后单独一行写「答案：<最终答案>」。"
OUT = Path(__file__).resolve().parent / "d2_cot_results.csv"   # 新增
ROWS = []                                                      # 新增


def run(question: str, mode: str):
    if mode == "思考模式":
        extra = {"extra_body": {"thinking": {"type": "enabled"}}}
    else:
        extra = {"extra_body": NO_THINK}

    prompt = question if mode != "显式CoT" else question + COT_SUFFIX
    start = time.perf_counter()
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,                              # 新增：三组统一
        **extra,
    )
    cost = time.perf_counter() - start
    msg = resp.choices[0].message
    return (
        msg.content,
        resp.usage.completion_tokens,
        cost,
        getattr(msg, "reasoning_content", None) or "",   # 新增
    )


if __name__ == "__main__":
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\n########## 第 {i} 题：{q}")
        for mode in ["直接", "显式CoT", "思考模式"]:
            text, tokens, cost, reasoning = run(q, mode)
            print(f"\n--- {mode}（{tokens} tokens, {cost:.2f}s）---")
            if reasoning:
                print(f"[思考] {reasoning[:300]}")
            print(text)
            ROWS.append({                                  # 新增
                "题": i, "模式": mode,
                "tokens": tokens, "秒": round(cost, 2),
                "回答": text, "思考": reasoning,
            })

    with OUT.open("w", newline="", encoding="utf-8-sig") as f:   # 新增
        w = csv.DictWriter(f, fieldnames=["题", "模式", "tokens", "秒", "回答", "思考"])
        w.writeheader()
        w.writerows(ROWS)
    print(f"\n已写入 {OUT}")