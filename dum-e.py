# Dum-E
# Noah Smyth

import os
import glob
import importlib

# First Priority:
# Recursively open files in plugins folder and remember their names / commands,
# Plugin names will be stored inside the file, so they need to be opened, read, and recorded in a variable when the program is initialised
# Plugins can also take parameters, so take note of these.
plugins = []

root_dir = "./Plugins"
for filename in glob.iglob(root_dir + '**/*.py', recursive=True):
    path = "./Plugins" + filename
    with open(filename, "r") as fh:
        pluginName = fh.readline()
        print(pluginName[1:].strip()) # Retrieve true plugin name rather than file name
        plugins.append(pluginName[1:].strip())

         
# Second priority:
# While loop that infinitely requests input

while True:
    userInput = input()
    for i in range(0,len(plugins)):
        if userInput == str(plugins[i]):
            print("Matched!")
            break