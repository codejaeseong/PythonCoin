import hashlib
import base58check
import json
from ecdsa import SigningKey, SECP256k1

def make_wallet():
    ver = '0.1' # version

    sign_key = SigningKey.generate(curve=SECP256k1)  # private key
    verify_key = sign_key.verifying_key  # public key

    skj = sign_key.to_string (). hex () # input json var : Sign.Key.Json
    vkj = verify_key.to_string (). hex ()  # Verify.Key.Json

    payload = verify_key.to_string (). hex ()
    checkSum = ver + payload
    checkSum = hashlib.sha256(checkSum.encode())
    checkSum = checkSum.hexdigest()
    checkSum = hashlib.sha256(checkSum.encode())
    checkSum = checkSum.hexdigest()[:2]

    result = ver + payload + checkSum
    result = result.encode('utf-8')
    result = base58check.b58encode(result)
    addr = str(result)[6:46] # cutting garbege text

    
    wallet = dict()

    wallet["sign_key"] = skj
    wallet["verifying_key"] = vkj
    wallet["address"] = addr

    with open(addr+'wallet.json', 'w',encoding='utf-8') as make_file:
        json.dump(wallet, make_file, indent="\t")

