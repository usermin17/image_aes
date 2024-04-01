# Import necessary modules
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

try:
    # Take path of image as input
    path = input(r'Enter path of Image : ')

    # Taking decryption key as input (it should be 16, 24, or 32 bytes long for AES)
    key = input('Enter Key (16/24/32 bytes) for decryption of Image : ').encode()

    # Print path of image file and decryption key that we are using
    print('The path of file : ', path)
    print('Key for decryption : ', key)

    # Open file for reading purpose
    with open(path, 'rb') as fin:
        # Store image data in variable "image"
        image = fin.read()

    # Initialize AES cipher with the provided key
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the image data
    decrypted_image = decryptor.update(image) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_image) + unpadder.finalize()

    # Open file for writing purpose
    with open(path, 'wb') as fout:
        # Write decrypted data to image file
        fout.write(unpadded_data)

    print('Decryption Done...')

except Exception as e:
    print('Error caught:', str(e))
