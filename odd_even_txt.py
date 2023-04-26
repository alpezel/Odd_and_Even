#Write a Python program that reads a text file named numbers.txt 
#that contains 20 integers. The program will create two other text file; 
#the first text file will be named even.txt that will contains all even numbers
#extracted from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers 
#extracted from the numbers.txt.

# open numbers.txt (read), even.txt (append), odd.txt (append)
with open("numbers.txt") as number_file, open("even.txt","a") as even_num,open("odd.txt","a") as odd_num:
    # read numbers.txt each line
    for line in number_file:
        input_num = int(line)
        if input_num % 2 == 0:
            print("Even number written:",input_num)
        else:
            print("Odd number written:",input_num)
