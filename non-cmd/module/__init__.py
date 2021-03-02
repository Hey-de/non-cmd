# Modules
# Here you can import some modules
# Import that as this example (replace %modulename% to your module name and delete the leading #
# from . import %modulename%

# Here is a list with command names
mods = {}


# Main method
def run(cmd):
    for cmdName, main in mods.items():
        if cmd.split(" ")[0] == cmdName:
            main(cmd)
