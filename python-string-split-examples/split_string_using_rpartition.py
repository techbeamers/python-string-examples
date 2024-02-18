# Example math expr
math_expr = "3 * (5 + 2) / 4"

# Using rpartition() to split the math expr
operator, _, operand = math_expr.rpartition(' ')

# Prin the results
print("Original Math Expression:", math_expr)
print("Operator:", operator)
print("Operand:", operand)
