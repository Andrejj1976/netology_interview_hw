class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


def check_brackets(sequence: str) -> str:
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


if __name__ == "__main__":
    # Проверка на всех примерах из условия задания
    examples = [
        ("(((([{}]))))", "Сбалансированно"),
        ("[([])((([[[]]])))]{()}", "Сбалансированно"),
        ("{{[()]}}", "Сбалансированно"),
        ("}{}", "Несбалансированно"),
        ("{{[(])]}}", "Несбалансированно"),
        ("[[{())}]", "Несбалансированно"),
    ]

    for seq, expected in examples:
        result = check_brackets(seq)
        assert result == expected, f"Ошибка для {seq}: получили {result}, ожидали {expected}"

    user_input = input("Введите строку со скобками: ")
    print(check_brackets(user_input))