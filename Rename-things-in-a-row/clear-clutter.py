import os

clutter = os.listdir ("D:\Programing\C++ projects")
print(clutter)

i = 0
for files in clutter:
    # if files.endswith(".cpp"):
    print(files)
    os.rename(f"D:\Programing\C++ projects\{files}",  f"D:\Programing\C++ projects\hero{i}")
    print (f"renamed {files} to hero")
    i =  i + 1