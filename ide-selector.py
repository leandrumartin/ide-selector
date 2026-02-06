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

command = None
if len(editors) == 1:
    command = f"{editors[0]} {path}"
else:
    print("Available editors:")
    for i, editor in enumerate(editors):
        print(f"\t{i + 1}. {editor}")
    selection = input("Choose which editor you would like to use. Enter the number or part of the name.\n").strip()
    
    selected_editor = None
    try:
        selected_editor = editors[int(selection) - 1]
    except:
        filtered = filter(lambda x: selection in x, editors)
        filtered_list = list(filtered)
        selected_editor = filtered_list[0]
    
    command = f"{selected_editor} {path}"
print(command)
os.system(command)
