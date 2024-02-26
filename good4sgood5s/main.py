master_list = [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 2]
output = 0


def main():
    num = int(input("\n"))
    
    if num <= 20:
        output = master_list[num-1]
        return output
    
    else:
        output = master_list[(num%20)-1]
        return output
    
if __name__ == "__main__":
    print(main())