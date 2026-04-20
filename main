import streamlit as st
import chess
import chess.pgn
import streamlit.components.v1 as components
from opponent import ChessOpponent

st.set_page_config(page_title="Chess Future Coach", layout="wide")

# --- הגדרות ---
# ודא שהנתיב לסטוקפיש כאן מדויק לפי המחשב שלך
STOCKFISH_PATH = r"C:\Users\97254\PycharmProjects\Python_101\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe"


# טעינת מחלקת היריב שיצרנו (נשמר בזיכרון כדי לא לאתחל את המנוע מחדש)
@st.cache_resource
def get_opponent():
    return ChessOpponent(STOCKFISH_PATH)


opponent = get_opponent()

# ניהול מצב הלוח
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()


# --- פונקציות עזר ---
def make_ai_move(elo_level):
    board = st.session_state.board
    if not board.is_game_over():
        # קריאה לפונקציה מתוך הקובץ opponent.py
        bot_move = opponent.get_best_move(board, elo_level)
        if bot_move:
            board.push(bot_move)


def interactive_board(fen):
    # הוספנו את pieceTheme כדי לטעון את התמונות כראוי משרת חיצוני
    board_html = f"""
    <link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>

    <div id="myBoard" style="width: 450px; margin: auto;"></div>

    <script>
        var board = Chessboard('myBoard', {{
            draggable: false, // ביטלתי זמנית את הגרירה כדי למנוע בלבול, נשתמש בתיבת הטקסט
            position: '{fen}',
            pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{{piece}}.png'
        }});
    </script>
    """
    components.html(board_html, height=500)


# --- ממשק משתמש ---
st.title("♟️ Chess Future Coach")

elo_level = st.select_slider(
    "בחר את רמת היריב (ELO):",
    options=[200, 400, 600, 800, 1000],
    value=400
)

col_board, col_controls, col_pgn = st.columns([5, 3, 2.5])

board = st.session_state.board

with col_board:
    interactive_board(board.fen())

    # סטטוס מתחת ללוח
    if board.is_checkmate():
        st.success("מט! המשחק הסתיים.")
    elif board.is_check():
        st.warning("שח!")
    elif board.turn == chess.WHITE:
        st.info("תורך (לבן)")
    else:
        st.warning("תור היריב (שחור)")

with col_controls:
    st.write("### שליטה")

    # שימוש בטופס כדי לאפס את תיבת הטקסט לאחר השליחה ולמנוע ריענונים כפולים
    with st.form("move_form", clear_on_submit=True):
        move_input = st.text_input("הזן מהלך (למשל e4 או Nf3):")
        submit_move = st.form_submit_button("בצע מהלך")

    if submit_move and move_input:
        try:
            # זיהוי המהלך מהטקסט של המשתמש
            user_move = board.parse_san(move_input)
            if user_move in board.legal_moves:
                board.push(user_move)

                # תור הבוט מופעל מיד לאחר מכן
                if not board.is_game_over():
                    with st.spinner("הבוט חושב..."):
                        make_ai_move(elo_level)
                st.rerun()
            else:
                st.error("מהלך לא חוקי")
        except ValueError:
            st.error("פורמט מהלך שגוי. נסה פורמט אלגברי כמו e4, Nf3, O-O")

    st.divider()
    if st.button("⬅️ בטל מהלך"):
        if len(board.move_stack) >= 2:
            board.pop()  # ביטול מהלך הבוט
            board.pop()  # ביטול המהלך שלך
            st.rerun()
        elif len(board.move_stack) == 1:
            board.pop()
            st.rerun()

    if st.button("🔄 איפוס משחק"):
        st.session_state.board = chess.Board()
        st.rerun()

with col_pgn:
    st.subheader("רישום מהלכים")

    # הדרך הנכונה לבנות PGN מתוך היסטוריית המהלכים שכבר שוחקו
    game = chess.pgn.Game()
    node = game
    for move in board.move_stack:
        node = node.add_variation(move)

    pgn_output = str(game.mainline_moves())
    if not pgn_output:
        pgn_output = "טרם בוצעו מהלכים."

    st.text_area("PGN:", value=pgn_output, height=300, disabled=True)
    st.download_button("הורד PGN", pgn_output, file_name="game.pgn")
