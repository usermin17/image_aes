# Import necessary modules
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

try:
    # Take path of image as input
    path = input(r'Enter path of Image : ')

    # Taking encryption key as input (it should be 16, 24, or 32 bytes long for AES)
    key = input('Enter Key (16/24/32 bytes) for encryption of Image : ').encode()

    # Print path of image file and encryption key that we are using
    print('The path of file : ', path)
    print('Key for encryption : ', key)

    # Open file for reading purpose
    with open(path, 'rb') as fin:
        # Store image data in variable "image"
        image = fin.read()

    # Initialize AES cipher with the provided key
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the image data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(image) + padder.finalize()
    encrypted_image = encryptor.update(padded_data) + encryptor.finalize()

    # Open file for writing purpose
    with open(path, 'wb') as fout:
        # Write encrypted data to image file
        fout.write(encrypted_image)

    print('Encryption Done...')

except Exception as e:
    print('Error caught:', str(e))
