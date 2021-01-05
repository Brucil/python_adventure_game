class Enemy:
    """ The base class for all enemies in the game. """

    def __init__(self, name, description, hp, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(
            self.name, self.description, self.hp, self.damage
        )

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(
            name="Giant Spider",
            description="A large hairy spider the size of a small dog.",
            hp=10,
            damage=2,
        )


class Ogre(Enemy):
    def __init__(self):
        super().__init__(
            name="Ogre",
            description="A large hideous man-like creature.",
            hp=30,
            damage=15,
        )

