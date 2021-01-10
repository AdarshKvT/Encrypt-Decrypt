alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

nums = "0123456789"

sym = "!#$%&()*+"

enc_list = []

dec_list = []


while True:
	cmds = input("Encrypt a word(enc) Decrypt a word(dec) Quit(q):\n>>").lower()

	if cmds == "enc":
		word = input("Word to encrypt: ")
		key = int(input("A key: "))
		
		for letter in word:
			if letter in alpha:
				index = alpha.index(letter) + key
				if index >=26:
					index -= 26
				final = alpha[index]
				
			elif letter in alpha_up:
				index = alpha_up.index(letter) +key
				if index >=26:
					index -= 26
				final = alpha_up[index]
				
			elif letter in nums:
				index = nums.index(letter) +key
				if index >=26:
					index -= 26
					
				final = nums[index]
				
			elif letter in sym:
				index = sym.index(letter)+key
				if index >= 26:
					index -= 26
				
				final = sym[index]
				
			enc_list.append(final)
		
		enc = "".join(enc_list)
		print(f"Your word: {word} \nYour key: {key}\nEncrypted word: {enc}")
	
	elif cmds == "dec":
		word = input("Word to decrypt: ")
		key = int(input("A key (the key which you have used to encrypt must be used here) : "))
		
		for letter in word:
			if letter in alpha:
				index = alpha.index(letter)-key
				final = alpha[index]
				
			elif letter in alpha_up:
				index = alpha_up.index(letter)-key
				final = alpha_up[index]
				
			elif letter in nums:
				index = nums.index(letter)-key
				final = nums[index]
				
			elif letter in sym:
				index = sym.index(letter)-key
				final = sym[index]
				
			dec_list.append(final)
			
		dec = "".join(dec_list)
		
		print(f"Your word: {word} \nYour key: {key}\nDecrypted word: {dec}")
		
	elif cmds == "q":
			print("You quit")
			break
			
	else:
			print("Invalid character")
			
			
		


		

  

	
	