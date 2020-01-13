import random 
import time

empty = False

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
red = [1, 3, 5, 7, 8, 12, 14, 16, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15 ,17, 20, 22, 24, 26 ,28, 29 ,31, 33, 35]
green = [0]

def main():
    rules()

def rules():
    print('Välkommen till Oskars Kasino')
    print('Du kommer att få 1000$ att börja med')
    print('Ditt uppdrag är att få 10 000$, då har du vunnit')
    print('Du kan betta på svart, rött, jämna tal, ojämna tal, grönt och valfitt nummer')
    print('Om du bettar på grönt eller valfritt nummer så får du 20 gånger det du bettade')
    print('Annars så får du det dubbla')
    print('Lycka till')

money = [1000]
while money < 10000:
    print('You have $' %money)
    if money == 0:
        empty = True
        break
    bet_amount = int(input('Bet: '))
    while bet_amount > money:
        print('\nDu har inte råd\n')
        bet_amount = int(input('Bet: '))
    money -= bet_amount
    bet = input('Vad vill du betta på?\n ')
    if bet.lower() == 'nummer':
        print('\n') 
        final_bet = int(input('Vilket nummer vill du betta på?\n'))
        if 1 <= final_bet <= 36:
            print('Roletten börjar snurra...')
            time.sleep(3)
            k = random.randint(0, 37)
            print('Det landar på nummer ', k )
            if k == final_bet:
                print('Grattis du vann 20 ggr ditt bet')
                money += bet_amount * 20
            else:
                print('Your noob you lost')
        else:
            print('ditt nummer fungerar inte, testa igen.')
            money += bet_amount
    elif bet.lower == 'färg':
        print('\n')
        final_bet = input('vilken färg vill du betta på?\n')
        if final_bet.lower == 'svart' or final_bet.lower == 'röd' or final_bet.lower == 'grön':
            print('Roletten börjar snurra...')
            time.sleep(3)
            k = random.randint(0, 37)
            if k in red:
                print('Rouletten landar på röd')
                if final_bet.lower == 'röd':
                    print('Grattis du vann 2 ggr ditt bet')
                    money += bet_amount * 2
                else:
                    print('Your noob you lost')
            elif k in black:
                print('Rouletten landar på svart')
                if final_bet.lower == 'svart':
                    print('Grattis du vann 2 ggr ditt bet')
                    money += bet_amount * 2
                else:
                    print('Your noob you lost')
            elif k in green:
                print('Rouletten landar på grön')
                if final_bet.lower == 'grön':
                    print(('Grattis du vann 20 ggr dit bet')
                    money += bet_amount * 20
                    else:
                        print('Your noob you lost')
        else:
            print('Ditt bet är inte tillgängligt, testa igen')
            money += bet_amount
    else:
        print('du kan inte betta på det i det här casinot, testa igen')
        money += bet_amount
if empty == False:
    print('\n')
else:
    print('du har inga pengar kvar')


            










if __name__ == '__main__':
    main()
