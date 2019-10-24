from math import *
from anytree import Node, RenderTree, AsciiStyle
from anytree import *
#import math
import random
a_lists = open("ballon.txt").read()
#a_lists = open("car.data.txt").read()
a_list = a_lists.split('\n')
#print(a_list)
alist2=[]
classes1=[]
for i in a_list:
        alist2.append(i.split(','))
print(alist2)
print(len(alist2))
k=0
for i in alist2:
    blist=[]
    for j in i:
        blist.append(j)
    alist2[k]=blist
    k+=1
print(alist2)
tr=int(len(alist2)*9/10)
test=int(len(alist2)*1/10)
length_1fold=test
index=[]
#trdataset=[]
fold_dts=[]
tdataset=[]
'''i=0
while(i<tr):
    ran=random.randint(0,len(alist2)-1)
    if(ran not in trindex):
        trindex.append(ran)
        trdataset.append(alist2[ran])
        i+=1
i=0'''
i=0
j=0
kfold=int(input("K-fold:"))
while(j<kfold):
    tdataset=[]
    i=0
    while(i<length_1fold):
        ran=random.randint(0,len(alist2)-1)
        if(ran not in index):
            index.append(ran)
            tdataset.append(alist2[ran])
            i+=1
    fold_dts.append(tdataset)
    j+=1
            
#print(fold_dts)
#print(len(fold_dts[0]))
pre_tt=[]
rec_tt=[]
m=0
kfold1=kfold
#knn=int(input("KNN:"))
total123=0 
while(m<kfold1):
    total=0
    root=[]
    index=[]
    trdataset=[]
    testdataset=[]
    i=0
    while i<kfold-1:
        ran=random.randint(0,len(fold_dts)-1)
        if ran not in index:
            index.append(ran)
            for ii in fold_dts[ran]:
                trdataset.append(ii)
            i+=1
    i=0
    while i<1:
        ran=random.randint(0,len(fold_dts)-1)
        if ran not in index:
            #index.append(ran)
            for ii in fold_dts[ran]:
                testdataset.append(ii)
            i+=1
    print(len(testdataset))            
    print(testdataset)
    print(len(trdataset))
    print(trdataset)
    temporary_train_dt=[]
    for i in range(len(trdataset)):
        temporary_train_dt.append([])
        for j in range(len(trdataset[i])):
            temporary_train_dt[i].append(trdataset[i][j])

    
    classes=[]
    class_count=[]
    for i in temporary_train_dt:
        #print(i)
       
        if i[len(i)-1] not in classes:
            classes.append(i[len(i)-1])
        length=len(i)-1
        
    classes.sort()
    print(classes)
   
    classes1=[]
    for i in classes:
        classes1.append(i)
    for i in classes:
        class_count.append(0)
    print(class_count)
    for i in temporary_train_dt:
        #print(i)
        for j in range(len(classes)):
            if i[len(i)-1] == classes[j]:
                class_count[j]+=1
    #print(class_count)
    total_ins=len(trdataset)
    #total_ins1=total_ins
    total_ins1=len(trdataset)
    ep=0
    for i in range(len(class_count)):
        ep-=(class_count[i]/total_ins)*log((class_count[i]/total_ins),2)
    #print(ep,' ',length)
    flag=0
    while(flag!=1):
        sub=[]
        count_sub=[]
        count_sub_c=[]
        ep_c=[]
        ig_c=[]
        for i in range(length):
            sub.append([])
            count_sub.append([])
            count_sub_c.append([])
            ep_c.append(float(0))
            ig_c.append(float(0))
        #print(sub)
    
        for i in temporary_train_dt:
            for j in range(len(i)-1):
                if i[j] not in sub[j]:
                    sub[j].append(i[j])
                    count_sub[j].append(0)
                    count_sub_c[j].append([])
        #print(sub)
        #print(count_sub)
        '''i=0
        while(i<len(sub)):
            j=0
            while(j<sub[i]):
                while(jj<length):
                    if 
                j+=1'''
        j=0
        while j< len(count_sub_c):
            print(count_sub_c[j])
        
            jj=0 
            while(jj<len(count_sub_c[j])):
            
                #print(count_sub_c[j][jj])
            
            
            
                for jk in classes:
                    count_sub_c[j][jj].append(0)            
                
                jj+=1
            j+=1
        for i in temporary_train_dt:
            for j in range(len(i)-1):
                jj=0
                while jj<len(sub[j]):
                    if i[j] == sub[j][jj]:
                        count_sub[j][jj]+=1
                        jjj=0
                        while jjj<len(classes):
                            if i[len(i)-1]== classes[jjj]:
                               count_sub_c[j][jj][jjj]+=1
                            jjj+=1
                    jj+=1
        #print(count_sub)
        #print(count_sub_c)
        for j in range(len(sub)):
            jj=0
            inter=0
            while jj<len(sub[j]):
                #print(sub[j][jj])
                jjj=0
                inter1=0
                while jjj<len(classes):
                    temp=(count_sub_c[j][jj][jjj]/count_sub[j][jj])
                    print(temp)
                    if temp==0:
                        temp1=0
                    else:
                        temp1=log(temp,2)
                    inter1-=temp*temp1
                    jjj+=1
                inter+=(count_sub[j][jj]*inter1)/total_ins
                jj+=1   
            ep_c[j]=inter
        #print(sub)
        #print(count_sub)
        #print(count_sub_c)
     
        #print(ep,total_ins)
        for i in range(len(ig_c)):
            ig_c[i]=ep-ep_c[i]
        #print(ep_c)
        #print(ig_c)
        max1=max(ig_c)
        #print(max1)
        indx=ig_c.index(max1)
        #print(indx)
        #print(sub[indx])
        #root.append(Node("a"+str(indx)))   
        #print(RenderTree(root, style=AsciiStyle()).by_attr())
        if len(root)==0:
            for i in sub[indx]:
                inqx1=sub[indx].index(i)
                trs=''
                for j in range(len(classes1)):
                    #print('a')
                    #print(count_sub_c[indx][inqx1][j])
                    if count_sub_c[indx][inqx1][j]==count_sub[indx][inqx1]:
                        total+=int(count_sub_c[indx][inqx1][j])
                        trs=classes1[j]
                        break
            #print(inqx1)
                root.append([indx,i,0,'',trs])
        else:
            indx1=list_of_in[indx]
            iinnddxx=len(root)
            for i in sub[indx]:
                inqx1=sub[indx].index(i)
                trs=''
                for j in range(len(classes)):
                    print(classes)
                    print(classes1)
                    #print(count_sub_c[indx][inqx1][j])
                    if count_sub_c[indx][inqx1][j]==count_sub[indx][inqx1]:
                        total+=int(count_sub_c[indx][inqx1][j])
                        trs=classes[j]
                        break
            #print(inqx1)
                root.append([indx1,i,parent,'',trs])  
            root[parent_ind][3]=iinnddxx
            root[parent_ind][4]=iinnddxx  
        print(root) 
        print(total)
        flag=1
        for i in root:
            if i[4]=='':
               flag=0
               break                
        #print(root)
        #print(classes1)
        #print(total)
        #print(class_count)
        #root.append(indx,sub[indx])
        #print(root)
        #print(total_ins)
        #parents=[]
        parent=[]
        for i in range(len(root)):
            #print(root[i][len(root[0])-1])
            if root[i][len(root[0])-1]=='':
                parent_value=root[i][1]
                parent_ind=i
                indx=root[i][0]
                #parent=root[i][0]
                if root[i][2]!=0:
                    parent.append(root[i][0])
                    for jjj in root[i][2]:
                        if jjj not in parent:
                            parent.append(jjj)
                        
                else:
                    parent.append(root[i][0])
                    
                parents=parent
                break
        print(parent_value)
        print(parent_ind)
        print(parent)    
        print(parents)
        print(indx)
        #indx=1
        temporary_train_dt1=[]
        for i in range(len(trdataset)):
            temporary_train_dt1.append([])
            for j in range(len(trdataset[i])):
                temporary_train_dt1[i].append(trdataset[i][j])

        list_of_in=[]
        print(trdataset[0])
        for i in range(len(trdataset[0])):
            list_of_in.append(i)
        print(list_of_in)
        #print(temporary_train_dt1)
        i=0
        while i <len(temporary_train_dt1):
            #print(temporary_train_dt1[i][indx])
            if temporary_train_dt1[i][indx]==parent_value:
               for j in range(len(temporary_train_dt1[0])):
                   if j in parents:
                      #print(j)
                      if j in list_of_in:
                          list_of_in.remove(j)
                      temporary_train_dt1[i][j]=''
                      
               i+=1
            else:
                del temporary_train_dt1[i] 
        i=0  
        while i <len(temporary_train_dt1):
            j=0
            while j <len(temporary_train_dt1[0]):
                if temporary_train_dt1[i][j]=='':
                   del temporary_train_dt1[i][j]
                else:
                    j+=1
            i+=1     
        #print(temporary_train_dt1)
        print(total_ins1)
        
             
        temporary_train_dt=[]
        for i in range(len(temporary_train_dt1)):
            temporary_train_dt.append([])
            for j in range(len(temporary_train_dt1[i])):
                temporary_train_dt[i].append(temporary_train_dt1[i][j])

        classes=[]
        class_count=[]
        for i in temporary_train_dt:
            #print(i)
       
            if i[len(i)-1] not in classes:
                classes.append(i[len(i)-1])
            length=len(i)-1
        
        classes.sort()

        #print(classes)
        
        for i in classes:
            class_count.append(0)
        #print(class_count)
        for i in temporary_train_dt:
            #print(i)
            for j in range(len(classes)):
                if i[len(i)-1] == classes[j]:
                    class_count[j]+=1
        #print(class_count)
        
        total_ins=len(temporary_train_dt)
        
        
        ep=0
        for i in range(len(class_count)):
            ep-=(class_count[i]/total_ins)*log((class_count[i]/total_ins),2)
        #print(ep,' ',length)
    text_bg=root[0][0]
    test_or=[]
    for i in testdataset:
        if i[len(testdataset[0])-1] in classes1:
           test_or.append(i[len(testdataset[0])-1])
    print(i[len(testdataset[0])-1])
    test_res=[]
    for i in testdataset:
        text_bg=root[0][0]
        j=0
        while(1):
            if i[text_bg]==root[j][1]:
                if root[j][4] in classes1:
                    test_res.append(root[j][4])
                    break
                else:
                     j=root[j][4]
                     text_bg=root[j][0]
            else:
                j+=1
               
                
  
    prscision=[]
    for i in range(len(classes1)):
        prscision.append([])
        for j in range(len(classes1)): 
            prscision[i].append(0)
     
    print(prscision)  
    print(classes1)  
    for i in classes1:
        for j in range(len(test_or)):
            indqx1=classes1.index(i)
            print(indqx1)
            if test_or[j]==i and test_res[j]==i:
                
                prscision[indqx1][indqx1]+=1
            elif test_or[j]==i and test_res[j]!=i:
                indqx=classes1.index(test_res[j])
                prscision[indqx1][indqx]+=1
    
            
    print(test_or)
    print(test_res)
    print(prscision)  
    acc=0
    tt_p=[]
    gT=[]
    pre_t=[]
    rec_t=[]

    totooal=0 
    for i in range(len(classes1)):
        tt_p.append(0)
        gT.append(0)
        if m==0:
            pre_tt.append(0)
            rec_tt.append(0)
        pre_t.append(0)
        rec_t.append(0)
    print(prscision)
    for i in range(len(classes1)):
        for j in range(len(classes1)):   
            tt_p[i]+= prscision[i][j]
            totooal+=  prscision[i][j]
    for i in range(len(classes1)):
        for j in range(len(classes1)):   
            gT[j]+= prscision[i][j]
    #print(tt_p)
    #print(gT)  
    
    for i in range(len(prscision)):
        acc+=prscision[i][i]
        if tt_p[i]==0:
            pre_t[i]=0
        else:
            pre_t[i]=prscision[i][i]/tt_p[i]
        if gT[i]==0:
            rec_t[i]=0
        else:
            rec_t[i]=prscision[i][i]/gT[i]
    for i in range(len(prscision)):
        pre_tt[i]+=pre_t[i]
        rec_tt[i]+=rec_t[i]
    acc=acc/totooal
    print(acc)
    total123+=acc
    m+=1
for i in range(len(prscision)):
    pre_tt[i]=pre_tt[i]/kfold1
    rec_tt[i]=rec_tt[i]/kfold1
total123=total123/kfold1
print(pre_tt)
print(rec_tt)
f=[]
for i in range(len(prscision)):
    f.append(0)
for i in range(len(prscision)):
    f[i]=2*(pre_tt[i]*rec_tt[i])/(pre_tt[i]+rec_tt[i])
print(f)
print(total123)

