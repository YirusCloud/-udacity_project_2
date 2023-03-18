import sys

def huffman_encoding(data):
    temp_dict = {} 
    _tree = {}  
    temp_str = '1'  
    encoded_str = "" 

    for char in data:
        temp_dict[char] = temp_dict.get(char, 0) + 1

    for num in sorted(temp_dict.items(), key=lambda x: x[1]):
        _tree[num[0]] = temp_str
        temp_str = '0' + temp_str

    for d in data:
        encoded_str += _tree[d]

    return encoded_str, _tree

def huffman_decoding(data, tree):
    temp_dict = {} 
    temp_str, decoded_str = "", "" 

    for c in tree:
        temp_dict[tree[c]] = c

    for d in data:
        if d == '1':
            decoded_str += temp_dict[temp_str + d]
            temp_str = ''
        else:
            temp_str += d

    return decoded_str


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))