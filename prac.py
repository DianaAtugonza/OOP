class Bodaboda:
    def __init__(self, stagename, district):
        self.stagename= stagename
        self.district= district

    def introduce(self):
        print(f"{self.stagename} in { self.district}district")
bodaboda1 = Bodaboda("Bishop tucker stage", "Mukono")

class Rider(Bodaboda):
    def __init__(self, stagename, district, Rider_name):
        super().__init__( stagename, district)
        self.Rider_name = Rider_name
    def introduce(self):
        base_introduce = super().introduce()
        print(f"Nze Mwami {self.Rider_name} mbeera ku {self.stagename} mu {self.district} district.")
rider=Rider("Bishop Tucker Stage", "Mukono", "Muwonge")
rider.introduce()