import os

print(dir(os))
print(os.getcwd())
print(os.listdir())
path = 'C:\\Users\\gicar\\Desktop\\Vedant\\Whitehatjr\\PYTHON\\Automate File Segregation (102)'
ie = os.path.exists(path)
print(ie)
path1 = 'Automate File Segregation (102)\os.py'
root,extension = os.path.splitext(path1)
print('Root of the path -> ', root)
print('Extension of the path -> ', extension)