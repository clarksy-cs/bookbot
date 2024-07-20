chars = {
    "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0,
    "i" : 0, "j" : 0, "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0,
    "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0,
    "y" : 0, "z" : 0
}

filename = "books/frankenstein.txt"

def main():

    with open(filename) as f:           # open file
        file_contents = f.read()        # read contents
        words = file_contents.split()   # split string into words
        word_count = len(words)

        # count characters of each word
        for eachword in words:        
            count_chars(eachword)

        # sort dictionary by value in descending order
        sortedchars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

        # print results
        print(f"--- begin report of {filename} ---\n")
        print(f"{word_count} words found in the document\n")
        for key, item in sortedchars.items():
            print(f"the \'{key}\' character was found {item} times")
        print("\n--- end report ---")

# count each character and update dictionary count values
def count_chars(word):
    target = word.lower()
    for char in target:
        if char in chars:
            chars[char] += 1

main()