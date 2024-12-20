def is_estimated_input(user_input, estimated_inputs):
    """想定したユーザ入力になっているか

    Args:
        user_input (str): メッセージ
    """
    return user_input.lower() in estimated_inputs

def is_valid_bet_money(bet_money, player_money):
    """掛け金が適切かどうか判定する。

    Args:
        bet_money (str): 掛け金
        player_money(int): 所持金
    """
    try:
        bet_money = int(bet_money)
        if not (10 <= bet_money <= 500) or bet_money > player_money:
                return False
    except ValueError:
        return False
    
    return True