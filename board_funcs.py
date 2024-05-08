

def create_board():
    board = []
    with open('board.txt') as board_file:
        for line in board_file:
            board.append(line.strip().split())
    return board


present_words = {}
coords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def bfs(board, words_list, word, path):
    (i,j) = path[-1]
    word += board[i][j]
    
    if word in words_list and len(word) > 3:
        if len(word) in present_words:
            present_words[len(word)].append(word)
        else:
            present_words[len(word)] = [word]

    if len(word) > 5: 
        return
    
    for pos in coords:
        new_x = pos[0]+i
        new_y = pos[1]+j
        new_coord = (new_x,new_y)

        if new_coord not in path and new_x>=0 and new_x<4 and new_y>=0 and new_y<4:
            new_path = path + [new_coord]
            bfs(board, words_list, word, new_path)


# this is where we use BFS to find all words
def find_words(board, words_list):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j])
            print(present_words)
            bfs(board, words_list, '', [(i,j)])
    return present_words