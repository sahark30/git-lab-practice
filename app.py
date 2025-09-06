#!/usr/bin/env python3
import json
from datetime import datetime

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def greet(name):
    """A simple greeting function with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Greetings, {name}! Welcome to our application. (Greeted at {timestamp})"

def main():
    config = load_config()
    print(f"=== {config['app_name']} v{config['version']} ===")
    print("-" * 40)
    
    # Get user input
    user_name = input("What's your name? ")
    greeting = greet(user_name)
    print(greeting)
    
    print("-" * 40)
    if config['settings']['debug']:
        print("[DEBUG] Application running in debug mode")
    print(f"Max users supported: {config['settings']['max_users']}")

if __name__ == "__main__":
    main()
