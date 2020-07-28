length_of_list=int(input('Please enter the length of list:\n'))   #Here we are taking input by user for the length of List where we will store the values.
list1=[]                                                         #Here we are declaring an list named list1

for i in range(0,length_of_list):                                #We are running the loop that will run in the range (0,length_of_list) i.e (0,1,2...length_of_list-1)
    list1.append(int(input()))

print(list1)
    
