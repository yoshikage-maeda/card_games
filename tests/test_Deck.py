import pytest
import sys
from ..Deck import Deck, Card

def test_cards():
    # 52枚のカードが生成されているかどうか
    deck = Deck()
    assert len(deck.cards) == 52

def test_shuffle_cards():
    # カードがシャッフルされているかどうか
    deck = Deck()
    another_deck = Deck()
    assert deck != another_deck # 等号が定義されているから確認可能

def test_draw_card():
    # カードが引けるかどうか
    deck = Deck()
    card = deck.draw()
    assert isinstance(card, Card)

def test_card_remain():
    # 引いたカードが山札に残っていないか
    deck = Deck()
    card = deck.draw()
    assert card not in deck.cards

def test_exceed_draw():
    # 山札がなくなったら例外が発生するか
    deck = Deck()
    for _ in range(52):
        deck.draw()
    with pytest.raises(ValueError):
        deck.draw()