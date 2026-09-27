class Tasks:
    def calc(self):
        while True:
            op = input("Operation (+, -, *, /) or 'exit': ").strip()
            if op == "exit":
                break
            if op not in ("+", "-", "*", "/"):
                print("Unknown operation")
                continue
            a = float(input("a = "))
            b = float(input("b = "))
            if op == "+":
                print(a + b)
            elif op == "-":
                print(a - b)
            elif op == "*":
                print(a * b)
            elif op == "/":
                print(a / b if b != 0 else "Division by zero")
    def test_list(self):
        arr = [4, 1, 7]
        arr.append(5)
        arr.extend([2, 9])
        arr.insert(0, 10)
        arr.remove(10)
        arr.sort()
        arr.reverse()
        copy_arr = arr.copy()
        arr.clear()
        for item in copy_arr:
            print(item, end=" ")
        print("\nCleared:", arr)
    def test_dict(self):
        data = {"a": 1, "b": 2}
        data.update({"c": 3, "d": 4})
        del data["a"]
        for k in data.keys():
            print("Key:", k)
        for v in data.values():
            print("Value:", v)
        for k, v in data.items():
            print(f"{k} -> {v}")

        data.clear()
        print("Empty:", data)

    def find_pos(self, lst, num):
        for i in range(len(lst)):
            if lst[i] >= num:
                return i
        return len(lst)
t = Tasks()
t.calc()
t.test_list()
t.test_dict()
print("Position:", t.find_pos([10, 20, 30, 40], 25))