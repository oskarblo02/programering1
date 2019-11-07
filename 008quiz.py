print("Hur många bor i Liechtenstein?")
 
print("a. 37 810")
print("b. 192 929")
print("c. 10 230")

user_input = input("Vad tror du? ")
 
if user_input == "a":
    print("Mhm")
    f1 = 1
else:
    print("Mhm")
    f1 = 0

print("Vem är grundaren av Wado-ryu Karate?")

user_input = input("Vad tror du? ")

if user_input == "Othsuka":
    print("Mhm")
    f2 = 1
else:
    print("Mhm")
    f2 = 0

print("Vad är 9 - 3 / (1/3) + 1?")

user_input = input("Vad tror du? ")

if user_input == "1":
    print("Mhm")
    f3 = 1
else:
    print("Mhm")
    f3 = 0

print("Om en man föddes i Norge, växte upp i Sverige, reser till Spanien och dör i Madrid. Vad är han då?")

user_input = input("Vad tror du? ")

if user_input == "död":
    print("Mhm")
    f4 = 1
else:
    print("Mhm")
    f4 = 0

print("Arkitekterna Jansson, Dalh och Bergqvist bygger ett hus tillsammans. Vad börjar arbetet med?")

user_input = input("Vad tror du? ")

if user_input == "a":
    print("Mhm")
    f5 = 1
else:
    print("Mhm")
    f5 = 0

poäng = f1 + f2 + f3 + f4 + f5

d = poäng/5

p = d * 100

print("du fick", p, "%", "rätt")