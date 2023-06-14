import random 

def encode_binary(x, num_bits):
    step = 10.0 / (2 ** num_bits) 
    scaled_x = round(x / step) #
    binary_string_with_prefix = bin(scaled_x)
    binary_string = binary_string_with_prefix[2:]
    binary_string_padded = binary_string.zfill(num_bits)
    return binary_string_padded

def decode_binary(binary_string, num_bits):
    step = 10.0 / (2 ** num_bits)
    binary_integer = int(binary_string, 2)
    x = binary_integer * step
    return x



#przyklad
num_bits = 8
#x = 6.5
x = random.uniform(0, 10)

binary_string = encode_binary(x, num_bits)
print(f"Binary representation of x: {binary_string}")

decoded_x = decode_binary(binary_string, num_bits)
print(f"Decoded value of x:  {decoded_x}")


