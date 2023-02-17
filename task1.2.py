n = int(input("How many numbers do you want to add to list? "))
my_list = []
for i in range (0,n):
    my_list.append(int(input()))
my_list.sort()
print("Min =", my_list[0])
print("Max =", my_list[-1])


