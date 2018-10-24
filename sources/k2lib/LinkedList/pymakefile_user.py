# -------------
# USER SETTINGS
# -------------

# Set the compiler command
CPP = 'g++'
# Set the linked command
LD  = 'g++'
# Set C++ flags
CPP_FLAGS = [
    '-Wall',
    '-pedantic',
    '-g',
    '-Wfatal-errors'
]
# Set the output binary file name
BIN_NAME = 'event-state-machine.exe'
# Set the binary output directory
BIN_DIR = 'bin'
# Set the objects output directory
OBJECTS_DIR = 'obj'
# Set source files
SOURCE_FILES = [
    'src/main.cpp',
    'src/EventSM/EventSM.cpp'
]
# Set include directories
INCLUDE_DIRS = [
    '.',
    'src'
]
