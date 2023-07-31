def read_labels_translate():
    from keytotext import pipeline
    with open('/home/tester/finalProject/translated_content.txt', 'r') as f:
        lines = f.readlines()

    words = []
    for line in lines:  # exclude last line
        words.extend(line.split())

    print("Key Words: " + str(words))
    nlp = pipeline("k2t-new")
    sentence = nlp(words)
    message = f"{sentence} | Key words: {str(words)}"
    print(message)
    return message

if __name__ == "__main__":
    read_labels_translate()
