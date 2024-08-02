import json
import os

# MISSION
# Grab the appropraite directory(base aerodrome tokens) and log them to console


# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

json_file_path = os.path.join(current_dir, 'tokenLists', 'lists', '8453', 'aerodrome.json')
print(f"Attempting to open file: {json_file_path}")



try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    print("Successfully loaded JSON data.")
    print(json.dumps(data, indent=2))

    for token in data.get('tokens', []):
        print(f"Token: {token.get('symbol')} - Address: {token.get('address')}")

except FileNotFoundError:
    print(f"Error: The file '{json_file_path}' was not found.")
    print("Please check if the file path is correct and the file exists.")

except json.JSONDecodeError:
    print(f"Error: The file '{json_file_path}' is not a valid JSON file.")
    print("Please check the file contents and ensure it's properly formatted.")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

