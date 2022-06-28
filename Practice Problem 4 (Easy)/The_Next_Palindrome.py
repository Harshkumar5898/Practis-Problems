try:
    no = int(input(" - Enter the total number of test - \n"))
    list = []
    for i in range(no):
        a = int(input("Enter a number of which you want to find next palindrome : "))
        list.append(a)

except Exception as e:
    print(f"There is an error [{e}]")
else:
    def reverse(num):
        rev = 0
        while num:
            dig = num % 10
            rev = rev * 10 + dig
            num = num//10
        return rev

    for i in list:
        temp = i
        if i == reverse(i):
            print(f"your number {i} is already a palindeome")

        else:
            while True:
                temp += 1
                if temp == reverse(temp):
                    print(f"Next palindrome for {i} is {temp}")
                    break
