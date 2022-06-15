def main():
    print(fatorial(5))

def fatorial(n):
    print('resolva fatorial de',n)
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)

main()