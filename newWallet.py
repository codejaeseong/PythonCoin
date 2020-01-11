import hashlib
import base58check
from ecdsa import SigningKey, SECP256k1

ver = '0.1' # version

sign_key = SigningKey.generate(curve=SECP256k1)  # private key
verify_key = sign_key.verifying_key  # public key

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
result = 0  # delete info

print(addr)