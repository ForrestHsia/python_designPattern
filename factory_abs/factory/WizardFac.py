class Wizard:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(
            f"{self.name} the Wizard fight against {obstacle} and {obstacle.action()}!!"
        )


class Ork:

    def __str__(self):
        return "An Ork"

    def action(self):
        return "destroy it"


class WizardWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t+++++++++ Welcome to the Wizard World +++++++++"

    def make_charactor(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()
