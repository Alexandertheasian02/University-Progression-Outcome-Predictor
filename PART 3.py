# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.
# Any code taken from other sources is referenced within my code solution.
# Date: 08/12/2022
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
File = open("File.txt", "w")  # open a text file for writing text
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
            print('Integer Required.')
    return entry


while Answer == "y":
    A = inputs("Enter your total PASS credits:")  # Pass credits
    B = inputs("Enter your total DEFER credits:")  # Defer credits
    C = inputs("Enter your total FAIL credits:")  # Fail credits
    if 120 == A + B + C:
        if A == 120:
            print("Progress")
            Progress = Progress + 1
            Progress_list.append("Progress -" + str(A) + "," + str(B) + "," + str(C) + "\n")
        elif A == 100:
            print("Progress(module trailer)")
            Progress_Module_Trailer = Progress_Module_Trailer + 1
            Progress_Module_Trailer_list.append("Progress(module trailer) -" + str(A) + "," + str(B) + "," + str(C) + "\n")
        elif A <= 80 and C < 80:
            print("Module Retriever")
            Module_Retriever = Module_Retriever + 1
            Module_Retriever_list.append("Module Retriever -" + str(A) + "," + str(B) + "," + str(C) + "\n")
        else:
            print("Exclude")
            Exclude = Exclude + 1
            Exclude_list.append("Exclude -" + str(A) + "," + str(B) + "," + str(C) + "\n")
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

File.write("Your Report:\n")
File.writelines(
    Progress_list + Progress_Module_Trailer_list + Module_Retriever_list + Exclude_list)  # write those lists to a file
File.close()

with open("File.txt", "r") as File:  # read text from a file
    content = File.read()
print(content)
