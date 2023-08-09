def add_product(product, lst):
    global all_products
    if product not in all_products:
        all_products.append(product)
    if product not in lst:
        lst.append(product)
    return lst, all_products


def remove_product(product, lst):
    global all_products
    if product in all_products:
        all_products.remove(product)
    if product in lst:
        lst.remove(product)
    return lst, all_products
class Product:
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        global current_offer
        self._name = name
        self._price = price
        self._description = description
        self._ingredients = ingredients
        self._nutritional_values = nutritional_values
        self._current_offer = is_current_offer
        self._amount = amount

    def to_current_offer(self):
        if not self.current_offer:
            self.current_offer = True
            current_offer.append(self)

    def not_current_offer(self):
        if self.current_offer:
            self.current_offer = False
            current_offer.remove(self)

    def show(self):
        print(f"Name: {self._name} \nPrice: {self._price} \nDescription: {self._description} \nIngredients: {self._ingredients} \nNutritial values: {self._nutritional_values} \nCurrent offer: {self._current_offer}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str:
            self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if type(value) in (int, float):
            self._price = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if type(value) == str:
            self._description = value

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        if type(value) == str:
            self._ingredients = value

    @property
    def nutritional_values(self):
        return self._nutritional_values

    @nutritional_values.setter
    def nutritional_values(self, value):
        if type(value) == type(self):
            self._nutritional_values = value

    @property
    def is_current_offer(self):
        return self._description

    @is_current_offer.setter
    def is_current_offer(self, value):
        self._is_current_offer = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if type(value) == str:
            self._amount = value


class BeefBurgers(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description,  ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == BeefBurgers:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Chicken(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Chicken:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Veggie(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Veggie:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Salads(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Salads:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Attachments(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Attachments:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class SaucesAndDressings(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == SaucesAndDressings:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Desserts(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Desserts:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)


class Beverages(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, hot_or_cold, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        if type(hot_or_cold) == str and hot_or_cold == 'Охолоджений' or hot_or_cold == 'Гарячий' or hot_or_cold == 'Холодний':
            self._hot_or_cold = hot_or_cold
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list and type(self) == Beverages:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)

    def sort_drinks(self):
        cold_drinks = filter(lambda x: x._hot_or_cold in ('Охолоджений', 'Холодний'), self._product_list)
        hot_drinks = filter(lambda x: x._hot_or_cold == 'Гарячий', self._product_list)
        return cold_drinks, hot_drinks


class Breakfast(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, type_, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        if type(type_) in (Attachments, Desserts, str) and type_ in ('Бублики і бургери', 'Макмаффіни і тости'):
            self._type = type_
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)

    def sort_breakfast_meals(self):
        bagels_and_burgers = filter(lambda x: x._type == 'Бублики і бургери', self._product_list)
        eggs = filter(lambda x: 'Яйця' in x._ingredients or 'Яйце' in x._ingredients, self._product_list)
        McMuffins_and_toasts = filter(lambda x: x._type == 'Макмаффіни і тости', self._product_list)
        attachments = filter(lambda x: type(x._type) == Attachments, self._product_list)
        sweet = filter(lambda x: type(x._type) == Desserts, self._product_list)
        return bagels_and_burgers, eggs, McMuffins_and_toasts, attachments, sweet

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        if type(value) == str and value in ('Бублики і бургери', 'Яйця', 'Макмаффіни і тости', 'Вкладення', 'Вкладення'):
            self._type = value


class McCafe(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, kind, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        if kind in ('Поточна пропозиція', 'Пропозиція McCafe в McDonald\'s', 'Пропозиція в McCafe'):
            self._kind = kind
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if value in ('Поточна пропозиція', 'Пропозиція McCafe в McDonald\'s', 'Пропозиція в McCafe'):
            self._kind = value


class HappyMeal(Product):
    def __init__(self, name, price, description, ingredients, nutritional_values, is_current_offer=False, amount=1):
        super().__init__(name, price, description, ingredients, nutritional_values, is_current_offer, amount)
        self._product_list = []

    def add_product_(self):
        if self not in self._product_list:
            add_product(self, self._product_list)

    def remove_product_(self):
        if self in self._product_list:
            remove_product(self, self._product_list)