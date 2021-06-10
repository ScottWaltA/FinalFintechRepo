# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import constants.py
from web3 import Web3
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from eth_account import Account

from pathlib import Path
from getpass import getpass

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
key = wif_to_key("PRIVATE_KEY_IN_WIF_FORMAT_HERE")

 
 
# Create a function called `derive_wallets`
def derive_wallets():
    command = 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = 

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account():
    

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx():
     

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx():


