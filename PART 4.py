# I declare that my work contains no examples of misconduct, such as plagiarism or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953268 
# Date: 09/12/2022
student_dict = {}
Progress = 0
Progress_Module_Trailer = 0
Module_Retriever = 0
Exclude = 0
Outcomes = 0
Answer = "y"
print("Hello", '\n')


def inputs(marks):    # User Defined Function
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


while Answer == "y":
    while True:
        ID = input("Enter your student ID with a 'w':")
        if ID[0] == "w" and len(ID) == 8:
            while True:
                A = inputs("Enter your total PASS credits:")  # Pass credits
                B = inputs("Enter your total DEFER credits:")  # Defer credits
                C = inputs("Enter your total FAIL credits:")  # Fail credits
                if 120 == A + B + C:
                    if A == 120:
                        print("Progress")
                        Progress = Progress + 1
                        student_dict[ID] = "Progress -", A, B, C
                    elif A == 100:
                        print("Progress(module trailer)")
                        Progress_Module_Trailer = Progress_Module_Trailer + 1
                        student_dict[ID] = "Progress(module trailer) -", A, B, C
                    elif A <= 80 and C < 80:
                        print("Module Retriever")
                        Module_Retriever = Module_Retriever + 1
                        student_dict[ID] = "Module Retriever -", A, B, C
                    else:
                        print("Exclude")
                        Exclude = Exclude + 1
                        student_dict[ID] = "Exclude -", A, B, C

                    Outcomes = Outcomes + 1
                    print("Would you like to enter another set of data?")
                    while True:
                        Answer = input("Enter 'y' for yes or 'q' to quit and view results:")
                        if Answer == 'y' or Answer == 'q':
                            break
                        else:
                            print("Enter either 'y' or 'q'")
                    break
                else:
                    print("Total incorrect.")
            break
        else:
            print("Enter a student ID starting with a 'w' and consists of 8 characters.")

print("------------------------------------------------------------------")
print("Histogram")  # horizontal histogram with asterisks
print("Progress", Progress, " " ":", end=" ")
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

for (ID, value) in student_dict.items():
    print(ID, ":", value[0], value[1], ",", value[2], ",", value[3])
