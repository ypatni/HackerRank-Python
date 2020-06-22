def swap_case(s):
    
    ans = ""
    for x in s:
        if(x.islower()):
            ans = ans + x.upper()
        else:
            ans = ans + x.lower()

    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)