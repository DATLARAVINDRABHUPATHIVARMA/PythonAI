def translate(phrase):
    translation = ""
    for a in phrase:
        if a.upper() in "AEIOU":
            if a.islower():
                translation = translation + "*"
            else:
                translation = translation + "/"
        else:
            translation = translation + a
    return translation

print(translate(input("Enter Phrase: ")))