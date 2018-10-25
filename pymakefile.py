import os
import importlib.util
import sys
import shutil
import subprocess as sp


# Check script input arguments
if len(sys.argv) != 2:
    print(f'Invalid usage!')
    print(f'\tpython pymakefile.py <PYMAKEFILE_USER_PATH>')
    print(f'\twhere PYMAKEFILE_USER_PATH is a pyth to the pymakefile_user.py file.')
    exit(1)
else:
    # Import dynamically user configuration module passed as second arguemnt
    file_path = sys.argv[1]
    if os.path.exists(file_path) and os.path.isfile(file_path):
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        user = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user)
        # Optional; only necessary if you want to be able to import the module
        # by name later.
        sys.modules[module_name] = user
    else:
        print(f'Provided PYMAKEFILE_USER_PATH user file "{pymakefile_user}" does not exist!')
        exit(1)


def join_and_normalize(path, *args):
    path = os.path.join(path, *args)
    return os.path.normpath(path)


# Reprocess user makefile paths to be relative to user.USER_MAKEFILE_PATH
user.BIN_DIR = join_and_normalize(user.USER_MAKEFILE_PATH, user.BIN_DIR)
user.OBJECTS_DIR = join_and_normalize(user.USER_MAKEFILE_PATH, user.OBJECTS_DIR)
user.SOURCE_FILES = [join_and_normalize(user.USER_MAKEFILE_PATH, x) for x in user.SOURCE_FILES]
user.INCLUDE_DIRS = [join_and_normalize(user.USER_MAKEFILE_PATH, x) for x in user.INCLUDE_DIRS]


def run_cmd(cmd):
    # Flatten the cmd argumet list
    flat_cmd = []
    for sub in cmd:
        if isinstance(sub, list):
            for item in sub:
                flat_cmd.append(item)
        else:
            flat_cmd.append(sub)
    # Run the command
    result = sp.run(flat_cmd,
                    stdout=sp.PIPE,
                    stderr=sp.PIPE,
                    encoding='utf-8')
    # Print commands result
    print(' '.join(flat_cmd))
    if str(result.stdout).strip() != '':
        print(f'{result.stdout}')
    if str(result.stderr).strip() != '':
        print(f'STDERR: {result.stderr}')
    return result.returncode


# Compilation start info
info = f' Compiling "{user.BIN_NAME}" '
print('')
print('')
print('*'*80)
print(f'{info:*^80}')
print('*'*80)


# Remove output directory
print(f'Removing objects output directory [{user.OBJECTS_DIR}]...')
if os.path.exists(user.OBJECTS_DIR) and os.path.isdir(user.OBJECTS_DIR):
    shutil.rmtree(user.OBJECTS_DIR)
print(f'Removing binaries output directory [{user.BIN_DIR}]...')
if os.path.exists(user.BIN_DIR) and os.path.isdir(user.BIN_DIR):
    shutil.rmtree(user.BIN_DIR)

# Run compilator for each source file
user.INCLUDE_DIRS = ['-I' + x for x in user.INCLUDE_DIRS]
print('')
print(f'Running compilation for all source files {user.SOURCE_FILES}...')
objectfiles = []
print('')
for srcfile in user.SOURCE_FILES:
    # Create directory for output
    outdir = join_and_normalize(user.OBJECTS_DIR, os.path.dirname(srcfile))
    if not os.path.exists(outdir):
        print(f'Creating output directory [{outdir}]...')
        os.makedirs(outdir)
    # Compiling source file
    outfilename = os.path.splitext(os.path.basename(srcfile))[0] + '.o'
    outpath = join_and_normalize(outdir, outfilename)
    print(f'Compiling source file [{srcfile}]...')
    returncode = run_cmd([user.CPP, '-c', user.CPP_FLAGS, user.INCLUDE_DIRS,
                          srcfile, '-o', outpath])
    if returncode != 0:
        break
    objectfiles.append(outpath)
    print('')

if returncode == 0:
    # Link object files
    print(f'Linking files {objectfiles}...')
    if not os.path.exists(user.BIN_DIR):
        print(f'Creating binaries output directory [{user.BIN_DIR}]...')
        os.makedirs(user.BIN_DIR)
    outpath = join_and_normalize(user.BIN_DIR, user.BIN_NAME)
    print(f'Creating binary file {outpath}...')
    returncode = run_cmd([user.LD, objectfiles, user.CPP_FLAGS, '-o', outpath])

if returncode == 0:
    print('')
    print(f'Compilation success!')
