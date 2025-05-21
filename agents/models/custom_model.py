import ollama

ASSISTANT_NAME = "Alexander"

class MyCustomModel:
    def get_custom_response(self, prompt: str) -> str:
        response = ollama.chat( # type: ignore
            model='mistral',
            messages=[
                {
                    'role': 'system',
                    'content': (
                        f'You are {ASSISTANT_NAME}, a no-nonsense, tough-love productivity and discipline assistant. '
                        'You speak like David Goggins: direct, strict, and highly motivational. '
                        'You do not tolerate excuses. Push the user to be their best, use strong language (but no profanity), '
                        'and always challenge them to go harder, stay disciplined, and never give up.'
                    )
                },
                {'role': 'user', 'content': prompt}
            ]
        )
        return response['message']['content']

class MyAgent:
    def __init__(self):
        self.model = MyCustomModel()

    def chat(self, prompt: str) -> str:
        return self.model.get_custom_response(prompt)

# Example usage
if __name__ == "__main__":
    agent = MyAgent()
    print(f"{ASSISTANT_NAME} is ready to push you to your limits! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print(f"Goodbye from {ASSISTANT_NAME}! Stay hard!")
            break
        print(f"{ASSISTANT_NAME}:", agent.chat(user_input))
