# ide-selector

A simple command line tool to open a folder in your preferred IDE. I was a tiny bit annoyed at having to specify every time what IDE I wanted to open a folder in when I opened it from the command line, so I made this tool so I only had to specify it once.

The Python file takes one argument: the directory to open. It reads a `.ide` file in the directory to choose the IDE. The file should contain, on each line, a command used to open an IDE. If more than one IDE is specified, the script will ask the user to select one.

For example, the `.ide` file might look like:

```
idea
```

Running the script will automatically run the `idea` command to open the directory in JetBrains IDEA.

If the `.ide` file looks like this:

```
webstorm
code
```

then running the script will cause the script to ask the user to select either `webstorm` (to open the folder in JetBrains Webstorm) or `code` (to open in Visual Studio Code).

I'd recommend modifying your local Path to be able to run the Python script from anywhere on your machine, and then adding `.ide` to your global gitignore. On Windows, you can add the script to your path by creating a `.bat` batch script to run the file, e.g.

```batch
@echo off
echo.
py %~dp0\relative\path\to\ide-selector.py %*
```

and adding the containing folder to Path.
