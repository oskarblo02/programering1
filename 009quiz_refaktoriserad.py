score = 0

questions =[
    ("Hur många bor i Liechtenstein? \na. 37 810 \nb. 192 929 \nc. 10 230\n", "a" ),
    ("Vem är grundaren av Wado-ryu Karate? ", "othsuka"),
    ("Vad är 9 - 3 / (1/3) + 1? ", "1"),
    ("Om en man föddes i Norge, växte upp i Sverige, reser till Spanien och dör i Madrid. Vad är han då? ", "död"),
    ("Arkitekterna Jansson, Dalh och Bergqvist bygger ett hus tillsammans. Vad börjar arbetet med? ", "a"),
    ("Vad är ett Kiai? ", "ett japanskt stridsrop"),
    ("Vad är Dojo kun? ", "reglerna i dojon"),
    ("Vad betyder arigatou gozaimashita? ", "tack så mycket"),
    ("Vem har varit i rymden? \na. Neil Armstrong och 11 andra \nb. Neil Armstrong \nc. Neil Armstrong och Buzz Aldrin\n", "b" ),
    ("Vilka tanter är mest populära? ", "kontanter"),
    ("Om en kartong ägg går på 14 kronor, vad går då en kyckling på? ", "två ben"),
    ("Hur många ord kan en människa som kan skriva, skriva med en genomsnittlg pennan skriva? ", "50000"),
    ("Hur många gånger andas en genomsnittlig levande människa på ett år? ", "5000000"),
    ("Vilken stad ligger mest söder ut?\na. Rom\nb. New York\n", "b"),
    ("Hur många sekel är en biljon sekunder? ", "317")
]

for q in questions:
    answer = str(input(q[0]))
    if answer.lower() == q[1]:
        score = score + 1
        print("Mhm")
    else:
        print("Mhmm")

print("du hade", score * 100 / len(questions), "%", "rätt")