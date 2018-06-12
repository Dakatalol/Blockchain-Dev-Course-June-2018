import hashlib, binascii
from Crypto.Hash import keccak
import whirlpool

text = 'blockchain'
data = text.encode("utf8")

sha384hash=hashlib.sha384(data).digest()
print("SHA384:   ",binascii.hexlify(sha384hash))


sha512hash=hashlib.sha512(data).digest()
print("SHA512:   ",binascii.hexlify(sha512hash))

sha3_512hash=hashlib.sha3_512(data).digest()
print("SHA3-512:   ",binascii.hexlify(sha3_512hash))

Keccak512hash=keccak.new(data=data,digest_bits=512).digest()
print("Keccak512:   ",binascii.hexlify(Keccak512hash))


Whirlpool512hash=whirlpool.new(data).digest()
print("SHA3-512:   ",binascii.hexlify(Whirlpool512hash))