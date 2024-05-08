

def create_board():
    board = []
    with open('board.txt') as board_file:
        for line in board_file:
            board.append(line.strip().split())
    return board


present_words = {}
coords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def bfs(board, words_list, word, path, num_words):
    (i,j) = path[-1]
    word += board[i][j]

    num_words += 1

    # set the min length of words you want to return
    if word in words_list and len(word) > 3:
        if len(word) in present_words:
            if word not in present_words[len(word)]:
                present_words[len(word)].append(word)
        else:
            present_words[len(word)] = [word]

    # set the maximum length of words you want
    if len(word) > 4: 
        return num_words
    
    for pos in coords:
        new_x = pos[0]+i
        new_y = pos[1]+j
        new_coord = (new_x,new_y)

        if new_coord not in path and new_x>=0 and new_x<len(board) and new_y>=0 and new_y<len(board[new_x]):
            new_path = path + [new_coord]
            num_words = bfs(board, words_list, word, new_path, num_words)
    
    return num_words


# this is where we use BFS to find all words
def find_words(board, words_list):
    total_words = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            num_words = bfs(board, words_list, '', [(i,j)], 0)
            total_words += num_words
            print(board[i][j], num_words)
    print(f"total words tested: {total_words}")
    return present_words