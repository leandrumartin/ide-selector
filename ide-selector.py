import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description="Open a folder in your preferred IDE or editor.")
parser.add_argument("directory", help="Path to the folder you want to open.")
args = parser.parse_args()

path = args.directory
ide_file = path + "/.ide"
editors = []

def select_default_editor():
    ide_name = input("Enter the command of your preferred editor to open the selected directory:\n").strip().lower()
    with open(ide_file, "w") as file:
        file.write(f"{ide_name}\n")
    return ide_name

if not os.path.exists(ide_file):
    create_file = input(f"No .ide file found in {path}. Would you like to create one? (Y/n)\n").strip().lower()
    if create_file.startswith("y") or create_file == "":
        select_default_editor()
    else:
        print("No .ide file created. Exiting.")
        exit(0)

with open(ide_file, "r") as file:
    for line in file:
        editors.append(line.strip())

def parse_selection(selection):
    """Parse user selection to determine the chosen editor."""
    def handle_index_error():
        return parse_selection(input("Invalid selection. Please try again.\n").strip())

    selected_editor = None
    try:
        # Interpret selection as an index
        selected_editor = editors[int(selection) - 1].strip().lower()
    except ValueError:
        # Interpret selection as a substring
        filtered = filter(lambda x: selection in x, editors)
        filtered_list = list(filtered)
        try:
            selected_editor = filtered_list[0]
        except IndexError:
            selected_editor = handle_index_error()
    except IndexError:
        selected_editor = handle_index_error()
    return selected_editor

command = None
if (len(editors) == 0 or all(editor.strip() == "" for editor in editors)):
    print("No editors found in .ide file.")
    ide_command = select_default_editor()
    command = f"{ide_command} {path}"
elif len(editors) == 1:
    command = f"{editors[0]} {path}"
else:
    print("Available editors:")
    for i, editor in enumerate(editors):
        print(f"\t{i + 1}. {editor}")
    selection = input("Choose which editor you would like to use. Enter the number or part of the name.\n").strip()
    selected_editor = parse_selection(selection)   
    command = f"{selected_editor} {path}"
print(command)
subprocess.run(command, shell=True, capture_output=True)
