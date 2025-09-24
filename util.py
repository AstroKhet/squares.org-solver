
def generate_board_from_str(flattened):
    """
    flattened (str): A 16 character string containing the squares board connected row by row
    
    Returns a 4x4 board with lowercase letters.
    """
    flattened = flattened.lower()
    board = []
    for i in range(4):
        board.append([l for l in flattened[i*4: (i+1)*4]])
    return board