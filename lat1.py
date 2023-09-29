# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi penjumlahan
def add(a, b):
    return a + b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol."
    return a / b

# Fungsi untuk mengevaluasi pohon ekspresi
def tree(expression):
    if isinstance(expression, tuple):
        left = tree(expression[0])
        operator = expression[1]
        right = tree(expression[2])

        if operator == '+':
            return add(left, right)
        elif operator == '-':
            return minus(left, right)
        elif operator == '*':
            return mult(left, right)
        elif operator == '/':
            return div(left, right)
    else:
        return expression  # Basis: expression adalah angka

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)