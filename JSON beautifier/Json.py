global s

def quit():
    exit(print('---'))
           
def checkNum(l , r):
    if(s[l] == '-'): l += 1
    if(s[l:r].count('.') > 1 or r-l == 0): quit()
    for i in range(l , r):
        if(s[i] not in "0123456789." or s[i] == '.' and (i == l or i == r-1)): quit()

def checkBool(l , r , end_of_str):
    if(s[l:r] == 'true'):
        end_of_str[l] = 'T'
    elif(s[l:r] == 'false'):
        end_of_str[l] = 'F'
    elif(s[l:r] == 'null'):
        end_of_str[l] = 'N'; end_of_str[l+1] = 'o'; end_of_str[l+2] = 'n'; end_of_str[l+3] = 'e'
    else: quit()

def checkArr(l , r , end_of_str):
    if(s[l] != '['): quit()
    if(r-l == 2): return
    i = l+1
    while(i < r):
        if(s[i] == '[' or s[i] == '{' or s[i] == '"'):
            i = end_of_str[i]
            if(s[i+1] != ',' and i+1 != r-1): quit()
            i += 2
        elif(s[i] in "0123456789-"):
            j = i
            while(s[j] != ',' and j != r-1): j += 1
            checkNum(i,j)
            i = j+1
        else:
            j = i
            while(s[j] != ',' and j != r-1): j += 1
            checkBool(i,j,end_of_str)
            i = j+1

def checkObj(l , r , end_of_str):
    if(s[l] != '{'): quit()
    if(r-l == 2): return
    i = l+1
    while(i < r):
        if(s[i] != '"' or s[end_of_str[i]+1] != ':'): quit()
        i = end_of_str[i]+2
        if(s[i] == '[' or s[i] == '{' or s[i] == '"'):
            i = end_of_str[i]
            if(s[i+1] != ',' and i+1 != r-1): quit()
            i += 2
        elif(s[i] in "0123456789-"):
            j = i
            while(s[j] != ',' and j != r-1): j += 1
            checkNum(i,j)
            i = j+1
        else:
            j = i
            while(s[j] != ',' and j != r-1): j += 1
            checkBool(i,j,end_of_str)
            i = j+1


def Print(end_of_str):
    lst = []
    tabs = 0
    quotation = 0
    i = 1
    while(i < len(s)-1):
        char = s[i]
        for c in "NoneTF":
            if(c == end_of_str[i]): char = c
        if(s[i] == '"'): quotation = 1 - quotation
        if(not quotation):
            if(s[i] == '[' or s[i] == '{'): tabs += 2
            if(s[i] == ']' or s[i] == '}'): tabs -= 2
            if(s[i] == ':'): 
                char += ' '
            if(s[i] == ',' or ((s[i] == '[' or s[i] == '{') and end_of_str[i] != i+1)):
                char = char + '\n' + tabs*' '
            if((s[i] == ']' or s[i] == '}') and (s[i-1] != '[' and s[i-1] != '{')):
                char = '\n' + tabs*' ' + char
        lst.append(char)
        i += 1
    print(''.join(lst))
 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=+++++++
            

s = input()
removedspace = ""
quotation = 0
for i in range(len(s)):
    if(s[i] == '"'): quotation = 1 - quotation
    if(quotation or s[i] != ' '): removedspace += s[i]

s = removedspace
s = '[' +s+ ']'

end_of_str = [0 for i in s]
quotation = 0
lastquotation = 0
openings = []
for i in range(len(s)):
    if(s[i] == '"'): 
        quotation = 1 - quotation
        if(quotation == 0):
            end_of_str[lastquotation] = i
        else:
            lastquotation = i
    if(quotation == 0 and s[i] == '[' or s[i] == '{'):
        openings.append(i)
    elif(quotation == 0 and s[i] == ']' or s[i] == '}'):
        if(len(openings) == 0): quit()
        end_of_str[openings[-1]] = i
        if(s[i] == ']'): checkArr(openings[-1] , i+1 , end_of_str)
        else: checkObj(openings[-1] , i+1 , end_of_str)
        openings.pop()
Print(end_of_str)
