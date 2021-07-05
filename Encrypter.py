
class Process():
    def makeAlphabet(self,keyAlphabet):
        alphabet = {"Numbers" : "0123456789",
"Special" : " ./;'[]<>?:@{}-=_+!\"$%^&*()`\\~#|",
"English" : "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
"Russian" : "яшертыуиопющэжьлкйчгфдсазхцвбнмёъЯШЕРТЫУИОПЮЩЭЖЬЛЙКЧГФДСАЗХЦВБНМЪЁ",
"Japanese Hirigana" : "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん",
"Japanese katakana" : "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン",
"Korean Hangul" : "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ",}
        tempList = []
        for x in alphabet:
            tempList.append(alphabet[x])
        alphabet = "".join(tempList)
        stringEnc = []
        for x in alphabet:
            letterID = alphabet.index(x) + keyAlphabet
            while letterID > len(alphabet)-1:
                letterID -= len(alphabet)
            stringEnc.append(alphabet[letterID]) 
        return "".join(stringEnc)
    def Encrypt(self,string,alphabet,Key):
        for x in range(0,int(Key[13:15])):
            stringEnc = []
            Temp = int(Key[6:10])
            for x in string:
                Temp += int(Key[10:12])
                letterID = alphabet.index(x) + Temp
                while letterID > len(alphabet)-1:
                    letterID -= len(alphabet)
                stringEnc.append(alphabet[letterID]) 
            string = "".join(stringEnc)
        return "".join(stringEnc)
    def Decrypt(self,string,alphabet,Key):
        for x in range(0,int(Key[13:15])):
            stringEnc = []
            Temp = int(Key[6:10])
            for x in string:
                Temp += int(Key[10:12])
                letterID = alphabet.index(x) - Temp
                while letterID < 0:
                    letterID += len(alphabet)
                stringEnc.append(alphabet[letterID]) 
            string = "".join(stringEnc)
        return "".join(stringEnc)
def InnitWrite(string):
    Key = "111111111111111"
    alphabet = Process.makeAlphabet(0,int(Key[1:3]))
    fullEnc = Process.Encrypt(0,string,alphabet,Key)
    return fullEnc
def InnitRead(string):
    Key = "111111111111111"
    alphabet = Process.makeAlphabet(0,int(Key[1:3]))
    fullDec = Process.Decrypt(0,string,alphabet,Key)
    return fullDec