def main():
    array = []

    for i in range(1000):
        num = int(input())
        if num != 0:
            array.append(num)
        
        else:
            array.pop(-1)
    
    print(array)
    


if __name__ == "__main__":
    main()