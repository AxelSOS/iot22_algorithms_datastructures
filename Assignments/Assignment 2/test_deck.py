from deck import Deck, Card

# Implementera tester ni anser lämpliga här. Motivera gärna varför de behövs (vad de testar och varför).

def test_card_init(suite, rank):

   pass





def test_card_str(suite, rank):

   pass





def test_card_eq(three_cards):

   pass





def test_card_lt(three_cards):

   pass





def test_card_gt():

   pass





def test_deck_insert():

   pass





def test_deck_len():

   pass




def test_deck_sort():
    """ Sort the deck according to card rank. All aces, the all two's, then all threes, ... """
    d = Deck()
    # Create a temporary deck
    # Go through the deck from left to right, insert the deck in the appropriate spot
    # Take a card from the old deck, insert it into the new one
    # Replace the old (empty) deck with the new (sorted) one


    pass

def test_deck_take():
    # Take the top card of the deck

    d = Deck()
    d.cards.append(1)
    d.cards.append(2)
    d.cards.append(3)
    assert d.cards.pop() == 3
    assert d.cards.pop() == 2
    assert d.cards.pop() == 1
    assert d.cards.pop() != 1


def test_deck_put():
    # Put a card on the top of the deck
    d = Deck()
    d.cards.append(1)
    assert d.cards[-1] == 1




