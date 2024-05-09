def create_board():
    board = []
    with open('board.txt') as board_file:
        for line in board_file:
            board.append(line.strip().split())
    return board

present_words = {}
coords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def dfs(board, words_list, word, path, num_words):
    (i,j) = path[-1]
    word += board[i][j]

    num_words += 1

    # set the min length of words you want to return
    if len(word) in words_list:
        if word in words_list[len(word)] and len(word) > 2:
            if len(word) in present_words:
                if word not in present_words[len(word)]:
                    present_words[len(word)].append(word)
            else:
                present_words[len(word)] = [word]

    # set the maximum length of words you want
    max_length = 6
    if len(word) >= max_length: 
        return num_words
    
    for pos in coords:
        new_x = pos[0]+i
        new_y = pos[1]+j
        new_coord = (new_x,new_y)

        if new_coord not in path and new_x>=0 and new_x<len(board) and new_y>=0 and new_y<len(board[new_x]):
            new_path = path + [new_coord]
            num_words = dfs(board, words_list, word, new_path, num_words)
    
    return num_words


# this is where we use DFS to find all words
def find_words(board, words_list):
    total_words = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            num_words = dfs(board, words_list, '', [(i,j)], 0)
            total_words += num_words
            print(board[i][j], num_words)
    print(f"total words tested: {total_words}")
    return present_words