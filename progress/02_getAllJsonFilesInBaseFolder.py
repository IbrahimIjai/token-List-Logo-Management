import json
import os

# MISSION
# GRAB all json file in the 8453(base) folder and log all the tokens to the console

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

folder_path = os.path.join(current_dir, 'tokenLists', 'lists', '8453')
print(f"Searching for JSON files in: {folder_path}")

json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]


if not json_files:
    print("No JSON files found in the specified folder.")
else:
    print(f"Found {len(json_files)} JSON file(s).")

    for json_file in json_files:
        json_file_path = os.path.join(folder_path, json_file)
        print(f"\nProcessing file: {json_file}")
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            print("Successfully loaded JSON data.")
            print(json.dumps(data, indent=2))

            if 'tokens' in data:
                print("\nToken list:")
                for token in data['tokens']:
                    print(f"Token: {token.get('symbol')} - Address: {token.get('address')}")
            else:
                print("No 'tokens' key found in this JSON file.")

        except json.JSONDecodeError:
            print(f"Error: The file '{json_file}' is not a valid JSON file.")
            print("Please check the file contents and ensure it's properly formatted.")

        except Exception as e:
            print(f"An unexpected error occurred while processing '{json_file}': {str(e)}")

        print("\n" + "="*50 + "\n")  # Separator between files


#         It finds the '8453' folder based on the current working directory.
# It searches for all files ending with '.json' in that folder.
# For each JSON file found:

# It attempts to load and parse the JSON data.
# It prints the entire JSON content.
# If there's a 'tokens' key, it prints each token's symbol and address.
# If there's an error (e.g., invalid JSON), it prints an error message.