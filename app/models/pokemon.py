#!/usr/bin/python3

class Pokemon:

    index: int
    name: str
    typeOne: str
    typeTwo: str
    baseStatsTotal: int
    hp: int
    attack: int
    defense: int
    specialAttack: int
    specialDefense: int
    speed: int
    generation: int
    legendary: bool

    # index, name, typeOne, baseStatsTotal, hp, attack, defense, generation, legendary required
    def __init__(self, index, name, typeOne, typeTwo, baseStatsTotal, hp, attack, defense, specialAttack, specialDefense, speed, generation, legendary):
        self.index = index;
        self.name = name;
        self.typeOne = typeOne;
        self.baseStatsTotal = baseStatsTotal;
        self.hp = hp;
        self.attack = attack;
        self.defense = defense;
        self.generation = generation;
        self.legendary = legendary;

        if typeTwo:
            self.typeTwo = typeTwo;
        else:
            self.typeTwo = '';
        
        if specialAttack:
            self.specialAttack = specialAttack;
        else:
            self.specialAttack = '';

        if specialDefense:
            self.specialDefense = specialDefense;
        else:
            self.specialDefense = '';

        if speed:
            self.speed = speed;
        else:
            self.speed = '';

    def to_string(self):
        return """
Index: {0}\nName: {1}\nType One: {2}\nType Two: {3}\nBase Stats total: {4}\nHP: {5}\nAttack: {6}\nDefense: {7}\n
Generation: {8}\nLegendary: {9}
""".format(self.index, self.name, self.typeOne, self.typeTwo, self.baseStatsTotal,
            self.hp, self.attack, self.defense, self.generation, self.legendary)

    def to_csv(self):
        return ', '.join([str(x) for x in vars(self).values()])
    
    def compare_to(self, pokemon):
        return vars(self) == vars(pokemon)
