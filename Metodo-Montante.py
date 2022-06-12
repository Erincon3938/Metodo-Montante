import os

def pp_matrix(m, n):

    print("M = ")

    for i in range(0, n):

        print("|", end=" ")
        
        for j in range (0, n + 1):

            print("%8d" % m[i][j], end=" ")

        print("|")

    print("")

def montante(m, n):
    piv = 1
    for k in range(0, n):

        for i in range(0, n):

            for j in range(0, n + 1):

                if j != k and i != k:

                    m[i][j] = (m[k][k] * m[i][j] - m[i][k] * m[k][j]) / piv

            if i != k:

                m[i][k] = 0

        piv = m[k][k]

        if (piv == 0):

            return 1 

        pp_matrix(m, n)

    return 0

def main():

    print("\n")
    n = int(input("Inserte el tamaño de la matriz (n): "))
    print("\n")
    m = []

    for i in range(0, n):

        print("Inserte la ecuación #" + str(i + 1) + ": ")
        r = []

        for j in range(0, n + 1):

            if (j <= n - 1):

                a = int(input("x" + str(j+1) + ": "))

            else:

                a = int(input("Termino independiente: "))

            r.append(a)
            
        m.append(r)
        print("")

    pp_matrix(m, n)

    if (montante(m, n) == 1):

        print("El sistema de ecuaciones no tiene solución.")
        return

    results = []

    for i in range(0, n):

        results.append(m[i][n] / m[i][i])

    print("\n|M| = " + str(m[n - 1][n - 1]))

    for i in range(0, n):
        print("\nx" + str(i + 1) + ": " + str(results[i]))

    print("\n")
    os.system("pause")

if __name__ == "__main__":
    main()
