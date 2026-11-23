from common import *

import json
system_prompt = """
The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

EXAMPLE INPUT: 
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "Which is the highest mountain in the world?",
    "answer": "Mount Everest"
}
"""
user_prompt = """  五岳有哪些？ """
messages=[
    {"role":"system","content":system_prompt},
    {"role":"user","content":user_prompt},
]

response= client.chat.completions.create(
    model="deepseek-flash",
    messages=messages,
    response_format={
        'type':'json_object',
    }
)
print(json.loads(response.choices[0].message.content))