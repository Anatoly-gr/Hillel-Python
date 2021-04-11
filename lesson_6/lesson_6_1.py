# 1.Дано два кортежа, напишите функцию которая соединит их в один dict:
#
#    Input:
#
# coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
# code = ('BTC', 'ETH', 'XRP', 'LTC')
#
#    Output:
#
# {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
def uplink(**kwargs):
    new_dict = {x: y for x, y in zip(coin, codes)}
    print(some_dict)


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
codes = ('BTC', 'ETH', 'XRP', 'LTC')

some_dict = {x: y for x, y in zip(coin, codes)}
print(some_dict)
