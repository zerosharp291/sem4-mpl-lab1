def calculate_lift_time(_peoples_count, _lift_capacity, _hariton_floor_number, _floors):
    # Добавляем этаж Харитона в список
    _floors.append(_hariton_floor_number)

    # Инициализация переменных
    time = _peoples_count * 2  # Вход и выход для каждого человека
    current_lift_floors = []  # Этажи, на которые едут люди в текущей поездке
    max_floor_in_ride = 1  # Максимальный этаж в текущей поездке

    counter = 0
    for floor in _floors:
        # Добавляем человека в лифт
        current_lift_floors.append(floor)
        max_floor_in_ride = max(max_floor_in_ride, floor)

        counter += 1
        # Проверка на то что это последняя поездка
        if counter == len(_floors):
            current_lift_floors.sort(reverse=True)  # вычтем из расчета времени людей которые выйду после  Харитона
            time += _hariton_floor_number
            for elem in current_lift_floors:
                if elem >= _hariton_floor_number:
                    time -= 1

        # Если лифт заполнен едем на максимальный этаж
        elif len(current_lift_floors) == _lift_capacity:
            time += (max_floor_in_ride - 1) * 2  # Время на поездку и возвращение
            current_lift_floors.clear()  # Очищаем лифт
            max_floor_in_ride = 1  # Сбрасываем максимальный этаж

    return time


# Ввод данных
peoples_count = int(input()) + 1
lift_capacity = int(input())
hariton_floor_number = int(input())

floors = []
for i in range(peoples_count - 1):
    floors.append(int(input()))

# Вычисление времени
total_time = calculate_lift_time(peoples_count, lift_capacity, hariton_floor_number, floors)
print(total_time)
