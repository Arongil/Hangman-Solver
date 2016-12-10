# This will contain the function that will determine the, statistically, best next letter to pick, for the given word and known letters.

# TODO: test if guessing vowels until one is found is more or less efficient than guessing "e", then running statistical analysis on the new subset created, to continue the guessing process.

from random import randint

# Change this to false to manually input if the guess is correct, and if so where, and to true for the computer to automatically do this for you.
automatic = True

# Change to match the current word length.
wordLength = 5
# This list will reflect everything we know about the word so far.
knownLetters = []
# This list will contain all letters not in the word.
knownNonLetters = []

vowels = ["e", "a", "o", "i", "u", "y"]
currentVowel = 0

def nextLetter():
  # If we know nothing about the word, we will guess vowels, until we find one.
  if len(knownLetters) == 0:
    global currentVowel
    currentVowel += 1
    return vowels[currentVowel - 1]
  
  # We now know at least one letter of the word. Our first step is to create a subset of the total words that only contains words that match our current knowledge of the word: length, knownLetters, and knownNonLetters.
  createSubset()
  
  # Now that we have a subset of the words to work with, that match our current knowledge of the word, we can run a statistcal analysis of the words to find the most highly occuring letter, and guess that next!
  # First we create a list of all the letters occurances, and set everything to 0.
  letterOccurances = [0 for i in xrange(26)]
  for word in words:
    for letter in word:
      # Each letter will add one to it's corresponding array index. Ord(char) returns that character's ASCII value. We substract 97, assuming all characters are lowercase, to find the index for each character. Chr(number) returns the ASCII value for that number.
      letterOccurances[ord(letter) - 97] += 1
  
  # Now we will find the most commonly occuring letter, and guess that.
  currentHighest = 0
  for letter in xrange(1, len(letterOccurances)):
    if letterOccurances[letter] > letterOccurances[currentHighest]:
      currentHighest = letter
  
  # We add 97 to currentHighest to revert currentHighest from being an index to the letterOccurances array, to an ASCII value.
  return chr(currentHighest + 97)

def createSubset(doneWordLength = True):
  subset = []
  # To create a subset of all words, we first need to check if we have already done the original wordLength check.
  
  if not doneWordLength:
    # Run through the words array, taking only words of length wordLength.
    for word in words:
      if len(word) == wordLength:
        subset.append(word)
    return subset
  
  # If we have checked wordLength already, we need to check for knownLetters and knownNonLetters. If a word contains any knownNonLetters, it's immediately disqualified. If not, we need to check for knownLetters. A word has to contain knownLetters in the exact position we know they are.
  for word in words:
    # We set disqualified to True if we know a word is wrong. If a word makes it to the end of the check without disqualification, it makes the new subset.
    disqualified = False
    # First we'll check for if the word contains any knownNonLetters. If so, it isn't added.
    for letter in word:
      for nonLetter in knownNonLetters:
        if letter == nonLetter:
          disqualified = True
          break
      if disqualified:
        break
    # We check if it has been disqualified already throughout the process to avoid unnecessary calculations. While rather pointless for only 1,000 words, this will make a world of difference for 300,000 words.
    if disqualified:
      break
    # Now that the word has passes the nonLetter phase, we see if it will contain the letters we know about, in the exact correct places.
    for word in words:
      for knownLetter in knownLetters:
        # We check each knownLetter, to see if there is the correct corresponding letter in the word. If not, it's disqualified! knownLetter is an array of arrays that follow the format [letter, positionInWord]. For each knownLetter we check, we find the position of that knownLetter, and find the word's letter at that position (word[knownLetter[1]]), and compare it to the letter we know should be there (knownLetter[0]).
        
        if word[knownLetter[1]] != knownLetter[0]:
          disqualified = True
          break
    # We've now completed the full test. If the word was disqualified, it isn't added. Otherwise, it is!
    if disqualified:
      break
    subset.append(word)
  
  return subset

# The nextLetter() function will slowly fill out this list.
wordSlots = ["" for i in xrange(wordLength)]

def guessWord():
  foundWord = False
  
  # We will create one original subset that will contain all the words of the given wordLength.
  createSubset(False)
  while not foundWord:
    nextGuess = nextLetter()
    print "'" + nextGuess + "' is the guess for the next letter."
    if automatic:
      pass
    else:
      correct = raw_input("Was the letter correct? [y/n]")
      if correct == "y":
        occurances = int(raw_input("How many times did it occur? [integer]"))
        for i in xrange(occurances):
          position = int(raw_input("Where in the word was the letter ('r' in 'word' is at '3', for example)? [integer]"))
          # knownLetters is made up of arrays, with the 0th element as the letter, and the first as position.
          knownLetters.append([nextGuess, position])
          wordSlots[position - 1] = nextGuess
      else:
        # knownNonLetters is just an array of letters that we have checked, that aren't in the word.
        knownNonLetters.append(nextGuess)

      # If we know the word, return.
      if len(knownLetters) == wordLength:
        foundWord = True

  print "\nCode Complete."
  return None


# List of all of the words given. Here a simple online python script I wrote to convert a .txt file into an array: https://trinket.io/library/trinkets/9252730ed1
words = ["the","of","to","and","a","in","is","it","you","that","he","was","for","on","are","with","as","I","his","they","be","at","one","have","this","from","or","had","by","hot","word","but","what","some","we","can","out","other","were","all","there","when","up","use","your","how","said","an","each","she","which","do","their","time","if","will","way","about","many","then","them","write","would","like","so","these","her","long","make","thing","see","him","two","has","look","more","day","could","go","come","did","number","sound","no","most","people","my","over","know","water","than","call","first","who","may","down","side","been","now","find","any","new","work","part","take","get","place","made","live","where","after","back","little","only","round","man","year","came","show","every","good","me","give","our","under","name","very","through","just","form","sentence","great","think","say","help","low","line","differ","turn","cause","much","mean","before","move","right","boy","old","too","same","tell","does","set","three","want","air","well","also","play","small","end","put","home","read","hand","port","large","spell","add","even","land","here","must","big","high","such","follow","act","why","ask","men","change","went","light","kind","off","need","house","picture","try","us","again","animal","point","mother","world","near","build","self","earth","father","head","stand","own","page","should","country","found","answer","school","grow","study","still","learn","plant","cover","food","sun","four","between","state","keep","eye","never","last","let","thought","city","tree","cross","farm","hard","start","might","story","saw","far","sea","draw","left","late","run","don't","while","press","close","night","real","life","few","north","open","seem","together","next","white","children","begin","got","walk","example","ease","paper","group","always","music","those","both","mark","often","letter","until","mile","river","car","feet","care","second","book","carry","took","science","eat","room","friend","began","idea","fish","mountain","stop","once","base","hear","horse","cut","sure","watch","color","face","wood","main","enough","plain","girl","usual","young","ready","above","ever","red","list","though","feel","talk","bird","soon","body","dog","family","direct","pose","leave","song","measure","door","product","black","short","numeral","class","wind","question","happen","complete","ship","area","half","rock","order","fire","south","problem","piece","told","knew","pass","since","top","whole","king","space","heard","best","hour","better","true","during","hundred","five","remember","step","early","hold","west","ground","interest","reach","fast","verb","sing","listen","six","table","travel","less","morning","ten","simple","several","vowel","toward","war","lay","against","pattern","slow","center","love","person","money","serve","appear","road","map","rain","rule","govern","pull","cold","notice","voice","unit","power","town","fine","certain","fly","fall","lead","cry","dark","machine","note","wait","plan","figure","star","box","noun","field","rest","correct","able","pound","done","beauty","drive","stood","contain","front","teach","week","final","gave","green","oh","quick","develop","ocean","warm","free","minute","strong","special","mind","behind","clear","tail","produce","fact","street","inch","multiply","nothing","course","stay","wheel","full","force","blue","object","decide","surface","deep","moon","island","foot","system","busy","test","record","boat","common","gold","possible","plane","stead","dry","wonder","laugh","thousand","ago","ran","check","game","shape","equate","hot","miss","brought","heat","snow","tire","bring","yes","distant","fill","east","paint","language","among","grand","ball","yet","wave","drop","heart","am","present","heavy","dance","engine","position","arm","wide","sail","material","size","vary","settle","speak","weight","general","ice","matter","circle","pair","include","divide","syllable","felt","perhaps","pick","sudden","count","square","reason","length","represent","art","subject","region","energy","hunt","probable","bed","brother","egg","ride","cell","believe","fraction","forest","sit","race","window","store","summer","train","sleep","prove","lone","leg","exercise","wall","catch","mount","wish","sky","board","joy","winter","sat","written","wild","instrument","kept","glass","grass","cow","job","edge","sign","visit","past","soft","fun","bright","gas","weather","month","million","bear","finish","happy","hope","flower","clothe","strange","gone","jump","baby","eight","village","meet","root","buy","raise","solve","metal","whether","push","seven","paragraph","third","shall","held","hair","describe","cook","floor","either","result","burn","hill","safe","cat","century","consider","type","law","bit","coast","copy","phrase","silent","tall","sand","soil","roll","temperature","finger","industry","value","fight","lie","beat","excite","natural","view","sense","ear","else","quite","broke","case","middle","kill","son","lake","moment","scale","loud","spring","observe","child","straight","consonant","nation","dictionary","milk","speed","method","organ","pay","age","section","dress","cloud","surprise","quiet","stone","tiny","climb","cool","design","poor","lot","experiment","bottom","key","iron","single","stick","flat","twenty","skin","smile","crease","hole","trade","melody","trip","office","receive","row","mouth","exact","symbol","die","least","trouble","shout","except","wrote","seed","tone","join","suggest","clean","break","lady","yard","rise","bad","blow","oil","blood","touch","grew","cent","mix","team","wire","cost","lost","brown","wear","garden","equal","sent","choose","fell","fit","flow","fair","bank","collect","save","control","decimal","gentle","woman","captain","practice","separate","difficult","doctor","please","protect","noon","whose","locate","ring","character","insect","caught","period","indicate","radio","spoke","atom","human","history","effect","electric","expect","crop","modern","element","hit","student","corner","party","supply","bone","rail","imagine","provide","agree","thus","capital","won't","chair","danger","fruit","rich","thick","soldier","process","operate","guess","necessary","sharp","wing","create","neighbor","wash","bat","rather","crowd","corn","compare","poem","string","bell","depend","meat","rub","tube","famous","dollar","stream","fear","sight","thin","triangle","planet","hurry","chief","colony","clock","mine","tie","enter","major","fresh","search","send","yellow","gun","allow","print","dead","spot","desert","suit","current","lift","rose","continue","block","chart","hat","sell","success","company","subtract","event","particular","deal","swim","term","opposite","wife","shoe","shoulder","spread","arrange","camp","invent","cotton","born","determine","quart","nine","truck","noise","level","chance","gather","shop","stretch","throw","shine","property","column","molecule","select","wrong","gray","repeat","require","broad","prepare","salt","nose","plural","anger","claim","continent","oxygen","sugar","death","pretty","skill","women","season","solution","magnet","silver","thank","branch","match","suffix","especially","fig","afraid","huge","sister","steel","discuss","forward","similar","guide","experience","score","apple","bought","led","pitch","coat","mass","card","band","rope","slip","win","dream","evening","condition","feed","tool","total","basic","smell","valley","nor","double","seat","arrive","master","track","parent","shore","division","sheet","substance","favor","connect","post","spend","chord","fat","glad","original","share","station","dad","bread","charge","proper","bar","offer","segment","slave","duck","instant","market","degree","populate","chick","dear","enemy","reply","drink","occur","support","speech","nature","range","steam","motion","path","liquid","log","meant","quotient","teeth","shell","neck"]

word = words[randint(0, len(words) - 1)]
print "The word is '" + word + "'; the computer does not know this.\n"

guessWord()
