letters="a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = letters.split(" ")
dic = {}
print(alphabet) 
letter_to_number = {}
for position, number in enumerate(alphabet):
     print(f"{position} is the position of {letters}")
     num=0
     output=""
     letters=("a b c d e f g h i j k l m n o p q r s t u v w x y z").split(" ")
for index, letter in enumerate(letters):
    dic[letter]=index
print(dic)
