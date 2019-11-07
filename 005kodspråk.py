def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "qwrtupsdfghjklzxcvbnmQWRTUPSDFGHJKLZXCVBNM":
            translation = translation + letter + "?" + letter
        if letter in "aouåeiyäö":
            translation = translation + letter + "!" + letter
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))