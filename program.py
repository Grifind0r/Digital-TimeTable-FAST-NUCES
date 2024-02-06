import pandas as pd
import numpy as np
import json


with open('classesDat.json', 'r') as f:
    classes_info = json.load(f)
with open('labsDat.json', 'r') as f:
    labs_info = json.load(f)

def func(subject, type):
    to_return=[]
    if (type== 'class'):
        for i in range(len(classes_info)):
            if(classes_info[i][-1]== subject):
                to_return.append('Day: '+str(classes_info[i][0])+'   Room: '+str(classes_info[i][1])+ '   Time: '+str(classes_info[i][2]))
    elif(type== 'lab'):
        for i in range(len(labs_info)):
            if(labs_info[i][-1]== subject):
                to_return.append('Day: '+str(labs_info[i][0])+'   Room: '+str(labs_info[i][1])+ '   Time: '+str(labs_info[i][2]) )

    return to_return

    
print('Subject name should match the way it is written in the timetable. i.e., PF (CS-A)\n\n\nPress q to exit')
subject='init'
while(1):
    subject= input('Enter the subject: ')
    if(subject=='q'):
        break
    type= input('Is it a lab or class(input in lower case): ')
    output= func(subject, type)

    for i in output:
        print(i)