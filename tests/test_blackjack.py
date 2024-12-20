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

@pytest.mark.parametrize(
        "player_money, bet_money, output",

        [
            (200, 50,  True), # happy 
            (50, 100, False), # 所持金を超えるケース
            (50, 5, False), # 範囲外
            (5000, 600, False)
        ]
)
def test_bet_money(player_money, bet_money, output):
    game = Blackjack()
    game.player_money = player_money
    success_f = game.set_bet_money(bet_money)
    assert success_f is output

@pytest.mark.parametrize(
    "hands_ranks, first_hands_f, who,  expected_hands_num",
    [
        (['4', '3', '5'], False, 'プレイヤー', 3),
        (['2', 'J'], True, 'ディーラー', 1)
    ]
)

def test_out_message(hands_ranks, first_hands_f, who, expected_hands_num):
    game = Blackjack()
    hands = [Card('♥', rank) for rank in hands_ranks]
    
    message = game._Blackjack__out_hands_info(hands, who, first_hands_f)
    assert len(message.split('_')) - 1 == expected_hands_num