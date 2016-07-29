def r_telephone_words(num, pos, word):
    if pos == len(num):
        print word
        return
    for i in lookup[num[pos]]:
        r_telephone_words(num, pos+1, word+i)

def telephone_words(num):
    r_telephone_words(num, 0, "")
    
if __name__ == "__main__":
    lookup = {'1': "1",
          '2': "ABC",
          '3': "DEF",
          '4': "GHI",
          '5': "JKL",
          '6': "MNO",
          '7': "PRS",
          '8': "TUV",
          '9': "WXY",
          '0': "0"}
    telephone_words("0231")
