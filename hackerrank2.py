### working with nested lists

print ("program starting")

list1 = []

try:
    N = int(input(""))
except ValueError:
    print ("please input an integer")

All_students = []
for i in range (N):
    sub_list = []
    name = str(input("\n enter a sudent name please:"))
    mark = float(int(input("\n enter sudent's mark please:")))
    sub_list.append (name)
    sub_list.append (mark)
    All_students.append(sub_list)

print(All_students)


for item in (All_students):
    list1.append(item[1])
print (list1)
list2 = sorted(list1)
print (list2)
## rearrange the list from the lowest to the highest
## take the lowest marks and print the students names
  
