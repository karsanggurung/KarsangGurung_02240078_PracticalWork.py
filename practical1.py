first_list = [0,1,2,3,4,5,6,7,8,9]
inverse_list = []

while first_list:
    inverse_list.append(first_list.pop())

print(inverse_list)
print(first_list)

# queestion 2

def reverse_array(first_list):
    inverse_list = reverse_array(first_list)  
    while first_list:
      inverse_list.append(first_list.pop())
   
      return inverse_list
first_list = [0,1,2,3,4,5,6,7,8,9]
print(inverse_list)