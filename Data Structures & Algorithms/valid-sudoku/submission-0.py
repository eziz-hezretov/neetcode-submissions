class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for num in row:
                if num in seen:
                    return False
                elif num == '.':
                    continue
                else:
                    seen.add(num)
        
        column_counter = 0

        while column_counter <= 8:
            row_counter = 0
            seen_2 = set()

            while row_counter <= 8:
                value = board[row_counter][column_counter]
                if value != '.':
                    if value in seen_2:
                        return False
                    else:
                        seen_2.add(value)
            
                row_counter += 1
        
            column_counter += 1

        for start_row in range(0, 9, 3):
            for start_column in range(0, 9, 3):

                seen_3 = set()

                for row in range(start_row, start_row + 3):
                    for column in range(start_column, start_column + 3):

                        value_2 = board[row][column]

                        if value_2 in seen_3:
                            return False
                        elif value_2 == '.':
                            continue
                        else:
                            seen_3.add(value_2)
        
        return True
