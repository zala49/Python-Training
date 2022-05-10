def python(n):
    H = 2*n - 2
    for i in range(0, n):
        for j in range(0, H):
            print(end=" ")
        H = H - 2
        for j in range(0, i + 1):
            print(" * ", end="")
        print("\r")


n = 5
python(5)
