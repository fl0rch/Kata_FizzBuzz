
if __name__ == '__main__':
    for i in range(1, 101):
        x = str(i)
        if '3' in x and '5' in x:
            print('FizzBuzz')
        elif '3' in x:
            print('Fizz')
        elif '5' in x:
            print('Buzz')
        else:
            print(x)
