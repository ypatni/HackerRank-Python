if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        #print(scores)
        student_marks[name] = scores
    
    query_name = input()
    
    sum = 0;
    for i in student_marks[query_name]:
       sum = sum+i
    avg = sum/3
    formatted_avg = "{:.2f}".format(avg)
    print (formatted_avg)
