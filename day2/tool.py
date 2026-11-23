from common import *
import openai

def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages,
        tools=tools,
        extra_body={"thinking": {"type": "disabled"}},
    )
    return response.choices[0].message
tools=[{
    "type":"function",
    "function":{
        "name":"get_weather",
        "description":"Get weather of a location, the user should supply a location first.",
        "parameters":{
            "type":"object",
            "properties":{
                "location":{
                    "type":"string",
                    "description":"The location to get the weather from.",
                }
            },
            "required":["location"]
        },
    }
}]
messages=[{"role":"user","content":"今天杭州天气怎么样"}]
message=send_messages(messages)
print(f"User>\t {messages[0]['content']}")

tool = message.tool_calls[0]
messages.append(message)

messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})
message = send_messages(messages)
print(f"Model>\t {message.content}")