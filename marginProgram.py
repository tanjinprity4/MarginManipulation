import sys

def margin(leftMargin,rightMargin,contents, outFile):
  # Print a row of numbers upto 80 on top to observe margin manipulation.
  for i in range(8):
    for j in range(10):
      print (j, end = '')
      outFile.write(str(j))
  print()
  outFile.write('\n')
  
  # Print & save input contents with specified margin. 
  totalChar = 80
  rightAdjust = totalChar - rightMargin
  charCount = 0
  wordCount = 0
  words = contents.split()
  while wordCount < len(words):
    # Start new line after 80 characters.
    if charCount > 79:
      print()
      outFile.write('\n')
      charCount = 0
    
    # Enter whitespaces along the specified margins.
    elif (charCount < leftMargin) or (charCount > (rightAdjust - 1)):
      print(' ', end = '')
      outFile.write(' ')
      charCount += 1
    else:
      # Include as many words as can “fit” between the margins.
      if len(words[wordCount]) <= (rightAdjust - charCount - 1):
        print(words[wordCount], end = ' ')
        outFile.write(words[wordCount])
        outFile.write(' ')
        
        # Leaves 2 blanks between sentences in the output.
        if '.' in words[wordCount]:
          print(' ', end = '')
          outFile.write(' ')

        # Increment character and word counts after printing & writing each word.
        charCount = charCount + len(words[wordCount]) + 1
        wordCount += 1
      else:
        print()
        outFile.write('\n')
        charCount = 0
  print()
  outFile.write('\n\n\n')

def main():
  # Open and read input file.
  path = sys.argv[1]
  inFile = open(path, "r")
  if inFile.mode == 'r':
    contents =inFile.read()

  # Output file to save contents with specified margin.
  outFile = open("output.txt", "a+")
  outFile.write('Starting Program.\n')
  
  # Initialize margins.
  leftMargin = 80
  rightMargin = 80
  while (leftMargin + rightMargin > 80):
    print('The maximum input line is 80 characters long. Keep sum of left and right margin less than 80.')
    outFile.write('The maximum input line is 80 characters long. Keep sum of left and right margin less than 80.\n')
    leftInches = float(input('Enter positive left margin in inches: '))
    outFile.write('Enter positive left margin in inches: ' + str(leftInches) + '\n')
    rightInches = float(input('Enter positive right margin in inches: '))
    outFile.write('Enter positive right margin in inches: ' + str(rightInches) + '\n')
    
    # If any margin is negative, ask user to enter margins again.
    if (leftInches < 0) or (rightInches < 0):
      print('Margin can not be negative.')
      outFile.write('Margin can not be negative.\n')
      continue
    
    # 1 inch = 72 points = 6 characters (in 12 pt font).
    leftMargin = int(leftInches * 6)
    print('Left margin is ' + str(leftMargin) + ' characters long.')
    outFile.write('Left margin is ' + str(leftMargin) + ' characters long.\n')
    rightMargin = int(rightInches * 6)
    print('Right margin is ' + str(rightMargin) + ' characters long.')
    outFile.write('Right margin is ' + str(rightMargin) + ' characters long.\n')
  
  margin(leftMargin, rightMargin, contents, outFile)
  inFile.close()
  outFile.close()
  
main()