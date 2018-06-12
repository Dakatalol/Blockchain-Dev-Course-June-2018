import eth_keys, binascii
import json
privKey = eth_keys.keys.PrivateKey(binascii.unhexlify(
  '97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
message = 'Message for signing'
messageInBytes = b'Message for signing'
signature = privKey.sign_msg(messageInBytes)
stringName = str(hex(signature.s))
stringName = stringName [0:1] + stringName [2:];
signatureString =  str(hex(signature.r)) + stringName+ "0"+str(signature.v)
pubKey=privKey.public_key
address=pubKey.to_checksum_address()
print(json.dumps({'address': address, 'msg': message, 'sig': signatureString, 'version': 1}, sort_keys=True, indent=4))
