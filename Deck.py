import random
from enum import Enum


class Card:
    # カード型を定義
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        assert suit in ['♣', '♥', '♦', '♠']
        assert rank in [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

class Deck:
    # カードデッキ生成モジュール
    suits = ['♣', '♥', '♦', '♠'] # 絵柄
    ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A'] # 数字
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards) # シャッフルする
    
    def draw(self):
        # デッキからカードを引く
        if len(self.cards) == 0:
            raise ValueError('No cards')
        return self.cards.pop(0)
    
    def remining_cards(self):
        # デッキの残り枚数を確認
        return len(self.cards)
