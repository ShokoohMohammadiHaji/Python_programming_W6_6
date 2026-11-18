
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def collectPlainText():
    print("Collecting plain text rows for ciphering.")

    content = ""
    plainText = input("Insert row(empty stops): ")

    while plainText != "":
        content += plainText + "\n"
        plainText = input("Insert row(empty stops): ")

    return content


def shiftCharacter(char, alphabet):
    index = alphabet.index(char)
    return alphabet[(index + 13) % 26]


def rot13(content):
    cipheredText = ""

    for i in range(len(content)):
        char = content[i]

        if char in LOWER_ALPHABETS:
            cipheredText += shiftCharacter(char, LOWER_ALPHABETS)

        elif char in UPPER_ALPHABETS:
            cipheredText += shiftCharacter(char, UPPER_ALPHABETS)

        else:
            cipheredText += char

    return cipheredText


def cipher(content):
    return rot13(content)


def writeFile(filename, content):
    targetFile = open(filename, "w", encoding="UTF-8")
    targetFile.write(content)
    targetFile.close()


def saveFile(content):
    fileSaveName = input("Insert filename to save: ")

    if fileSaveName != "":
        writeFile(fileSaveName, content)
        print("Ciphered text saved!")

    else:
        print("File name not defined.")
        print("Aborting save operation.")

    return None


def main():
    print("Program starting.\n")

    file = collectPlainText()

    cipherFile = cipher(file)

    print("\n#### Ciphered text ####")

    print(cipherFile)

    saveFile(cipherFile)

    print("Program ending.")


if __name__ == "__main__":
    main()
