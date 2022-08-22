import uuid
from datetime import datetime


class Vehicle():
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.ID = uuid.uuid4()
        self.last_pass_date = None


class Otomobil(Vehicle):
    pass


class Minibus(Vehicle):
    pass


class Otobus(Vehicle):
    pass


class tollBooth():
    def __init__(self):
        self.otomobilFee = 100
        self.minibusFee = 200
        self.otobusFee = 300
        self.daily_vehicle = {}

    def getPayment(self, vehicle):
        now = datetime.now()
        today = now.strftime("%d-%m-%Y")

        if today not in self.daily_vehicle:
            self.daily_vehicle[today] = [vehicle]
        else:
            self.daily_vehicle[today].append(vehicle)

        vehicle.last_pass_date = now
        if isinstance(vehicle, Otomobil):
            vehicle.balance -= self.otomobilFee
        elif isinstance(vehicle, Minibus):
            vehicle.balance -= self.minibusFee
        elif isinstance(vehicle, Otobus):
            vehicle.balance -= self.otobusFee
        else:
            return 0


class Report():
    def __init__(self, toolBooth):
        self.toolBooth = toolBooth
        self.daily_vehicle = toolBooth.daily_vehicle

    def todayReport(self):
        now = datetime.now()
        today = now.strftime("%d-%m-%Y")
        self.dailyReport(today)

    def dailyReport(self, today):
        dailyCost = 0
        for vehicle in self.daily_vehicle[today]:
            if isinstance(vehicle, Otomobil):
                dailyCost += self.toolBooth.otomobilFee
            elif isinstance(vehicle, Minibus):
                dailyCost += self.toolBooth.minibusFee
            elif isinstance(vehicle, Otobus):
                dailyCost += self.toolBooth.otobusFee
        print(today, 'gunu kazanc:', dailyCost)


gise1 = tollBooth()


arac1 = Otomobil("Ahmet", "Kaya", 1000)
arac2 = Otomobil("Mehmet", "Kaya", 1000)
arac3 = Minibus("Ali", "Kaya", 1000)
arac4 = Minibus("Veli", "Kaya", 1000)
arac5 = Otobus("Ayse", "Kaya", 1000)

gise1.getPayment(arac1)
gise1.getPayment(arac2)
gise1.getPayment(arac3)
gise1.getPayment(arac4)
gise1.getPayment(arac5)
gise1.getPayment(arac5)

Report(gise1).todayReport()
