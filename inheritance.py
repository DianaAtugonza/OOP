class Familymember:
    def __init__(self, Skin_color,tribe):
        self.Skin_color= Skin_color
        self.tribe= tribe

    def describe(self):
        print(f"They are all {self.Skin_color} and belong to the {self.tribe} tribe.")

Family1= Familymember ("Caramel", "batooro")
Family1.describe()
class Child(Familymember):
    def __init__(self, skin_color, tribe, status):
        super().__init__(skin_color,tribe)
        self.status=status

    def describe (self):
          base_describe = super().describe()
          print  (f"Diana is {self.Skin_color} in color belongs to {self.tribe} and happily {self.status}.")
child1 = Child("Caramel", "Batooro", "married")
child1.describe()    
        

