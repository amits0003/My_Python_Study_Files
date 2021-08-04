try:
    input_score = float(input("Enter a Score between 0.0 and 1.0: "))

    if input_score < 0.0 or input_score > 1.0:
        print("Given range is out of range, please provide range between 0.0 and 1.0")
        exit()
    else:
        if input_score < 0.6:
            print("F")
        elif 0.6 <= input_score < 0.7:
            print("D")
        elif 0.7 <= input_score < 0.8:
            print("C")
        elif 0.8 <= input_score < 0.9:
            print("B")
        else:
            print("A")
except NameError and ValueError as e:
    print(e)
