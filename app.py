from flask import Flask, render_template, request, jsonify
from utils.scraper import get_auctions
from utils.snipe import snipe_auction
from utils.ebay_api import get_ebay_price
import logging
import json

# Initialize Flask app
app = Flask(__name__)

# Load config
with open('config.json', 'r') as file:
    config = json.load(file)

# Setup logging
logging.config.dictConfig(config['logging'])
logger = logging.getLogger('auction_sniper')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keywords = request.form.get('keywords')
    auctions = get_auctions(keywords)
    return jsonify(auctions)

@app.route('/snipe', methods=['POST'])
def snipe():
    auction_id = request.form.get('auction_id')
    bid_amount = request.form.get('bid_amount')
    snipe_auction(auction_id, bid_amount)
    return jsonify({'status': 'success'})

@app.route('/ebay_price', methods=['POST'])
def ebay_price():
    item_name = request.form.get('item_name')
    price = get_ebay_price(item_name)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)
