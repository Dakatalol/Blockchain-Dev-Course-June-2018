import eth_keys, binascii
privKey = eth_keys.keys.PrivateKey(binascii.unhexlify(
  '97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
#print('Private key (64 hex digits):', privKey)
signature = privKey.sign_msg(b'exercise-cryptography')


pubkey = signature.recover_public_key_from_msg(b'exercise-cryptography')
#print('Signer public key (recovered):', pubkey)
signerAddress = pubkey.to_checksum_address()
print('Signer address:', signerAddress)
