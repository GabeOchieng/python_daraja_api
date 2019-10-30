# Python Daraja Api Client
## Description
- Yet another (of many) python daraja api client library.
- WIP (pre-alpha).

## why re-inventing the wheel?
- They exists "many" daraja api python libraries, but none of them suited my project needs, and are trying to tweek them just ended up with almost not meeting my deadlines.

## Contributions
- Highly welcomed, documenting(please someone!), bug fixes and new features, got some time on you, write the b2b api client.

## Work Done
- [x] Generate Auth Token.
- [x] Lipa Na Mpesa Api.
- [ ] C2B Api
- [ ] B2B Api
- [ ] B2B Api
- [ ] Reversal Api

## Installation
```bash
pip install daraja_api
```

## Usage
- I swear i'll write a documetation when I get time, for now just look at the code sample below, i'll provide info where you can 
- This is not a detailed doc of how daraja api works, for that i highly recommend this article [https://peternjeru.co.ke/safdaraja/ui/](https://peternjeru.co.ke/safdaraja/ui/).

### Lipa Na Mpesa Example
```python
# Lipa na mpesa example
from daraja_api.conf import ConfigFromObject
from daraja_api.clients.lnm_api_client import LNMApiClient

settings={
    "MPESA_CONSUMER_KEY":"Your project Consumer Key",
    "MPESA_CONSUMER_SECRET":"Your project",
    "MPESA_ENVIRONMENT":"sandbox",
    "MPESA_PASSKEY":"YOUR PASSKEY",
    "MPESA_EXPRESS_SHORTCODE":"Your express shortcode"
}

config = ConfigFromObject(settings)
lnm = LNMApiClient(config)

# sends an stk push to the clients phone
# phone,amount, callback_url
res = lnm.stk_push('0712345678',1,'https://en0o5cquqd6r2.x.pipedream.net/')
'''
{'MerchantRequestID': '19198-5754897-1', 'CheckoutRequestID': 'ws_CO_DMZ_409543028_30102019071229528', 
'ResponseCode': '0', 'ResponseDescription': 'Success. Request accepted for processing', 
'CustomerMessage': 'Success. Request accepted for processing'}
'''

# after getting a response on the callback url, to parse the response
parsed_callback_response = lnm.parse_stk_callback_response(callback_response)
'''
{'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 
'MerchantRequestID': '9817-6110965-1', 'CheckoutRequestID': 
'ws_CO_DMZ_409542433_30102019070632000', 'meta': {'Amount': 1, 'MpesaReceiptNumber': 
'NJU9LE0O5Z', 'Balance': None, 'TransactionDate': 20191030070701, 'PhoneNumber':
 254705774995}}
'''
```


## References
- [https://peternjeru.co.ke/safdaraja/ui/](https://peternjeru.co.ke/safdaraja/ui/), This guy is a hero.
- [https://developer.safaricom.co.ke/docs](https://developer.safaricom.co.ke/docs)
- [https://github.com/martinmogusu/django-daraja](https://github.com/martinmogusu/django-daraja)
