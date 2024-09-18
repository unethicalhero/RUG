# R.U.G. aka Random Username Generator
A fork of [Username-Generator](https://github.com/purry03/Username-Generator/) with extra functionalities.

## What is  [Username-Generator](https://github.com/purry03/Username-Generator/) ?
A simple python script created by [purry03](https://github.com/purry03) that combines one adjective with one noun and adds a number between 1 and 99 to the end to generate random usernames.
Possible number of distinct usernames is 850 million.

## Original Code
The [original script](https://github.com/purry03/Username-Generator/blob/master/generator.py) reads from text files containing nouns and adjectives, prompts the user for the number of usernames to generate, and prints them directly to the console. The code also checks if any generated username includes a blacklisted word.

### Key Features of the Original Code:
- User input for the number of usernames.
- Reads from local files for nouns, adjectives, and a blacklist.
- Generates usernames in the format: `AdjectiveNounXX` where `XX` is a random number.
- Validates usernames against a blacklist before printing.

## Changes Made
The new version of the code introduces several improvements and additional functionalities:
1. **Function Encapsulation**: The username generation logic is encapsulated in a function `generate_usernames(num)`, enhancing modularity and reusability.
2. **Absolute File Paths**: The paths to the word lists and blacklist are specified as absolute paths to prevent issues related to file location.
3. **Clipboard Functionality**: Each generated username is automatically copied to the clipboard using the `pyperclip` library, allowing for easy pasting.
4. **Command Line Arguments**: The script now accepts command-line arguments, allowing users to specify the number of usernames to generate directly via terminal.
5. **Case-Insensitive Blacklist Check**: The blacklist check is now case-insensitive, enhancing user experience by allowing variations in casing.
6. **Improved User Feedback**: The script provides clear output, indicating which usernames have been generated and copied to the clipboard.

### Key Features of the New Code:
- Supports generating multiple usernames via command-line input.
- Improved input validation with error messages for invalid input.
- Uses f-strings for clearer string formatting.
- Enhanced readability and structure.

## Usage

To run the script, either add the script to your $PATH or make an alias, for example:
```bash
alias generate='python3 <script_directory>/generator.py'
```
For example :

```bash
$ generate 5
--> huskyLiquidity67
--> slightTreasury3
--> stainedBoundary94
--> equalFlu74
--> insubstantialMasonry71
```
or run it directly from the script directory using the following command in your terminal:

```bash
python generator.py <number_of_usernames>
```
