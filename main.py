import utils, board_funcs

board = board_funcs.create_board()
words_list = utils.get_words_list()

present_words = board_funcs.find_words(board, words_list)
utils.print_results(present_words)

