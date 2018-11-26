import numpy as np


def parse(obs, emit, chain):
    bias = []
    matrix = []
    with open(obs) as f:
        line = f.readline()
        line = line.replace("\n", "")
        input = line.split(" ")

        for i in input:
            i = i.strip()
        f.close()
    with open(emit) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            bias.append(line)
        f.close()
    with open(chain) as f:
        lines = f.readlines()
        for line in lines:
            matrixLine = []
            line = line.replace("\n", "")
            matrixLine = line.split(" ")

            for i in matrixLine:
                i = i.strip()
            matrix.append(matrixLine)

        print(input)
        print(matrix)
        print(bias)
        return input, np.array(matrix, dtype=float), np.array(bias, dtype=float)

obsv, matrix, bias = parse("obs-1.txt", "emit-1.txt", "chain-1.txt")
#obsv, matrix, bias = parse("obs-2.txt", "emit-2.txt", "chain-2.txt")
#obsv, matrix, bias = parse("testobs.txt","testemit.txt", "testchain.txt")

with open("output.txt", "w") as f:

    obsv = obsv[1:]
    x = bias[0]
    y = bias[1]
    if(obsv[0] == "1"):
        prev = np.argmax(bias)
    else:
        prev = np.argmin(bias)
    print(str(prev) + " " + str(obsv[0]))
    for i in obsv:
        if(i == "1"):
            prob = (max(matrix[prev]) * bias)
            print(str(np.argmax(prob)) + " " + str(i))
            f.write(str(np.argmax(prob)) + " ")
            prev = np.argmax(prob)
        else:
            prob = (max(matrix[prev]) * (100 - bias))
            print(str(np.argmax(prob)) + " " + str(i))
            f.write(str(np.argmax(prob)) + " ")
            prev = np.argmax(prob)
    f.close()


# for i in obsv:
#     if(i == "H"):
#         if(prev == "X"):
#             #probX = (matrix[0][0] * x) / x
#             #probY = (matrix[0][1] * y) / y
#             probX = (max(matrix[0]) * bias)
#             if(probX[0] > probX[1]):
#                 print("X " + "H")
#                 prev = "X"
#             else:
#                 print("Y " + "H")
#                 prev = "Y"

#         else:
#             # probX = (matrix[1][0] * x) / x
#             # probY = (matrix[1][1] * y) / y
#             probX = (max(matrix[1]) * (bias))
#             if(probX[0] > probX[1]):
#                 print("X " + "H")
#                 prev = "X"
#             else:
#                 print("Y " + "H")
#                 prev = "Y"


#     else:
#         if(prev == "X"):
#             #probX = (matrix[0][0] * (100-x)) / (100-x)
#             #probY = (matrix[0][1] * (100-y)) / (100-y)
#             probX = (max(matrix[0]) * (100-bias))
#             if(probX[0] > probX[1]):
#                 print("X " + "T")
#                 prev = "X"
#             else:
#                 print("Y " + "T")
#                 prev = "Y"

#         else:
#             # probX = (matrix[1][0] * (100-x)) / (100-x)
#             # probY = (matrix[1][1] * (100-y)) / (100-y)
#             probX = (max(matrix[1]) * (100-bias))
#             if(probX[0] > probX[1]):
#                 print("X " + "T")
#                 prev = "X"
#             else:
#                 print("Y " + "T")
#                 prev = "Y"

        

            



