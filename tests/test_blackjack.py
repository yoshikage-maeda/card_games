import pytest
from ..blackjack import Blackjack
from ..Deck import Card

@pytest.mark.parametrize(
        "hands, value",
        [
            ([Card('♥', 'J'), Card('♥', 'K')], 20),
            ([Card('♥', '2'), Card('♥', 'A')], 13),
            ([Card('♥', 'A'), Card('♥', 'A')], 12),
            ([Card('♥', 'A'), Card('♥', 'A'), Card('♥', 'A')], 13),
            ([Card('♥', 'K'), Card('♥', 'J'), Card('♥', '10')], 30),
            ([Card('♥', 'K'), Card('♥', 'A')], 21)
        ]
)
def test_hand_value(hands, value):
    # 手札のスコア値をテスト
    game = Blackjack()
    assert game._Blackjack__hand_value(hands) == value
