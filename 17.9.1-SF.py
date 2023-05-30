while True:
    try:
        nums = list(map(int, input("Введите список чисел через пробел:").split()))
        break
    except ValueError:
        print('Недопустимый ввод')
while True:
    try:
        num = int(input("Введите случайное число:"))
        break
    except ValueError:
        print('Недопустимый ввод')

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

def binary_search(nums, num, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит число отсутствует

        middle = (right + left) // 2  # находимо середину
        if nums[middle] == num:  # если число в середине,
            return middle  # возвращаем этот индекс
        elif num < nums[middle]:  # если число меньше числа в середине
            # рекурсивно ищем в левой половине
            return binary_search(nums, num, left, middle - 1)
        else:  # иначе в правой
            return binary_search(nums, num, middle + 1, right)
    except IndexError:
        return -1

result = binary_search(nums, num, 0, len(nums))

big = 'Ближайшее большее число:'
little = 'Ближайшее меньшее число:'

if not binary_search(nums, num, 0, len(nums)):
    rI = min(nums, key=lambda x: (abs(x - num), x))
    ind = nums.index(rI)
    more_ind = ind + 1
    less_ind = ind - 1

    if rI < num:
        print(f'''В списке нет введенного числа      
        {big} {nums[more_ind]} его индекс: {more_ind}
        {little} {rI}, его индекс: {ind}''')
    elif nums.index(rI) == 0:
        if num == nums[0]:
            print(f'''Индекс введенного числа: {ind}
            {big} {nums[more_ind]}, его индекс: {more_ind}
            {little} отсутствует''')
        else:
            print(f'''В списке нет введенного числа
            {big} {nums[0]}, его индекс: {ind}
            {little} отсутствует''')
    elif less_ind < 0:
        print(less_ind)
        print(f'''В списке нет введенного числа
        {big} {rI}, его индекс: {nums.index(rI)}
        В списке нет меньшего числа''')
    elif rI > num:
        print(f'''В списке нет введенного числа
        {big} {rI}, его индекс: {nums.index(rI)}
        {little} {nums[less_ind]} его индекс: {less_ind}''')

else:
    if result == -1:
        print(f'''Число находится за правой границей списка, 
        Индекс введенного числа: отсутствует
        {little} {nums[-1]}, его индекс: {nums.index(nums[-1])} ''')
    else:
        print(f'''Индекс введенного числа: {binary_search(nums, num, 0, len(nums))}
        {big} отсутствует
        {little} {nums[result - 1]}, его индекс {result - 1} ''')