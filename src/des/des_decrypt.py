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

def decrypt(ciphertext, key):
    """
    Decrypt a message using DES algorithm
    
    Args:
        ciphertext (bytes or str): The encrypted message
        key (bytes): The 64-bit key used for decryption
        
    Returns:
        bytes: The decrypted plaintext
    """
    # Convert ciphertext to binary if it's a string
    if isinstance(ciphertext, str):
        ciphertext = bytes.fromhex(ciphertext)
    
    # Ensure ciphertext length is a multiple of 8 bytes (64 bits)
    if len(ciphertext) % 8 != 0:
        padding = 8 - (len(ciphertext) % 8)
        ciphertext += bytes([padding]) * padding
    
    # Generate subkeys (same as encryption)
    subkeys = generate_subkeys(key)
    
    # Reverse the order of subkeys for decryption
    subkeys.reverse()
    
    # Process each 64-bit (8-byte) block
    result = bytearray()
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
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
        
        # Final swap of left and right
        block_bits = right + left
        
        # Final permutation
        block_bits = final_permutation(block_bits)
        
        # Convert bits back to bytes
        for j in range(0, 64, 8):
            result.append(int(block_bits[j:j+8], 2))
    
    # Remove padding if needed
    if result[-1] < 8 and all(b == result[-1] for b in result[-result[-1]:]):
        result = result[:-result[-1]]
    
    return bytes(result)

def main():
    # Read the ciphertext and key from the input file
    with open('data/input.txt', 'r') as file:
        lines = file.readlines()
        ciphertext = lines[0].strip()
        key = lines[1].strip()

    # Decrypt the ciphertext
    plaintext = decrypt(ciphertext, key)

    # Write the plaintext to the output file
    with open('data/output_des.txt', 'w') as file:
        file.write(plaintext.decode('utf-8'))

if __name__ == "__main__":
    main()