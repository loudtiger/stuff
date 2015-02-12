#Write fibbonaci iteratively (bonus: use dynamic programming)
import sys

upTo = sys.argv[1]

sequence = []

nextValue = 1
while nextValue < int(upTo):
	if not sequence:
		sequence.append(nextValue)
	else:
		sequence.append(nextValue)
		nextValue = sequence[len(sequence)-1] + sequence[len(sequence)-2]
		
print sequence
