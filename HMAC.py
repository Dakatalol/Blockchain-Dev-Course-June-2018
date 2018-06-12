import hashlib, hmac, binascii

def hmac_sha512(key,msg):
    return hmac.new(key,msg,hashlib.sha512).digest()


key="devcamp".encode("utf8")
msg="blockchain".encode("utf8")
print(binascii.hexlify(hmac_sha512(key, msg)))