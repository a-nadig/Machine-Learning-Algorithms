'''
Created on 14-Nov-2016

@author: ankit
'''
import random
import math
import matplotlib.pyplot as plt
import sys


def kmeans():
    
    f=open('seeds_dataset.txt', 'r')
    list1=[]
    list0=[x for x in list(f)]
    for str1 in list0:
        ll=str1.strip().split()
        list1.append([float(x) for x in str1.strip().split()[:-1]])
    

    #print (list1)
    
    flag=0
    k_list=[2,3,4,5,6,7,8,9,10]
    obj_list=[0]*len(k_list)
    
    for k in range(2,11): 
        cluster_label=[None]*len(list1)
        convergence=0
        prev_centroid_list=[]
        curr_centroid_list=[]
        flag=0
        count_to_converge=0
        while convergence==0:
            curr_centroid_list=[random.choice(list1) for i in range(0,k)]
            #loop through the dataset and find distances of points from all centroids and assign them to the nearest centroid
            #classify points
            for i in range(0,len(list1)):
                
                distances=[0]*len(curr_centroid_list)
                for j in range(0,len(curr_centroid_list)):
                    #distance between curr_centroid_list[j] and list1[i]
                    
                    for index in range(0,7):
                        distances[j]+=(abs(curr_centroid_list[j][index]-list1[i][index]))**2
                #find minimum distance
                min1=min(distances)
                cluster_label[i]=distances.index(min1) 
            
            
            
            jhanda=1
            while jhanda==1:
                jhanda=0
                count=[0]*k
            
                for label in cluster_label:
                    count[label]+=1
                    
                for c in count:
                    if c==0:
                        jhanda=1
                        ne_label=count.index(c)
                        max_count=max(count)
                        max_index=count.index(max_count)
                        break
                if(jhanda==0):
                    break
                        
                if jhanda==1:
                    cc=0
                    for i in range(0,len(list1)):
                    
                        if cluster_label[i]== max_index:
                            cc+=1
                            cluster_label[i]=ne_label
                        if cc==math.floor(max_count/2):
                            break
                    
         
                        
            #recenter every cluster
            for i in range(0,k):
                for j in range(0,7):
                    sum=0
                    count1=0
                    for l in range(0,len(list1)):
                        if(cluster_label[l]==i):
                            count1+=1
                            sum+=list1[l][j]
                    #print(k)        
                    avg=(sum/count1)
                    curr_centroid_list[i][j]=avg    
            
            if flag==1:
                for i in range(0,len(curr_centroid_list)):
                    dist=0
                    convergence=0
                    for j in range(0,7):
                        #print("i:",i,"j",j,"k",k)
                        #print(curr_centroid_list)
                        #print(prev_centroid_list)
                        dist+=abs(curr_centroid_list[i][j]-prev_centroid_list[i][j])**2
                    if(dist>2.5):
                        break
                    convergence=1
                    
            if convergence==1:
                print(count_to_converge)
                continue
            flag=1
            prev_centroid_list=curr_centroid_list[:]
            count_to_converge+=1    
        #calculate objective function
        obj_fun=0
        for i in range(0,k):
            for j in range(0,len(list1)):
                if cluster_label[j]==i:
                    for l in range(0,7):
                        
                        obj_fun+=abs(curr_centroid_list[i][l]-list1[j][l])**2
        obj_list[k-2]=obj_fun
        
    plt.plot(k_list,obj_list)
    plt.ylabel('Objective Function')
    plt.xlabel('k')
    plt.show()

                
             
    
kmeans()

          