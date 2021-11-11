
import base64


def str_to_b64(text=""):
    base64_bytes = base64.b64encode(text.encode())
    return base64_bytes.decode()


def b64_to_str(base64_text):
    base64_bytes = base64_text.encode()
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode()
    return message


def to_ascii_code(base64_text):
    buffer = []
    final_base_text = padding_block(base64_text)
    for char in final_base_text:
        buffer.append(ord(char))
    return buffer


def to_string(ascii_buffer):
    text_buffer = ""
    for ascii in ascii_buffer:
        text_buffer = text_buffer + chr(ascii)
    return text_buffer


def padding_block(base64_text):
    while len(base64_text) % 8 != 0:
        base64_text = base64_text + " "
    return base64_text


def get_binary_16(number):
    text = ""
    if number == 2 ** 16:
        return "0000000000000000"
    for x in range(15, -1, -1):
        if (number - 2 ** x) >= 0:
            text = text + "1"
            number = number - 2 ** x
        else:
            text = text + "0"
    return text


def get_binary(number):
    text = ""
    for x in range(7, -1, -1):
        if (number - 2 ** x) >= 0:
            text = text + "1"
            number = number - 2 ** x
        else:
            text = text + "0"
    return text


def get_str_from_binary(text):
    number = 0
    for bit_index in range(len(text) - 1, -1, -1):
        if text[bit_index] == "1":
            if len(text) > 8:
                number = number + 2 ** (15 - bit_index)
            else:
                number = number + 2 ** (7 - bit_index)
    return number


def buffer_to_binary(buffer):
    text_binary = ""
    for ascii in buffer:
        text_binary = text_binary + get_binary(ascii)
    return text_binary


def binarystr_to_ascii_buffer(text):
    if (len(text) % 8) == 0:
        binary_buffer = []
        for index in range(7, len(text), 8):
            binary_buffer.append(get_str_from_binary(text[index - 7:index + 1]))
        return binary_buffer
    else:
        return []


def key_validation(key):
    if len(key) > 16:
        return key[0:17]
    else:
        while len(key) < 16:
            key = key + " "
        return key


def binary_plaintext_to_64bit_array(plain_text):
    binary_buffer = []
    for index in range(63, len(plain_text), 64):
        binary_buffer.append(plain_text[index - 63:index + 1])
    return binary_buffer


def key_schedule(key):
    b64_key = str_to_b64(key)
    b64_key = key_validation(b64_key)
    print(key, len(key))
    binary_key = buffer_to_binary(to_ascii_code(b64_key))
    print(binary_key, len(binary_key))
    keys = []
    ins = 1
    while len(keys) < 52:
        print("Round", ins)
        for index in range(15, len(binary_key), 16):
            print(binary_key[index - 15:index + 1])
            keys.append(binary_key[index - 15:index + 1])
        binary_key = binary_key[25:len(binary_key)] + binary_key[0:25]
        ins = ins + 1
    return keys


def function_XOR(entry, key):
    binary = ""
    for bit in range(0, 16):
        if entry[bit] != key[bit]:
            binary = binary + "1"
        else:
            binary = binary + "0"
    return binary


def module_2_16_plus_1(number):
    return number % ((2 ** 16) + 1)


def module_2_16(number):
    return number % (2 ** 16)


def function_multiply(entry, key):
    A = get_str_from_binary(entry)
    B = get_str_from_binary(key)
    if A == 0:
        A = 2 ** 16
    if B == 0:
        B = 2 ** 16
    result = module_2_16_plus_1(module_2_16_plus_1(A) * module_2_16_plus_1(B))
    return get_binary_16(result)


def function_addition(entry, key):
    A = get_str_from_binary(entry)
    B = get_str_from_binary(key)
    result = module_2_16(module_2_16(A) + module_2_16(B))
    return get_binary_16(result)


def cypher_round(entries, keys_round, round_number):
    keys_round = keys_round[round_number * 6:(round_number * 6) + 6]
    step_1 = function_multiply(entries[0], keys_round[0])
    print("step_1", entries[0], keys_round[0], step_1)
    step_2 = function_addition(entries[1], keys_round[1])
    print("step_2", entries[1], keys_round[1], step_2)
    step_3 = function_addition(entries[2], keys_round[2])
    print("step_3", entries[2], keys_round[2], step_3)
    step_4 = function_multiply(entries[3], keys_round[3])
    print("step_4", entries[3], keys_round[3], step_4)
    step_5 = function_XOR(step_1, step_3)
    print("step_5", step_1, step_3, step_5)
    step_6 = function_XOR(step_2, step_4)
    print("step_6", step_2, step_4, step_6)
    step_7 = function_multiply(step_5, keys_round[4])
    print("step_7", step_5, keys_round[4], step_7)
    step_8 = function_addition(step_6, step_7)
    print("step_8", step_6, step_7, step_8)
    step_9 = function_multiply(step_8, keys_round[5])
    print("step_9", step_8, keys_round[5], step_9)
    step_10 = function_addition(step_7, step_9)
    print("step_10", step_7, step_9, step_10)
    step_11 = function_XOR(step_1, step_9)
    print("step_11", step_1, step_9, step_11)
    step_12 = function_XOR(step_3, step_9)
    print("step_12", step_3, step_9, step_12)
    step_13 = function_XOR(step_2, step_10)
    print("step_13", step_2, step_10, step_13)
    step_14 = function_XOR(step_4, step_10)
    print("step_14", step_4, step_10, step_14)
    return [step_11, step_13, step_12, step_14]


def cypher_half_round(entries, keys):
    keys = keys[(6 * 8):(6 * 8 + 6)]
    step_1 = function_multiply(entries[0], keys[0])
    step_2 = function_addition(entries[1], keys[1])
    step_3 = function_addition(entries[2], keys[2])
    step_4 = function_multiply(entries[3], keys[3])
    return step_1 + step_2 + step_3 + step_4


def cypher_process(block, keys):
    entries = [block[0:16], block[16:32], block[32:48], block[48:64]]
    print(entries)
    for x in range(0, 8):
        entries = cypher_round(entries, keys, x)
        print("round ", (x + 1), entries)
    output = cypher_half_round(entries, keys)
    return output


def cypher_bit_block(block_array, keys):
    cypher_array = []
    for block in block_array:
        print("block  ", block)
        cypher_array.append(cypher_process(block, keys))
    return cypher_array


def encrypt(text, keys):
    text_b64 = str_to_b64(text)
    ascii_buffer = to_ascii_code(text_b64)
    binary_buffer = buffer_to_binary(ascii_buffer)
    bit64_array = binary_plaintext_to_64bit_array(binary_buffer)
    cypher_array = cypher_bit_block(bit64_array, keys)
    cypher_binary_text = ""
    for cypher_block in cypher_array:
        cypher_binary_text = cypher_binary_text + cypher_block
    ascii_cypher_buffer = binarystr_to_ascii_buffer(cypher_binary_text)
    cypher_text = to_string(ascii_cypher_buffer)
    return str_to_b64(cypher_text)


def euclides_algorithm(A, B):
    division = A // B
    module = A % B
    if module != 0:
        print(A, " = ", B, " * ", division, " + ", module)
        return euclides_algorithm(B, module)
    else:
        return B


def multiply_inverse(A):
    return (A ** 65535) % 65537


def additive_inverse(A):
    return 2 ** 16 - A


def prepare_encription_keys_to_decript(encription_keys):
    prepared_keys = []
    for key in encription_keys[48:52]:
        prepared_keys.append(key)
    for key in encription_keys[42:48]:
        prepared_keys.append(key)
    for key in encription_keys[36:42]:
        prepared_keys.append(key)
    for key in encription_keys[30:36]:
        prepared_keys.append(key)
    for key in encription_keys[24:30]:
        prepared_keys.append(key)
    for key in encription_keys[18:24]:
        prepared_keys.append(key)
    for key in encription_keys[12:18]:
        prepared_keys.append(key)
    for key in encription_keys[6:12]:
        prepared_keys.append(key)
    for key in encription_keys[0:6]:
        prepared_keys.append(key)
    return prepared_keys


def decription_keys_scheduling(encription_keys):
    encription_keys = encription_keys[0:52]
    decription_keys = []
    prepared_encription_keys = prepare_encription_keys_to_decript(encription_keys)
    decription_keys.append(get_binary_16(multiply_inverse(get_str_from_binary(prepared_encription_keys[0]))))
    decription_keys.append(get_binary_16(additive_inverse(get_str_from_binary(prepared_encription_keys[1]))))
    decription_keys.append(get_binary_16(additive_inverse(get_str_from_binary(prepared_encription_keys[2]))))
    print((get_str_from_binary(prepared_encription_keys[3])))
    decription_keys.append(get_binary_16(multiply_inverse(get_str_from_binary(prepared_encription_keys[3]))))
    decription_keys.append(prepared_encription_keys[8])
    decription_keys.append(prepared_encription_keys[9])
    prepared_encription_keys = prepared_encription_keys[4:len(prepared_encription_keys)]
    print(len(prepared_encription_keys))
    for key_index in range(0, 7):
        key_1 = get_binary_16(multiply_inverse(get_str_from_binary(prepared_encription_keys[key_index * 6])))
        key_2 = get_binary_16(additive_inverse(get_str_from_binary(prepared_encription_keys[(key_index * 6) + 1])))
        key_3 = get_binary_16(additive_inverse(get_str_from_binary(prepared_encription_keys[(key_index * 6) + 2])))
        key_4 = get_binary_16(multiply_inverse(get_str_from_binary(prepared_encription_keys[(key_index * 6) + 3])))
        key_5 = prepared_encription_keys[(key_index * 6) + 10]
        key_6 = prepared_encription_keys[(key_index * 6) + 11]

        decription_keys.append(key_1)
        decription_keys.append(key_2)
        decription_keys.append(key_3)
        decription_keys.append(key_4)
        decription_keys.append(key_5)
        decription_keys.append(key_6)

        # 48,49,50,51,     46,47,
    # half round
    decription_keys.append(get_binary_16(multiply_inverse(get_str_from_binary(prepared_encription_keys[42]))))
    decription_keys.append(get_binary_16(additive_inverse(get_str_from_binary(prepared_encription_keys[43]))))
    decription_keys.append(get_binary_16(additive_inverse(get_str_from_binary(prepared_encription_keys[44]))))
    decription_keys.append(get_binary_16(multiply_inverse(get_str_from_binary(prepared_encription_keys[45]))))
    # 0  42,43,44,45,     40,41, 5  0 * 6 = 00, +10 +11
    # 6  36,37,38,39,     34,35  11 1 * 6 = 06, +10 +11
    # 12 30,31,32,33,     28,29  17 2 * 6 = 12, +10 +11
    # 18 24,25,26,27,     22,23  23 3 * 6 = 18, +10 +11
    # 24 18,19,20,21,     16,17, 29 4 * 6 = 24, +10 +11
    # 30 12,13,14,15,     10,11, 35 5 * 6 = 30, +10 +11
    # 36 06,07,08,09,     04,05, 41 6 * 6 = 36, +10 +11
    # 42 00,01,02,03,            47 7 * 6 = 42, +10 +11
    return decription_keys


def decrypt(text, keys):
    text = b64_to_str(text)
    ascii_buffer = to_ascii_code(text)
    binary_buffer = buffer_to_binary(ascii_buffer)
    print("binary  ", binary_buffer)
    bit64_array = binary_plaintext_to_64bit_array(binary_buffer)
    print("bit array ", bit64_array)
    decrypted_array = cypher_bit_block(bit64_array, keys)
    decrypted_binary_text = ""
    for decrypted_block in decrypted_array:
        decrypted_binary_text = decrypted_binary_text + decrypted_block
    ascii_decrypted_buffer = binarystr_to_ascii_buffer(decrypted_binary_text)
    decrypted_text = to_string(ascii_decrypted_buffer)

    return b64_to_str(decrypted_text)


def idea_cypher():
    print("Insert text to be cypher")
    text = input()
    print("Insert password")
    password = input()
    keys = key_schedule(password)
    decription_keys = decription_keys_scheduling(keys)
    print("decript lent ", len(decription_keys))
    crypted = encrypt(text, keys)
    decripted = decrypt(crypted, decription_keys)
    print(crypted)
    print(decripted)


def test_keys(keys):
    keys = keys[0:28]
    test_keys = ["1101", "1100", "0110", "1111", "0011", "1111", "0101", "1001", "0001", "1011", "1100", "1111", "1101",
                 "0110", "0111", "0111", "1111", "0011", "1111", "0101", "1001", "1101", "1100", "0110", "1111", "1101",
                 "0110", "0111"]
    for i in range(0, 28):
        if keys[i] != test_keys[i]:
            return False
    return True


def test_encript(text):
    return text == "1011101101001011"


def test_decript(text):
    return text == "1001110010101100"


def test_decription_keys(keys):
    test_keys = ["1000", "0011", "1010", "0101", "1100", "0110", "1000", "1011", "0111", "0100", "1111", "0011", "0100",
                 "1010", "1001", "0101", "1100", "1111", "0111", "0111", "1111", "1110", "0011", "1111", "0100", "0100",
                 "1010", "1000"]
    for i in range(0, 28):
        if keys[i] != test_keys[i]:
            return False
    return True


idea_cypher()
