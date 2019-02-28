"""
Tate Dyer
Lab 5
"""

import string

"""
constant function that can be changed to have a different number of rotations
"""
def CHANGE():
    return 11

"""
Function that checks if file is a mud file or a txt file and determines the action that can be taken for each.
"""
def check_suffix(file):
    if file[-4:]==".mud":
        clarify(file)
    elif file[-4:]==".txt":
        muddle(file)
    else:
        print("File must end in .mud or .txt.")
        return 0

"""
function that muddles a txt file. Then asks if user wants to muddle and write 
the affected file or not and just print the content of the file.
"""
def muddle(file):
    new_words=""
    with open(file, encoding='utf-8') as f:
        words=f.read()
        for c in words:
            new_words+=chr(ord(c)+CHANGE())
    usr=input("Enter 'y' to write results to file "+file[:-4]+".mud: ")
    if usr[0] == 'y' or usr[0]== 'Y':
        with open(file[:-4]+ '.mud', 'w', encoding='utf-8') as fd:
            fd.write(new_words)
    else:
        print(new_words)

"""
function that clarifies a mud file. Then asks if user wants to clarify and write 
the file or not and just print the content of the file.
"""
def clarify(file):
    new_words = ""
    with open(file, encoding='utf-8') as f:
        words = f.read()
        for c in words:
            new_words += chr(ord(c) - CHANGE())
    usr = input("Enter 'y' to write results to file " + file[:-4] + ".txt: ")
    if usr[0] == 'y' or usr[0]== 'Y':
        with open(file[:-4] + '.txt', 'w', encoding='utf-8') as fd:
            fd.write(new_words)
    else:
        print(new_words)

def main():
    file_name=input("Enter file name: ")
    if file_name=="":
        quit()
    else:
        check_suffix(file_name)

main()