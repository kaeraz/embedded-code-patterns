import os

# -------------
# DO NOT MODIFY
# -------------
# Path to this user settings makefile
USER_MAKEFILE_PATH = os.path.relpath(os.path.dirname(os.path.abspath(__file__)))

# -------------
# USER SETTINGS
# -------------
# Set the compiler command
CPP = 'g++'
# Set the linked command
LD = 'g++'
# Set C++ flags
CPP_FLAGS = [
    '-Wall',
    '-pedantic',
    '-g',
    '-Wfatal-errors'
]
# Set the output binary file name
BIN_NAME = 'test-linkedlist.exe'
# Set the binary output directory relative to USER_MAKEFILE_PATH
BIN_DIR = 'bin'
# Set the objects output directory relative to USER_MAKEFILE_PATH
OBJECTS_DIR = 'obj'
# Set source files relative to USER_MAKEFILE_PATH
SOURCE_FILES = [
    'test_main.cpp',
]
# Set include directories relative to USER_MAKEFILE_PATH
INCLUDE_DIRS = [
    '.',
    'src'
]
