def evaluate_expression(expression: str) -> str:
    """
    Evaluate a simple Python math expression safely.
    """
    try:
        # VERY basic safety restriction
        allowed_names = {"__builtins__": {}}
        result = eval(expression, allowed_names, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
