

num_scores = int(input("Enter number of scores here:"));
score = [0]*num_scores;
for i in range (len(score)):
	score[i] = int(input("enter scores:"));
print(score);
for i in range (len(score)):
	print(score[i]);


num2 = int(input("enter your extra number here:"));
for i in range (len(score)):
	if(num2 != score[i]):
		replacement = int(input("do you want to replace the number?(1 = yes, 0= no)"));
		if (replacement == 1):
			score[i] = num2;
for i in range(len(score)):
	print(score[i]);	
	
