from player_class import Player
class Game:
    def __init__(self, players_list):
        self.plays_object = []
        self.player_init(players_list)

    @property
    def plays_object(self):
        return self._plays_object

    @plays_object.setter
    def plays_object(self ,plays_object):
        self._plays_object = plays_object
        print('plays_object setter:', plays_object)

    def player_init(self, players_list):
        for player in players_list:
            self.plays_object.append(Player(name = player))
            print(self.plays_object)


def player_create():
    players_list = []
    while True:
        user_name_input = input('請輸入遊戲名稱(結束請輸入q):')
        if user_name_input == 'q':
            break
        else:
            players_list.append(user_name_input)
    return players_list

def player_attack(object1, object2):
    object1.target_attack(object2)

def main():
    g1 = Game(player_create())
    player_attack(g1.plays_object[0], g1.plays_object[1])


if __name__ == '__main__':
    main()