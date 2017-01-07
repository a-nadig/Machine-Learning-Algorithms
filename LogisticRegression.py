'''
Created on 19-Sep-2016

@author: ankit
'''
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def LogisticRegression(z):
    count=0
    nita=0.0001
    f=open('breast-cancer-wisconsin10.txt', 'r')
    list1=list(f)
    #print(training_list)
    break1= (len(list1)*(2/3))
    break1= int(round(break1,0))
    #print(break1)
    r_percent=int(round(z*break1))
    starting_index=random.randrange(0,break1-r_percent+1)
    
    training_list=list1[starting_index:starting_index+r_percent]   #will stop 1 element before stop value
    test_list=list1[break1:]
    #print(test_list)
    predict=[None]*(len(test_list))
    prob=[0.5]*len(list1)
    w_list=[]
    convergence=0
    
    y=[None]*(len(list1))
    x=[[1 for j in range(0,10)] for i in range(0,len(list1))]
    #print(x)
    i=0
    cost=10000000000
    flag=0
    #print("**************")
    #print(training_list)
    #print("*****************")
    while(not convergence):
        i=0
        count+=1
        #print(count)
        for aaa in training_list:
            #print(aaa)
            if '?' in aaa:
                continue
            
            train_row=[int(x) for x in aaa.split(',')]
            #print(len(y))
            #print(len(training_list))
            #print(test_row)
            #print(i)
            y[i]=train_row[10]
            for index in range(1,10):
                x[i][index]=train_row[index]
            if  not w_list:
                w_list=[0]*10
                #print("Kya 0 se hamaara chutiya kat raha hai dost?")
                
            else:
                #print("Kabhi gaye ho idhar")
                theta=w_list[0]
                for j in range(1,10):
                    theta+=w_list[j]*train_row[j]
                prob[i]=float((math.e**theta)/(1+(math.e**theta)))
                #print(prob[i])
            #print("ending loop")
            i=i+1
        #print("****************** Main yahan bhi aaya")
        '''
        if count==100:
            convergence=1    
            continue    
        '''    
        len_train_list=i
        for index in range(0,9):
            summant=0
            
            for j in range(0,len_train_list):
                    
                summant+=x[j][index]*(y[j]-prob[j])
            
            #print(summant)
            w_list[index]+=(nita*summant)
            #print("divider")
            #print(w_list)
        
        #Calculating the cost function
        #*******Consistent
        curr_cost=0
        new_index=-1
        for str1 in training_list:
            if '?' in str1:
                continue
            new_index+=1
            temp_train_row=[int(x) for x in str1.split(',')]
            
            if temp_train_row[10]==1:
                curr_cost+=float(math.log(prob[new_index]))
            elif temp_train_row[10]==0:
                curr_cost+=float(math.log(1-prob[new_index]))
            
                
        curr_cost=float(curr_cost*float(-1/new_index))
        
        if curr_cost<cost:
            cost=curr_cost
            #print(cost )
        else:
            print("Cost is increasing")
        
        if cost<0.2:
            convergence=1
            continue           
            
            
        
        #*************consistent end
    t=-1
    for str2 in test_list:
        if '?' in str2:
            continue
        t+=1
        test_row=[int(x) for x in str2.split(',')]
        theta2=w_list[0]
        for j in range(1,10):
            theta2+=w_list[j]*test_row[j]
    
        prob[t]=float(math.e**(theta2)/(1+math.e**(theta2)))
        antiprob=1-prob[t]
        if prob[t]>antiprob:
            predict[t]=1
        elif prob[t]<=antiprob:
            predict[t]=0
    
    i=0
    for num1 in range(0,t+1):
        if predict[num1]==y[num1]:
            #print(type(predict[num1]))
            #print("Dusra")
            #print(type(y[num1]))
            
            i+=1
        
    accuracy=float((i/(t+1))*100)
    #print(accuracy)
    return accuracy
        
        
        
 
accuracy=[0]*6
list1=[.01,.02 ,.03, .125, .625 ,1]

for i in range(0,5):            
    
    for j in range(0,6):
        accuracy[j]+=(LogisticRegression(list1[j]))
        #print(accuracy)
accuracy1=[float(x/5) for x in accuracy]
#print(accuracy1)
plt.plot(list1,accuracy1)
#plt.ylabel('some numbers')
plt.show()        


'''
accuracy=LogisticRegression(1)
print(accuracy)
            
'''       
        
    