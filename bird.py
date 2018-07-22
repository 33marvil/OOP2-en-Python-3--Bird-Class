"""code goes here"""
"""Bird class"""

class Bird:
    # #variable de class

    def __init__(self, name):
        # Variable de instancia
        self.name = name
        self.mts = 0

    # Method comportamiento
    def jump(self):
        return "Saltando..."

    # Method comportamiento
    def flying(self, mts=0):
        self.mts = self.mts + mts # Contador
        return 'Volando ' + str(self.mts) + ' mts...'


    # Metodo de class
    @classmethod
    def who_am_i(cls):
        return "Soy un pájaro"



# bird_3 = Bird("Zulu")
#
# print(bird_3.jump())
# #>> "Saltando..."
#
# print(bird_3.fly(20))
# #>> "Volando 20 mts..."
#
# print(bird_3.fly(10))
# #>> "Volando 30 mts..."
#
# print(Bird.who_am_i())
# #>> "Soy un pájaro"
