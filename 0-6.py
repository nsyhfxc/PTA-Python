def acronym(phrase):
    result = ''
    for word in phrase.split():
        result += word[0].upper()
    return result

phrase = input()
print(acronym(phrase))