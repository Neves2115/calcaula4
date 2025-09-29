def calcular(primeiro, segundo, operacao):
    try:
        x = float(primeiro)
        y = float(segundo)
    except (ValueError, TypeError):
        return None

    if operacao == '/':
        if y == 0:
            return None
        return x / y
    if operacao == '+':
        return x + y
    if operacao == '-':
        return x - y
    if operacao == '*':
        return x * y
    if operacao == '^':
        return x ** y

    return None
