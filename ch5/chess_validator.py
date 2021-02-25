from collections import Counter



def isValidChessBoard(board):
    valid = True
    white = []
    black = []
    for k, v in board.items():
        if k[0] not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print(k[0])
            print("Invalid number")
            valid = False
            return valid
        elif k[1] not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            print("Invalid letter")
            valid = False
            return valid
        elif v[0] == "b":
            black.append(v)
        elif v[0] == "w":
            white.append(v)
        elif v[0] != "b" and v[0] != "w":
            print("Invalid Color")
            value = False
            return value
    black_count = (Counter(black))
    white_count = (Counter(white))
    if sum(white_count.values()) > 16 or \
            white_count["wpawn"] > 8 or \
            white_count["wknight"] > 2 or \
            white_count["wbishop"] > 2 or \
            white_count["wrook"] > 2 or \
            white_count["wqueen"] > 1 or \
            white_count["wking"] != 1:
        print("Invalid white pieces")
        valid = False
        return valid
    elif sum(black_count.values()) > 16 or \
            black_count["bpawn"] > 8 or \
            black_count["bknight"] > 2 or \
            black_count["bbishop"] > 2 or \
            black_count["brook"] > 2 or \
            black_count["bqueen"] > 1 or \
            black_count["bking"] != 1:
        print("Invalid black pieces")
        valid = False
        return valid
    else:
        print("Valid")
        return valid


def print_board():
    board = {}
    alphalist = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for i in range(8):
        for j in range(8):
            board.setdefault(str(j + 1) + alphalist[i], " ")

    the_board =[
        "_" * 33 + "\n",
        "| " + board['1h'] + " | " + board['2h'] + " | " + board['3h'] + " | " + board['4h'] + " | " + board['5h'] + " | " + board['6h'] + " | " + board['7h'] + " | " + board['8h'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1g'] + " | " + board['2g'] + " | " + board['3g'] + " | " + board['4g'] + " | " + board['5g'] + " | " + board['6g'] + " | " + board['7g'] + " | " + board['8g'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1f'] + " | " + board['2f'] + " | " + board['3f'] + " | " + board['4f'] + " | " + board['5f'] + " | " + board['6f'] + " | " + board['7f'] + " | " + board['8f'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1e'] + " | " + board['2e'] + " | " + board['3e'] + " | " + board['4e'] + " | " + board['5e'] + " | " + board['6e'] + " | " + board['7e'] + " | " + board['8e'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1d'] + " | " + board['2d'] + " | " + board['3d'] + " | " + board['4d'] + " | " + board['5d'] + " | " + board['6d'] + " | " + board['7d'] + " | " + board['8d'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1c'] + " | " + board['2c'] + " | " + board['3c'] + " | " + board['4c'] + " | " + board['5c'] + " | " + board['6c'] + " | " + board['7c'] + " | " + board['8c'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1b'] + " | " + board['2b'] + " | " + board['3b'] + " | " + board['4b'] + " | " + board['5b'] + " | " + board['6b'] + " | " + board['7b'] + " | " + board['8b'] + " |\n",
        "_" * 33 + "\n",
        "| " + board['1a'] + " | " + board['2a'] + " | " + board['3a'] + " | " + board['4a'] + " | " + board['5a'] + " | " + board['6a'] + " | " + board['7a'] + " | " + board['8a'] + " |\n",
        "_" * 33 + "\n"]
    return the_board

board = print_board()
for t in board:
    print(t)


# Validator tests

tboard1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #valid
tboard3 = {'1h': 'bking', '9c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #invalid column
tboard4 = {'1h': 'bking', '8z': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #invalid row
tboard5 = {'1h': 'bking', '6c': 'rqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #invalid piece color
tboard6 = {'1h': 'bpawn', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #missing king
tboard7 = {'1h': 'bking', '6c': 'bking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #multiple bking
tboard8 = {'1h': 'bking', '6c': 'bqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "1c": 'wbishop'} #multiple bqueen
tboard9 = {'1a': 'bking', '2a': 'bqueen', '3a': 'bbishop', '4a': 'bbishop', '5a': 'bknight', '6a': 'bknight', '7a': 'brook', '8a': 'brook', '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn', '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn', '1c': 'wking'} #valid
tboard0 = {'1a': 'bking', '2a': 'bqueen', '3a': 'bbishop', '4a': 'bbishop', '5a': 'bknight', '6a': 'bknight', '7a': 'brook', '8a': 'brook', '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn', '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn', '1c': 'wking', '2c': 'bpawn'} #too many pawns

print(isValidChessBoard(tboard1))
print(isValidChessBoard(tboard3))
print(isValidChessBoard(tboard4))
print(isValidChessBoard(tboard5))
print(isValidChessBoard(tboard6))
print(isValidChessBoard(tboard7))
print(isValidChessBoard(tboard8))
print(isValidChessBoard(tboard9))
print(isValidChessBoard(tboard0))
