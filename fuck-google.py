#encodeing:utf-8
import csv
import fnmatch
import os
import os.path
import re

print("start fuck google!")
dict = {}
with open('androidx-class-mapping.csv','r') as csvfile:
    fieldnames = ("Support Library class", "Android X class")
    dict_reader = csv.DictReader(csvfile, fieldnames)
    for i in dict_reader:
        dict[i['Support Library class']] = i['Android X class']
includes = ['*.xml', '*.java', '*.kt'] 
excludes = ['build','lib', '.svn'] 
includes = r'|'.join([fnmatch.translate(x) for x in includes])
for root, dirs, files in os.walk("./"):
    dirs[:] = [d for d in dirs if d not in excludes]
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(includes, f)]
    text = ""
    for file in files:
        f = open(file, 'r', encoding="utf-8")
        text = f.read()
        f.close()
        for key in dict.keys():
            text = text.replace(key, dict[key])
        with open(file, "w", encoding="utf-8") as f_w:
            f_w.write(text)
            f_w.close()
print("success!")
