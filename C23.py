'''

'''
import urllib
import json
import urllib.request

baker_address = 'tz1UUgPwikRHW1mEyVZfGYy6QaxrY6Y7WaG5'
payment_account = 'test_imp'  # account from which to make payments
fee_percent = 5.0  # delegation service fee
tx_fee = 0.00  # tx fee on payouts
cycle = 23

response = urllib.request.urlopen('http://api.tzscan.io/v2/rewards_split/{}?cycle={}'.format(baker_address, cycle))
data = json.loads(response.read())
total_staking_balance = int(data['delegate_staking_balance'])
total_rewards = data['blocks_rewards'] + \
                data['endorsements_rewards'] + \
                data['fees'] + \
                data['gain_from_denounciation'] - \
                data['lost_deposit_from_denounciation'] - \
                data['lost_fees_denounciation'] - \
                data['lost_rewards_denounciation']
for del_balance in data['delegators_balance']:
    delegator_address = del_balance[0]['tz']
    payout = (float(del_balance[1]) / total_staking_balance) * total_rewards
    payout = (payout * (100 - fee_percent)) / 100  # subtract fee
    payout = round(payout / 10000000000, 8)  # convert to XTZ
    print('./tezos-client transfer {} from {} to {} --fee {}'.format(payout,payment_account,delegator_address,tx_fee))
    
    
  
    
    
