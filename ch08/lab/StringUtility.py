class StringUtility:
  def __init__(self, string):
    self.string = string
    '''
    intitializes class
    string: (var) instance variable
    '''

  def __str__(self):
    return self.string
    '''
    returns string
    '''
  def vowels(self):
    '''
    self: (var) self.string is checked for vowels
    '''
    count = 0
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for alphabet in self.string:
      if alphabet in vowels:
        count = count + 1
      if count >= 5:
        return "many"
      else:
        count = count
    return str(count)
  def bothEnds(self):
    '''
    self: (var) adds first 2 and last 2 letters together from self .string
    '''
    if len(self.string)>2:
      return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    else:
      return ""
  def fixStart(self):
    '''
    self: (var) replaces letters in self.string and returns a new
    string
    '''
    if len(self.string)>1:
      newstr = self.string[1:]
      newstr = newstr.replace(self.string[0],"*" )
      newstr2 = self.string[0] + newstr
      return newstr2
    else:
      return self.string
  def asciiSum(self):
    '''
    self: (var) return sum of ascii numbers from self.string
    '''
    return sum(map(ord,self.string))
    
  def cipher(self):
    '''
    self: (var) create a new string from self.string
    '''
    Message = ""
    capalphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    loweralp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(0,len(self.string)):
      letternumber = ord(self.string[i])
      length = len(self.string)
      if length + letternumber>90 and (self.string[i]) in capalphabet_list :
        new = letternumber + length -26
        ztoa = chr(new)
        Message+=(ztoa)
      elif (length +letternumber) <= 148 and (self.string[i]) in loweralp:
        new = letternumber + length -26
        ztoa = chr(new)
        Message+=(ztoa)
      elif (length + letternumber) > 148 and (self.string[i]) in loweralp:
        new = letternumber + length - 52
        ztoa = chr(new)
        Message+=(ztoa)
      elif " " == self.string[i]:
        new = letternumber
        ztoa = chr(new)
        Message+=(ztoa)

      else:
        Message+=chr(letternumber+length)
    return Message
