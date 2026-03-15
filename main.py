import unittest
class DynArray:
    def __init__(self, initial_capacity=4):
        if initial_capacity <= 0:
            raise ValueError("Начальная емкость должна быть больше 0")
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity
    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        i = 0
        while i < self._size:
            new_data[i] = self._data[i]
            i += 1
        self._data = new_data
        self._capacity = new_capacity
    def _check_index(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Индекс вне диапазона")
    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1
    def get(self, index):
        self._check_index(index)
        return self._data[index]
    def set(self, index, value):
        self._check_index(index)
        self._data[index] = value
    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Индекс вне диапазона")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        i = self._size
        while i > index:
            self._data[i] = self._data[i - 1]
            i -= 1
        self._data[index] = value
        self._size += 1
    def remove_at(self, index):
        self._check_index(index)
        removed_value = self._data[index]
        i = index
        while i < self._size - 1:
            self._data[i] = self._data[i + 1]
            i += 1
        self._data[self._size - 1] = None
        self._size -= 1
        return removed_value
    def size(self):
        return self._size
    def capacity(self):
        return self._capacity
    def __str__(self):
        result = "["
        i = 0
        while i < self._size:
            result += str(self._data[i])
            if i != self._size - 1:
                result += ", "
            i += 1
        result += "]"
        return result
def main():
    arr = DynArray()
    try:
        n = int(input("Введите количество элементов, которые нужно добавить в массив "))
        if n < 0:
            print("Количество элементов не может быть отрицательным")
            return
        i = 0
        while i < n:
            value = int(input(f"Введите элемент {i + 1}"))
            arr.append(value)
            i += 1
        print("Массив после добавления элементов", arr)
        print("Размер массива", arr.size())
        print("Ёмкость массива", arr.capacity())
        index = int(input("Введите индекс элемента для получения"))
        print("Элементпо индексу", index, "=", arr.get(index))
        index = int(input("Введите индекс элемента для замены"))
        value = int(input("Введите новое значение"))
        arr.set(index, value)
        print("Массив после set", arr)
        index = int(input("Введите индекс для вставки"))
        value = int(input("Введите значение для вставки"))
        arr.insert(index, value)
        print("Массив после insert", arr)
        index = int(input("Введите индекс элемента для удаления"))
        removed = arr.remove_at(index)
        print("Удалённый элемент", removed)
        print("Массив после remove_at", arr)
        print("Количество элементов", arr.size())
        print("Текущая ёмкость массива", arr.capacity())

    except ValueError:
        print("Вводи целые числа")
    except IndexError as e:
        print("Ошибка", e)

class TestDynArray(unittest.TestCase):
    def test_append(self):
        arr = DynArray(2)
        arr.append(10)
        arr.append(20)
        arr.append(30)
        self.assertEqual(str(arr), "[10, 20, 30]")
        self.assertEqual(arr.size(), 3)
        self.assertEqual(arr.capacity(), 4)
    def test_get(self):
        arr = DynArray()
        arr.append(5)
        arr.append(7)
        self.assertEqual(arr.get(1), 7)
    def test_set(self):
        arr = DynArray()
        arr.append(1)
        arr.append(2)
        arr.set(0, 99)
        self.assertEqual(arr.get(0), 99)
    def test_insert(self):
        arr = DynArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        arr.insert(1, 15)
        self.assertEqual(str(arr), "[10, 15, 20, 30]")
    def test_remove_at(self):
        arr = DynArray()
        arr.append(10)
        arr.append(15)
        arr.append(20)
        arr.append(30)
        removed = arr.remove_at(2)
        self.assertEqual(removed, 20)
        self.assertEqual(str(arr), "[10, 15, 30]")
    def test_size(self):
        arr = DynArray()
        arr.append(1)
        arr.append(2)
        self.assertEqual(arr.size(), 2)
    def test_capacity(self):
        arr = DynArray(2)
        self.assertEqual(arr.capacity(), 2)
        arr.append(1)
        arr.append(2)
        arr.append(3)
        self.assertEqual(arr.capacity(), 4)


if __name__ == "__main__":
    main()
    print("Тесты")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)