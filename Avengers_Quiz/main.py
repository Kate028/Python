from questions import quiz
from questions import options
from questions import Avenger

a = 0  # Ironman
b = 0  # Captain America
c = 0  # Hulk
d = 0  # Thor
e = 0  # Wanda
f = 0  # Dr. Strange
g = 0  # Vision
h = 0  # Spiderman
i = 0  # Black Widow
j = 0  # Hawkeye


def error():
    print("Enter a valid integer answer!")


def check(question, ans):
    global a, b, c, d, e, f, g, h, i, j
    if question == 1:
        if 0 < ans < 5:
            if ans == 1:
                a += 1
                h += 1
                e += 1
                f += 1
            elif ans == 2:
                b += 1
                f += 1
                g += 1
            elif ans == 3:
                i += 1
                j += 1
            else:
                c += 1
            return 1
        else:
            error()
            return 0

    elif question == 2:
        if 0 < ans < 5:
            if ans == 1:
                c += 1
            elif ans == 2:
                a += 1
                d += 1
                h += 1
            elif ans == 3:
                b += 1
                g += 1
                i += 1
                j += 1
                e += 1
            else:
                f += 1
                a += 1
                d += 1
            return 1
        else:
            error()
            return 0

    elif question == 3:
        if 0 < ans < 5:
            if ans == 1:
                a += 1
                b += 1
            elif ans == 2:
                c += 1
                d += 1
                e += 1
                h += 1
                i += 1
            elif ans == 3:
                c += 1
            else:
                j += 1
                g += 1
                f += 1
            return 1
        else:
            error()
            return 0

    elif question == 4:
        if 0 < ans < 5:
            if ans == 1:
                b += 1
                i += 1
                c += 1
            elif ans == 2:
                e += 1
                h += 1
                g += 1
            elif ans == 3:
                a += 1
                d += 1
                j += 1
            else:
                h += 1
            return 1
        else:
            error()
            return 0

    elif question == 5:
        if 0 < ans < 4:
            if ans == 1:
                b += 1
                c += 1
                i += 1
                j += 1
            elif ans == 2:
                a += 1
                d += 1
                e += 1
                h += 1
            else:
                f += 1
                g += 1
            return 1
        else:
            error()
            return 0

    elif question == 6:
        if 0 < ans < 3:
            if ans == 1:
                a += 1
                c += 1
                e += 1
                f += 1
                g += 1
            else:
                b += 1
                d += 1
                h += 1
                i += 1
                j += 1
            return 1
        else:
            error()
            return 0

    elif question == 7:
        if 0 < ans < 5:
            if ans == 1:
                e += 1
                g += 1
                j += 1
            elif ans == 2:
                b += 1
            elif ans == 3:
                a += 1
                f += 1
                h += 1
                d += 1
            else:
                c += 1
                i += 1
            return 1
        else:
            error()
            return 0

    elif question == 8:
        if 0 < ans < 5:
            if ans == 1:
                i += 1
                b += 1
                j += 1
            elif ans == 2:
                a += 1
                d += 1
                e += 1
                c += 1
            elif ans == 3:
                f += 1
                g += 1
            else:
                h += 1
                a += 1
                g += 1
            return 1
        else:
            error()
            return 0

    elif question == 9:
        if 0 < ans < 5:
            if ans == 1:
                g += 1
                h += 1
            elif ans == 2:
                e += 1
                i += 1
            elif ans == 3:
                a += 1
                c += 1
                j += 1
                f += 1
            else:
                b += 1
                d += 1
            return 1
        else:
            error()
            return 0

    elif question == 10:
        if 0 < ans < 4:
            if ans == 1:
                h += 1
                f += 1
                e += 1
                b += 1
                c += 1
                j += 1
            elif ans == 2:
                a += 1
                i += 1
                g += 1
            elif ans == 3:
                d += 1
            return 1
        else:
            error()
            return 0


print("\n")
print("##################################################################################")
print("WELCOME! Let's try to find out which avenger you are?!")
print("You will be given 10 questions, choose among the given options to find out your avenger type...")
print("##################################################################################")

fail = 0

for question, option in zip(quiz, options):
    print(quiz[question])
    print(options[option])

    try:
        ans = int(input("Enter your answer: "))
        print("-----------------------------------------------------------------")
        if check(question, ans):
            continue
        else:
            print("Sorry, You need to retake the quiz!!")
            fail = 1
            break

    except (ValueError, TypeError):
        error()
        print("Sorry, You need to retake the quiz!!")
        fail = 1
        break

if fail == 0:
    answers = []
    answers.append((a, "Ironman"))
    answers.append((b, "Captain America"))
    answers.append((c, "Hulk"))
    answers.append((d, "Thor"))
    answers.append((e, "Wanda"))
    answers.append((f, "Dr. Strange"))
    answers.append((g, "Vision"))
    answers.append((h, "Spiderman"))
    answers.append((i, "Black Widow"))
    answers.append((j, "Hawkeye"))

    answers.sort(reverse=True)

    # print(a,b , c, d, e, f, g, h, i, j)
    # print(answers)
    # print(answers[0][1])

    print(Avenger[answers[0][1]])
