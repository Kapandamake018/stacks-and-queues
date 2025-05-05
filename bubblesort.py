def bubble_sort(my_list):
  for i in range(len(my_list)-1):
    for j in range(len(my_list)-i-1):
      if my_list[j] > my_list[j+1]:
        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
  return my_list



print(bubble_sort([7, 3, 5, 8, 10, 1]))
    
    