point={"x":3,
"y":5,
"t":10}
point.get("x")
print(point.get("x"))

#by keys
for key in point.keys():
    print(key)
    for value in point.values():
        print(value)
        for item in point.items():
            print(item)
            item[0]
            