import json

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

def get_conversation_context():
    scratchpad = open_file('data/scratchpad.txt')
    system_message = open_file('data/system_prompt.txt').replace('<<INPUT>>', '')
    system_message += scratchpad
    
    conversation = [{'role': 'system', 'content': system_message}]
    return conversation

