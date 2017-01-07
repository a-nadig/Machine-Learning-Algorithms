'''
Created on 18-Sep-2016

@author: ankit
'''
import numpy as np
import matplotlib.pyplot as plt
import random



def NaiveBayess(z):
    count=0
    f=open('breast-cancer-wisconsin.data.txt', 'r')
    list1=list(f)
    #print(training_list)
    break1= (len(list1)*(2/3))
    break1= int(round(break1,0))
    #print(break1)
    r_percent=int(round(z*break1))
    starting_index=random.randrange(0,break1-r_percent+1)
    
    training_list=list1[starting_index:starting_index+r_percent]   #will stop 1 element before stop value
    test_list=list1[break1:]
    count_benign=0
    count_malign=0
    
    for i in training_list:
        if '?' in i:
            continue
        temp_list=[int(x) for x in i.split(',')]
        count=count+1
        if temp_list[10]==2:
            temp_list[10]= 1
            count_benign=count_benign+1
        elif temp_list[10]==4:
            temp_list[10]=-1
            count_malign=count_malign+1
            
    pyb=float(count_benign/count)
    pym=float(count_malign/count)
    #print(pyb)
    #print(pym)
    
    accuracy_numer=0
    accuracy_denom=0
    
    for i in test_list:
        b_prob_dict={}
        m_prob_dict={}
        if '?' in i:
            continue
        accuracy_denom+=1
        temp_test_list=[int(x) for x in i.split(',')] 
        vb=pyb
        vm=pym
        for j in range(1,10):
            
            b_denom=0
            b_numer=0
            m_denom=0
            m_numer=0
            xvalue=temp_test_list[j]
            for str1 in training_list:
                if '?' in str1:
                    continue
                temp_training_list=[int(x) for x in str1.split(',')]
                #Finding p(xi|Y=2)
                if temp_training_list[10]==2:
                    b_denom+=1
                    if temp_training_list[j]==xvalue:
                        b_numer+=1
                
                if temp_training_list[10]==4:
                    m_denom+=1
                    if temp_training_list[j]==xvalue:
                        m_numer+=1
            if b_denom==0:
                b_prob_dict[j]=0
            else:    
                b_prob_dict[j]=float(b_numer/b_denom)
            if m_denom==0:
                m_prob_dict[j]=0
            else:
                m_prob_dict[j]=float(m_numer/m_denom)
        
        for k in range(1,10):
            vb*=b_prob_dict[k]
        vb+=1
        
        for k in range(1,10):
            vm*=m_prob_dict[k]
        vm+=1
        if vb>vm:
            i=i+",2"
            
            estimated_class=2
            
        else:
            i=i+",4"
            
            estimated_class=4
        if temp_test_list[10]==estimated_class:
            accuracy_numer+=1

    accuracy=float((accuracy_numer/accuracy_denom)*100)
    #print(test_list)
    return accuracy    



accuracy=[0]*6
list1=[.01,.02 ,.03, .125, .625 ,1]
for i in range(0,5):            
    
    for j in range(0,6):
        accuracy[j]+=(NaiveBayess(list1[j]))
    #print(accuracy)
accuracy1=[float(x/5) for x in accuracy]
print(accuracy1)
plt.plot(list1,accuracy1)
plt.ylabel('Accuracy')
plt.xlabel('Training Data size')
plt.show()
     