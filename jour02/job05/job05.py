def fizz_buzz(num):
    string = ''
    if num % 3==0: string +='Fizz' 
    if num % 5==0: string +='Buzz'
    return string if string else num
if __name__ == "__main__":

    for n in range(1, 100+1):
        print(fizz_buzz(n))