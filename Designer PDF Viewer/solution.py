import os


def designerPdfViewer(h, word):
    max_high = 0
    for char in word:
        char_index_in_h = ord(char) - 97
        high_of_char = h[char_index_in_h]
        if high_of_char > max_high:
            max_high = high_of_char
    return max_high * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
