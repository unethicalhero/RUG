import os
import sys
import random
import pyperclip
import argparse

def generate_usernames(num, use_blacklist=True, append_number=True):
    # Specify relative paths to your files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    nouns_file = os.path.join(base_dir, "nouns.txt")
    adjectives_file = os.path.join(base_dir, "adjectives.txt")
    blacklist_file = os.path.join(base_dir, "blacklist.txt")

    # Read word lists
    with open(nouns_file, 'r') as infile:
        nouns = infile.read().strip().split('\n')
    with open(adjectives_file, 'r') as infile:
        adjectives = infile.read().strip().split('\n')
    
    # Load blacklist if required
    censored = []
    if use_blacklist:
        with open(blacklist_file, 'r') as infile:
            censored = infile.read().strip().split('\n')

    # Generate usernames
    generated_usernames = []
    for _ in range(num):
        while True:
            word1 = random.choice(adjectives)
            word2 = random.choice(nouns).capitalize()
            username = f"{word1}{word2}"
            if append_number:
                username += str(random.randint(1, 99))

            # Check against blacklist
            if word2.lower() not in map(str.lower, censored):
                generated_usernames.append(username)
                break

    # Copy each generated username to the clipboard individually
    for username in generated_usernames:
        pyperclip.copy(username)
        print(f"--> {username}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random usernames.")
    parser.add_argument('num', type=int, nargs='?', default=1, help="Number of usernames to generate")
    parser.add_argument('--no-blacklist', action='store_false', dest='use_blacklist', help="Ignore blacklisted words")
    parser.add_argument('--no-number', action='store_false', dest='append_number', help="Do not append a number to usernames")

    args = parser.parse_args()

    generate_usernames(args.num, args.use_blacklist, args.append_number)
                    