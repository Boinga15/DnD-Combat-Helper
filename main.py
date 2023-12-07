from actors import *

import os
import copy
import random

activeCharacters = []

isDone = False
currentTurn = 0

cRound = 1

f = open("PCs.txt", "r")

for line in f.readlines():
    cLine = line.strip()

    name = cLine[0:cLine.index("|")]

    newLine = cLine[cLine.index("|")+1:]
    initBonus = int(newLine[0:newLine.index("|")])

    advantage = newLine[newLine.index("|")+1:]

    newCharacter = Player(initBonus, name)

    rolledNumber = random.choice(range(1, 21))

    if advantage == "a":
        secondRoll = random.choice(range(1, 21))
        if secondRoll > rolledNumber:
            rolledNumber = secondRoll

    elif advantage == "d":
        secondRoll = random.choice(range(1, 21))
        if secondRoll < rolledNumber:
            rolledNumber = secondRoll

    finalInitiative = rolledNumber + initBonus
    newCharacter.rolledInitiative = finalInitiative
    
    if len(activeCharacters) <= 0:
        activeCharacters.append(newCharacter)
    else:
        activeCharacters.append(newCharacter)
        while activeCharacters[activeCharacters.index(newCharacter)].rolledInitiative > activeCharacters[activeCharacters.index(newCharacter) - 1].rolledInitiative:
            temporary = copy.deepcopy(activeCharacters[activeCharacters.index(newCharacter) - 1])
            tempIndex = activeCharacters.index(newCharacter)
            
            activeCharacters[activeCharacters.index(newCharacter) - 1] = newCharacter
            activeCharacters[tempIndex] = temporary

            if activeCharacters.index(newCharacter) == currentTurn:
                currentTurn += 1

            if activeCharacters.index(newCharacter) <= 0:
                break

f.close()

while not isDone:
    os.system("cls")
    
    print("Round: " + str(cRound) + "\n")
    print("Initiative Order:")
    for character in activeCharacters:
        print(character.name + " (" + character.relationshipStatus + ")" + ((" [ " + str(character.health) + "/" + str(character.maxHealth) + " HP ]") if isinstance(character, NonPC) else "") + (" <---" if currentTurn == activeCharacters.index(character) else ""))

    print("\n1 - Add PC")
    print("2 - Add NPC")
    print("3 - Remove PC")
    print("4 - Remove NPC")
    print("5 - Edit PC")
    print("6 - Edit NPC")
    print("7 - Advance Order")
    print("8 - Reset Initiative")

    try:
        op = int(input("> "))
        os.system("cls")

        if not 1 <= op <= 8:
            print("\nError: Invalid input.")

        else:
            match op:
                case 1:
                    name = input("Enter PC name: ")
                    initBonus = int(input("Enter PC Initiative Bonus: "))
                    advantage = input("Enter 'a' for advantage on initiative bonus, and 'd' for disadvantage. Anything else for neutral: ")

                    newCharacter = Player(initBonus, name)

                    rolledNumber = random.choice(range(1, 21))

                    if advantage == "a":
                        secondRoll = random.choice(range(1, 21))
                        if secondRoll > rolledNumber:
                            rolledNumber = secondRoll

                    elif advantage == "d":
                        secondRoll = random.choice(range(1, 21))
                        if secondRoll < rolledNumber:
                            rolledNumber = secondRoll

                    finalInitiative = rolledNumber + initBonus
                    newCharacter.rolledInitiative = finalInitiative

                    print("\nRolled initiative: " + str(finalInitiative) + " (" + str(rolledNumber) + " + " + str(initBonus) + ")")

                    if len(activeCharacters) <= 0:
                        activeCharacters.append(newCharacter)
                        print("Position in initiative order: 1")
                    else:
                        activeCharacters.append(newCharacter)
                        while activeCharacters[activeCharacters.index(newCharacter)].rolledInitiative > activeCharacters[activeCharacters.index(newCharacter) - 1].rolledInitiative:
                            temporary = copy.deepcopy(activeCharacters[activeCharacters.index(newCharacter) - 1])
                            tempIndex = activeCharacters.index(newCharacter)
                            
                            activeCharacters[activeCharacters.index(newCharacter) - 1] = newCharacter
                            activeCharacters[tempIndex] = temporary

                            if activeCharacters.index(newCharacter) == currentTurn:
                                currentTurn += 1

                            if activeCharacters.index(newCharacter) <= 0:
                                break
                        print("Position in initiative order: " + str(activeCharacters.index(newCharacter) + 1))

                    input("Press enter to continue...")
                
                case 2:
                    name = input("Enter NPC name: ")
                    health = int(input("Enter the health of the NPC: "))
                    relationship = input("Enter relationship with the party: ")
                    initBonus = int(input("Enter NPC Initiative Bonus: "))
                    advantage = input("Enter 'a' for advantage on initiative bonus, and 'd' for disadvantage. Anything else for neutral: ")
                    number = int(input("Enter the number of enemies you want to add: "))

                    if number < 0:
                        break

                    for i in range(0, number):
                        newCharacter = NonPC(initBonus, name + (" #" + str(i + 1) if number > 1 else ""), health)
                        newCharacter.relationshipStatus = relationship

                        rolledNumber = random.choice(range(1, 21))

                        if advantage == "a":
                            secondRoll = random.choice(range(1, 21))
                            if secondRoll > rolledNumber:
                                rolledNumber = secondRoll

                        elif advantage == "d":
                            secondRoll = random.choice(range(1, 21))
                            if secondRoll < rolledNumber:
                                rolledNumber = secondRoll

                        finalInitiative = rolledNumber + initBonus
                        newCharacter.rolledInitiative = finalInitiative

                        print("\nRolled initiative: " + str(finalInitiative) + " (" + str(rolledNumber) + " + " + str(initBonus) + ")")

                        if len(activeCharacters) <= 0:
                            activeCharacters.append(newCharacter)
                            print("Position in initiative order: 1")
                        else:
                            activeCharacters.append(newCharacter)
                            while activeCharacters[activeCharacters.index(newCharacter)].rolledInitiative > activeCharacters[activeCharacters.index(newCharacter) - 1].rolledInitiative:
                                temporary = copy.deepcopy(activeCharacters[activeCharacters.index(newCharacter) - 1])
                                tempIndex = activeCharacters.index(newCharacter)
                                
                                activeCharacters[activeCharacters.index(newCharacter) - 1] = newCharacter
                                activeCharacters[tempIndex] = temporary

                                if activeCharacters.index(newCharacter) == currentTurn:
                                    currentTurn += 1

                                if activeCharacters.index(newCharacter) <= 0:
                                    break
                            
                            print("Position in initiative order: " + str(activeCharacters.index(newCharacter) + 1))

                        input("Press enter to continue...")
                    
                case 3:
                    availableCharacters = []
                    for character in activeCharacters:
                        if isinstance(character, Player):
                            availableCharacters.append(character)

                    if len(availableCharacters) > 0:
                        print("Available PCs:")
                        for character in availableCharacters:
                            print(str(availableCharacters.index(character) + 1) + ": " + character.name)

                        op = int(input("\n> "))

                        if 1 <= op <= len(availableCharacters):
                            if currentTurn > activeCharacters.index(availableCharacters[op - 1]):
                                currentTurn -= 1
                            
                            activeCharacters.remove(availableCharacters[op - 1])
                        else:
                            print("Error: Invalid input.")
                            input("\nPress enter to continue...")
                        
                    else:
                        print("There are no PCs in the Initiative List.")
                        input("\nPress enter to continue...")
                
                case 4:
                    availableCharacters = []
                    for character in activeCharacters:
                        if isinstance(character, NonPC):
                            availableCharacters.append(character)

                    if len(availableCharacters) > 0:
                        print("Available PCs:")
                        for character in availableCharacters:
                            print(str(availableCharacters.index(character) + 1) + ": " + character.name + " [ " + str(character.health) + "/" + str(character.maxHealth) + " ] {" + character.relationshipStatus + ")")

                        op = int(input("\n> "))

                        if 1 <= op <= len(availableCharacters):
                            if currentTurn > activeCharacters.index(availableCharacters[op - 1]):
                                currentTurn -= 1
                            
                            activeCharacters.remove(availableCharacters[op - 1])
                        else:
                            print("Error: Invalid input.")
                            input("\nPress enter to continue...")
                        
                    else:
                        print("There are no NPCs in the Initiative List.")
                        input("\nPress enter to continue...")
                
                case 5:
                    availableCharacters = []
                    for character in activeCharacters:
                        if isinstance(character, Player):
                            availableCharacters.append(character)

                    if len(availableCharacters) > 0:
                        print("Available PCs:")
                        for character in availableCharacters:
                            print(str(availableCharacters.index(character) + 1) + ": " + character.name)

                        op = int(input("\n> "))

                        if 1 <= op <= len(availableCharacters):

                            selectedCharacterID = activeCharacters.index(availableCharacters[op - 1])
                            selectedCharacter = availableCharacters[op - 1]

                            os.system("cls")

                            print(selectedCharacter.name + ":")
                            print("Rolled Initiative: " + str(selectedCharacter.rolledInitiative))
                            print("Is dead: " + ("Yes" if selectedCharacter.isDead else "No"))
                            print("\n============ Notes ============")
                            for note in selectedCharacter.turnlessNotes:
                                print(note + "\n")

                            print("\n============ Timed Notes ============")
                            for note in selectedCharacter.turnedNotes:
                                print(note[0] + " [Turns Left: " + str(note[1]) + "]\n")

                            print("\n1: Change is dead or not.")
                            print("2: Add a note.")
                            print("3: Remove a note.")
                            print("4: Add a timed note.")
                            print("5: Remove a timed note.")

                            op2 = int(input("\n> "))
                            os.system("cls")

                            if not 1 <= op2 <= 5:
                                print("Error: Invalid input.")
                                input("\nPress enter to continue...")
                            else:
                                match op2:
                                    case 1:
                                        print("Enter 'y' to set the character as dead. Anything else to not set them as dead.")
                                        choice = input("> ")

                                        print("\n")
                                        if choice == "y":
                                            print(selectedCharacter.name + " is dead.")
                                            activeCharacters[selectedCharacterID].isDead = True
                                        else:
                                            print(selectedCharacter.name + " is not dead.")
                                            activeCharacters[selectedCharacterID].isDead = False

                                        input("\nPress enter to continue...")
                                    
                                    case 2:
                                        note = input("Enter the note you want to add to this character:\n")

                                        activeCharacters[selectedCharacterID].turnlessNotes.append(note)
                                        print("\nNote addded successfully.")
                                        input("\nPress enter to continue...")
                                    
                                    case 3:
                                        if len(activeCharacters[selectedCharacterID].turnlessNotes) > 0:
                                            print("Select a note to delete:")
                                            for note in range(0, len(activeCharacters[selectedCharacterID].turnlessNotes)):
                                                print("(" + str(note + 1) + ") = " + activeCharacters[selectedCharacterID].turnlessNotes[note] + "\n")

                                            choice = int(input("\n> "))
                                            if 1 <= choice <= len(activeCharacters[selectedCharacterID].turnlessNotes):
                                                activeCharacters[selectedCharacterID].turnlessNotes.remove(activeCharacters[selectedCharacterID].turnlessNotes[choice - 1])
                                            else:
                                                print("Error: Invalid input.")
                                                input("\nPress enter to continue...")
                                            
                                        else:
                                            print("This character has no turnless notes.")
                                            input("\nPress enter to continue...")
                                    
                                    case 4:
                                        turns = int(input("Enter the number of turns this note should last: "))
                                        note = input("Enter the note you want to add to this character:\n")

                                        activeCharacters[selectedCharacterID].turnedNotes.append([note, turns])
                                        
                                        print("\nNote addded successfully.")
                                        input("\nPress enter to continue...")
                                    
                                    case 5:
                                        if len(activeCharacters[selectedCharacterID].turnedNotes) > 0:
                                            print("Select a note to delete:")
                                            for note in range(0, len(activeCharacters[selectedCharacterID].turnedNotes)):
                                                print("(" + str(note + 1) + ") = " + activeCharacters[selectedCharacterID].turnedNotes[note][0] + " [Turns Left: " + str(activeCharacters[selectedCharacterID].turnedNotes[note][1]) + "]\n")

                                            choice = int(input("\n> "))
                                            if 1 <= choice <= len(activeCharacters[selectedCharacterID].turnedNotes):
                                                activeCharacters[selectedCharacterID].turnedNotes.remove(activeCharacters[selectedCharacterID].turnedNotes[choice - 1])
                                            else:
                                                print("Error: Invalid input.")
                                                input("\nPress enter to continue...")
                                        else:
                                            print("This character has no turn-based notes.")
                                            input("\nPress enter to continue...")
                            
                        else:
                            print("Error: Invalid input.")
                            input("\nPress enter to continue...")
                        
                    else:
                        print("There are no PCs in the Initiative List.")
                        input("\nPress enter to continue...")
                
                case 6:
                    availableCharacters = []
                    for character in activeCharacters:
                        if isinstance(character, NonPC):
                            availableCharacters.append(character)

                    if len(availableCharacters) > 0:
                        print("Available NPCs:")
                        for character in availableCharacters:
                            print(str(availableCharacters.index(character) + 1) + ": " + character.name)

                        op = int(input("\n> "))

                        if 1 <= op <= len(availableCharacters):

                            selectedCharacterID = activeCharacters.index(availableCharacters[op - 1])
                            selectedCharacter = availableCharacters[op - 1]

                            os.system("cls")

                            print(selectedCharacter.name + ":")
                            print("Rolled Initiative: " + str(selectedCharacter.rolledInitiative))
                            print("Health: " + str(selectedCharacter.health) + "/" + str(selectedCharacter.maxHealth) + " HP.")
                            print("Relationship with party: " + str(selectedCharacter.relationshipStatus))
                            print("\n============ Notes ============")
                            for note in selectedCharacter.turnlessNotes:
                                print(note + "\n")

                            print("\n============ Timed Notes ============")
                            for note in selectedCharacter.turnedNotes:
                                print(note[0] + " [Turns Left: " + str(note[1]) + "]\n")

                            print("\n1: Increase or decrease health.")
                            print("2: Add a note.")
                            print("3: Remove a note.")
                            print("4: Add a timed note.")
                            print("5: Remove a timed note.")
                            print("6: Change relationship with party status.")

                            op2 = int(input("\n> "))
                            os.system("cls")

                            if not 1 <= op2 <= 6:
                                print("Error: Invalid input.")
                                input("\nPress enter to continue...")
                            else:
                                match op2:
                                    case 1:
                                        print("Choose how much health the NPC should lose. Positive numbers decrease their health, negative numbers heal them.")
                                        choice = int(input("> "))

                                        activeCharacters[selectedCharacterID].health = max(0, min(activeCharacters[selectedCharacterID].maxHealth, activeCharacters[selectedCharacterID].health - choice))
                                    
                                    case 2:
                                        note = input("Enter the note you want to add to this character:\n")

                                        activeCharacters[selectedCharacterID].turnlessNotes.append(note)
                                        print("\nNote addded successfully.")
                                        input("\nPress enter to continue...")
                                    
                                    case 3:
                                        if len(activeCharacters[selectedCharacterID].turnlessNotes) > 0:
                                            print("Select a note to delete:")
                                            for note in range(0, len(activeCharacters[selectedCharacterID].turnlessNotes)):
                                                print("(" + str(note + 1) + ") = " + activeCharacters[selectedCharacterID].turnlessNotes[note] + "\n")

                                            choice = int(input("\n> "))
                                            if 1 <= choice <= len(activeCharacters[selectedCharacterID].turnlessNotes):
                                                activeCharacters[selectedCharacterID].turnlessNotes.remove(activeCharacters[selectedCharacterID].turnlessNotes[choice - 1])
                                            else:
                                                print("Error: Invalid input.")
                                                input("\nPress enter to continue...")
                                            
                                        else:
                                            print("This character has no turnless notes.")
                                            input("\nPress enter to continue...")
                                    
                                    case 4:
                                        turns = int(input("Enter the number of turns this note should last: "))
                                        note = input("Enter the note you want to add to this character:\n")

                                        activeCharacters[selectedCharacterID].turnedNotes.append([note, turns])
                                        
                                        print("\nNote addded successfully.")
                                        input("\nPress enter to continue...")
                                    
                                    case 5:
                                        if len(activeCharacters[selectedCharacterID].turnedNotes) > 0:
                                            print("Select a note to delete:")
                                            for note in range(0, len(activeCharacters[selectedCharacterID].turnedNotes)):
                                                print("(" + str(note + 1) + ") = " + activeCharacters[selectedCharacterID].turnedNotes[note][0] + " [Turns Left: " + str(activeCharacters[selectedCharacterID].turnedNotes[note][1]) + "]\n")

                                            choice = int(input("\n> "))
                                            if 1 <= choice <= len(activeCharacters[selectedCharacterID].turnedNotes):
                                                activeCharacters[selectedCharacterID].turnedNotes.remove(activeCharacters[selectedCharacterID].turnedNotes[choice - 1])
                                            else:
                                                print("Error: Invalid input.")
                                                input("\nPress enter to continue...")
                                        else:
                                            print("This character has no turn-based notes.")
                                            input("\nPress enter to continue...")

                                    case 6:
                                        print("Choose this NPC's new relationship with the party.")
                                        choice = input("> ")

                                        activeCharacters[selectedCharacterID].relationshipStatus = choice

                case 7:
                    currentTurn += 1
                    pauseProgram = False

                    gotValidTarget = False
                    while not gotValidTarget:
                        gotValidTarget = True
                        
                        if currentTurn >= len(activeCharacters):
                            cRound += 1
                            currentTurn = 0

                            for character in activeCharacters:
                                for note in character.turnedNotes:
                                    note[1] -= 1

                                    if note[1] <= 0:
                                        pauseProgram = True
                                        print("Removed note from " + character.name + ":")
                                        print(note[0])
                                        print("")

                                        character.turnedNotes.remove(note)

                                        pauseProgram = True

                        elif isinstance(activeCharacters[currentTurn], Player):
                            if activeCharacters[currentTurn].isDead:
                                gotValidTarget = False
                                currentTurn += 1

                        elif isinstance(activeCharacters[currentTurn], NonPC):
                            if activeCharacters[currentTurn].health <= 0:
                                gotValidTarget = False
                                currentTurn += 1

                    if pauseProgram:
                        input("Press enter to continue...")

                case 8:
                    currentTurn = 0
                    cRound = 1
            
    except ValueError:
        os.system("cls")
        print("Error: Invalid input.\n")
