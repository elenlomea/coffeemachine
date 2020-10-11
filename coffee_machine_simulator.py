class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def action(self):
        self.act = input('Write action (buy, fill, take, remaining, exit):')

    def remaining(self):
        if self.act == 'remaining':
            print(f'The coffee machine has:')
            print(f'{self.water} of water')
            print(f'{self.milk} of milk')
            print(f'{self.beans} of coffee beans')
            print(f'{self.cups} of disposable cups')
            print(f'$ {self.money} of money')

    def take(self):
        if self.act == 'take':
            print(f'I gave you $ {self.money}')
            self.money = 0

    def fill(self):
        if self.act == 'fill':
            self.water_add = int(input('Write how many ml of water do you want to add:'))
            self.milk_add = int(input('Write how many ml of milk do you want to add:'))
            self.beans_add = int(input('Write how many grams of coffee beans do you want to add:'))
            self.cups_add = int(input('Write how many disposable cups of coffee do you want to add:'))
            self.water += self.water_add
            self.milk += self.milk_add
            self.beans += self.beans_add
            self.cups += self.cups_add

    def buy(self):
        if self.act == 'buy':
            self.need = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            if self.need == '1':
                if self.water >= 250:
                    if self.beans >= 16:
                        print('I have enough resources, making you a coffee!')
                        self.water -= 250
                        self.beans -= 16
                        self.cups -= 1
                        self.money += 4
                elif self.water < 250 or self.beans < 16:
                    print("Sorry, there aren't enough resources!")
            elif self.need == '2':
                if self.water >= 350:
                    if self.milk >= 75:
                        if self.beans >= 20:
                            print('I have enough resources, making you a coffee!')
                            self.water -= 350
                            self.milk -= 75
                            self.beans -= 20
                            self.cups -= 1
                            self.money += 7
                elif self.water < 350 or self.milk < 75 or self.beans < 20:
                    print("Sorry, there aren't enough resources!")
            elif self.need == '3':
                if self.water >= 200:
                    if self.milk >= 100:
                        if self.beans >= 12:
                            print('I have enough resources, making you a coffee!')
                            self.water -= 200
                            self.milk -= 100
                            self.beans -= 12
                            self.cups -= 1
                            self.money += 6
                elif self.water < 200 or self.milk < 100 or self.beans < 12:
                    print("Sorry, there aren't enough resources!")
            elif self.need == 'back':
                return self.act

    def run(self):
        if self.act == 'buy':
            return self.buy()
        elif self.act == 'take':
            return self.take()
        elif self.act == 'fill':
            return self.fill()
        elif self.act == 'remaining':
            return self.remaining()


machine = CoffeeMachine()

while True:
    machine.action()
    machine.run()
    if machine.act == 'exit':
        break
