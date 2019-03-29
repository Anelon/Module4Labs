def convert(word):
  s = ""
  for c in word:
    if c <> " " and c <> "-": s += "_"
    else: s += c
  return s

def printBoard(word, guesses):
  print("Word so far:")
  soFar = ""
  for c in word:
    soFar += (c + " ")
  printNow(soFar)
  printNow("Incorrect guesses:")
  if len(guesses): printNow(guesses)
  printNow("You have used " + str(len(guesses)) + " of six guesses\n")
    

def hangman():
  printNow("Welcome to Hangman.")
  printNow("To guess make a guess enter a letter.")
  printNow("But you only get 6 guesses to get the whole word.")
  printNow("Good luck!")
  win = True
  word = "Hello World"
  guesses = ""
  curr = convert(word)
  while word <> curr:
    printBoard(curr, guesses)
    guess = requestString("Please make a guess.")
    if type(guess) is str:
      for g in guess:
        printNow(g)
        tempWord = word
        inWord = False
        for i in range(0, len(word)):
          if word[i].upper() == g.upper(): 
            temp = list(curr)
            temp[i] = word[i]
            curr = "".join(temp)
            inWord = True
        if not inWord: guesses += g
    else: print("Please make a real guess")
    if len(guesses) >= 6: 
      win = False
      break
  if win: print("You Win!")
  else: print("You Loose!")

