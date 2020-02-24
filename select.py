def selection_sort(nums):  
    # значение i соответствует тому, сколько значений было отсортировано
    for i in range(len(nums)):
        # Мы предполагаем, что первый элемент несортированного сегмента является наименьшим
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Поменять местами значения самого низкого несортированного элемента с первым несортированным
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
# Проверяем, что это работает
random_list_of_nums = [12, 46, 86, 75, 8, 3, 16, 20, 11, 55, 98, 1, 3, 5, 14, 6, 23, 33, 42]  
selection_sort(random_list_of_nums)  
print(random_list_of_nums)
