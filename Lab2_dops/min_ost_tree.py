graph = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
         (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

graph = sorted(graph, key=lambda x: x[0])
connected = set()  # список соединенных вершин
isolated = {}  # словарь списка изолированных групп вершин
skeleton = []  # список ребер остова

for ver in graph:
    if ver[1] not in connected or ver[2] not in connected:  # проверка для исключения циклов в остове
        if ver[1] not in connected and ver[2] not in connected:  # если обе вершины не соединены, то
            isolated[ver[1]] = {ver[1], ver[2]}  # формируем в словаре ключ с номерами вершин
            isolated[ver[2]] = isolated[ver[1]]  # и связываем их с одним и тем же списком вершин
        else:  # иначе
            if not isolated.get(ver[1]):  # если в словаре нет первой вершины, то
                isolated[ver[2]].add(ver[1])  # добавляем в список первую вершину
                isolated[ver[1]] = isolated[ver[2]]  # и добавляем ключ с номером первой вершины
            else:
                isolated[ver[1]].add(ver[2])  # иначе, все то же самое делаем со второй вершиной
                isolated[ver[2]] = isolated[ver[1]]

        skeleton.append(ver)  # добавляем ребро в остов
        connected.add(ver[1])  # добавляем вершины в множество U
        connected.add(ver[2])

for ver in graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
    if ver[2] not in isolated[ver[1]]:  # если вершины принадлежат разным группам, то объединяем
        skeleton.append(ver)  # добавляем ребро в остов
        isolated[ver[1]].update(isolated[ver[2]])  # объединем списки двух групп вершин
        isolated[ver[2]].update(isolated[ver[1]])

print(skeleton)
