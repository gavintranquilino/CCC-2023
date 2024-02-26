def main():
    Poblano = 1500
    Mirasol = 6000
    Serrano = 15500
    Cayenne = 40000
    Thai = 75000
    Habanero = 125000
    peppers = []
    
    total_spiciness = 0

    num_peppers = int(input())

    for i in range(num_peppers):
        peppers.append(str(input()))
    
    for j in peppers:
        if j == "Poblano":
            total_spiciness += Poblano

        if j == "Mirasol":
            total_spiciness += Mirasol

        if j == "Serrano":
            total_spiciness += Serrano

        if j == "Cayenne":
            total_spiciness += Cayenne

        if j == "Thai":
            total_spiciness += Thai
            
        if j == "Habanero":
            total_spiciness += Habanero
    
    print(total_spiciness)


if __name__ == "__main__":
    main()