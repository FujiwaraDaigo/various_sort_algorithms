import numpy as np
import copy
import time
 


def bubble_sort(arr):
    a=copy.copy(arr)

    res=None

    if len(a)==1:
        res=a
    
    else:
        while True:
            change=0
            for i in range(1,len(a)):
                if a[i]<a[i-1]:
                    change=1
                    temp=a[i]
                    a[i]=a[i-1]
                    a[i-1]=temp
            if change==0:
                break
        res=a

    return res


def shaker_sort(arr):
    a=copy.copy(arr)

    res=None

    if len(a)==1:
        res=a
    
    else:
        count=0
        while True:
            change=0
            for i in range(1+count,len(a)-count):
                if a[i]<a[i-1]:
                    change=1
                    temp=a[i]
                    a[i]=a[i-1]
                    a[i-1]=temp
            if change==0:
                break

            change=0
            for i in reversed(range(1+count,len(a)-count-1)):
                if a[i]<a[i-1]:
                    change=1
                    temp=a[i]
                    a[i]=a[i-1]
                    a[i-1]=temp
            if change==0:
                break

            count+=1
        res=a

    return res

def merge_sort(arr):
    
    def merge(arr1,arr2):
        A=[]
        i=0
        j=0
        while True:
            if arr1[i]<arr2[j]:
                A.append(arr1[i])
                i+=1
            else :
                A.append(arr2[j])
                j+=1

            if i==len(arr1):
                A.extend(arr2[j:])
                break
            
            elif j==len(arr2):
                A.extend(arr1[i:])
                break
        return A

    a=copy.copy(arr)
    res=0
    n=len(a)
    if n==1:
        res=a

    elif n==2:
        if a[0]>a[1]:
            temp=a[1]
            a[1]=a[0]
            a[0]=temp
        res=a

    else:
        m=n//2
        a1=a[:m]
        a2=a[m:]

        res=merge(merge_sort(a1),merge_sort(a2))

    return res

def select_sort(arr):
    a=copy.copy(arr)
    for i in range(len(a)):
        index=i
        m=a[i]
        for j in range(i,len(a)):
            if a[j]<m:
                index=j
                m=a[j]
        a[index]=a[i]
        a[i]=m
    return a

def insert_sort(arr):
    a=copy.copy(arr)
    for i in range(len(a)):
        for j in range(i):
            if a[i]<a[j]:
                temp=a[i]
                a.pop(i)
                a.insert(j,temp)
    return a

def quick_sort(arr):
    a=copy.copy(arr)

    res=None

    if len(a)<2:
        res=a

    elif len(a)==2:
        if a[0]>a[1]:
            temp=a[0]
            a[0]=a[1]
            a[1]=temp
        res=a

    else:
        """
        b=a[:3]
        m=b[0]
        mind=0
        M=b[2]
        Mind=2
        for i in range(3):
            if b[i]<m:
                m=b[i]
                mind=i
            if b[i]>M:
                M=b[i]
                Mind=i
        s=[0,1,2]
        s.remove(mind)
        s.remove(Mind)
        pivot=a[s[0]]
        a.pop(s[0])
        """
        pivot=a[0]
        a.pop(0)


        i=0
        j=len(a)-1
        while True:
            
            while True:
                
                if a[i]>=pivot:
                    break
                i+=1
                if j<i:
                    break

            
            while True:
                if a[j]<pivot:
                    break
                j-=1
                if j<i:
                    break

            if j<i:
                break
            else:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp

        a1=a[:i]
        a2=a[i:]

        res=quick_sort(a1)
        res.append(pivot)
        res.extend(quick_sort(a2))

    return res

def quick_sort2(arr):
    a=copy.copy(arr)

    res=None

    if len(a)<2:
        res=a

    elif len(a)==2:
        if a[0]>a[1]:
            temp=a[0]
            a[0]=a[1]
            a[1]=temp
        res=a

    elif len(a)<128:
        """
        b=a[:3]
        m=b[0]
        mind=0
        M=b[2]
        Mind=2
        for i in range(3):
            if b[i]<m:
                m=b[i]
                mind=i
            if b[i]>M:
                M=b[i]
                Mind=i
        s=[0,1,2]
        s.remove(mind)
        s.remove(Mind)
        pivot=a[s[0]]
        a.pop(s[0])
        """
        pivot=a[0]
        a.pop(0)

        i=0
        j=len(a)-1
        while True:
            
            while True:
                
                if a[i]>=pivot:
                    break
                i+=1
                if j<i:
                    break

            
            while True:
                if a[j]<pivot:
                    break
                j-=1
                if j<i:
                    break

            if j<i:
                break
            else:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp

        a1=a[:i]
        a2=a[i:]

        res=quick_sort2(a1)
        res.append(pivot)
        res.extend(quick_sort2(a2))

    else:
        
        """
        b=a[:3]
        m=b[0]
        mind=0
        M=b[2]
        Mind=2
        for i in range(3):
            if b[i]<m:
                m=b[i]
                mind=i
            if b[i]>M:
                M=b[i]
                Mind=i
        s=[0,1,2]
        s.remove(mind)
        s.remove(Mind)
        pivot=a[s[0]]
        a.pop(s[0])
        """
        a[:3]=insert_sort(a[:3])
        pivot=a[1]
        a.pop(1)

        i=0
        j=len(a)-1
        while True:
            
            while True:
                
                if a[i]>=pivot:
                    break
                i+=1

            
            while True:
                if a[j]<pivot:
                    break
                j-=1
                if j<i:
                    break

            if j<i:
                break
            else:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp

        a1=a[:i]
        a2=a[i:]

        res=quick_sort2(a1)
        res.append(pivot)
        res.extend(quick_sort2(a2))

    return res


arr=np.random.randint(0,100000,10000)

arr=arr.tolist()

t1=time.time()
bubble=bubble_sort(arr)
t2=time.time()
print("bubble sort:",t2-t1,"\n")

t1=time.time()
shaker=shaker_sort(arr)
t2=time.time()
print("shaker sort:",t2-t1,"\n")

t1=time.time()
merge=merge_sort(arr)
t2=time.time()
print("merge sort:",t2-t1,"\n")

t1=time.time()
select=select_sort(arr)
t2=time.time()
print("select sort:",t2-t1,"\n")

t1=time.time()
insert=insert_sort(arr)
t2=time.time()
print("insert sort:",t2-t1,"\n")

t1=time.time()
quick=quick_sort(arr)
t2=time.time()
print("quick sort:",t2-t1,"\n")

t1=time.time()
quick2=quick_sort2(arr)
t2=time.time()
print("quick sort 2:",t2-t1,"\n")

TF=True
for i,j,k,l,m,n,o in zip(merge,shaker,merge,select,insert,quick,quick2):
    TF = TF and i==j and j==k and k==l and l==m and m==n and n==o
print("correct:",TF)