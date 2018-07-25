from mystyle.my_class import *

if __name__ == '__main__':
    test_deck = Deck()
    test_deck.shuffle()

    test_player = Hand()
    pulled_card = test_deck.deal()
    print(pulled_card)

    test_player.add_card(pulled_card)
    print(test_player.value)

