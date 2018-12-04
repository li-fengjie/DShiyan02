import random
import time
n=[]
for i in range(0,10000):
    x=random.randint(0,10000)
    n.append(x)
def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    print(n)

def quick_sort(n):

    for i in range(len(n)-1):
        for j in range(i,len(n)):
            if n[j] < n[i]:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp
    print(n)

def insert_sort(n):
    for i in range(1, len(n)):
        if n[i - 1] > n[i]:
            temp = n[i]
            index = i
            while index > 0 and n[index - 1] > temp:
                n[index] = n[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                index -= 1
            n[index] = temp  # 把需要排序的元素，插入到指定位置
    print(n)

#while True:
#bubble_sort(n)
quick_sort(n)
#insert_sort(n)
end=time.clock()
print(round(end,3))
