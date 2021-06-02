import os
import re
import zipfile


def unzip_instructions():
    unzip_instructions = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
    unzip_instructions.extractall('Instructions')
    unzip_instructions.close()


def main():
    # unzip_instructions()
    unzip_folder = f'{os.getcwd()}/Instructions'
    instruction_path = f'{unzip_folder}/extracted_content/Instructions.txt'
    with open(instruction_path, 'r') as inst:
        instructions = inst.readlines()
    for i in instructions:
        print(i)
    for folder, sub_folders, files in os.walk(unzip_folder):
        for filename in files:
            isTxt = re.search(r'.txt', filename)
            fileLines = []
            filePath = os.path.join(folder, filename)
            if isTxt is not None:
                pattern_regex = r'(\d{3})-(\d{3})-(\d{4})'
                with open(filePath, 'r') as content:
                    fileLines = content.readlines()
                for line in fileLines:
                    pr = re.search(pattern_regex, line)
                    if pr is not None:
                        print(
                            f'Number was found in file {filename} and it is {pr.group()}')


if __name__ == "__main__":
    main()
