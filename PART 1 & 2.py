# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953268  
# Date: 06/12/2022
Progress_list = []  # lists
Progress_Module_Trailer_list = []
Module_Retriever_list = []
Exclude_list = []
Progress = 0  # variables
Progress_Module_Trailer = 0
Module_Retriever = 0
Exclude = 0
Outcomes = 0
Answer = "y"


def inputs(marks):  # User Defined Function
    while True:
        try:
            entry = int(input(marks))
            if entry % 20 == 0 and 0 <= entry <= 120:
                break
            else:
                print("out of range.")
        except ValueError:
            print('Integer Required')
    return entry


print("Hello!,\n")
while True:
    try:
        print('Press "1" if you are a Student.\n'
              'Press "2" if you are a Staff Member(Multiple progress outcome with histogram + lists).')
        decision = int(input('Decision : '))
        if decision == 1:
            while True:
                A = inputs("Please enter your credits at pass:")  # Pass credits
                B = inputs("Please enter your credit at defer:")  # Defer credits
                C = inputs("Please enter your credit at fail:")  # Fail credits
                if 120 == A + B + C:
                    if A == 120:
                        print("Progress")
                    elif A == 100:
                        print("Progress(module trailer)")
                    elif A <= 80 and C < 80:
                        print("Module Retriever")
                    else:
                        print("Exclude")
                    print("Program exits....")
                    break
                else:
                    print("total incorrect.")
            break
        elif decision == 2:
            while Answer == "y":
                A = inputs("Enter your total PASS credits:")  # Pass credits
                B = inputs("Enter your total DEFER credits:")  # Defer credits
                C = inputs("Enter your total FAIL credits:")  # Fail credits
                if 120 == A + B + C:
                    if A == 120:
                        print("Progress")
                        Progress = Progress + 1
                        Progress_list.append([A, B, C])
                    elif A == 100:
                        print("Progress(module trailer)")
                        Progress_Module_Trailer = Progress_Module_Trailer + 1
                        Progress_Module_Trailer_list.append([A, B, C])
                    elif A <= 80 and C < 80:
                        print("Module Retriever")
                        Module_Retriever = Module_Retriever + 1
                        Module_Retriever_list.append([A, B, C])
                    else:
                        print("Exclude")
                        Exclude = Exclude + 1
                        Exclude_list.append([A, B, C])
                    Outcomes = Outcomes + 1
                    print("Would you like to enter another set of data?")
                    while True:
                        Answer = input("Enter 'y' for yes or 'q' to quit and view results:")
                        if Answer == 'y' or Answer == 'q':
                            break
                        else:
                            print("Enter either 'y' or 'q'")
                else:
                    print("total incorrect.")
            print("------------------------------------------------------------------")
            print("Histogram")  # horizontal histogram with asterisks
            print("Progress", Progress, " "":", end=" ")
            print(Progress * "*")
            print("Trailer", Progress_Module_Trailer, " ", ':', end=" ")
            print(Progress_Module_Trailer * "*")
            print("Retriever", Module_Retriever, ':', end=" ")
            print(Module_Retriever * "*")
            print("Excluded", Exclude, " "":", end=' ')
            print(Exclude * "*")
            print("\n")
            print(Outcomes, "outcomes in total.")  # total of outcomes
            print("------------------------------------------------------------------")

            for i in Progress_list:
                print("Progress -", i[0], ",", i[1], ",", i[2])
            for i in Progress_Module_Trailer_list:
                print("Progress(module trailer) -", i[0], ",", i[1], ",", i[2])
            for i in Module_Retriever_list:
                print("Module Retriever -", i[0], ",", i[1], ",", i[2])
            for i in Exclude_list:
                print("Exclude -", i[0], ",", i[1], ",", i[2])
            break
        else:
            print("Enter a valid DECISION!")
    except ValueError:
        print("Enter an integer!")
