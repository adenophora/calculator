import sys

def main():
    userInput = input("Введите: ")

    checkLenght(userInput)

    result = returnNumbersIfCorrect(userInput)

    areNumbersCorrect(result)

    Sign = checkSign(result, userInput)

    print(int(solution(result, Sign)))

def returnNumbersIfCorrect(x):
    try:
        a = int(x[:2])
        b = int(x[-2:])
    except:
        print("throws Exception 1")
        sys.exit()
    else:
        return a,b

def areNumbersCorrect(x):
    if x[0] < 1 or x[0] > 10 or x[1] < 1 or x[1] > 10:
        print("throws Exception 2")
        sys.exit()
    else:
        return 0

def checkLenght(x):
    if len(x) < 5 or len(x) > 7:
        print("throws Exception 3")
        sys.exit()

def checkSign(numbers, x):
    if numbers[0] == numbers[1]:
        pos = int(len(x) / 2)
    elif numbers[1] == 10:
        pos = int(len(x) / 2 - 1)
    else:
        pos = int(len(x) / 2)
    return x[pos]

def solution(numbers, sign):
    if sign == "+":
        return numbers[0] + numbers[1]
    elif sign == "-":
        return numbers[0] - numbers[1]
    elif sign == "*":
        return numbers[0] * numbers[1]
    elif sign == "/":
        return numbers[0] / numbers[1]
    print("throws Exception 4")
    sys.exit()

main()