num_scores = int(input("Enter number of scores here:"));
score = [0]*num_scores;
for i in range (len(score)):
	score[i] = float(input("enter scores:"));
print(score);
for i in range (len(score)):
	print(score[i]);
average = sum(score)//(len(score));
print("your average  is " +str(average));

