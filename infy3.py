# reverse a string keeping its special character in place
import re
string=input()
string_list=re.findall("[a-zA-Z]",string)
string_list.reverse()
for i in range(len(string)):
    if string[i]=='#' or string[i]=='@':
        string_list.insert(i,string[i])
print(''.join(string_list))
