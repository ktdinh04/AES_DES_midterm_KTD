from .aes_utils import (
    aes_key_expansion,
    sub_bytes,
    shift_rows,
    mix_columns,
    add_round_key
)
import os

def pad(data):
    """
    PKCS#7 padding for AES blocks
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    block_size = 16
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length]) * padding_length
    return data + padding

def encrypt(plaintext, key):
    """
    Encrypt plaintext using AES-128 in CBC mode
    
    Args:
        plaintext (str): Text to encrypt
        key (bytes): 16, 24, or 32 bytes for AES-128, AES-192, or AES-256
        
    Returns:
        bytes: IV + encrypted data
    """
    # Ensure key is bytes
    if isinstance(key, str):
        key = key.encode('utf-8')
    
    # Ensure key length is valid (16, 24, or 32 bytes)
    assert len(key) in (16, 24, 32), "Key must be 16, 24, or 32 bytes long"
    
    # Ensure plaintext is bytes and padded to block size
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    plaintext = pad(plaintext)
    
    # Generate random IV
    iv = os.urandom(16)
    
    # Determine number of rounds based on key length
    num_rounds = {16: 10, 24: 12, 32: 14}[len(key)]
    
    # Key expansion
    expanded_key = aes_key_expansion(key, num_rounds)
    
    blocks = [plaintext[i:i+16] for i in range(0, len(plaintext), 16)]
    ciphertext = bytearray()
    
    # Use IV as previous block for first iteration
    prev_block = iv
    
    # Process each block
    for block in blocks:
        # XOR with previous ciphertext block (or IV for first block)
        xored_block = bytearray(16)
        for i in range(16):
            xored_block[i] = block[i] ^ prev_block[i]
        
        # Convert block to 4x4 state matrix (column-major order)
        state = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                state[i][j] = xored_block[i + 4*j]
        
        # Initial AddRoundKey
        state = add_round_key(state, expanded_key, 0)
        
        # Main rounds
        for round_num in range(1, num_rounds):
            state = sub_bytes(state)
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_key(state, expanded_key, round_num)
        
        # Final round (no MixColumns)
        state = sub_bytes(state)
        state = shift_rows(state)
        state = add_round_key(state, expanded_key, num_rounds)
        
        # Convert state matrix back to bytes
        encrypted_block = bytearray(16)
        for i in range(4):
            for j in range(4):
                encrypted_block[i + 4*j] = state[i][j]
        
        # Append to ciphertext and use as next previous block
        ciphertext.extend(encrypted_block)
        prev_block = encrypted_block
    
    # Return IV + ciphertext

    return iv + bytes(ciphertext)   