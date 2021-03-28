#Question: For a given array of elements find the greatest possible number from all the possible combinations  

#input number of elements
#append the elements to a list
#sort the list in descending order, so that the maximum and minimum digit can be found
#iterate across loop and place maximum digit at highest position and minimum digit at lowest position
lstarr = [] #python does not have anything specific called arrays, so used lists
n = int(input("Enter the number of digit: "))#accept number of digits
for i in range(0,n):#appending elements to list
    ele = int(input())
    lstarr.append(ele)

def findMaxNum(lstarr,n):
    lstarr.sort(reverse = True)#sorting list in Descending order
    num = lstarr[0]

    for i in range(1,n):
        num = num * 10 + lstarr[i]#adding max digit to highest place
    
    return num

print(findMaxNum(lstarr,n))
