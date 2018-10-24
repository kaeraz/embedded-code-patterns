import shutil
import os
import subprocess as sp
import pymakefile_user as user


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


# Compilation start info
info = f' Compiling "{user.BIN_NAME}" '
print('')
print('*'*80)
print(f'{info:*^80}')
print('*'*80)


# Remove output directory
print(f'Removing output directory [{user.OBJECTS_DIR}]...')
outdir = os.path.join('.', user.OBJECTS_DIR)
outdir = os.path.normpath(outdir)
if os.path.exists(outdir) and os.path.isdir(outdir):
    shutil.rmtree(outdir)

# Run compilator for each source file
user.SOURCE_FILES = [os.path.normpath(x) for x in user.SOURCE_FILES]
user.INCLUDE_DIRS = ['-I' + x for x in user.INCLUDE_DIRS]
print(f'Running compilation for all source files {user.SOURCE_FILES}...')
objectfiles = []
print('')
for srcfile in user.SOURCE_FILES:
    # Create directory for output
    outdir = os.path.join('.', user.OBJECTS_DIR, os.path.dirname(srcfile))
    outdir = os.path.normpath(outdir)
    if not os.path.exists(outdir):
        print(f'Creating output directory [{outdir}]...')
        os.makedirs(outdir)
    # Compiling source file
    outfilename = os.path.splitext(os.path.basename(srcfile))[0] + '.o'
    outpath = os.path.join(outdir, outfilename)
    outpath = os.path.normpath(outpath)
    print(f'Compiling source file [{srcfile}]...')
    run_cmd([user.CPP, '-c', user.CPP_FLAGS, user.INCLUDE_DIRS,
             srcfile, '-o', outpath])
    objectfiles.append(outpath)
    print('')

# Link object files
print(f'Linking files {objectfiles}...')
outdir = os.path.join('.', user.BIN_DIR)
outdir = os.path.normpath(outdir)
if not os.path.exists(outdir):
    print(f'Creating output directory [{outdir}]...')
    os.makedirs(outdir)
outpath = os.path.join(outdir, user.BIN_NAME)
outpath = os.path.normpath(outpath)
print('')
print(f'Creating binary file {outpath}...')
run_cmd([user.LD, objectfiles, user.CPP_FLAGS, '-o', outpath])
