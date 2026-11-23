import time

from common import client, MODEL

start = time.perf_counter()
stream = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "用 100 字介绍杭州"}],
    stream=True,
)

first = None
for chunk in stream:
    piece = chunk.choices[0].delta.content if chunk.choices else None
    if piece:
        if first is None:
            first = time.perf_counter()
            print(f"[TTFT {first - start:.2f}s] ", end="")
        print(piece, end="", flush=True)

print(f"\n[总耗时 {time.perf_counter() - start:.2f}s]")