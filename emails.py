def email_to_numbers(email):
    alphabet= list("abcdefghijklmnopqrstuvwxyz")
    numbers = []
    for letter in email.lower():
        if letter in alphabet:
            position= alphabet.index(letter) + 1
            numbers.append(position)
        elif letter.isdigit():
            numbers.append(int(letter))
        else:
            numbers.append(0)
    return numbers
result = email_to_numbers("benyi@gmail.com")
print(result)