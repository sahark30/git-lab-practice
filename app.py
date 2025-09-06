#!/usr/bin/env python3
import json

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def greet(name):
    """A simple greeting function"""
    return f"Greetings, {name}! Welcome to our application."

def main():
    config = load_config()
    print(f"=== {config['app_name']} v{config['version']} ===")
    
    # Get user input
    user_name = input("What's your name? ")
    print(greet(user_name))
    
    if config['settings']['debug']:
        print("[DEBUG] Application running in debug mode")

if __name__ == "__main__":
    main()
