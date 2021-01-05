# *********Base Class for Items **********
class Item:
    """The base class for all items in the game."""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(
            self.name, self.description, self.value
        )


# ********** Money ****************
class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(
            name="Gold",
            description="A round coin with {} stamped on the front.".formate(
                str(self.amount)
            ),
            value=self.amount,
        )


class Silver(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(
            name="Silver",
            ddescription="A round coin with {} stamped on the front.".formate(
                str(self.amount)
            ),
            value=self.amount,
        )


class Copper(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(
            name="Copper",
            description="A round coin with {} stamped on the front.".formate(
                str(self.amount)
            ),
            value=self.amount,
        )


# ******** Weapons*****************
class Weapon(Item):
    """The base class for all weapons in the game."""

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(
            self.name, self.description, self.value, self.damage
        )


class Rock(Weapon):
    def __init__(self):
        super().__init__(
            name="Rock",
            description="A fist-sized rock, suitable for bludgeoning.",
            value=0,
            damage=5,
        )


class Dagger(Weapon):
    def __init__(self):
        super().__init__(
            name="Dagger",
            description="A small dagger with some rust. Somewhat more dangerous than a rock.",
            value=10,
            damage=10,
        )


class Rusty_sword(Weapon):
    def __init__(self):
        super().__init__(
            name="Rusty_sword",
            description="A sword with some rust. Somewhat more dangerous than a Dagger.",
            value=20,
            damage=15,
        )

