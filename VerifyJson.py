import eth_keys, binascii
import json



json_string = """
{
    "address": "0xa44f70834a711F0DF388ab016465f2eEb255dEd0",
    "msg": "Message for signing",
    "sig": "0x6f0156091cbe912f2d5d1215cc3cd81c0963c8839b93af60e0921b61a19c54300c71006dd93f3508c432daca21db0095f4b16542782b7986f48a5d0ae3c583d401",
    "version": 1
}
"""
data = json.loads(json_string)
address = data['address']
signature = eth_keys.keys.Signature(binascii.unhexlify(data['sig'][2:]))
signerPubKey = signature.recover_public_key_from_msg(data['msg'].encode())
signerAddress = signerPubKey.to_checksum_address()
print('Signature valid?:', signerAddress == address)