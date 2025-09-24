import json
import time

from util import generate_board_from_str

# Type out today's board here!
flattened_board = "ENTERSQUARESHERE"

# 1. Constants
BOARD = generate_board_from_str(flattened_board)
SIZE = len(BOARD)
with open("data/trie.json") as f:
    TRIE = json.load(f)


# 2. Helper functions
def neighbour(r, c):
    """
    r, c (int): Center location
    """
    coords = []
    for y in (-1, 0, 1):
        for x in (-1, 0, 1):
            if x == y == 0:
                continue
            
            nr = r + y
            nc = c + x
            if 0 <= nr < SIZE and 0 <= nc < SIZE:
                coords.append((nr, nc))
                
    return coords

def explore(r, c, node, used, words):
    """
    r, c (int): Row and column of position to explore from
    node (dict): The point from TRIE to explore from
    used (list[tuple]): Contains (r, c) coordinates of already used letters
    words (set): Container in outer scope to store all valid words
    """
    if node.get("!") and len(used) >= 4:
        word = "".join(BOARD[wr][wc] for wr, wc in used)
        words.add(word)

    for coord in neighbour(r, c):
        if coord in used:
            continue
        nr, nc = coord
        l = BOARD[nr][nc]
        if child := node.get(l):
            explore(nr, nc, child, used + [coord], words)
            
            
# 3. Main solver function
def solve():
    found_words = set()
    for r in range(SIZE):
        for c in range(SIZE):
            used = [(r, c)]
            words = set()
            node = TRIE.get(BOARD[r][c])
            explore(r, c, node, used, words)
            found_words |= words
    return found_words


if __name__ == "__main__":
    print("Board:")
    for row in BOARD:
        print(" ".join(char.upper() for char in row))
    print()
    
    start = time.time()
    found_words = solve()
    end = time.time()
    
    print(f"{len(found_words)} words found in {(end-start)*1000:.3f}ms")
    found_words = list(set(found_words))
    
    # Sort by length
    length_dict = {}
    for word in found_words:
        l = len(word)
        if l not in length_dict:
            length_dict[l] = []
        length_dict[l].append(word)
    
    for length in sorted(length_dict):
        print(f"{length}-letter words:")
        print(", ".join(length_dict[length]))
        print()
        
        