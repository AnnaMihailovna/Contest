def can_place_cows(coords, k, distance):
    """
    Проверяет, возможно ли разместить k коров на заданных
    координатах coords с минимальным расстоянием distance между ними
    :param coords: координаты стойла
    :param k: количество коров на размещение
    :param distance: расстояние между стойлами
    :return: True - если возможно, иначе False
    """
    count = 1
    prev_position = coords[0]

    for i in range(1, len(coords)):
        if coords[i] - prev_position >= distance:
            count += 1
            prev_position = coords[i]
            if count >= k:
                return True

    return False


def place_cows(coords, k):
    """
    Функция, реализует жадный алгоритм,
    используется для размещения коров
    :return cows - координаты стойл
    """
    coords.sort()  # Сортируем стойла по возрастанию координат
    left = 1
    right = coords[-1] - coords[0]
    max_distance = 0
    # Нахождение максимального расстояния между
    # коровами в стойлах через алгоритм бинарного поиска
    while right - left > 1:
        mean  = (left + right) // 2
        if can_place_cows(coords, k, mean):
            max_distance = max(max_distance, mean)
            left = mean
        else:
            right = mean

    return max_distance


# тестовые данные
stall = [1, 2, 4, 6, 8, 10, 13] # координаты стойл
k = 3 # количество коров для размещения

result = place_cows(stall, k) # ответ 5 - максимальная длина между стойлами коров
print(result)

# n, k = map(int, input().split())
# coords = list(map(int, input().split()))
# def check(x):
#     cows = 1
#     lastcow = coords[0]
#     for i in coords:
#         if i - lastcow >= x:
#             cows += 1
#             lastcow = i
#     return cows >= k
# def solve():
#     left = 0
#     right = coords[-1] - coords[0] + 1
#     m = (left + right) // 2
#     if check(m):
#         left = m
#     else:
#         right = m
#     return left
# print(solve())
