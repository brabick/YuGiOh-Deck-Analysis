import random
import varname

class DeckAnalysis:
    def __init__(self):
        self.deck_list = []
        self.hand_list = []
        self.hand_data = []
        self.card_types = {
            'HDT': 0,
            'SRT': 0,
            'AHT': 0,
            'CBP': 0,
            'DRC': 0,
            'DCC': 0,
            'EXT': 0,
            'SCH': 0,
            'GAR': 0,
            'BRD': 0,
            'OTH': 0
        }

    def make_deck(self):
        # Reads the deck file and adds the adds the contents to a list for further work
        read_deck = input('Do you want to read the deck? y/n')
        if read_deck == 'y':
            deck = open("deck.txt", "r")
            self.deck_list = []
            for line in deck:
                line = line[:-1]
                self.deck_list.append(line)
            # Shuffle the deck
            random.shuffle(self.deck_list)
        else:
            self.input_data(self)

    def make_hands(self):
        self.__init__(self)
        self.make_deck(self)
        self.hand_list = []
        loop_times = len(self.deck_list) / 5
        loop = 0
        # Go through the deck, 5 cards at a time
        # and add them to the hand.
        while loop < loop_times:
            hand = []
            for card in self.deck_list[0:5]:
                # Creates the dictionary that will be used to store the data for each hand
                types_in_hand = self.card_types.fromkeys(self.card_types, 0)
                # Remove the cards from the deck that have already been drawn
                self.deck_list.remove(card)
                # Split the card from the card type, then add the card types to the hand list
                # The specific card doesn't really matter, just the type of card
                card = card.split(" :")
                card = card[1]
                # if a card covers more than one category, split it and add each
                # card to the list
                if len(card) > 3:
                    card = card.split(",")
                    #print(card)
                    for c in card:
                        c = c.strip()
                        hand.append(c)
                        #print(c)
                else:
                    hand.append(card)
                for card in hand:
                    for type in self.card_types:
                        #print(card, type)
                        if card == type:
                            types_in_hand[type] = types_in_hand[type] + 1

            self.hand_list.append(types_in_hand)
            # print(len(self.deck_list))
            loop = loop + 1

    def input_data(self, hdt=0, srt=0, aht=0, cbp=0, drc=0, dcc=0, ext=0, sch=0, gar=0, brd=0, neg=0, oth=0):
        self.__init__(self)
        param_index = 0
        #self.input_card_types = self.card_types.fromkeys(self.card_types, 0)
        for key in self.card_types:
            for param in self.input_data.__code__.co_varnames:
                if param.upper() == key:
                    key_input = int(input('How many %s' % key))
                    locals()[param_index] = key_input
                    param_index = param_index + 1
                    for x in range(key_input):
                        self.deck_list.append(key)
        print(self.deck_list)

    def prep_data(self, num_runs):
        loop = 0
        self.make_hands(self)
        self.hands_with = self.card_types.fromkeys(self.card_types, 0)
        while loop < num_runs:
            self.make_hands(self)
            for hand in self.hand_list:
                if hand['HDT'] > 0:
                    self.hands_with['HDT'] = self.hands_with['HDT'] + 1
                if hand['AHT'] > 0:
                    self.hands_with['AHT'] = self.hands_with['AHT'] + 1
                if hand['SRT'] > 0:
                    self.hands_with['SRT'] = self.hands_with['SRT'] + 1
                if hand['CBP'] > 0:
                    self.hands_with['CBP'] = self.hands_with['CBP'] + 1
                if hand['DRC'] > 0:
                    self.hands_with['DRC'] = self.hands_with['DRC'] + 1
                if hand['DCC'] > 0:
                    self.hands_with['DCC'] = self.hands_with['DCC'] + 1
                if hand['EXT'] > 0:
                    self.hands_with['EXT'] = self.hands_with['EXT'] + 1
                if hand['SCH'] > 0:
                    self.hands_with['SCH'] = self.hands_with['SCH'] + 1
                if hand['GAR'] > 0:
                    self.hands_with['GAR'] = self.hands_with['GAR'] + 1
                if hand['BRD'] > 0:
                    self.hands_with['BRD'] = self.hands_with['BRD'] + 1
                if hand['OTH'] > 0:
                    self.hands_with['OTH'] = self.hands_with['OTH'] + 1
                loop = loop + 1

        print(self.hands_with)

    def do_maths(self, num_runs):
        self.prep_data(self, num_runs)
        for key in self.hands_with:
            chance = self.hands_with[key] / num_runs * 100
            print('Percentage of hands with %s after %s hands is %s' % (key, num_runs, chance))


if __name__ == "__main__":
    #DeckAnalysis.do_maths(DeckAnalysis, 100)
    DeckAnalysis.input_data(DeckAnalysis)
