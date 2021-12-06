import os 

ll = "linkedlist_testcase_"
ms = "musicstream_testcase_"
print("Testing outputs...")
print("--------------------------------------------------------")
failed = 0
for i in range(1,23):
    file = ll + str(i) + ".out"
    expected = open("../expected_outputs/" + file).read()
    given = open("../given_outputs/"+file).read()
    if expected != given:
        print("Linkedlist case: ", i, "failed.")
        failed += 1
    os.system("diff ../expected_outputs/" + file + " ../given_outputs/"+file+" > ../result_linkedlist.out")

ll_score = round(((23-failed)/23)*100)/2
print("Score from LinkedList: [{}/50]".format(ll_score,2))

print("--------------------------------------------------------")

failed = 0
for i in range(1,16):
    file = ms + str(i) + ".out"
    expected = open("../expected_outputs/" + file).read()
    given = open("../given_outputs/"+file).read()
    if expected != given:
        print("Musicstream case: ", i, "failed.")
        failed += 1
    os.system("diff ../expected_outputs/" + file + " ../given_outputs/"+file+" > ../result_musicstream.out")

ms_score = round(((15-failed)/15)*100)/2
print("Score from Musicstream: [{}/50]".format(ms_score,2))


print("--------------------------------------------------------")

print("Overall score: [{}/100]".format(ll_score+ms_score))
print("You can find the differences in the result_linkedlist.out & \
result_musicstream.out\ngenereated by diff command.")
