import chess
import chess.engine

# 1. אתחול הלוח והמנוע
board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("path/to/stockfish")


def play_turn(move_uci):
    # ביצוע מהלך השחקן
    move = chess.Move.from_uci(move_uci)
    board.push(move)

    # ניתוח המהלך ע"י המנוע
    info = engine.analyse(board, chess.engine.Limit(time=0.1))
    score = info["score"].relative.score(mate_score=10000)

    # כאן תבוא הפנייה ל-AI להסבר המהלך
    # get_ai_explanation(board, move, score)

    # מהלך הבוט (לפי רמת קושי)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)

    return board
