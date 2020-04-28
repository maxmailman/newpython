def interact():
    print('Hello stream world!')
    while True:
        try:
            reoly = input('Enter a number\n')
        except EOFError:
            break
        else:
            num = int(reoly)
            print('%d squared is %d' %(num, num**2))
    print('Bye!')

if __name__ == '__main__':
    interact()