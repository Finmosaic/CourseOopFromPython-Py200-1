class Calculator:
    # TODO Написать статический метод add для сложения двух чисел

    @staticmethod
    def add(a, b):
        if not isinstance(a, (int, float)):
            raise TypeError
        if not isinstance(b, (int, float)):
            raise TypeError
        return a + b
    # TODO  Написать статический метод mul для умножения двух чисел
    @staticmethod
    def mul(a, b):
        if not isinstance(a, (int, float)):
            raise TypeError
        if not isinstance(b, (int, float)):
            raise TypeError
        return a * b

if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
