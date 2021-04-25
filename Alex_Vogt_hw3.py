def error_handling(num):
	while(num < 0):
		print("Please input a positive integer as a year.")
		num = int(input("Enter a year: "))
	return num

print('\nWelcome to HW1!')

num = int(input("Enter a year: "))
leapYear = 0

num = error_handling(num)


if (num % 4) == 0:
	leapYear = 1
	if (num % 100) == 0:
		leapYear = 0
		if (num % 400) == 0:
			leapYear = 1

if (leapYear == 0):
	print(num, "is not a leap year.\n")

if (leapYear == 1):
	print(num, "is a leap year.\n")