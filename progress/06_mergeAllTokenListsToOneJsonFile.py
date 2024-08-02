import json
import os

def is_pair(token):
    name = token.get('name', '').lower()
    symbol = token.get('symbol', '').lower()
    
    # Check for common patterns indicating a pair
    pair_patterns = ['amm', '/', '+', '-f', 'yvaero-']
    return any(pattern in name for pattern in pair_patterns) or any(pattern in symbol for pattern in pair_patterns)
    
# Get the current working directory
current_dir = os.getcwd()

# Path to the 8453 folder
json_folder_path = os.path.join(current_dir, 'tokenLists', 'lists', '8453')

# Path to save the merged JSON file
merged_json_path = os.path.join(current_dir, 'results', 'tokenList', 'base.json')

# Create the newList directory if it doesn't exist
os.makedirs(os.path.dirname(merged_json_path), exist_ok=True)

# Initialize an empty list for storing unique tokens
merged_tokens = []

# Use a set to keep track of seen addresses to avoid duplicates
seen_addresses = set()

# Iterate over all JSON files in the 8453 folder
json_files = [f for f in os.listdir(json_folder_path) if f.endswith('.json')]

for json_file in json_files:
    json_file_path = os.path.join(json_folder_path, json_file)

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(f"Successfully loaded {json_file}.")

        tokens = data.get('tokens', [])

        for token in tokens:
            address = token.get('address')

            if is_pair(token):
                print(f"Skipping pair token: {token.get('symbol')}")
                print("-" * 40)
                continue

            if address not in seen_addresses:
                seen_addresses.add(address)
                merged_tokens.append(token)

        print(f"Processed tokens from {json_file}.")
        print("-" * 40)

    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")

    except json.JSONDecodeError:
        print(f"Error: The file '{json_file_path}' is not a valid JSON file.")

    except Exception as e:
        print(f"An unexpected error occurred while processing {json_file}: {str(e)}")

# Save the merged tokens list to 'base.json'
try:
    with open(merged_json_path, 'w', encoding='utf-8') as outfile:
        json.dump({"tokens": merged_tokens}, outfile, indent=4)
    print(f"Successfully saved the merged tokens list to '{merged_json_path}'.")

except Exception as e:
    print(f"An error occurred while saving the merged tokens list: {str(e)}")
