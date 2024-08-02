import json
import os
import requests

def is_pair(token):
    name = token.get('name', '').lower()
    symbol = token.get('symbol', '').lower()
    return 'amm' in name or 'amm' in symbol or '/' in name or '/' in symbol or '+' in name or '+' in symbol

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
# json_file_path = os.path.join(current_dir, 'tokenLists', 'lists', '8453', 'aerodrome.json')

# Construct the path to save the token logos
logo_save_path = os.path.join(current_dir, 'tokenLogos', 'base')

# Create the directory if it doesn't exist
os.makedirs(logo_save_path, exist_ok=True)

extracted_list = ['aerodrome.json']
extracted_list_path = os.path.join(current_dir, 'image-extracted-list.json')

json_folder_path = os.path.join(current_dir, 'tokenLists', 'lists', '8453')

# Iterate over all JSON files in the 8453 folder, excluding 'aerodrome.json'
json_files = [f for f in os.listdir(json_folder_path) if f.endswith('.json') and f != 'aerodrome.json']



for json_file in json_files:
    json_file_path = os.path.join(json_folder_path, json_file)

    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(f"Successfully loaded {json_file}.")

        tokens = data.get('tokens', [])

        for token in tokens:
            symbol = token.get('symbol')
            address = token.get('address')
            logo_url = token.get('logoURI')

            if is_pair(token):
                print(f"Skipping pair token: {symbol}")
                print("-" * 40)
                continue

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

        # Append the processed JSON file name to the extracted list
        extracted_list.append(json_file)

    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")

    except json.JSONDecodeError:
        print(f"Error: The file '{json_file_path}' is not a valid JSON file.")

    except Exception as e:
        print(f"An unexpected error occurred while processing {json_file}: {str(e)}")

# Save the extracted list to 'image-extracted-list.json'
try:
    with open(extracted_list_path, 'w', encoding='utf-8') as outfile:
        json.dump(extracted_list, outfile, indent=4)
    print(f"Successfully saved the extracted list to '{extracted_list_path}'.")

except Exception as e:
    print(f"An error occurred while saving the extracted list: {str(e)}")

