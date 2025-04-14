def main():
    from src.utils.file_handler import read_input, write_output
    from src.aes.aes_encrypt import encrypt as aes_encrypt
    from src.aes.aes_decrypt import decrypt as aes_decrypt
    from src.des.des_encrypt import encrypt as des_encrypt
    from src.des.des_decrypt import decrypt as des_decrypt
    from src.aes.aes_utils import generate_key as aes_generate_key
    from src.des.des_utils import generate_key as des_generate_key

    # Read input data
    plaintext = read_input('data/input.txt')

    # AES Encryption
    aes_key = aes_generate_key()
    aes_ciphertext = aes_encrypt(plaintext, aes_key)
    write_output('data/output_aes.txt', aes_ciphertext)

    # DES Encryption
    des_key = des_generate_key()
    des_ciphertext = des_encrypt(plaintext, des_key)
    write_output('data/output_des.txt', des_ciphertext)

if __name__ == "__main__":
    main()