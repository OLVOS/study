

def union(nums1, nums2):
    f, s = 0, 0
    res = []
    while f < len(nums1) and s < len(nums2):
        f_num, s_num = nums1[f], nums2[s]

        if f_num < s_num:
            f += 1
        elif f_num > s_num:
            s += 1
        elif f_num == s_num:
            res.append(f_num)
            f += 1
            s += 1

    return res


def check_intersection_function(func):
    tests = [
        # 1. Базовый случай (твой пример из условия)
        ([0, 2, 4, 8, 8], [1, 2, 2, 7, 8, 8, 8], [2, 8, 8]),

        # 2. Вообще нет общих элементов
        ([1, 2, 3], [4, 5, 6], []),

        # 3. Один список пустой (частая причина ошибок)
        ([], [1, 2, 3], []),

        # 4. Списки полностью идентичны
        ([1, 1, 2], [1, 1, 2], [1, 1, 2]),

        # 5. Списки сильно разной длины, совпадает один элемент
        ([5], [1, 2, 3, 4, 5, 6], [5]),

        # 6. Отрицательные числа и нули
        ([-5, -1, 0, 2], [-5, 0, 3], [-5, 0]),

        # 7. Общие элементы только в самом начале или самом конце
        ([1, 2, 3], [1, 8, 9], [1]),
        ([3, 4, 5], [1, 2, 5], [5])
    ]

    passed = True
    for i, (nums1, nums2, expected) in enumerate(tests, 1):
        result = func(nums1, nums2)
        if result == expected:
            print(f"✅ Тест {i} пройден")
        else:
            print(f"❌ Тест {i} ПРОВАЛЕН!")
            print(f"   Вход: {nums1} | {nums2}")
            print(f"   Ожидалось: {expected}, Получено: {result}")
            passed = False

    if passed:
        print("🎉 Все тесты успешно пройдены!")


check_intersection_function(union)
