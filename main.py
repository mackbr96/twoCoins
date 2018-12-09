import numpy as np
import sys

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

def findProbSeq(obsv, matrix, bias):
    print("\n\n")
    totalprob = 0.4

    obsv = obsv[1:]
    x = bias[0]
    y = bias[1]
    if(obsv[0] == "1"):
        prev = np.argmax(bias)
    else:
        prev = np.argmin(bias)
    for i in obsv:
        if(i == "1"):
            prob = (max(matrix[prev]) * bias)
            totalprob = totalprob * (bias[np.argmax(prob)])
            prev = np.argmax(prob)
        else:
            prob = (max(matrix[prev]) * (100 - bias))
            totalprob = totalprob * (1 - bias[np.argmax(prob)])
            prev = np.argmax(prob)
    print(totalprob)
    


if(len(sys.argv) == 4):
    obsv, matrix, bias = parse(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    obsv, matrix, bias = parse("testobs.txt","testemit.txt", "testchain.txt")

with open("output.txt", "w") as f:

    obsv = obsv[1:]
    x = bias[0]
    y = bias[1]
    if(obsv[0] == "1"):
        prev = np.argmax(bias)
    else:
        prev = np.argmin(bias)
    print(str(prev) + " " + str(obsv[0]))
    f.write(str(prev) + " ")
    for i in obsv:
        if(i == "1"):
            prob = (max(matrix[prev]) * bias)
            print(str(np.argmax(prob)) + " " + str(i))
            f.write(str(np.argmax(prob)) + " ")
            prev = np.argmax(prob)
        else:
            prob = (max(matrix[prev]) * (1 - bias))
            print(str(np.argmax(prob)) + " " + str(i))
            f.write(str(np.argmax(prob)) + " ")
            prev = np.argmax(prob)
    f.close()

#findProbSeq("111", matrix, bias)