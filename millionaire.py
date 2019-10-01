sorry = "I'm sorry, that is incorrect"
player_name = input("Welcome to Millionaire! What is your name? ")
money_made = 0
print("Currently, you have made " + "$" + str(money_made))
answer_question1 = input("what's is the capital of Ghana\na.Dakar\nb.Tunis\nc.Abuja \nd.Accra\n>>").upper()
if answer_question1 == "D":
    print("Correct")
    money_made += 500
    print("Currently you have made " + "$" + str(money_made))
    answer_question2 = input("What's the biggest country in Africa\na.Nigeria\nb.Algeria\nc.DRC\nd.Mali\n>>").upper()
    if answer_question2 == "B":
        print("Correct")
        money_made += 500
        print("Currently you have made " + "$" + str(money_made))
        answer_question3 = input(
            "Who is the president of Rwanda\na.Nana Addo\nb.Buhari\nc. Ramphosa\nd.Paul kagame\n>>").upper()
        if answer_question3 == "D":
            print("Correct")
            money_made += 4000
            print("Currently you have made " + "$" + str(money_made))
            answer_question4 = input(
                "In what year did Senegal gain independence\na.1996\nb.1965\nc.1960\nd.1963\n>>").upper()
            if answer_question4 == "C":
                print("Correct")
                money_made += 15000
                print("Currently you have made " + "$" + str(money_made))
                answer_question5 = input(
                    "In what Country are the krobos predominently found\na.Gambia\nb.Ghana\nc.Zimbabwe\nd.Guinea\n>>").upper()
                if answer_question5 == "B":
                    print("Correct")
                    money_made += 30000
                    print("Currently you have made " + "$" + str(money_made))
                    answer_question6 = input(
                        "Who is the first president of Nigeria\na.Kwame Nkrumah\nb.Nnamdi azikiwi\nc.Thomas Sankara\nd.Julius Maleama\n>>").upper()
                    if answer_question6 == "B":
                        print("Correct")
                        money_made += 200000
                        print("Currently you have made " + "$" + str(money_made))
                        answer_question7 = input(
                            "In what year was the OAU formed\na.1956\nb.1965\nc.1960\nd.1963\n>>").upper()
                        if answer_question7 == "B":
                            print("Correct")
                            money_made += 250000
                            print("Currently you have made " + "$" + str(money_made))
                            answer_question8 = input(
                                "who is the first king of the Ashanti Kingdom\na.Osei Yaw\nb.Osei Tutu\nc.Prempeh Agyeman\nd.opoku Ware\n>>").upper()
                            if answer_question8 == "B":
                                print("Correct")
                                money_made += 500000
                                print("You are a millionaire")
                            else:
                                print(sorry)
                                print(money_made)
                        else:
                            print(sorry)
                    else:
                        print(sorry)
                else:
                    print(sorry)
            else:
                print(sorry)
        else:
            print(sorry)
    else:
        print(sorry)
else:
    print(sorry)

