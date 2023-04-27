#Write a Python program that reads a text file named numbers.txt 
#that contains 20 integers. The program will create two other text file; 
#the first text file will be named even.txt that will contains all even numbers
#extracted from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers 
#extracted from the numbers.txt.

# change colors in output
yellow ="\033[1;33m"
light_blue ="\033[1;34m"
orange ="\033[4;32m"
white = "\033[1;37m"

# open numbers.txt (read), even.txt (append), odd.txt (append)
with open("numbers.txt") as number_file, open("even.txt","w") as even_num,open("odd.txt","w") as odd_num:
    # read numbers.txt each line
    for line in number_file:
        input_num = int(line)
        if input_num % 2 == 0:
            # if even append to files and print,
            even_num.write(str(input_num)+"\n")
            print(yellow + "Even number written:",input_num)
            
        else:
            # if odd append to files and print,
            odd_num.write(str(input_num)+"\n")
            print(light_blue + "Odd number written:",input_num)

print("\n"+ orange +"Done writing output to each files.")
#add enpty output to change the font color 
#so that it will not conflict with the other output
print(white)