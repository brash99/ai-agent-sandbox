import json
import sys

from src.run_agent import ask_agent
from src.logger import save_response

def extract_text(response) -> str:
    # The SDK exposes a convenience property in many examples,
    # but we also keep the full object logged for inspection.
    text = getattr(response, "output_text", None)
    if text:
        return text

    # Fallback for safety if shape changes or property is absent
    try:
        return json.dumps(response.model_dump(), indent=2)
    except Exception:
        return str(response)

def main():
    if len(sys.argv) < 2:
        print('Usage: python -m src.main "your question here"')
        sys.exit(1)

    question = sys.argv[1]
    response = ask_agent(question)

    try:
        dumped = response.model_dump()
    except Exception:
        dumped = {"raw": str(response)}

    log_path = save_response(dumped)
    print("\n=== ANSWER ===\n")
    print(extract_text(response))
    print(f"\n[full response saved to {log_path}]")

if __name__ == "__main__":
    main()
