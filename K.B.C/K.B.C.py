print("\n----------------------------------(Question Game)---------------------------------\n")

def procedure():
    levels = ["100,000",  "200,000", "300,000", "400,000", "500,000", "1,000,000"]
    money = 0
    for i in range(0, len(questions)):
        question = questions[i]
        print(f"\nQuestion {i+1} for Rs.{levels[i]} money is:\n\n")
        print(f"==> {question[0]}")
        print(f"\na. {question[1]}                        b. {question[2]}")
        print(f"c. {question[3]}                        d. {question[4]}")
        print("----------------------------------------------------------------------------------")
        reply = int(input("Enter you answer between (1-4): "))
        print("----------------------------------------------------------------------------------\n")

        if reply == question[-1]:
            print(f"Your answer is correct. You have won Rs.{levels[i]}")
            print("\n----------------------------------------------------------------------------------\n")
            money = levels[i]
            if 5 > i >= 1 :
                choice =  input("Do you want to play next question? (yes/no): ")
                print("\n----------------------------------------------------------------------------------\n")
                if choice.lower() == "yes":
                    continue
                else:
                    break
        else:
            print(f"You have lost this question. The correct answer is: {question[-1]}")
            print("\n----------------------------------------------------------------------------------\n")
            break
    return (f"You are going your home back with taking Rs.{money}\n-----------------------------------------\n\nThanks for participating in this game.\n\nThe coder of this quiz game is '❤️ ❤️ ❤️  HACKSTAR ❤️ ❤️ ❤️ ' ")

    
questions =[
    ["Who is the Owner of Google?", "Shahzaib Idrees", "Elon musk", "Sundar Pichai", "Ronaldo", 3],
    ["Who is the Owner of Facebook?", "Bilgates", "Mark zuckerberg", "Elon Musk", "Ronaldo",  2],
    ["Who is the Owner of Microsoft?", "Bill gates", "Elon musk", "Ein Stine", "Ronaldo", 1],
    ["Who Scores more runs in a match in a one day international match?", "Rohit Sharma", "Ricky Ponting", "Martin Guptill", "Fakhar Zaman", 1],
    ["Which team set a highest total in a one day international match?", "India", "South Africa", "England", "Australia", 3],
    ["How much the highest total from a team in a five day test match?", 695, 717, 793, 927, 4]
]

# correct_answers = ["Sundar Pichai", "Mark zuckerberg", "Bill Gates", "Rohit Sharma", "England", "927"]

print(procedure ())
print("\n----------------------------------------------------------------------------------\n")