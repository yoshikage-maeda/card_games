
class InputHandler:

    def get_user_input(self, input_message, is_valid_function):
        """ユーザの入力を受け取る関数

        Args:
            input_message (_type_): inputメッセージ
            is_valid_function: 
              (_type_): 想定されるinputのリスト
        """
        while True:
            user_input  = input(input_message)
            if is_valid_function(user_input):
                return user_input
            else:
                print('不正な入力です。もう一度入力してください')



