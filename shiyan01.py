def bubble_sort(n):
    n=str(n)
    n = n.split(',')
    n=list(map(int, n))
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    print(n)
while True:
    n=input()
    bubble_sort(n)

