from openai import OpenAI, RateLimitError
from src.config import OPENAI_API_KEY, OPENAI_MODEL
from src.prompts import SYSTEM_PROMPT
from src.tools import evaluate_expression

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_agent(question: str):
    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions=SYSTEM_PROMPT,
        input=question,
        tools=[
            {"type": "web_search"},
            {
                "type": "function",
                "name": "evaluate_expression",
                "description": "Evaluate a mathematical expression",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {"type": "string"}
                    },
                    "required": ["expression"]
                }
            }
        ]
    )

    # --- TOOL LOOP ---
    while True:
        tool_calls = [
            item for item in response.output
            if item.type == "tool_call"
        ]

        if not tool_calls:
            break

        tool_outputs = []

        for call in tool_calls:
            if call.name == "evaluate_expression":
                args = call.arguments
                result = evaluate_expression(**args)

                tool_outputs.append({
                    "type": "tool_result",
                    "tool_call_id": call.id,
                    "output": result
                })

        # Send tool results back to model
        response = client.responses.create(
            model=OPENAI_MODEL,
            instructions=SYSTEM_PROMPT,
            input=tool_outputs,
            previous_response_id=response.id
        )

    return response

#except RateLimitError as e:
#        raise RuntimeError(
#            "API quota exceeded. Check billing at https://platform.openai.com/account/billing"
#        ) from e
