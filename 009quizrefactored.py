score = 0
questions =[
    ("Hur många bor i Liechtenstein? \na. 37 810 \nb. 192 929 \nc. 10 230\n", "a" ),
    ("Vem är grundaren av Wado-ryu Karate? ", "othsuka"),
    ("Vad är 9 - 3 / (1/3) + 1? ", "1"),
    ("Om en man föddes i Norge, växte upp i Sverige, reser till Spanien och dör i Madrid. Vad är han då? ", "död"),
    ("Arkitekterna Jansson, Dalh och Bergqvist bygger ett hus tillsammans. Vad börjar arbetet med? ", "a"),
]
for q in questions:
    answer = str(input(q[0]))
    if answer.lower() == q[1]:
        score = score + 1
        print("Mhm")
    else:
        print("Mhmm")

print("du hade", score * 100 / len(questions), "%", "rätt")