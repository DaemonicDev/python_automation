import shutil, os, glob
from pathlib import Path

"""
Author - DaemonicDev
Purpose:
The purpose of this program is to separate and sort a folder by its contents in file extension into smaller
more managable folders. 

Example if Downloads folder has txt, jpg, and doc files then this program would separate those into 
named folders that the user wants, and however many they want.

Downside to this however is that this doesn't scale well with more user input or huge amount of files.

As such, the problem as of right now is of O(N^2) where N is the amount of filetypes and amount of files.
"""


"""
   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Version that comes with this software by default is version 3.
"""

def fileSorter(path, fileTypes, destFolders):
    #Current implementation O(N^2)
    #Where N is the number of files for a given filetype
    #TODO Find a way to optimize this further.

    dest_index = -1

    print(path)

    #print all the destination folders
    for i in range(len(destFolders)):
        print(f'{i}) {destFolders[i]}\n')

    for file_type_index in range(len(fileTypes)):

        while dest_index == -1:
            dest_index = int(input(f"Where do you want to put files of type {fileTypes[file_type_index]}? "))

            if dest_index < 0 or (dest_index > len(destFolders)):
                dest_index = -1

        tPath = os.path.join(path + '\\' + destFolders[dest_index])

        #Collect every file with the following extension
        files = glob.glob(os.path.join(path, '*' + fileTypes[file_type_index]))
        print(files[0] + '\n')
        for file in files:
            if os.path.isfile(file):
                try:
                    shutil.move2(file, tPath)
                except IOError:
                    print("Failed to move files due to filetype not being in use.")
        print(f"\n\nCompleted moving {fileTypes[file_type_index]}")
        file_type_index += 1
        dest_index = -1

def init():
    #Needs the C:/ or F:/ or whatever and everything included.
    m_path = " "

    while m_path == " ":
        m_path = str(input("What is the path of the files you wish to have sorted? "))

        if os.path.isdir(m_path): continue
        else: m_path = " "

    _filetypes = str(input("What are_ the file types you wish to add separated by comma? "))
    _filetypes = [x.strip() for x in _filetypes.split(',')]

    dest_folders = str(input("What are the destinations you want to move them to separated by comma? "))
    #Store the destinations in a string array.
    #This is used to move files into folders of that name.
    #If the folder is not found, it will be created inside the current path.
    dest_folders = [x.strip() for x in dest_folders.split(',')]

    print("hello world")
    print(dest_folders)
    # #Combine the path and destination for ease of use.

    print(_filetypes)
    print(m_path)

    for i in range(len(dest_folders)):
        dest_path = os.path.join(m_path + '\\' + dest_folders[i])
        print(f"\n\n\nDEBUG MODE {dest_path}\n\n\n")
        if os.path.isdir(dest_path) == True:
            continue
        else:
            os.mkdir(dest_path)
            print(f"Destination path created.")

    fileSorter(m_path, _filetypes, dest_folders)

init()

if __name__ == "main.py":
    init()