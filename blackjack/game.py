import sys
import os

# 一つ上のディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Deck import Deck
from enum import Enum

class GameResult(Enum):
    WIN = "win"
    BLACKJACK = "blackjack"
    LOSE = "lose"
    DRAW = "draw"
    SURRENDER = "surrender"
    
class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.player_hand = [] # playerのハンド
        self.dealer_hand = [] # ディーラーのハンド
        self.player_money = 1000 # 所持金
        pass
    
    def deal_initial_cards(self):
        # 最初にプレイヤーとディーラーがお互いに２枚ずつカードを引く
        self.player_hand = [self.deck.draw() for _ in range(2)]
        message = self.__out_hands_info(self.player_hand, 'プレイヤー')
        self.dealer_hand = [self.deck.draw() for _ in range(2)]
        message += self.__out_hands_info(self.dealer_hand, 'ディーラー', initial_dealer_hand = True)
        print(message)
    
    def player_hit(self):
        # プレイヤーがカードを引く
        self.player_hand.append(self.deck.draw())
        message = self.__out_hands_info(self.player_hand, 'プレイヤー')
        print(message)

    def dealer_hit(self):
        # ディーラーは手札の合計が17以下であればカードを引く
        while self.__hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw())
        message = self.__out_hands_info(self.dealer_hand, 'ディーラー')
        print(message)
    
    def is_bust(self, hand):
        # バストしているか判定
        return self.__hand_value(hand) > 21
    
    def is_blackjack(self, hand):
        # ブラックジャックかどうか判定
        return self.__hand_value(hand) == 21
    
    def check_winner(self, surrender_flg, even_flg):
        if surrender_flg:
            return GameResult.SURRENDER, 'サレンダーを選択したので、掛け金の半額を返金します。'
        if even_flg:
            return GameResult.WIN, 'イーブンのため、掛け金分の勝ちです。'
        

        # 勝敗判定
        if self.is_bust(self.player_hand) and self.is_bust(self.dealer_hand):
            return GameResult.LOSE, 'プレイヤーとディーラーどちらもバーストしました。ディーラーの勝ちです。'
        elif self.is_bust(self.player_hand):
            return GameResult.LOSE, 'プレイヤーがバストしました。ディーラーの勝ちです。'
        elif self.is_bust(self.dealer_hand):
            return GameResult.WIN, 'ディーラーがバストしました。プレイヤーの勝ちです。'
        
        # ハンドの値を算出
        player_value = self.__hand_value(self.player_hand)
        dealer_value = self.__hand_value(self.dealer_hand)

        if player_value == dealer_value:
            return GameResult.DRAW, '引き分けです。'
        
        if self.is_blackjack(self.dealer_hand):
            return GameResult.LOSE, 'ディーラーがブラックジャックです。ディーラーの勝ちです。'

        if self.is_blackjack(self.player_hand):
            return GameResult.BLACKJACK, 'プレイヤーがブラックジャックです。プレイヤーの勝ちです。'
        
        if player_value > dealer_value:
            return GameResult.WIN, 'プレイヤーの勝ちです。'
        else:
            return GameResult.LOSE, 'ディーラーの勝ちです。'

    def reset(self):
        #残り枚数を確認し、少なくなっていたらデッキを再生成
        self.player_hand = []
        self.dealer_hand = []
        if self.deck.remining_cards() < 15:
            self.deck = Deck()

    def __hand_value(self, hand):
        # ハンドの合計値を計算
        value = 0
        aces = 0

        for card in hand:
            rank = card.rank
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
                aces += 1
            else:
                value += int(rank)
            
        # Aを1にするか11にするかをポイントの合計値で判断
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value
    
    def set_bet_money(self, bet_money):
        # 掛け金の設定
        self.bet_money = int(bet_money)
    
    def place_money(self):
        # 掛け金分へらす
        self.player_money -= self.bet_money
    
    def offer_insurance(self):
        # インシュアランス処理
        self.insurance = int(self.bet_money * 0.5)
        self.player_money -= self.insurance

    def update_money(self, result, insurance_flg):
        # 所持金の更新

        # インシュアランスの処理
        if insurance_flg:
            if self.is_blackjack(self.dealer_hand):
                self.player_money += self.insurance * 3 # 掛け金とインシュアランスの費用が返却される
                self.bet_money = 0
                return 
        if result == GameResult.WIN:
            self.player_money += self.bet_money * 2
        elif result == GameResult.BLACKJACK:
            self.player_money += int(self.bet_money * 2.5)
        elif result == GameResult.DRAW:
            self.player_money += self.bet_money
        elif result == GameResult.SURRENDER:
            self.player_money += self.bet_money // 2
        
        return
    
    def __out_hands_info(self, hands, name, initial_dealer_hand=False):
        message = f'{name}のハンド\n'
        if initial_dealer_hand:
            message += f'{hands[0].suit}_{hands[0].rank}'
        else:
            for hand in hands:
                message += f'{hand.suit}_{hand.rank} '
        message += '\n'
        return message

