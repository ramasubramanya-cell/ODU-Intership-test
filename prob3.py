#Write a big number calculator ( numbers are represented as strings to avoid number overflow ). 
#The calculator should at least do addition, subtraction, multiplication, and division. Additional points will be given for other operations.
import math
def findSum(str1, str2):#to calculate sum of two big numbers

    #checking is length of string 2 is greater  
    if len(str1)> len(str2):
        temp = str1
        str1 = str2
        str2 = temp

    str3 = "" #empty string to store result
   
    #calculate length of both string
    n1 = len(str1)
    n2 = len(str2)
    diff = n2 - n1
   
    carry = 0#initially zero

    for i in range(n1-1,-1,-1):#Traverse from end of both strings
        
        sum = ((ord(str1[i])-ord('0')) +
                   int((ord(str2[i+diff])-ord('0'))) + carry)
        str3 = str3+str(sum%10 )
        carry = sum//10
   
    for i in range(n2-n1-1,-1,-1):# Add remaining digits of str2[]
      
        sum = ((ord(str2[i])-ord('0'))+carry)
        str3 = str3+str(sum%10 )
        carry = sum//10

    if (carry):
        str3+str(carry+'0')# Add remaining carry

    str3 = str3[::-1] # reverse resultant string
   
    return str3

def isSmaller(str1, str2):
     
    # Calculate lengths of both string
    n1 = len(str1)
    n2 = len(str2)
 
    if (n1 < n2):
        return True
    if (n2 < n1):
        return False
 
    for i in range(n1):
        if (str1[i] < str2[i]):
            return True
        elif (str1[i] > str2[i]):
            return False
 
    return False
 
# Function for find difference of larger numbers
def findDiff(str1, str2):
 
    #checking if str1 is smaller
    if (isSmaller(str1, str2)):
        temp = str1
        str1 = str2
        str2 = temp
 
    str3 = ""#empty string to store result
 
    #Calculate length of both string
    n1 = len(str1)
    n2 = len(str2)
 
    #Reverse both of strings
    str1 = str1[::-1]
    str2 = str2[::-1]
 
    carry = 0
 
    # Run loop till small string length
    # and subtract digit of str1 to str2
    for i in range(n2):

        sub = ((ord(str1[i])-ord('0'))-(ord(str2[i])-ord('0'))-carry)
        # If subtraction is less then zero
        # we add then we add 10 into sub and
        # take carry as 1 for calculating next step
        if (sub < 0):
            sub = sub + 10
            carry = 1
        else:
            carry = 0
        str3 = str3+str(sub)
 
    # subtract remaining digits of larger number
    for i in range(n2, n1):
 
        sub = ((ord(str1[i])-ord('0')) - carry)
 
        # if the sub value is -ve, then make it positive
        if (sub < 0):
 
            sub = sub + 10
            carry = 1
 
        else:
            carry = 0
 
        str3 = str3+str(sub)
 
    #reverse resultant string
    str3 = str3[::-1]
 
    return str3

# This function multiplies two numbers
def multiply(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    if len1 == 0 or len2 == 0:
        return "0"
  
    # will keep the result number in vector
    # in reverse order
    result = [0] * (len1 + len2)
      
    # Below two indexes are used to 
    # find positions in result.
    i_n1 = 0
    i_n2 = 0
  
    # Go from right to left in num1
    for i in range(len1 - 1, -1, -1):
        carry = 0
        n1 = ord(num1[i]) - 48
  
        # To shift position to left after every
        # multiplication of a digit in num2
        i_n2 = 0
  
        # Go from right to left in num2
        for j in range(len2 - 1, -1, -1):
            
            # Take current digit of second number
            n2 = ord(num2[j]) - 48
          
            # Multiply with current digit of first number
            # and add result to previously stored result
            # at current position.
            summ = n1 * n2 + result[i_n1 + i_n2] + carry
  
            # Carry for next iteration
            carry = summ // 10
  
            # Store result
            result[i_n1 + i_n2] = summ % 10
  
            i_n2 += 1
  
            # store carry in next cell
        if (carry > 0):
            result[i_n1 + i_n2] += carry
  
            # To shift position to left after every
            # multiplication of a digit in num1.
        i_n1 += 1
          
        # print(result)
  
    # ignore '0's from the right
    i = len(result) - 1
    while (i >= 0 and result[i] == 0):
        i -= 1
  
    # If all were '0's - means either both or
    # one of num1 or num2 were '0'
    if (i == -1):
        return "0"
  
    # generate the result string
    s = ""
    while (i >= 0):
        s += chr(result[i] + 48)
        i -= 1
  
    return s

# This function divides two numbers
def longDivision(number, divisor): 
  
    # As result can be very large 
    # store it in string 
    ans = ""; 
      
    # Find prefix of number that 
    # is larger than divisor. 
    idx = 0; 
    temp = ord(number[idx]) - ord('0');
    while (temp < divisor):
        temp = (temp * 10 + ord(number[idx + 1]) -
                            ord('0'));
        idx += 1;
      
    idx += 1;
  
    # Repeatedly divide divisor with temp. 
    # After every division, update temp to 
    # include one more digit. 
    while ((len(number)) > idx): 
          
        # Store result in answer i.e. temp / divisor 
        ans += chr(math.floor(temp // divisor) + ord('0')); 
          
        # Take next digit of number
        temp = ((temp % divisor) * 10 + ord(number[idx]) -
                                        ord('0'));
        idx += 1;
  
    ans += chr(math.floor(temp // divisor) + ord('0'));
      
    # If divisor is greater than number 
    if (len(ans) == 0): 
        return "0"; 
      
    # else return ans 
    return ans; 

def multiplypow(x, res, res_size):
     
    # Initialize carry
    carry = 0
 
    # One by one multiply n with
    # individual digits of res[]
    for i in range(res_size):
        prod = res[i] * x + carry
 
        # Store last digit of
        # 'prod' in res[]
        res[i] = prod % 10
 
        # Put rest in carry
        carry = prod // 10
 
    # Put carry in res and
    # increase result size
    while (carry):
        res[res_size] = carry % 10
        carry = carry // 10
        res_size+=1
 
    return res_size
 
 
# This function finds power of a number x
MAX=100000
def power(x,n):
     
    # printing value "1" for power = 0
    if(n==0):
        print("1")
     
    res=[0 for i in range(MAX)]
    res_size = 0
    temp = x
 
    # Initialize result
    while (temp != 0):
        res[res_size] = temp % 10;
        res_size+=1
        temp = temp // 10
 
 
    # Multiply x n times
    # (x^n = x*x*x....n times)
    for i in range(2, n + 1):
        res_size = multiplypow(x, res, res_size)
 
    print(x , "^" , n , " = ",end="")
    for i in range(res_size - 1, -1, -1):
        print(res[i], end="")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power of a number")
while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        if choice == '1':
            print(num1, "+", num2, "=", findSum(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", findDiff(num1, num2))

        elif choice == '3':
            if((num1[0] == '-' or num2[0] == '-') and (num1[0] != '-' or num2[0] != '-')):
                print("-", end = '')
            if(num1[0] == '-' and num2[0] != '-'):
                num1 = num1[1:]
            elif(num1[0] != '-' and num2[0] == '-'):
                num2 = num2[1:]
            elif(num1[0] == '-' and num2[0] == '-'):
                num1 = num1[1:]
                num2 = num2[1:]

            print(multiply(num1, num2))

        elif choice == '4':
            print(longDivision(num1, int(num2)))

        elif choice == '5':
            print(power(int(num1),int(num2)))
        break
    else:
        print("Invalid Input")
