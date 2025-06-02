def meow(m):
    return m, len(m);

cityINP = input().strip();
city = cityINP.split();
d = {gorod: meow(gorod)[1] for gorod in city};

for city in sorted(d, key=d.get):
    print(f"{city}: {d[city]}")