class Firearm:
    def __init__(self, rounds, rate, length, mass):
        self.rounds, self.rate, self.length, self.mass = rounds, rate, length, mass

    def specifications(self):
        """Вывод характеристик оружия"""
        print(f'\nХарактеристики оружия:')
        print(f'\nВместимость магазина: {self.rounds} патронов')
        print(f'Скорострельность: {self.rate} выстрелов/минута')
        print(f'Дальнобойность: {self.length} метров ')
        print(f'Масса оружия: {self.mass} кг')

    def time_to_empty(self):
        """Функция расчёта времени, необходимого для опустошения магазина"""
        self.emptytime = round(self.rounds / self.rate, 2)
        return f'Время для опустошения магазина: {self.emptytime}'

    def rate_to_length(self):
        """Функция расчёта соотношения скорострельности к дальности стрельбы"""
        self.rtl = round(self.rate / self.length, 2)
        return f'Соотношение скорострельности к дальности стрельбы: {self.rtl}'

    # Перегрузка оператора
    def __add__(self, other):
       print(f'\nОбщее число патронов в двух магазинах: {self.rounds + other.rounds}',
             f'\nОбщая масса: {self.mass+other.mass}')



class AssaultRifle(Firearm):
    def __init__(self, rounds, rate, length, mass, colour):
        super().__init__(rounds, rate, length, mass)
        self.skin = colour

    def new_skin(self, colour):
        """Функция смены скина"""
        self.skin = colour
        print(f'\nУстановлен новый скин: {self.skin}')

    def info(self):
        self.specifications()
        print(f'Текущий окрас: {self.skin}')


class Rifle(Firearm):
    def __init__(self, rounds, rate, length, mass, magnification):
        super().__init__(rounds, rate, length, mass)
        self.magn = magnification

    def change_mag(self, mag):
        """Функция смены магазина"""
        self.rounds = mag
        print(f'\nУстановлен новый магазин: {self.rounds} патронов')

    def change_aim(self, nmagn):
        """Функция смены прицела"""
        self.magn = nmagn
        print(f'\nКратность нового прицела: {self.magn}')

    def info(self):
        super().specifications()
        print(f'Кратность прицела: {self.magn}')


ak74 = AssaultRifle(30, 600, 300, 3.6, 'Moonrise')
ak74.info()
ak74.new_skin('Momentum')
ak74.info()
print()
SVD = Rifle(10, 830, 1200, 4.85, 5)
SVD.info()
SVD.change_aim(2.5)
SVD.change_mag(20)
SVD.info()
SVD + ak74