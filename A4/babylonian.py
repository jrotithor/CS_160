num = input("enter number here: ");
guess = int(num)/2;
for x in range (0, int(num)*2):
	r = int(num)/guess;
	guess =(guess + r)/2;
	x+=1;

	
print(guess);
print(int(num)**.5);

