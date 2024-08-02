import json
import logging
import requests
import time

logger = logging.getLogger('auction_sniper.snipe')

class ShopGoodwillSniper:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.session = requests.Session()
        self.authenticate()

    def load_config(self, path):
        with open(path, 'r') as file:
            self.config = json.load(file)

    def authenticate(self):
        auth_info = self.config["auth_info"]
        response = self.session.post('https://www.shopgoodwill.com/Login', data=auth_info)
        if response.status_code == 200:
            logger.info("Successfully authenticated.")
        else:
### Enhanced `utils/snipe.py` (continued)

```python
import json
import logging
import requests
import time

logger = logging.getLogger('auction_sniper.snipe')

class ShopGoodwillSniper:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.session = requests.Session()
        self.authenticate()

    def load_config(self, path):
        with open(path, 'r') as file:
            self.config = json.load(file)

    def authenticate(self):
        auth_info = self.config["auth_info"]
        response = self.session.post('https://www.shopgoodwill.com/Login', data=auth_info)
        if response.status_code == 200:
            logger.info("Successfully authenticated.")
        else:
            logger.error(f"Authentication failed: {response.status_code}")
            raise Exception("Authentication failed.")

    def snipe_auction(self, auction_id, bid_amount):
        bid_url = 'https://www.shopgoodwill.com/Bid'
        payload = {
            'itemId': auction_id,
            'bidAmount': bid_amount
        }
        retry_count = 0
        while retry_count < 3:
            response = self.session.post(bid_url, data=payload)
            if response.status_code == 200:
                logger.info(f"Successfully placed bid of {bid_amount} on auction {auction_id}")
                return True
            else:
                logger.error(f"Failed to place bid on auction {auction_id}: {response.status_code}")
                retry_count += 1
                time.sleep(2)
        return False

def snipe_auction(auction_id, bid_amount):
    sniper = ShopGoodwillSniper('config.json')
    return sniper.snipe_auction(auction_id, bid_amount)
