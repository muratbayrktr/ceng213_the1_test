## ceng213 the1 testcase inspector

You can use these scripts to see your mistakes and compare your results to the expected outputs.

Under Student_Evaluate provided by the department there are two essential files :  
  
Student_Evaluate:  
    -expected_outputs  
    -mains  
    
Note: It might not pop an error but I highly recommend using this makefile in order for consistency.

1. Under the main folder copy all your the1 .h and .cpp files and make sure you don't miss any.
2. Copy test.py, compare.py and Makefile under the main folder.
3. open a bash terminal inside the mains folder.
4. ```>python3 test.py``` 
5. Wait for the compiling and evaluation process.
6. Extra compiled files will be cleared after evaluation.
7. You can see your failed cases in the terminal.
8. Also for further examination, tester will generate two files: "result_linkedlist.out" & "result_musicstream.out" outside 
the mains folder so that you can clearly see them.

