import os
import sys

def add_to_path(script_path):
    # Determine the shell configuration file to modify
    home = os.path.expanduser("~")
    shell_config_file = None

    # Check which shell the user is using
    if os.path.isfile(os.path.join(home, ".bashrc")):
        shell_config_file = os.path.join(home, ".bashrc")
    elif os.path.isfile(os.path.join(home, ".bash_profile")):
        shell_config_file = os.path.join(home, ".bash_profile")
    elif os.path.isfile(os.path.join(home, ".zshrc")):
        shell_config_file = os.path.join(home, ".zshrc")
    else:
        print("No suitable shell configuration file found.")
        return

    # Define the alias command
    alias_command = f"alias generate='python3 {script_path}'\n"
    
    # Check if the alias is already present
    with open(shell_config_file, 'r') as file:
        if alias_command in file.read():
            print("Alias already exists in the configuration file.")
            return

    # Append the alias to the configuration file
    with open(shell_config_file, 'a') as file:
        file.write("\n" + alias_command)
    
    print(f"Added alias to {shell_config_file}. Please restart your terminal or run 'source {shell_config_file}' to apply changes.")

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to generator.py
    generator_script_path = os.path.join(script_dir, 'generator.py')
    
    # Check if generator.py exists
    if not os.path.isfile(generator_script_path):
        print("generator.py not found in the same directory.")
        sys.exit(1)
    
    add_to_path(generator_script_path)
