import os
import threading
ll = "linkedlist_testcase_"
ms = "musicstream_testcase_"

os.system("make clean")
if os.path.isdir("../given_outputs"):
    os.system("rm -rf ../given_outputs")
os.system("mkdir ../given_outputs")



print("Compiling...")
for i in range(1,23):
    file = ll + str(i) 
    clean = "rm -rf " + file + ".o " + file
    comp = "g++ -c -ansi -Wall -pedantic-errors -O0 -ggdb3 " + file + ".cpp -o " + file + ".o"
    link = "g++ " + file + ".o -o " + file 
    run = "./" + file + " > ../given_outputs/"+file+".out"
    os.system(comp)
    os.system(link)
    os.system(run)

#compile other files
os.system("make album.o")
os.system("make artist.o")
os.system("make playlist.o")
os.system("make profile.o")
os.system("make song.o")
os.system("make musicstream.o")


for i in range(1,16):
    file = ms + str(i)
    clean = "rm -rf " + file + ".o " + file
    comp = "g++ -c -ansi -Wall -pedantic-errors -O0 -ggdb3 " + file + ".cpp -o " + file + ".o"
    link = "g++ " + file + ".o album.o artist.o playlist.o profile.o song.o musicstream.o -o " + file 
    run = "./" + file + " > ../given_outputs/"+file+".out"
    os.system(comp)
    os.system(link)
    os.system(run)



print("Cleaning...")
for i in range(1,23):
    file = ll + str(i) 
    clean = "rm -rf " + file + ".o " + file
    os.system(clean)
    os.system("make clean")
    
for i in range(1,16):
    file = ms + str(i)
    clean = "rm -rf " + file + ".o " + file
    os.system(clean)

os.system("clear")
os.system("python3 compare.py")
