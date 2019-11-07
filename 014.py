import time

teme.sleep(1)

print('Välommen.. ')

welcome = input('Har du ett konto? j/n')
if welcome == 'n':
    username = input('Användarnamn: ')
    password = input('Lösenord: ')
    Password2 = input('Konfirmera lösenord: ')
if password != password2:
    print('Lösenorden matchar inte')
    username = input('Användarnamn: ')
    password = input('Lösenord: ')
    Password2 = input('Konfirmera lösenord: ')
text_file = open(username + '.txt', 'r')
f = file = open(login1 + '.txt', 'r')
if(file.readline()) == (login1 + ':' + login2):
    print('Välkommen!!')

if welcome == 'j':
    login1 = input('Logga in: ')
    login2 = input('Lösenord: ')
f = file = open(login1 + '')