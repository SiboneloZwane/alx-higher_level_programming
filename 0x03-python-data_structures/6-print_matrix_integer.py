def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    else:
        for n in range(len(matrix)):
            for l in range(len(matrix[n])):
                print("{:d}".format(matrix[n][l]), end="")
                if l != len(matrix[n]) - 1:
                    print(" ", end="")
            print("")
