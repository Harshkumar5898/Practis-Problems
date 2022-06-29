import random


def rohanMultiplication(Number):
    wrong = random.randint(0, 9)
    table = [i * Number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(1, 8)
    return table


def isCorrect(Table, Number):
    realTable = []
    for i in range(1, 11):
        realTable.append(i*Number)

    print(f"Original table is {realTable}\n")
    wrong = 0
    for i in range(10):
        if Table[i] != realTable[i]:
            print(
                f"The table is wrong at index {i} which should be {realTable[i]}")
            wrong += 1

    if wrong == 0:
        print("Your table is correct")


if __name__ == "__main__":

    table = rohanMultiplication(int(input("Enter a number : ")))
    print(f"\nYour table is {table}")
    a = isCorrect(table, table[0])
