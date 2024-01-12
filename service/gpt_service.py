import openai

class ChatAssistant:
    def __init__(self, model="gpt-3.5-turbo-1106"):
        self.model = model
        self.messages = []

    def add_messages(self, system_content, user_content):
        system_message = {"role": "system", "content": system_content}
        user_message = {"role": "user", "content": user_content}
        self.messages.append(system_message)
        self.messages.append(user_message)

        client = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        response = client['choices'][0]['message']['content']
        return response
