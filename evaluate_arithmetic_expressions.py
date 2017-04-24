import sympy
x, y, z = sympy.symbols('x y z')
print sympy.sympify("x**3").evalf(subs={x:1})
