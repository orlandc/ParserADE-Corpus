import os

path = os.getcwd() + '/ADE-Corpus-V2'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for i, f in enumerate(files):
    path2 = f.replace("ADE-Corpus-V2/", "raw/")
    if(f.find('.txt') != -1):
        name2 = path2.replace(".txt", "_raw.txt")
    else:
        name2 = path2.replace(".rel", "_raw.txt")
    
    if not os.path.exists(os.path.dirname(name2)):
        os.makedirs(os.path.dirname(name2))
    
    print (name2 + "\n" )

    file2 = open(name2, "a+")

    k = open(f, "r")
    
    if(f.find('DRUG') != -1):
        previus_line = ''
        for line in k:
            pubmed_id, text = line.strip().split('|')[:2]
            if(previus_line != text):
                file2.write(text + "\n")
                previus_line = text
    else:
        previus_line = ''
        for line in k:
            text = ' '.join(line.strip().split(' ')[2:])
            if(previus_line != text):
                file2.write(text + "\n")
                previus_line = text

    file2.close()
