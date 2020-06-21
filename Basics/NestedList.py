if __name__ == '__main__':
    arr = []
    personarr = []
    n = int(input())
    arr = [[input(), float(input())] for i in range(n)]
        
    max = float(arr[0][1])
    person = arr[0][0]
    min = float(arr[0][1])

    for r in range(len(arr)):
        if  float(arr[r][1])>max:
            max = float(arr[r][1])
        if(float(arr[r][1])<min):
            min = float(arr[r][1])

    for r in range(len(arr)):
        if float(arr[r][1])>min and float(arr[r][1])<max:
            max = arr[r][1]
        if(float(arr[r][1]) == max):
            person = arr[r][0]
            personarr.append(person)
            x = sorted(personarr)
    for i in x:
        print (i)