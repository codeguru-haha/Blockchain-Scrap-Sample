from kwenta import Kwenta
from config import *

kwenta = Kwenta(
    network_id=10,
    provider_rpc=PROVIDER_RPC,
    wallet_address=WALLET_ADDRESS
)
for attr_name in dir(kwenta):
    attr_value = getattr(kwenta, attr_name)
    print(attr_name, ":", attr_value)
