class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.level_hp = 10
        self.attack = 5
        self.add_attack = 5
        print(self.name, 'was born, level', self.level, ', hp', self.hp, ', attack', self.attack )

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        print('hp setter:', hp)
        self._hp = hp

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        print('level setter:', level)
        self._level = level

    @property
    def level_hp(self):
        return self._level_hp

    @level_hp.setter
    def level_hp(self, level_hp):
        print('level_hp setter:', level_hp)
        self._level_hp = level_hp

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, attack):
        print('attack setter:', attack)
        self._attack = attack

    @property
    def add_attack(self):
        return self._add_attack

    @add_attack.setter
    def add_attack(self, add_attack):
        print('add_attack setter:', add_attack)
        self._add_attack = add_attack

    def target_attack(self, target):
        if isinstance(target, Player):
            print(self.name, '被', target.name, '攻擊，扣除hp', target.attack)
            self.hp -= target.attack
            print(self.name, '剩餘hp:', self.hp)

