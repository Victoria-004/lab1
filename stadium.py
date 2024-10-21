class Stadium:
    __viewership = None
    __name = None
    __lightning = None

    def __init__(self, viewership, name, lightning):
        """
        Задання значень полів
        """
        self.__viewership = viewership
        self.__name = name
        self.__lightning = lightning

    def __str__(self):
        return f"Stadium(viewership:{self.viewership}, name:{self.name}, lightning:{self.lightning})"

    def __repr__(self):
        return f"Stadium('{self.viewership}', '{self.name}', '{self.lightning}')"

    def set_data(self, viewership, name, lightning):
        """
        Встановлення значень
        """
        self.name = name
        self.lightning = lightning
        self.viewership = viewership

    def get_data(self):
        """
        Виведення значень
        """
        print("viewership:", self.__viewership, "name:", self.__name, "lightning:", self.__lightning)

    def __del__(self):
        """
        Деструктор класу
        """
        print('Object is deleted')


def main():
        stad1 = Stadium(39415, 'Arena Lviv', '2400 lux')
        stad2 = Stadium(40000, 'Metalist', '2400 lux')
        stad3 = Stadium(21000, 'Karpaty', '2400 lux')


        stad1.get_data()
        stad2.get_data()
        stad3.get_data()

if __name__ == "__main__":
    main()

