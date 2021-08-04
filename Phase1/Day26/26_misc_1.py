
while True:
    try:
        x = int(input("Enter the number : "))
        if int(x):
            print('input value ', x)
        break
    except ValueError as e:
        raise e
        #print(e)
    finally:
        print("Mandatory Executed Line")


