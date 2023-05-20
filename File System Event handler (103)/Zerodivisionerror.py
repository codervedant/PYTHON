num_list= [5,0,2]

for elem in num_list:
    try:
        result=5/elem
        print("The result of 5/",elem,"is",result)
    except ZeroDivisionError:
        print("Oops! An Error")

