import os, shutil

#Choose what directory you want sorted
path = input('Please input the path of desired sorted directory.\n')

#Checks if given path is valid
while not os.path.exists(path):
    answer = input('Would you like to try again? [Y/N]\n')
    if (answer == 'Y') | (answer == 'y'):
        path = input('Please input the path of desired sorted directory.\n')
    elif (answer == 'N') | (answer == 'n'):
        exit()

os.chdir(path)
for files in os.listdir():
    if os.path.isfile(os.getcwd() + '\\' + files):
        name, extension = os.path.splitext(os.getcwd() + '\\' + files)
        extension = extension.replace('.', '')
    
        #If dir of file type already exists -> moves file
        if os.path.isdir(os.getcwd() + '\\' + extension):
            shutil.move(os.getcwd() + '\\' + files, os.getcwd() + '\\' + extension)
            print(name + ' has been moved to ' + extension + ' directory.')
    
        #Makes dir of specific file type -> moves file
        else:
            os.mkdir(os.getcwd() + '\\' + extension)
            shutil.move(os.getcwd() + '\\' + files, os.getcwd() + '\\' + extension)
            print(extension + ' directory has been created.')
            print(name + ' has been moved to ' + extension + ' directory.')




        
