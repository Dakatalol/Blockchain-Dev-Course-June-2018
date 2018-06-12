import eth_keys, binascii
privKey = eth_keys.keys.PrivateKey(binascii.unhexlify(
  '97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
#print('Private key (64 hex digits):', privKey)
signature = privKey.sign_msg(b'exercise-cryptography')
print('{"signature" : "', signature,'"')
print(',"v" : "{0}", "r" : "{1}", "s" : "{2}"]'.format(
  hex(signature.v), hex(signature.r), hex(signature.s)))
