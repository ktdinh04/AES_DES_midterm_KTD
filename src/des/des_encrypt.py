from .des_utils import (
    generate_subkeys,
    initial_permutation,
    final_permutation,
    expand,
    substitution,
    permutation,
    xor,
    split_blocks
)

def permute(key, arr):
    return ''.join(key[i] for i in arr)

def left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

def generate_keys(key):
    key = permute(key, [56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35])
    keys = []
    left, right = key[:28], key[28:]
    for i in [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]:
        left = left_shift(left, i)
        right = left_shift(right, i)
        keys.append(permute(left + right, [0, 13, 10, 3, 1, 2, 15, 4, 5, 6, 7, 8, 9, 12, 11, 14]))
    return keys

def f_function(right, key):
    # Placeholder for the function that applies the DES function
    return right  # This should be replaced with the actual implementation

def encrypt(plaintext, key):
    """
    Encrypt a message using DES algorithm
    
    Args:
        plaintext (str or bytes): The message to encrypt
        key (bytes): The 64-bit key used for encryption
        
    Returns:
        bytes: The encrypted ciphertext
    """
    # Convert plaintext to bytes if it's a string
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # Ensure plaintext length is a multiple of 8 bytes (64 bits)
    if len(plaintext) % 8 != 0:
        padding = 8 - (len(plaintext) % 8)
        plaintext += bytes([padding]) * padding
    
    # Generate subkeys
    subkeys = generate_subkeys(key)
    
    # Process each 64-bit (8-byte) block
    result = bytearray()
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        # Convert block to bits
        block_bits = ''.join(format(b, '08b') for b in block)
        
        # Initial permutation
        block_bits = initial_permutation(block_bits)
        
        # Split into left and right halves
        left, right = split_blocks(block_bits)
        
        # 16 rounds of the Feistel network
        for j in range(16):
            # Save the current right half
            old_right = right
            
            # Expansion
            expanded = expand(right)
            
            # Key mixing
            mixed = xor(expanded, subkeys[j])
            
            # S-box substitution
            substituted = substitution(mixed)
            
            # P-box permutation
            permuted = permutation(substituted)
            
            # XOR with left half and swap
            right = xor(left, permuted)
            left = old_right
        
        # Final swap (the 16th round doesn't swap, so we need to swap here)
        block_bits = right + left
        
        # Final permutation
        block_bits = final_permutation(block_bits)
        
        # Convert bits back to bytes
        for j in range(0, 64, 8):
            result.append(int(block_bits[j:j+8], 2))
    
    return bytes(result)

def main():
    # Read input from file
    with open('data/input.txt', 'r') as file:
        plaintext = file.read().strip()
    
    # Define a key (this should be securely generated)
    key = '1010101010111011000011110000111100001111000011110000111100001111'  # Example 64-bit key
    
    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    
    # Write output to file
    with open('data/output_des.txt', 'w') as file:
        file.write(ciphertext)

if __name__ == "__main__":
    main()