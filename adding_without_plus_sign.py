def add(a, b):
	if a!=b:
		return (a*a-b*b)/(a-b)
	else:
		return 2*b


def main():
	a = int(input("Enter the 1st number : "))
	b = int(input("Enter the 2nd number : "))
	print(f"Sum of {a} + {b} is ", int(add(a,b)))


main()
