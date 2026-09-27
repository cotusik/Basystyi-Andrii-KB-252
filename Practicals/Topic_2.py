class ADRA1A:
    def formula(self, a, b, c): return b**2 - 4*a*c
    def roots(self, a, b ,c): 
        d = self.formula(a, b, c)
        if d > 0:
          return (-b + d**0.5) / (2 * a), (-b - d**0.5) / (2 * a)
        elif d==0:
            return -b / (2*a)
        else:
            return "no rooots"
    def plus(self, a, b): return a + b
    def minus(self, a, b): return a - b
    def multiply(self, a, b): return a *b
    def divide(self, a, b): return a / b
    def iff(self, a, symbol, b):
        if symbol == "+": return self.plus(a,b)
        elif symbol == "-": return self.minus(a,b)
        elif symbol == "*": return self.multiply(a,b)
        elif symbol == "/": return self.divide(a,b)
        else: return "?"
    def matchh(self, a, symbol, b):
        match symbol:
            case "+": return self.plus(a, b)
            case "-": return self.minus(a, b)
            case "*": return self.multiply(a, b)
            case "/": return self.divide(a, b)
            case _: return "??"
B = ADRA1A()
print(B.roots(1, -5, 6))
print(B.iff(10, "+", 190))
print(B.matchh(1000, '/', 2))
