def count_substring(string, sub_string):
    num = 0
    check = True
    starting_index =0
    while check:
        x = string.find(sub_string, starting_index)
        if x== -1:
            check = False
        else: 
            num+=1
            starting_index =x+1
    return num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)