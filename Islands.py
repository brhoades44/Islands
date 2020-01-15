###############################################################################################
## Bruce Rhoades -  Class representing a "Geographic Area" (A 2 x 2 2D grid)
##
## It currently has a method to determing the number of "Islands" in the area. An island is 
## considered to be an area of 1's (land) with 0's (water) or borders surrounding it. 
###############################################################################################


class GeographicArea:
    ## No of rows and columns 
    ## Can be expanded to allow for dimensions to be allocated by client code
    __ROW = 5
    __COL = 5

    ###########################################################################################
    ## A function to check if a given cell (row, col) can be included in a search to determine
    ## if it is part of an island
    ##
    ## matrix: Reference to full matrix area the code is analyzing
    ## row: The current row of the target cell
    ## column: The current column of the target cell
    ## visited: Reference to matrix representing cells that have already been examined 
    ###########################################################################################
    @staticmethod
    def __isSafe(matrix, row, col, visited):
        ## Return true if row and column number is in range, 
        ## and cell value is 1 and not yet visited 
        ## Otherwise return false
        return (row >= 0) and (row < GeographicArea.__ROW) and (col >= 0) and (col < GeographicArea.__COL) and (matrix[row][col] == 1 and visited[row][col] == False)

    ###########################################################################################
    ## A recursive utility function to traverseNeighbors through a 2D boolean matrix
    ## It considers the 8 neighbors as adjacent vertices
    ##
    ## matrix: Reference to full matrix area the code is analyzing
    ## row: The current row of the target cell
    ## column: The current column of the target cell
    ## visited: Reference to matrix representing cells that have already been examined 
    ###########################################################################################
    @staticmethod
    def __traverseNeighbors(matrix, row, col, visited):
        ## These arrays are used to get row and column numbers of 8 neighbors of a given cell 
         # three cells in row above, two cells in current row, three cells in row below        
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1 ]
        # row above: cell in prior col, cell in cur col, cell in next col 
        # cur row: cell in prior col, cell in next col
        # next row: cell in prior col, cell in cur col, cell in next col
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1 ] 

        ## Mark this cell as visited 
        visited[row][col] = True

        ## Recur for all neighbors 
        for i in range(8):
            if (GeographicArea.__isSafe(matrix, row + rowNbr[i], col + colNbr[i], visited)):
                GeographicArea.__traverseNeighbors(matrix, row + rowNbr[i], col + colNbr[i], visited)

    ###########################################################################################
    ## The main driver function that traverses the 2D matrix and returns the count of islands 
    ##
    ## matrix: Reference to full matrix area the code is analyzing
    ###########################################################################################
    @staticmethod
    def countIslands(matrix):
        ## Make a bool array to mark visited cells. Initially all cells are unvisited (false)
        visited = [] #[ROW, COL];
        for _ in range(GeographicArea.__ROW):
            subVisited = []
            for _ in range(GeographicArea.__COL):
                subVisited.append(False)
            visited.append(subVisited)

        ## Initialize count as 0 and traverse through all cells of given matrix 
        count = 0
        for k in range(GeographicArea.__ROW):
            for l in range(GeographicArea.__COL):
                if (matrix[k][l] == 1 and visited[k][l] == False):
                    ## If a cell with value 1 is not visited yet, then a new island is found
                    ## Visit all cells in this island and increment island count 
                    GeographicArea.__traverseNeighbors(matrix, k, l, visited)
                    count += 1

        return count
