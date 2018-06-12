using System;
using System.Globalization;
using System.Numerics;
using System.Security.Cryptography;

namespace BitcoinAddressGenerator
{
    class BitcoinAddress
    {
        static void Main(string[] args)
        {
            string HexHash = "7e4670ae70c98d24f3662c172dc510a085578b9ccc717e6c2f4e547edd960a34";
            byte[] PubKey = HexToByte(HexHash);
            Console.WriteLine("Public Key:" + ByteToHex(PubKey));

            byte[] PubKeySha = Sha256(PubKey);
            Console.WriteLine("Sha Public Key:" + ByteToHex(PubKeySha));

            byte[] PubKeyShaRIPE = RipeMD160(PubKeySha);
            Console.WriteLine("Ripe Sha Public Key:" + ByteToHex(PubKeyShaRIPE));

            byte[] PreHashWNetwork = AppendBitcoinNetwork(PubKeyShaRIPE, 0);
            byte[] PublicHash = Sha256(PreHashWNetwork);
            Console.WriteLine("Public Hash:" + ByteToHex(PublicHash));

            byte[] PublicHashHash = Sha256(PublicHash);
            Console.WriteLine("Public HashHash:" + ByteToHex(PublicHashHash));

            Console.WriteLine("Checksum:" + ByteToHex(PublicHashHash).Substring(0, 4));

            byte[] Address = ConcatAddress(PreHashWNetwork, PublicHashHash);
            Console.WriteLine("Address:" + ByteToHex(Address));

            Console.WriteLine("Human Address:" + Base58Encode(Address));
        }

        public static byte[] HexToByte(string HexString)
        {
            if (HexString.Length % 2 != 0)
            {
                throw new Exception("Invalid HEX");
            }

            byte[] retArray = new byte[HexString.Length / 2];

            for (int i = 0; i < retArray.Length; ++i)
            {
                retArray[i] = byte.Parse(HexString.Substring(i * 2, 2), NumberStyles.HexNumber, CultureInfo.InvariantCulture);
            }

            return retArray;
        }

        public static byte[] Sha256(byte[] array)
        {
            SHA256Managed hashstring = new SHA256Managed();
            return hashstring.ComputeHash(array);
        }

        public static byte[] RipeMD160(byte[] array)
        {
            RIPEMD160Managed hashstring = new RIPEMD160Managed();
            return hashstring.ComputeHash(array);
        }

        public static byte[] AppendBitcoinNetwork(byte[] RipeHash, byte Network)
        {
            byte[] extended = new byte[RipeHash.Length + 1];
            extended[0] = (byte)Network;
            Array.Copy(RipeHash, 0, extended, 1, RipeHash.Length);
            return extended;
        }

        public static byte[] ConcatAddress(byte[] RipeHash, byte[] Checksum)
        {
            byte[] ret = new byte[RipeHash.Length + 4];
            Array.Copy(RipeHash, ret, RipeHash.Length);
            Array.Copy(Checksum, 0, ret, RipeHash.Length, 4);
            return ret;
        }

        private static string ByteToHex(byte[] pubKeySha)
        {
            byte[] data = pubKeySha;
            string hex = BitConverter.ToString(data);
            return hex;
        }

        public static string Base58Encode(byte[] array)
        {
            const string ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
            string retString = string.Empty;
            BigInteger encodeSize = ALPHABET.Length;
            BigInteger arrayToInt = 0;
            for (int i = 0; i < array.Length; ++i)
            {
                arrayToInt = arrayToInt * 256 + array[i];
            }
            while (arrayToInt > 0)
            {
                int rem = (int)(arrayToInt % encodeSize);
                arrayToInt /= encodeSize;
                retString = ALPHABET[rem] + retString;
            }
            for (int i = 0; i < array.Length && array[i] == 0; ++i)
                retString = ALPHABET[0] + retString;

            return retString;
        }
    }
}