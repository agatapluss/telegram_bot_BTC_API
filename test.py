from pony.orm.examples.estore import *
from datetime import timedelta
set_sql_debug(True)
pony.MODE = 'INTERACTIVE'


# wallet = bit.PrivateKeyTestnet('cPKhaAcAuJacin1xYjWu1GCMeM8TPtpncQ1NTEKhbSCjzb8VqpTE')  # наш кошелек готов и содержится в переменной wallet
# print(f"Баланс: {wallet.get_balance()}")
# print(f"Адрес: {wallet.address}")
# print(f"Приватный ключ: {wallet.to_wif()}")
# print(f'Все транзакции {wallet.get_transactions()}')

# output =[('muh9DYMTWXfPEd9zPnfvCS1yX8hPLbkE9e', 0.00001, 'btc')]

# Transaction = wallet.send(output)