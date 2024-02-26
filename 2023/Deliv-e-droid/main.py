total_points = 0
def main():
    num_packages = int(input())
    num_collisions = int(input())

    total_points = (50*num_packages) + (-10 * num_collisions)

    if num_packages > num_collisions:
        total_points += 500
    
    print(total_points)


if __name__ == "__main__":
    main()