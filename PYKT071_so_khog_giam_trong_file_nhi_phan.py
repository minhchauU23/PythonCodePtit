import pickle
import io
fileOut = open("DATA2.out", "ab")

a = ["1", "2", "3"]


pickle.dump(a, fileOut)
fileOut.close()

fileIn = open("DATA2.out", "rb")
a2 = pickle.load(fileIn)
print(a2)


