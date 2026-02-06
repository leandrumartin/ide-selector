import argparse
import os

parser = argparse.ArgumentParser(description="Open a folder in your preferred IDE or editor.")
parser.add_argument("directory", help="Path to the folder you want to open.")
args = parser.parse_args()

path = args.directory
ide_file = path + "/.ide"
editors = []

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
        selected_editor = editors[int(selection) - 1]
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
if len(editors) == 1:
    command = f"{editors[0]} {path}"
else:
    print("Available editors:")
    for i, editor in enumerate(editors):
        print(f"\t{i + 1}. {editor}")
    selection = input("Choose which editor you would like to use. Enter the number or part of the name.\n").strip()
    selected_editor = parse_selection(selection)   
    command = f"{selected_editor} {path}"
print(command)
os.system(command)
