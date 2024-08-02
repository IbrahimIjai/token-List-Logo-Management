import json
import os
import requests

# Function to download and save an image
def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        return True
    return False

# Get the current working directory
current_dir = os.getcwd()

# Construct the path to the aerodrome.json file
json_file_path = os.path.join(current_dir, 'tokenLists', 'lists', '8453', 'aerodrome.json')

# Construct the path to save the token logos
logo_save_path = os.path.join(current_dir, 'tokenLogos', 'base')

# Create the directory if it doesn't exist
os.makedirs(logo_save_path, exist_ok=True)

try:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    print("Successfully loaded JSON data.")

    # Get the first 5 tokens
    tokens = data.get('tokens', [])

    for token in tokens:
        symbol = token.get('symbol')
        address = token.get('address')
        logo_url = token.get('logoURI')

        if logo_url and address:
            # Construct the filename
            filename = os.path.join(logo_save_path, f"{address}.png")
            
            if os.path.exists(filename):
                print(f"Logo for {symbol} ({address}) already exists. Skipping.")
            else:
                print(f"Downloading logo for {symbol} ({address})")
                if download_image(logo_url, filename):
                    print(f"Successfully saved logo to {filename}")
                else:
                    print(f"Failed to download logo for {symbol}")
        else:
            print(f"Missing logo URL or address for {symbol}")

        print("-" * 40)

except FileNotFoundError:
    print(f"Error: The file '{json_file_path}' was not found.")

except json.JSONDecodeError:
    print(f"Error: The file '{json_file_path}' is not a valid JSON file.")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")