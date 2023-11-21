# yo I did it
# I'll make it better at some point
# see I was lazy and then I needed a Ceasar decrypter for CyberStart
# ngl I would feel mildly fancy if this weren't Python
# but there's a built-in Python IDE you need to use rip lol

def caesar(key, message, mode):
  m = message.upper()
  a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  output = ""

  for l in m: # letter in message
    if l in a: # if letter is in the alphabet
      match mode:
        case "encrypt": 
          ind = (a.find(l) + key) % len(a) # shift + to find ciphertext letter
        case "decrypt":
          ind = (a.find(l) - key) % len(a) # shift - to find original letter
        case _:
          print("invalid mode")
      output = output + a[ind]
    else: # if it's a symbol, keep it
      output = output + l

  return output
  
