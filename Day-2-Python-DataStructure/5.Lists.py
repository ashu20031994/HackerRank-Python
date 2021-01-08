"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order 
and perform the corresponding operation on your list.
"""

def operation(N):
    lst=[]
    for i in range(0,N):
        command=(input().split())
        if(str(command[0])=='insert'):
            lst.insert(int(command[1]),int(command[2]))
        elif(command[0]=='print'):
            print(lst)
        elif(command[0]=='append'):
            lst.append(int(command[1]))
        elif(command[0]=='remove'):
            lst.remove(int(command[1]))
        elif(command[0]=='pop'):
            if(lst!=0):
                b=lst.pop()
        elif(command[0]=='sort'):
            lst.sort()
        elif(command[0]=='reverse'):
            lst.reverse()
            
if __name__ == '__main__':
    N = int(input())
    operation(N)
