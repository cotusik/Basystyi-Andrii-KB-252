class Homework:
    def revers_text(self, text):
        return text[::-1]
    def test_strings(self, text):
        print(text.strip())
        print(text.capitalize())
        print(text.title())
        print(text.upper())
        print(text.lower())
    def get_discriminant(self, a, b, c):
        return b**2-4*a*c

hw = Homework()
print(hw.revers_text("Cyp450"))
hw.test_strings("amino keto")
print(hw.get_discriminant(-8, 8, 8))