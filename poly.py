class PhoneAlarm:
    def __init__(self, snooze_count = 0):
        self.snooze_count = snooze_count

    def wake_me_up(self):
        return "Scream at full volume"

class Roommate:
    def __init__(self, name):
        self.name = name


    def wake_me_up(self):
        return f"{self.name} Pours water"

class MotherCall:
    def wake_me_up(self):
        return "Calls at 4:30"
        
class Sunlight_thru_the_window:
    def wake_me_up(self):
        return "sunlight creeps in"
morning =[
    PhoneAlarm(5),
    Roommate('Alice'),
    MotherCall(),
    Sunlight_thru_the_window()
]

def start_the_day(wake_me_method):
    return wake_me_method.wake_me_up()
    
for tap_me in morning:
    print (start_the_day(tap_me))