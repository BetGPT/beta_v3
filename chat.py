from context_manager import get_conversation_context
from openai_api import chatgpt_completion
import os

if __name__ == "__main__":
    conversation = get_conversation_context()
    
    while True:
        user_input = input('\n\nUSER: ')
        conversation.append({'role': 'user', 'content': user_input})
        
        response = chatgpt_completion(conversation)
        conversation.append({'role': 'assistant', 'content': response})
        
        print('\n\nVINNY: %s' % response)
