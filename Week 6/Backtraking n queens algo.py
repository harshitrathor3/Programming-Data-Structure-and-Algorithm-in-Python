def placequeen(i, board):
    for each c if (i, c) is available
    place queen at (i, c) and update board

        if i==n-1:
            return True
        else:
            extendsol = placequeen(i+1, board)
        if extendsol:
            return True
        else:
            Undo this move and update board
    else:
        return False
