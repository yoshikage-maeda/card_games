from blackjack import Blackjack
import logging
import datetime
from util import InputHandler, is_estimated_input, is_valid_bet_money
from functools import partial

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
in_handler = InputHandler()

while True:
    logger.info('--------------------------------')
    logger.info('新しいラウンド')
    logger.info(f'現在の所持金:{game.player_money}')

    # 掛け金の設定
    valid_func = partial(is_valid_bet_money, player_money=game.player_money) #部分適用して引数を入れる
    bet_money = in_handler.get_user_input('掛け金を設定してください。最低掛け金は10$, 最大掛け金は500$です:', valid_func)
    game.set_bet_money(bet_money)
    
    # 初期カードの表示
    game.deal_initial_cards()

    # イーブンとインシュアランスの処理
    even_flag = False
    insurance_flg = False
    if game.dealer_hand[0].rank == 'A':
        # イーブンの処理
        if game.is_blackjack(game.player_hand):
            even_flag = True
            logger.info('プレイヤーの手札がブラックジャックかつディーラがAのため、イーブンです!')
        else:
            valid_func = partial(is_estimated_input, estimated_inputs=['y', 'n'])
            user_input = in_handler.get_user_input('ディーラの手がAです。インシュアランスしますか。(y/n)?:', valid_func)
            if user_input.lower() == 'y':
                insurance_flg = True


    # サレンダーの設定
    valid_func = partial(is_estimated_input, estimated_inputs=['y', 'n'])
    user_input = in_handler.get_user_input('ハンドが公開されました。サレンダーしますか。(y/n)?:', valid_func)
    surrender_flg = user_input.lower() == 'y'
    
    if surrender_flg is False:
        while not game.is_bust(game.player_hand) and not game.is_blackjack(game.player_hand):
            valid_func = partial(is_estimated_input, estimated_inputs=['h', 's'])
            user_input = in_handler.get_user_input('「h」でヒット、「s」でスタンド:', valid_func)

            if user_input.lower() == 'h':
                game.player_hit()
            else:
                break
        # ディーラーがカードを引く
        game.dealer_hit()

    result, result_print = game.check_winner(surrender_flg, even_flag) # 結果の確認
    logger.info(result_print)
    game.update_money(result, insurance_flg) # 所持金の更新
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
