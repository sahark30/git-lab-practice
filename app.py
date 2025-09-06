#!/usr/bin/env python3
import json

def load_config():
    """Load configuration from config.json"""
    with open('config.json', 'r') as f:
        return json.load(f)

def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}!"

def main():
    config = load_config()
    print(f"Welcome to {config['app_name']} v{config['version']}")
    
    # Get user input
    user_name = input("Please enter your name: ")
    print(greet(user_name))
    
    print(f"Debug mode: {config['settings']['debug']}")

if __name__ == "__main__":
    main()
