# Obsolete file for solving; this for storing words in words.txt as a Trie data structure

import json

def generate_trie():
    root = dict()
    
    with open("data/words.txt") as words:
        words = [line.rstrip() for line in words]
    
    for word in words:
        if len(word) < 4 or len(word) > 16:
            continue
        node = root
        for char in word:
            node = node.setdefault(char, {})
        node["!"] = True
        
    with open("data/trie.json", "w") as trie:
        json.dump(root, trie)
        
    
if __name__ == "__main__":
    generate_trie()