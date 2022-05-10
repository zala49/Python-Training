def python(n):
    a = []
    for i in range(1, n+1):
        a.append("*"*i)
    print("\n".join(a))


n = 5
python(5)
