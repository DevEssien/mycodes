def gcd(numerator, denominator):
	divisor = numerator if numerator < denominator else denominator
	dividend = numerator if numerator > denominator else denominator
	
	rem = dividend % divisor
	
	while rem != 0:
		dividend, divisor = divisor, rem
		rem = dividend % divisor
		continue
	
	global gcD	
	gcD = divisor
	return gcD

    #Decimal to fraction conversion
decimal = float(input('enter decimal >>> '))
deciToStr = str(decimal)

dotIndex = deciToStr.index('.')
n = len(deciToStr[dotIndex+1:])

num, den = decimal * (10**n), 10**n
gcd(num, den)

print(f'{decimal} is {int(num/gcD)}/{int(den/gcD)} in fraction')
