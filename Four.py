"""
Four by Christopher Scott
http://www.scottdchris.com/

In 7th grade my math teacher taught me a cool trick.
When you take the amount of letters in the textual representation of any number recursively,
you will always end up with four.

Makes use of my NumToWords implementation.
"""
import NumToWords

def calc(num):
	if (num == 4):
		return
	word = NumToWords.numToWords(num)
	newNum = 0
	for letters in word:
		if(letters!=' '):
			newNum += 1
	print '%i = %s (%i)' % (num, word, newNum)
	calc(newNum)
	
number = input('\nPlease enter a number: ')
print '\nFormat: Number = Word (Length of word)\n'
calc(number)
printTimes=3
while (printTimes>0):
	print '4 = four (4)'
	printTimes-=1
print "The length of four is always four!"