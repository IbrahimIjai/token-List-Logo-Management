# Project details

This project is designed to scrape token lists from various exchanges and compile a comprehensive list of tokens along with their logos. The goal is to support the creation of a complete token list for koanprotocol.xyz. The choice of Python as the primary language is to enhance proficiency and leverage Python's capabilities in data manipulation and file handling.

## Stacks

python

## token lists

Smold
Sushiswap
Pancakeswap

## Python Scripts Overview (./progress/**)

09_BuildALogoAddressMapForApi.py
    Description: Constructs a JSON file mapping token addresses to their image types (e.g., png, jpg, svg) for accurate URL construction in the API.

08_DownLoadLogoFromAUrl.py
    Description: Downloads token logos from specified URLs and saves them in the logo directory. The script accepts an array of tokens as input.

07_replaceTokenLogoWithNew.py
Description: Replaces outdated token logos with newer, more reliable logos from the Sushiswap token list.

06_mergeAllTokenListsToOneJsonFile.py
Description: Merges all token lists from the "tokenlisttobeMined" folder into a single JSON file.

05_extractTokensLogoFromAllJsonfilesInBASE.py
Description: Extracts token logos from JSON files in the base directory. Includes a fix to correctly identify image extensions (svg, jpg, png).

04_extractTokenLogoFromAeroDrome.py
Description: Extracts logo URLs from the Aerodrome JSON file for testing purposes.

03_extractAerodromTokenLogo.py
Description: Initial script to test extracting logo URLs from the Aerodrome JSON file.

02_getAllJsonFilesInBaseFolder.py
Description: Experiments with the os and json modules to navigate directories and manipulate file contents. Serves as an introduction to path handling and file operations.

01_gettokensinBaseAerodromjson.py
Description: Initial experimentation with token extraction.


## Outcome
The outcome of this project can be found in the ./result/** folder, which contains the generated files and mappings.

example command to run scripts

python  progress/01_gettokensinBaseAerodromjson.py