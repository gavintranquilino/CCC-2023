def main():
    week = []
    num_columns = int(input())
    
    for i in range(num_columns):
        week.append(list(map(int, input().split())))
    
    print(week)

if __name__ == "__main__":
    main()