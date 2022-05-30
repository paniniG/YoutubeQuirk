#This is the link to the problem statement and solution: https://www.youtube.com/watch?v=C5-I0bAuEUE&ab_channel=minutephysics
#I wanted to code this puzzle and verify that winning probability approximately equals 31%

import random as rn
def list_of_succesful_people(number_of_people):
    succ=[]
    temp=[]
    box=[0]*(number_of_people+1)
    i=1
    while i<number_of_people+1:
        x=rn.randint(1,number_of_people)
        if x in temp:
            continue
        box[i]=x
        temp.append(x)
        i+=1

    for k in range(1,number_of_people+1):
        temp2=[]
        j=1
        y=k
        while j in range(int((number_of_people/2)+1)):
            j+=1
            if k==box[y]:
                succ.append(k)
                break
            y=box[y]
    return(succ)
result_of_experiment=[]
for i in range(10000):   
    result_of_experiment.append(len(list_of_succesful_people(100))==100)
p=dict()
p['True']=result_of_experiment.count(True)
p['False']=result_of_experiment.count(False)
p['Success_Percentage']=result_of_experiment.count(True)/len(result_of_experiment)*100
print(p)

