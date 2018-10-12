from string import ascii_uppercase
from random import choice 
    
def make_grid(columns, rows):
    return {(c,r): choice(ascii_uppercase) for r in range(rows) for c in range(columns)}
    
def potential_neighbours(position):
    c, r = position
    return [(c-1, r-1), (c, r-1),  (c+1, r-1), 
            (c-1, r),              (c+1, r), 
            (c-1, r+1), (c, r+1),  (c+1, r+1)]
            
def path_to_word(path, grid):
    word = ""
    for position in path:
        word += grid[position]
    return word
    
def load_word_list(filename):
     with open(filename) as f:
       text = f.read().upper().split("\n")
     return text
     
def get_real_neighbours(grid):
    real_neighbours = {}
    
    for position in grid:
        pn = potential_neighbours(position)
        on_the_grid = [ p for p in pn if p in grid]
        real_neighbours[position] = on_the_grid
    
    return real_neighbours
    
    # another way to do the function 'get_real_neighbours'
# def get_real_neighbours(grid):
#     real_neighbours = {}
    
#     for position in grid:
#         pn = potential_neighbours(position)
#         on_the_grid = []
#         for p in pn:
#             if p in grid:
#                 on_the_grid.append(p)
        
#         real_neighbours[position] = on_the_grid
    
#     return real_neighbours


