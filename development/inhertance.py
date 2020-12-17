class Character :

    speed = 10
    points = 0
    sprite = None

    def __init__(self) :
        print("De constructor van Character")

    def Walk(self) :
        print("Character loopt nu", self.speed)


class Mario (Character) :

    lives = 3
    item = None

    def __init__(self) :
        # We vullen aan op de contructor van de Character:
        super().__init__()

        # De snelheid van Mario is standaard hoger:
        self.speed = 30
        

    # De "Walk" functionaliteit van Character ga ik OVERSCHRIJVEN
    def Walk(self) :
        print("Mario loopt heel anders! Maar wel met snelheid", self.speed)


    def Jump(self) :
        print("Mario springt!")


# Instanties maken:
characterA = Character()
marioX = Mario()

characterA.Walk()
marioX.Walk()
marioX.Jump()

print(characterA.speed)
print(marioX.speed)
print(marioX.lives)

# Het resultaat in de console geeft een geheugenadres weer. 
# Dit geheugenadres verwijst naar de locatie van het volledige object:
print(marioX)