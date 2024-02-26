class Grid:
    def __init__(self, n=None, r1=None, r2=None):
        self.num_columns = n
        self.row1 = r1
        self.row2 = r2
        self.perimeter = 0
    
    def check_adjacent_row(self, row, index): 

        if self.num_columns == 1:
            return
        
        if index == 0: # first item
            if row[index+1]: # if next side is a 1
                self.perimeter -= 1
            
            else:
                return
                

        elif index == self.num_columns-1: # last item
            if row[index-1]: # if prev side is 1
                self.perimeter -= 1

            else:
                return        

        else:
            if row[index+1]: # any middle item
                self.perimeter -= 1

            if row[index-1]:
                self.perimeter -= 1
    
    def check_adjacent_column(self, index):

        if not index%2: # if not odd

            if self.row1[index] and self.row2[index]: # if they 
                self.perimeter -= 2
        
        else:
            return
        

    def get_perimeter(self): 
        for i in range(self.num_columns): 

            if self.row1[i]:
                self.perimeter += 3
                self.check_adjacent_row(self.row1, i)

            if self.row2[i]:
                self.perimeter += 3   
                self.check_adjacent_row(self.row2, i)
            
            self.check_adjacent_column(i)
        
        return self.perimeter
            
            
def main():
    num_columns = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))

    grid = Grid(num_columns, row1, row2)
    print(grid.get_perimeter()) 

if __name__ == "__main__":
    main()