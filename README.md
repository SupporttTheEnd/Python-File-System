# File System Simulator

This Python program simulates a file system with various commands such as `cd`, `ls`, `mkdir`, and others.

## Overview

- **File:** `file_system.py`
- **Author:** Andrew Tang
- **Date:** 12/1/2022
- **Lab Section:** Section 45
- **Email:** andrew73@umbc.edu
- **Description:** This program simulates a file system with various commands such as `cd`, `ls`, `mkdir`, and etc.

## File Structure

The program utilizes a dictionary-based data structure to represent the file system, where directories are represented as keys mapping to nested dictionaries, and files are represented as values in lists.

## Constants

- `FIRST_ITEM`, `SECOND_ITEM`, `THIRD_ITEM`, `LAST_ITEM`: Constants representing indices used for accessing items in lists.
- `TWO`: Constant representing the value 2.
- `MKDIR`, `TOUCH`, `PWD`, `CD`, `LS`, `RM`, `LOCATE`, `EXIT`: Constants representing command strings.
- `EMPTY`, `SPACE`, `DOT_DOT`, `DOT`, `SLASH`: Constants representing empty strings and special characters used in the program.
- `DIRECTORY`, `FILE`: Constants representing directory and file types.

## Functions

The program contains several functions for handling various file system operations, including:

- `reformat(steps)`: Helper function to format a line of directions associated with absolute/relative paths into a list.
- `locate_validator(inputs)`: Function to validate input parameters for the `locate` command.
- `locate_helper(out)`: Helper function to format and print the output from the `locate` function.
- `ls_base(new_path, place)`: Function to print the contents of the current directory.
- `ls_absolute(root, steps)`: Function to handle absolute paths for the `ls` command.
- `ls_relative(new_path, steps, place)`: Function to handle relative paths for the `ls` command.
- `cd(inputs, root, place, new_path)`: Function to handle the `cd` command.
- `cd_back(root, place)`: Function to set location back one space.
- `cd_absolute(root, steps)`: Function to handle absolute paths for the `cd` command.
- `cd_relative(new_path, steps, place)`: Function to handle relative paths for the `cd` command.
- `mkdir(inputs, new_path)`: Function to make a new directory.
- `touch(inputs, new_path, root)`: Function to make a new file.
- `rm(inputs, new_path)`: Function to delete a file.
- `locate(new_path, file, place)`: Function to locate a file recursively.

## Usage

To run the program, execute the `file_system.py` script. The program provides a command-line interface where users can interact with the simulated file system by entering various commands.

Here are some example commands:

- `mkdir directory_name`: Create a new directory.
- `touch file_name`: Create a new file.
- `cd directory_path`: Change directory.
- `ls [path]`: List contents of the current directory or specified path.
- `rm file_name`: Remove a file.
- `locate file_name`: Locate a file recursively within the file system.
- `pwd`: Print the current working directory.
