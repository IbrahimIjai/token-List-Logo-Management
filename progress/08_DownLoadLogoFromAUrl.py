import os
import json

# Define paths
current_dir = os.getcwd()
token_logos_path = os.path.join(current_dir, 'tokenLogos', 'base')
output_folder = os.path.join(current_dir, 'results', 'tokenLogoMappings')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to extract token address from filename
def get_token_address(filename):
    return os.path.splitext(filename)[0].lower()

# Initialize a dictionary to store mappings for each chain
chain_mappings = {}

# Iterate over the files in the tokenLogos/base directory
for filename in os.listdir(token_logos_path):
    if filename.endswith(('.png', '.jpg', '.svg')):
        token_address = get_token_address(filename)
        image_type = os.path.splitext(filename)[1][1:]  # Extract file extension without the dot

        # Assuming chain ID is fixed for this example
        chain_id = '8453'

        if chain_id not in chain_mappings:
            chain_mappings[chain_id] = {}

        # Add the token address and image type to the chain mapping
        chain_mappings[chain_id][token_address] = image_type

# Save each chain's mapping to a JSON file
for chain_id, mappings in chain_mappings.items():
    output_path = os.path.join(output_folder, f'{chain_id}.json')
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(mappings, outfile, indent=4)
    print(f"Mapping for chain {chain_id} saved to {output_path}")

print("All mappings generated and saved successfully.")
