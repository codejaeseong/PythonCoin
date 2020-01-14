import random
import hashlib

WORD = 'ironcoin'  
WORD = hashlib.sha256(WORD.encode())
WORD = WORD.hexdigest()  # make genesis hash

SEED = random.randrange(0,10) # random number 0 ~ 10
SEED = str(SEED)

GENESIS = WORD + SEED     
GENESIS = hashlib.sha256(GENESIS.encode())
GENESIS = GENESIS.hexdigest()

i = 0
while True:   # loop to verify end
	
	num = i
	num = str(num)  # change type int to string

	guess = WORD + num
	guess = hashlib.sha256(guess.encode())
	guess = guess.hexdigest()

	if guess == GENESIS:    # if guess hash == GENESIS, mining correct
		print('Mining Success!')
		break
	else:
		i=i+1  # if answer is wong, try another SEED
