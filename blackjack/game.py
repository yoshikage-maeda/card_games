from Deck import Deck

class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.player_hand = [] # playerのハンド
        self.dealer_hand = [] # ディーラーのハンド
        pass
    
    def deal_initial_cards(self):
        # 最初にプレイヤーとディーラーがお互いに２枚ずつカードを引く
        self.player_hand = [self.deck.draw() for _ in range(2)]
        self.__print_hands(self.player_hand, 'プレイヤー')
        self.dealer_hand = [self.deck.draw() for _ in range(2)]
        self.__print_hands(self.dealer_hand, 'ディーラー')
    
    def player_hit(self):
        # プレイヤーがカードを引く
        self.player_hand.append(self.deck.draw())
        self.__print_hands(self.player_hand, 'プレイヤー')

    def dealer_hit(self):
        # ディーラーは手札の合計が17以下であればカードを引く
        while self.__hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw())
        self.__print_hands(self.dealer_hand, 'ディーラー')
    
    def is_bust(self, hand):
        # バストしているか判定
        return self.__hand_value(hand) > 21
    
    def is_blackjack(self, hand):
        # ブラックジャックかどうか判定
        return self.__hand_value(hand) == 21
    
    def check_winner(self):
        # 勝敗判定

        if self.is_bust(self.player_hand):
            return 'プレイヤーがバストしました。ディーラーの勝ちです.'
        if self.is_bust(self.dealer_hand):
            return 'Dealerがバストしました。プレイヤーの勝ちです.'
        
        # ハンドの値を算出
        player_value = self.__hand_value(self.player_hand)
        dealer_value = self.__hand_value(self.dealer_hand)

        if player_value ==dealer_value:
            return '引き分けです。'
        
        if self.is_blackjack(self.dealer_hand):
            return 'ディラーがブラックジャックです。ディーラーの勝ちです'

        if self.is_blackjack(self.player_hand):
            return 'プレイヤーがブラックジャックです。プレイヤーの勝ちです'
        
        if player_value > dealer_value:
            return 'プレイヤーの勝ちです'
        else:
            return 'ディーラーの勝ちです'

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
    
    
    def __print_hands(self, hands, name):
        print(f'{name}のハンド')
        for hand in hands:
            print(f'{hand.suit}_{hand.rank}', end=' ')
        print()

