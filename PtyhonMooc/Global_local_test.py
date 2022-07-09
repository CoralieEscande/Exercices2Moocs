# Premier programme
print("premier programme")
a = 2

def test():
    a = 3
    print("intérieur de test: ", a)

test()


# Deuxième programme
print("deuxième programme")
a = 2

def test():
    print("intérieur de test", a)

test()
print("après test", a)


# Troisième programme
print("troisième programme")
a = 2

def test():
    a = 3
    print("intérieur de test", a)

test()
print("Après test", a)


# Quatrième programme
print("quatrième programme")
a = 2

def test():
    global a
    a = 3
    print("intérieur de test", a)

test()
print("après test", a)
