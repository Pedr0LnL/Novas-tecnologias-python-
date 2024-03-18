def main():
    print("Caixa:")
    print_box(5, 5)
    print("\nOval:")
    print_oval(5, 9)
    print("\nSeta:")
    print_arrow(5)
    print("\nLosango:")
    print_diamond(5)

def print_box(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * width)
        else:
            print('*' + ' ' * (width - 2) + '*')

def print_oval(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print(' ' * (width // 2) + '*' * (width // 2 + 1))
        else:
            if i < height // 2:
                spaces = ' ' * (width // 2 - i)
                stars = '*' * (width - 2 * (width // 2 - i))
            else:
                spaces = ' ' * (i - width // 2)
                stars = '*' * (width - 2 * (i - width // 2))
            print(spaces + '*' + stars + '*')

def print_arrow(height):
    for i in range(height):
        if i == 0:
            print(' ' * (height - 1) + '*')
        elif i < height // 2:
            print(' ' * (height - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
        elif i == height // 2:
            print('*' * (2 * height - 1))
        else:
            print(' ' * (i) + '*' + ' ' * (2 * height - 2 * i - 3) + '*')

def print_diamond(height):
    for i in range(height):
        if i < height // 2:
            print(' ' * (height // 2 - i) + '*' * (2 * i + 1))
        else:
            print(' ' * (i - height // 2) + '*' * (2 * (height - i) - 1))

if __name__ == "__main__":
    main()
