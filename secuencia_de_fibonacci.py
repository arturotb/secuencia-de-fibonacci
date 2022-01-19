TITLE = "Secuencia de Fibonacci"

def title(title):
    print("-" * len(title) + "{}".format(title) + "-" * len(title) + "\n")

def ask_limit():
    limit = int(input("hasta que numero en la secuencia de fibonacci quieres llegar? "))
    while limit < 0:
        limit = int(input("el limite debe ser un numero mayor a cero, hasta que numero en la secuencia de fibonacci quieres llegar? "))
    return limit

def fibonacci(limit):
    a = 0
    b = 1
    c = a + b
    fibonacci_sequence = []
    fibonacci_sequence.append(a)
    fibonacci_sequence.append(b)
    while c < limit:
        c = a + b
        if c <= limit:
            fibonacci_sequence.append(c)
            a = b
            b = c
    print("\nLa secuencia de fibonacci, antes de pasar al {}, es esta".format(limit))
    print(fibonacci_sequence)
    print("xd")

def recursion():
    recursion = input("quieres volver a usar el programa? [S/n]")
    if recursion == "s":
        main()
    elif recursion == "S":
        main()
    
    

def main():
    title(TITLE)
    limit = ask_limit()
    fibonacci(limit)
    recursion()


if __name__ == "__main__":
    main()
