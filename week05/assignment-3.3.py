score = input("Enter Score: ")
fscore = float(score)

if fscore > 1.0 :
    print("Error: Number needs to be betwen 0.0 and 1.0")
    quit()
elif fscore < 0.0 :
    print("Error: Number needs to be betwen 0.0 and 1.0")
    quit()
elif fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
else :
    print("F")