import os

# Paths
current_dir = os.getcwd()
token_logos_path = os.path.join(current_dir, 'tokenLogos', 'base')

# Function to get token addresses from filenames
def get_token_address(filename):
    return os.path.splitext(filename)[0].lower()

# Get list of all token logos
all_files = os.listdir(token_logos_path)

# Separate .png and .jpg files
png_files = {get_token_address(f): f for f in all_files if f.endswith('.png')}
jpg_files = {get_token_address(f): f for f in all_files if f.endswith('.jpg')}

total_deleted = 0
replaced_tokens = []

# Process each token address
for address, jpg_file in jpg_files.items():
    png_file = png_files.get(address)
    if png_file:
        # Both .jpg and .png exist, so delete .png
        png_path = os.path.join(token_logos_path, png_file)
        os.remove(png_path)
        replaced_tokens.append(address)
        total_deleted += 1

# Summary report
print(f"Total number of .png files deleted: {total_deleted}")

# Detailed report of replaced tokens
print("\nList of tokens with .png deleted:")
for token in replaced_tokens:
    print(token)
