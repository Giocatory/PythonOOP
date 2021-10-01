class Stack:
    def __init__(self):
        self.value = []

    def push(self, item):
        self.value.append(item)

    def pop(self):
        if len(self.value) != 0:
            return self.value.pop()
        else:
            print("Empty Stack")

    def peek(self):
        if len(self.value) != 0:
            return self.value[-1]
        else:
            print("Empty Stack")
            return None

    def is_empty(self):
        return True if len(self.value) == 0 else False

    def size(self):
        return len(self.value)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2
