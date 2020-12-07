#MorseCodeByJosué

code = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'..-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..'
}

#MorseCipherAlgorithmByJosué
def morseCipher(message):
  low = message.lower()
  print("The message  to cipher is: {}".format(low))
  finalmessage=''
  for i in low:
    if i == ' ':
      finalmessage +=  ' '
    else:
      finalmessage += code[i] + ' '
  return finalmessage



#MorseDecoderAlgorithmByJosué
def morseDecoder(coded):
  print("Morse code to decode is: {}".format(coded))
  a = []
  morseMessage = ''
  letter = ''
  if coded == '..--' or coded == '.-.-' or coded == '---.' or coded == '----':
    print("Characters not supported")
  else:  
    for j in coded:
        if j != '' :
          k = 0
          letter += coded            
        else:
            k += 1
            if k == 2:
              morseMessage += ''
            else:
              morseMessage +=  a(code.keys())[a(code.values()).index(letter)]
              letter = ''
  return morseMessage




#RunFunction
def run():
  mess = "josue"
  final1 = morseCipher(mess)
  print("Cipher message: {}".format(final1))
  mess2 = "."
  final2 = morseDecoder(mess2)
  print("Decoded message : {}".format(final2))


run()


