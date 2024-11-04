# Function to perform XOR between two strings
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

# Function to perform Mod-2 division
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:  # If first bit is '0', perform XOR with 0's
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    # Perform XOR for the last time
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

# Function to encode data using the given key
def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

# Taking input from user
data = input("Enter the data: ")
key = input("Enter the key (polynomial): ")

# Encoding the data
encoded_data = encodeData(data, key)

# Displaying the encoded data
print("Encoded data: ", encoded_data)
