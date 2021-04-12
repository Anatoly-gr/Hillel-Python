# 1.Дано два кортежа, напишите функцию которая соединит их в один dict:
#
#    Input:
# coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
# code = ('BTC', 'ETH', 'XRP', 'LTC')
#
#    Output:
# {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}

def uplink(*first):
    k = list(first[0])
    v = list(first[1])
    new_dict = {x: y for x, y in zip(k, v)}
    return new_dict


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
codes = ('BTC', 'ETH', 'XRP', 'LTC')
print(uplink(coin, codes))
