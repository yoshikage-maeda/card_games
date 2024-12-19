from blackjack import Blackjack
import logging
import datetime

# ロガーの設定
logging.basicConfig(
    level=logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', # 出力フォーマット
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(f'logs/{datetime.datetime.now()}.log', mode='a', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

logger.info('ブラックジャックへようこそ')
game =  Blackjack()

while True:
    logger.info('--------------------------------')
    logger.info('新しいラウンド')
    logger.info(f'現在の所持金:{game.player_money}')
    while True:
        bet_money = input('掛け金を設定してください。最低掛け金は10$, 最大掛け金は500$です:')
        suceed_flag = game.set_bet_money(bet_money)
        if suceed_flag:
            break
        else:
            logger.info('掛け金が正しく設定されていません。')
    game.deal_initial_cards()

    while not game.is_bust(game.player_hand) and not game.is_blackjack(game.player_hand):
        user_input = input('「h」でヒット、「s」でスタンドです:')

        if user_input.lower() not in ['h', 's']:
            logger.info('不正な入力です。もう一度入力してください')
            continue

        if user_input.lower() == 'h':
            game.player_hit()
        else:
            break
    
    game.dealer_hit()
    result, result_print = game.check_winner() # 結果の確認
    logger.info(result_print)
    game.update_money(result) # 所持金の更新
    logger.info(f'現在の所持金:{game.player_money}')
    if game.player_money < 10:
        logger.info('所持金が最低掛け金より少なくなりました。Game Overです。')
        exit()

    game.reset()
    while True:
        user_input = input('「n」で新しいラウンド、「q」で終了:')
        if user_input.lower() == 'q':
            logger.info('ゲームを終了します。ありがとうございました。')
            exit()
        if user_input.lower() != 'n':
            logger.info('不正な入力です。もう一度入力してください')
            continue
        break
