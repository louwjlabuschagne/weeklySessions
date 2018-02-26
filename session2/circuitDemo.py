#define the function
def calcCurrent(V,R):
	I = V/R
	return(I)

#get input from user
V_input = input("V?")
R_input = input("R?")

#calculate the current using the calcCurrent fucntion
I_result = calcCurrent(float(V_input), float(R_input))

#print the results
print(str(I_result)+"A")
