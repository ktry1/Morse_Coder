class Decoder:
    def __init__(self):
        self.ciphered_text=None
        self.deciphered_text=None
        self.letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.',
                      '?', '/', '-', '(', ')']
        self.symbols=['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                      '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
                      '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----',
                      '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']

    def cipher(self,text):
        self.deciphered_text=text
        self.ciphered_text=""
        for key in self.deciphered_text:
            if key==" ":
                self.ciphered_text += " "
            elif key.upper() in self.letters:
                index=self.letters.index(key.upper())
                self.ciphered_text=self.ciphered_text+" " + self.symbols[index]
        return self.ciphered_text

    def decipher(self,text):
        user_input=text
        self.ciphered_text = user_input.split("  ")
        self.deciphered_text=""
        for word in self.ciphered_text:
            separated_word=word.split()
            for key in separated_word:
                if key in self.symbols:
                    index = self.symbols.index(key)
                    self.deciphered_text=self.deciphered_text + self.letters[index]
            self.deciphered_text=self.deciphered_text+" "
        return self.deciphered_text

class Butler:
    def __init__(self):
        pass
    def direct(self,text,choice,*args):
        if choice=="Cipher":
            return args[0](text)
        elif choice=="Decipher":
            return args[1](text)
