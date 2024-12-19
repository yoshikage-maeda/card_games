from blackjack import Blackjack

print('ブラックジャックへようこそ')
game =  Blackjack()

while True:
    print('--------------------------------')
    print('新しいラウンド')
    game.deal_initial_cards()

    while not game.is_bust(game.player_hand) and not game.is_blackjack(game.player_hand):
        user_input = input('「h」でヒット、「s」でスタンド、「q」で終了です')

        if user_input.lower() == 'q':
            print('ゲームを終了します。ありがとうございました。')
            break
        if user_input.lower() not in ['h', 's']:
            print('不正な入力です。もう一度入力してください')
            continue

        if user_input.lower() == 'h':
            game.player_hit()
        else:
            break
    
    game.dealer_hit()
    result = game.check_winner()
    print(result)

    game.reset()
    while True:
        user_input = input('「n」で新しいラウンド、「q」で終了:')
        if user_input.lower() == 'q':
            print('ゲームを終了します。ありがとうございました。')
            exit()
        if user_input.lower() != 'n':
            print('不正な入力です。もう一度入力してください')
            continue
        break
