import os
import sys


file_name = sys.argv[1]
folder = sys.argv[2]
library = sys.argv[3]
cpp_files = []
command = f"g++ -o {file_name}"


for root, folders, files in os.walk(folder):
    for file in files:
        if file.endswith('.cpp'):
            cpp_files.append(file)


for file in cpp_files:
    command = f'{command} {file}'


if library == 'raylib':
    command = f'{command} -lraylib -lGL -lm -lpthread -ldl -lrt -lX11'


print(command)
os.system(command)
os.system(f'./{file_name}')
