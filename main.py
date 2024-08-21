
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You have come at crossroads, which way do you want to go?left or right").lower()

if choice1 == "left":
    choice2 = input(
        "You face a monster.You can either use a sword or a axe to challenge it. What do you choose?\n").lower()
    if choice2 == "sword":
        print("You are dead as your sword broke in battle.")
    else:
        choice3 = input(
            "You defeated the monster in battle. However due to the wounds attained in battle you need to rest for a "
            "while. You can either rest in a cave or in a tree. Where do you want to rest?\n").lower()
        if choice3 == "cave":
            choice4 = input("You have survived the night and now need to resume your journey to find the treasure. "
                            "would you like to cross the forest or the mountains?\n").lower()
            if choice4 == "forest":
                choice5 = input("you get discovered by a tribe which is not trying to hunt you down. You have two "
                                "choices hide or hunt. what do you do?\n").lower()
                if choice5 == "hide":
                    choice6 = input("You manage to ditch the tribe and escape the forest. "
                                    "You are on the correct path to finding the treasure and you discover a village. "
                                    "There are shops in this village that sell multiple items such as Weapons, "
                                    "enchantments, and Armor. You have money to purchase only one item from a "
                                    "shop.Type the shop name to enter the shop\n").lower()
                    if choice6 == "weapons":
                        choice6_1 = input("Welcome to the Weapons shop we have "
                                          "a sphere, katana, sai, bow and arrow with the limit of 15 arrows, "
                                          "and war-hammer. What would you like to purchase")
                        if (choice6_1 == "sphere" or choice6_1 == "katana" or choice6_1 == "sai" or
                                choice6_1 == "bow and arrow with the limit of 15 arrows" or choice6_1 == "war-hammer"):
                            choice7 = input(
                                "Thankyou for your purchase. You are now heading out of the village and closer to the "
                                "treasure.You find a troll blocking your path. what do you do?Fight or Run")
                            if choice7 == "fight":
                                import random
                                fight_outcome = random.choice(["win", "lose"])
                                if fight_outcome == "win":
                                    print("You defeated the troll!")
                                else:
                                    print("You lost the fight and were defeated by the troll.")
                            elif choice7 == "run":
                                print("You run away from the troll, but you lose the treasure.")
                            else:
                                print("Invalid choice. Please choose 'Fight' or 'Run'.")
                    elif choice6 == "enchantment" or choice6 == "enchantments":
                        choice6_2 = input("Welcome to the potion house what can we get you healing tablets, "
                                          "fight enhancing tablets, or speed increasing tablets")
                        if (choice6_2 == "healing tablets" or choice6_2 == "fight enhancing tablets" or
                                choice6_2 == "speed increasing tablets"):
                            print("You die as there was a explosion in one of the furnaces which causes "
                                  "you to get fatally wounded at which point event he healers could not revive you.")
                    elif choice6 == "armor":
                        print("You die as the armor was too heavy for you to carry.")
                    else:
                        print("Invalid shop name.")
        else:
            print("You did not survive the night as you died to a gorilla attack")

else:
    choice_left = input("You encounter a river. do you wish to cross it or go around it?")
    if choice_left == "cross":
                        print("There were crocodiles waiting for to surprise you and therefore you died in surprise")
    else:
        choice_left_1 = input("you meet a trader who is selling a war-hammer, bow and arrow, healing spell "
                                              "and a shield. what do you want to buy? Type the item you want to buy")
        if choice_left_1 == "war-hammer" or choice_left_1 == "healing spell" or choice_left_1 == "shield":
            choice_left_2 = input("Item has been added to your inventory. you are now headed to the "
                                                        "treasure where you encounter a dragon. what do you do? Fight or"
                                                        " Run")
            if choice_left_2 == "fight" and choice_left_1 == "bow and arrow":
                choice_left_3 = input("You defeated the dragon but your mom is behind you and "
                                                                  "you need to close the game :(")


