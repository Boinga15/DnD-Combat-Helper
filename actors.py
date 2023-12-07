class Character:
    def __init__(self, initiativeBonus, name):
        self.initBonus = initiativeBonus
        self.name = name

        self.turnlessNotes = []
        self.turnedNotes = []

        self.relationshipStatus = "Player Character"

        self.rolledInitiative = 0

class Player(Character):
    def __init__(self, initiativeBonus, name):
        super().__init__(initiativeBonus, name)

        self.isDead = False

class NonPC(Character):
    def __init__(self, initiativeBonus, name, health):
        super().__init__(initiativeBonus, name)

        self.maxHealth = health
        self.health = health
