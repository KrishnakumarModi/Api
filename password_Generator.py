import random
import string

def generate_password(number_Alpha, number_Sym, number_Num):
    
    alpha= random.choices(string.ascii_letters, k=number_Alpha)
    Sym = random.choices(string.punctuation, k=number_Sym)
    num = random.choices(string.digits, k=number_Num)
    

    password_Alpha=alpha
    password_Sym=Sym
    password_Num=num
    
    random.shuffle(password_Alpha)
    random.shuffle(password_Sym)
    random.shuffle(password_Num)
    
    password_chars=password_Alpha +password_Sym +password_Num
    
    password = "".join(password_chars)
    
    return password

def check_valid(prompt):
    while True:
        try:
            value=int(input(prompt))
            if (value < 0):
                print("Please enter a Non Negative integer.")
            if (value !=int(value)):
                print("Please enter a integer .")
            else:
                return value
        except ValueError :
            print("Entered a non-Integer value, Please enter integer value")

def main():
    number_Alpha = check_valid("Number of alphabets you want in your password:\n")
    number_Sym = check_valid("Number of symbols you want in your password:\n")
    number_Num = check_valid("Number of numbers you want in your password:\n")

    password = generate_password(number_Alpha, number_Sym, number_Num)
    if (password):
       
        print("Generated password:\n", password)
       
    else:
        print("error")

        
if __name__=="__main__":
    main()