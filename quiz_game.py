print("Welcome to my computer quiz!")

playing = input("Do you want to play a game?  ")

if playing.lower() != "yes":
	quit()
	

print("Let's play!")

score = 0

q1 = input("What does CPU stand for?  ")
if q1.lower() == "central processing unit":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")
		
q2 = input("What does GPU stand for?  ")
if q2.lower() == "graphics processing unit":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")
		
q3 = input("What does PSU stand for?  ")
if q3.lower() == "power supply unit":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")
		
q4 = input("What does RAM stand for?  ")
if q4.lower() == "random-access memory":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")
	

print("Your score is " + str(score) + "/4")
print("Your score is " + str((score / 4) * 100) + "%.")