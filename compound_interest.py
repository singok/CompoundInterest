
# Compound Interest Calculator

print('Welcome to the Wolving compound interest calculator.')
print('This program calculates your potential returns when you invest with us.')

def call_interest(rate,principal,time): 
    interest = (rate*0.01) * (principal/time) 
    return interest 

fprincipal = float(input('What is the principal amount? '))
rate = float(input('What is the rate? '))
year = int(input('What is the number of years? ')) 
time = int(input('What is the number of times the interest is compounded per year? ')) 
print('Year       Period         Old Balance          Interest           New Balance')
print('-----------------------------------------------------------------------------')
i=0
j=0
k=1
principal = fprincipal
for i in range(year*time):
    i += 1
    j += 1
    if j == 1:
        print(str(k),end = ' '*(11 - len(str(k))))                                           
        print(str(i),end = ' '*(15 - len(str(i))))                                               
    else:
        print(' '*11 + str(i),end = ' '*(15 - len(str(i))))
    if j == time:
        j = 0 
        k += 1 
    principalStr = '{:.2f}'.format(principal) 
    print('£' + principalStr,end = ' '*(20 - len(principalStr)))
    interest = call_interest(rate,principal,time)
    interestStr = '{:.2f}'.format(interest)
    print('£' + interestStr,end = ' '*(18 - len(interestStr)))
    principal += interest 
    print('£' + '{:.2f}'.format(principal)) 
  
print('-----------------------------------------------------------------------------')
print('£{0:.2f} invested at {1:}% for {2:} years compounded {3:} times per year is: £{4:.2f}'.format(fprincipal,rate,year,time,principal))
