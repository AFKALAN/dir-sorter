import os, shutil

#Choose what directory you want sorted
path = input('Please input desired sorted directory.\n')
if os.path.exists(path):
    os.chdir(path)

    for files in os.listdir():
        if os.path.isfile(os.getcwd() + '\\' + files):
            name, extension = os.path.splitext(os.getcwd() + '\\' + files)
            extension = extension.replace('.', '')
        
            #If dir of file type already exists -> moves file
            if os.path.isdir(os.getcwd() + '\\' + extension):
                shutil.move(os.getcwd() + '\\' + files, os.getcwd() + '\\' + extension)
        
            #Makes dir of specific file type -> moves file
            else:
                os.mkdir(os.getcwd() + '\\' + extension)
                shutil.move(os.getcwd() + '\\' + files, os.getcwd() + '\\' + extension)

else:
    print('This is not a valid path.')



        
