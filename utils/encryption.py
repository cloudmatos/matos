import base64
from Crypto.Cipher import AES



class Encryptor:

    def __init__(self,
                 key,
                 init_vector,
                 ):
        """
        Class contructoer
        """

        # if not key:
        #     key = config.ENCRYPTION_KEY
        #
        # if not init_vector:
        #     init_vector = config.ENCRYPTION_VECTOR

        self.key = key
        self.init_vector = init_vector

    def _pad(self,
             data,
             ):
        """
        pads the data for encryption
        """

        return data + (AES.block_size - len(data) % AES.block_size) *\
            chr(AES.block_size - len(data) % AES.block_size)

    def _unpad(self,
               data,
               ):
        """
        unpads data after decryption
        """

        return data[:-ord(data[len(data) - 1:])]

    def _cipher(self):
        """
        returns cipher object
        """

        return AES.new(key=self.key.encode('utf-8'), mode=AES.MODE_CBC, IV=self.init_vector.encode('utf-8'))

    def encrypt(self,
                data,
                ):
        """
        return encrypted string of the given data
        """

        padded_data = self._pad(data)
        encrypted_data = self._cipher().encrypt(padded_data)
        encrypted_utf8 = base64.b64encode(
            encrypted_data).decode('utf-8', 'ignore')

        return encrypted_utf8

    def decrypt(self,
                data,
                ):
        """
        return decrypted string of the given encrypted data
        """

        decoded_data = base64.b64decode(data)
        decrypted_data = self._cipher().decrypt(decoded_data)
        decrypted_utf8 = self._unpad(decrypted_data).decode('utf-8', 'ignore')

        return decrypted_utf8
