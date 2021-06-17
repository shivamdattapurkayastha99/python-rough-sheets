# add and concat list valueswith given condition
num_list=input().split(',')
length=len(num_list)
index_five=num_list.index('5')
index_eight=num_list.index('8')
num2=''
num1=0
for i in range(index_five,index_eight+1):
    num2+=(''.join(num_list[i]))
for i in range(0,length):
    if i<index_five or i>index_eight:
        num1+=int(num_list[i])
print(num1+int(num2))
