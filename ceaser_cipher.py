alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
restart = 'yes'
while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction =='encode':
        text = input("type your message:\n").lower()
        text1 = ""
        shift = int(input("Type the shift number:\n"))
        print(alphabet)
        for i in range(shift):
            alphabet.append(alphabet[i])
        for i in range(shift):
            del alphabet[0]
        print(alphabet)
        index = []
        for letter in text:
            index.append(alphabet1.index(letter))
        print(index)
        for i in index:
            i2=int(i)
            text1+=alphabet[i2]
        print(f"Here's the encoded result: {text1}")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    else:
        text = input("type your message:\n").lower()
        text1 = ""
        shift = int(input("Type the shift number:\n"))
        # for i in range(shift):
        #     alphabet.append(alphabet[i])
        # for i in range(shift):
        #     del alphabet[0]
        index = []
        for letter in text:
            index.append(alphabet.index(letter))
        for i in index:
            i2=int(i)
            text1+=alphabet1[i2]
        print(f"Here's the decoded result: {text1}")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")