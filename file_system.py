"""
File: file_system.py
Author: Andrew Tang
Date: 12/1/2022
Email:  andrew73@umbc.edu
Description:  This program simulates a file system with various commands such as cd, ls, mkdir, and etc.
"""

FIRST_ITEM = 0
SECOND_ITEM = 1
THIRD_ITEM = 2
LAST_ITEM = -1
TWO = 2
MKDIR = "mkdir"
TOUCH = "touch"
PWD = "pwd"
CD = "cd"
LS = "ls"
RM = "rm"
LOCATE = "locate"
EXIT = "exit"
EMPTY = ""
SPACE = " "
DOT_DOT = ".."
DOT = "."
SLASH = "/"
DIRECTORY = "directory"
FILE = "file"


def reformat(steps):
    """
    Helper function, takes a line of directions associated with absolute/relative paths and formats it into a list.
    :param steps: line of directions associated with absolute and relative paths
    :return: a reformatted list
    """
    pathway = steps.split(SLASH)
    # removes unnecessary empty strings from either end
    if pathway[FIRST_ITEM] == EMPTY:
        pathway.remove(pathway[FIRST_ITEM])
    if pathway[LAST_ITEM] == EMPTY:
        pathway.remove(pathway[LAST_ITEM])
    return pathway


def locate_validator(inputs):
    if len(inputs.split(" ")) == TWO:
        steps = inputs.split(" ")[SECOND_ITEM]
        if len(steps) != 0:
            if SLASH not in steps:
                return True
            else:
                print("'/' is an illegal character.")
            return False
        else:
            print("You must have at least one parameter.")
            return False
    else:
        print("You must have at least one parameter.")
        return False


def locate_helper(out):
    """
     Helper function, formats and prints the raw output from the recursive locate function.
    :param out: the output from the locate function
    :return: None
    """
    filtered_list = []
    pathway = out.split(" ")
    # puts all the items that are not empty strings into the filtered list
    for x in pathway:
        if x != EMPTY:
            filtered_list.append(x)
    # checks if the locate function found anything
    if len(filtered_list) != 0:
        print("A file with that name was found at the following paths:")
        for x in filtered_list:
            print("\t", x)
    else:
        print("No file of that name was found.")


def ls_base(new_path, place):
    """
    Prints the contents of the current directory.
    :param place: a string containing the steps to get to the current directory
    :param new_path: the current directory we are in
    :return: None
    """
    # adds together the file names and the directory keys
    all_items = list(new_path[DIRECTORY]) + new_path[FILE]
    print("Contents for", place)
    for item in all_items:
        print("\t", item)


def ls_absolute(root, steps):
    """
    Handles absolute paths for ls.
    :param root: the overall file structure
    :param steps: the argument given by user
    :return: None
    """
    no_error = True
    place = "/"
    new_path = root
    pathway = reformat(steps)
    # goes through each step denoted by the pathway
    for x in pathway:
        # checks if each step is valid
        if x in new_path[DIRECTORY]:
            place += str(x) + "/"
            new_path = new_path[DIRECTORY][x]
        elif not (x in new_path[FILE] and x == pathway[LAST_ITEM] and steps[LAST_ITEM] != SLASH):
            no_error = False
    if no_error:
        true_items = list(new_path[DIRECTORY]) + new_path[FILE]
        print("Contents for", place)
        for x in true_items:
            print("\t", x)
    else:
        print("Invalid location")


def ls_relative(new_path, steps, place):
    """
    Handles relative paths for ls.
    :param new_path: the current directory we are in
    :param place: a string containing the steps to get to the current directory
    :param steps: the argument given by user
    :return: None
    """
    no_error = True
    pathway = reformat(steps)
    # goes through each step denoted by the pathway
    for x in pathway:
        # checks if each step is valid
        if x in new_path[DIRECTORY]:
            place += str(x) + "/"
            new_path = new_path[DIRECTORY][x]
        elif not (x in new_path[FILE] and x == pathway[LAST_ITEM] and steps[LAST_ITEM] != SLASH):
            no_error = False
    if no_error:
        true_items = list(new_path[DIRECTORY]) + new_path[FILE]
        print("Contents for", place)
        for x in true_items:
            print("\t", x)
    else:
        print("Invalid location")


def cd(inputs, root, place, new_path):
    """
    Overall cd function, calls or operates more specific cd commands.
    :param new_path: the current directory we are in
    :param root: the overall file structure
    :param place: a string containing the steps to get to the current directory
    :param inputs: user input
    :return: returns, a list containing place and new_path
    """
    returns = []
    if len(inputs.split(" ")) == TWO:
        steps = inputs.split(" ")[SECOND_ITEM]
        # goes through the conditions for specific commands
        if steps == DOT_DOT:
            cd_back_output = cd_back(root, place)
            place = cd_back_output[FIRST_ITEM]
            new_path = cd_back_output[SECOND_ITEM]
        elif steps == EMPTY or steps == DOT:
            new_path = new_path
        elif steps[FIRST_ITEM] == SLASH:
            cd_absolute_output = cd_absolute(root, steps)
            if len(cd_absolute_output) == TWO:
                place = cd_absolute_output[FIRST_ITEM]
                new_path = cd_absolute_output[SECOND_ITEM]
            else:
                print("Invalid location")
        else:
            cd_relative_output = cd_relative(new_path, steps, place)
            if len(cd_relative_output) == TWO:
                place = cd_relative_output[FIRST_ITEM]
                new_path = cd_relative_output[SECOND_ITEM]
            else:
                print("Invalid location")
    else:
        print("Improper format, likely missing space.")
    returns.append(place)
    returns.append(new_path)
    return returns


def cd_back(root, place):
    """
    Sets location back one space
    :param root: the overall file structure
    :param place: a string containing the steps to get to the current directory
    :return: returns, a list containing true_place and new_path
    """
    returns = []
    true_place = "/"
    new_path = root
    pathway = reformat(place)[:LAST_ITEM]
    # goes through each step, except the last
    for x in pathway:
        true_place += str(x) + "/"
        new_path = new_path[DIRECTORY][x]
    returns.append(true_place)
    returns.append(new_path)
    return returns


def cd_absolute(root, steps):
    """
    Handles cd for absolute paths.
    :param root: the overall file structure
    :param steps: line of directions associated with absolute and relative paths
    :return: returns, a list containing place and new_path
    """
    returns = []
    place = "/"
    no_error = True
    new_path = root
    pathway = reformat(steps)
    # goes through each step denotes by user input
    for x in pathway:
        # checks if each step is valid
        if x in new_path[DIRECTORY]:
            place += str(x) + "/"
            new_path = new_path[DIRECTORY][x]
        elif not (x in new_path[FILE] and x == pathway[LAST_ITEM] and steps[LAST_ITEM] != SLASH):
            no_error = False
    if no_error:
        returns.append(place)
        returns.append(new_path)
    return returns


def cd_relative(new_path, steps, place):
    """
    Handles cd for relative paths.
    :param new_path: the current directory we are in
    :param steps: line of directions associated with absolute and relative paths
    :param place: a string containing the steps to get to the current directory
    :return: returns, a list containing place and new_path
    """
    returns = []
    no_error = True
    pathway = reformat(steps)
    # goes through each step denotes by user input
    for x in pathway:
        # checks if each step is valid
        if x in new_path[DIRECTORY]:
            place += str(x) + "/"
            new_path = new_path[DIRECTORY][x]
        elif not (x in new_path[FILE] and x == pathway[LAST_ITEM] and steps[LAST_ITEM] != SLASH):
            no_error = False
    if no_error:
        returns.append(place)
        returns.append(new_path)
    return returns


def mkdir(inputs, new_path):
    """
    Makes a new directory.
    :param new_path: the current directory we are in
    :param inputs: user input
    :return: None
    """
    if len(inputs.split(" ")) == TWO:
        steps = inputs.split(" ")[SECOND_ITEM]
        # checks if argument is empty
        if len(steps) != 0:
            # checks if name is taken
            if steps not in list(new_path[DIRECTORY]) + new_path[FILE]:
                if SLASH not in steps and steps != DOT and steps != DOT_DOT:
                    # creates dictionary if all conditions are met
                    new_path[DIRECTORY][steps] = {"file": [], "directory": {}}
                else:
                    print("Illegal name, with either '/', '.', or '..'")
            else:
                print("The name already exists as a file or directory in this level.")
        else:
            print("You must have at least one parameter.")
    else:
        print("You must have at least one parameter.")


def touch(inputs, new_path, root):
    """
    Makes a new file.
    :param root:
    :param new_path: the current directory we are in
    :param inputs: user input
    :return: None
    """
    if len(inputs.split(" ")) == TWO:
        steps = inputs.split(" ")[SECOND_ITEM]
        if len(steps) != 0:
            if SLASH == steps[FIRST_ITEM]:
                if SLASH != steps:
                    no_error = True
                    new_path = root
                    file_name = reformat(steps)[LAST_ITEM]
                    pathway = reformat(steps)[:LAST_ITEM]
                    # goes through each step denoted by the pathway
                    for x in pathway:
                        # checks if each step is valid
                        if x in new_path[DIRECTORY]:
                            new_path = new_path[DIRECTORY][x]
                        else:
                            no_error = False
                    if no_error:
                        if file_name not in list(new_path[DIRECTORY]) + new_path[FILE]:
                            if steps[LAST_ITEM] != SLASH:
                                new_path[FILE].append(file_name)
                            else:
                                print("No slashes in file name.")
                        else:
                            print("The name already exists as a file or directory in this level.")
                    else:
                        print("Invalid location")
                else:
                    print("Argument can't just be '/'")
            else:
                no_error = True
                file_name = reformat(steps)[LAST_ITEM]
                pathway = reformat(steps)[:LAST_ITEM]
                # goes through each step denoted by the pathway
                for x in pathway:
                    # checks if each step is valid
                    if x in new_path[DIRECTORY]:
                        new_path = new_path[DIRECTORY][x]
                    else:
                        no_error = False
                if no_error:
                    if file_name not in list(new_path[DIRECTORY]) + new_path[FILE]:
                        if steps[LAST_ITEM] != SLASH:
                            new_path[FILE].append(file_name)
                        else:
                            print("No slashes in file name.")
                    else:
                        print("The name already exists as a file or directory in this level.")
                else:
                    print("Invalid location")
        else:
            print("Improper format, extra space or single slash.")
    else:
        print("Improper format, likely missing space.")


def rm(inputs, new_path):
    """
    Deletes a file.
    :param new_path: the current directory we are in
    :param inputs: user input
    :return: None
    """
    if len(inputs.split(" ")) == TWO:
        steps = inputs.split(" ")[SECOND_ITEM]
        if len(steps) != 0:
            if steps in new_path[FILE]:
                # removes a file if all conditions are met
                new_path[FILE].remove(steps)
            else:
                print("File name not found.")
        else:
            print("You must have at least one parameter.")
    else:
        print("You must have at least one parameter.")


def locate(new_path, file, place):
    """
    Locates a file recursively.
    :param new_path: the current directory we are in
    :param file: file to be found
    :param place: a string containing the steps to get to the current directory
    :return: container, a string that holds all locations file was found
    """
    # base case, where there is not more child directories and does not contain file of interest
    if len(new_path[DIRECTORY]) == 0 and file not in new_path[FILE]:
        return ""
    # recursive call, where file of interest is found
    elif file in new_path[FILE]:
        container = str(place) + str(file)
        for x in new_path[DIRECTORY]:
            container += " " + locate(new_path[DIRECTORY][x], file, place + str(x) + "/")
    # recursive call, where file of interest is not found
    else:
        container = ""
        for x in new_path[DIRECTORY]:
            container += " " + locate(new_path[DIRECTORY][x], file, place + str(x) + "/")
    return container


if __name__ == "__main__":
    root_system = {
        "file": [], "directory": {}
    }
    user_input = input("[cmsc201 proj3]$ ")
    location = "/"
    new_location = root_system
    while user_input != EXIT:
        # validates the all inputs have less than two items
        if len(user_input.split(" ")) <= TWO:
            command = user_input.split(" ")[FIRST_ITEM]
            # finds the targeted command
            if MKDIR == command:
                mkdir(user_input, new_location)
            elif TOUCH == command:
                touch(user_input, new_location, root_system)
            elif PWD == command:
                print(location)
            elif CD == command:
                cd_output = cd(user_input, root_system, location, new_location)
                location = cd_output[FIRST_ITEM]
                new_location = cd_output[SECOND_ITEM]
            elif LS == command:
                if len(user_input) == TWO:
                    ls_base(new_location, location)
                else:
                    if len(user_input.split(" ")[SECOND_ITEM]) > 0:
                        specification = user_input.split(" ")[SECOND_ITEM]
                        if specification[FIRST_ITEM] == "/":
                            ls_absolute(root_system, specification)
                        else:
                            ls_relative(new_location, specification, location)
                    else:
                        print("Improper format, likely extra space.")
            elif RM == command:
                rm(user_input, new_location)
            elif LOCATE == command:
                if locate_validator(user_input):
                    specification = user_input.split(" ")[SECOND_ITEM]
                    output = locate(new_location, specification, location)
                    locate_helper(output)
            else:
                print("Error, not a recognized command.")
        else:
            print("Too many arguments (one maximum).")
        user_input = input("[cmsc201 proj3]$ ")
    print("Successfully terminated connection.")
