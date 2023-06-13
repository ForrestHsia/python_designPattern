import builder, time


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print("prepare the {} dough of the {} pizza".format(
            self.dough.name, self))
        time.sleep(builder.STEP_DELAY)
        print("done with the {} dough".format(self.dough.name))