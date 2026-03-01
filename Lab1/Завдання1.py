from bank_analysis import analyze_transactions

def get_input():
    print("=== Банківський аналізатор операцій ===\n")
    a = input("Введіть підозрілий патерн : ")
    b = []
    for i in a.split(","):
        b.append(int(i.strip()))
    c = input("Введіть операції клієнта за день : ")
    d = []
    for i in c.split(","):
        d.append(int(i.strip()))
    return b, d

def main():
    x, y = get_input()
    res = analyze_transactions(x, y)
    print("\n--- Результат ---")
    if res:
        print(f" Патерн є")
    else:
        print(" Патерна нема. Результат: -1")

if __name__ == "__main__":
    main()