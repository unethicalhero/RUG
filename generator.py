    import sys
    import random
    import string
    import pyperclip

    def generate_usernames(num):
        # Specify the absolute paths to your files
        nouns_file = "~/Github/Username-Generator/nouns.txt"
        adjectives_file = "~/Github/Username-Generator/adjectives.txt"
        blacklist_file = "~     /Github/Username-Generator/blacklist.txt"

        # read word lists
        with open(nouns_file, 'r') as infile:
            nouns = infile.read().strip().split('\n')
        with open(adjectives_file, 'r') as infile:
            adjectives = infile.read().strip().split('\n')
        with open(blacklist_file, 'r') as infile:
            censored = infile.read().strip().split('\n')

        # generate usernames
        generated_usernames = []
        for _ in range(num):
            while True:
                word1 = random.choice(adjectives)
                word2 = random.choice(nouns).capitalize()  # Capitalize first letter
                username = f"{word1}{word2}{random.randint(1, 99)}"
                
                if word2.lower() not in map(str.lower, censored):
                    generated_usernames.append(username)
                    break

        # Copy each generated username to the clipboard individually
        for username in generated_usernames:
            pyperclip.copy(username)
            print(f"--> {username}")

    if __name__ == "__main__":
        if len(sys.argv) == 1:
            num = 1
        elif len(sys.argv) == 2 and sys.argv[1].lower() == "generate":
            num = 1
        elif len(sys.argv) == 2:
            try:
                num = int(sys.argv[1])
            except ValueError:      
                print("Error: Invalid number of usernames.")
                sys.exit(1)
        else:
            print("Usage: python script_name.py <number_of_usernames>")
            sys.exit(1)

        generate_usernames(num)
