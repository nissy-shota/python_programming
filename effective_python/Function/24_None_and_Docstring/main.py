from time import sleep
from datetime import datetime


def log(message, when=datetime.now()):
    print(f'{when} : {message}')


# falut
log('Hi there!')
sleep(1)
log('Hello again!')

def log2(message, when=None):

    """
    Args:
        message: Message to print
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when} : {message}')

log2('Hi there! (log2)')
sleep(1)
log2('Hello again! (log2)')


# デフォルト引数は一度しか評価されない．モジュール読み込み時の関数定義の時．動的な値をデフォルト引数に入れるとバグる． 
# このときはNoneにするのが良い．Docstringにもその旨を記載．
# デフォルトのNoneはかたヒントでも正しく動作する．