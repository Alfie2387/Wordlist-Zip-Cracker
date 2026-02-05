import zipfile

zip_file = zipfile.ZipFile("filenamehere.zip") # Put your zip folder name here

with open("rockyou.txt", "rb") as file: # Or use a wordlist of your choice
    for line in file:
        line = line.strip()
        try:
            zip_file.extractall(pwd=line)
            print("File Cracked! Password is ", line)
            break
        except:
            continue