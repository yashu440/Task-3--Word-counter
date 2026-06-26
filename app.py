def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total words: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found!")

filename = input("Enter file name: ")
count_words(filename)