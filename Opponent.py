import chess
import chess.engine


class ChessOpponent:
    def __init__(self, engine_path):
        self.engine_path = engine_path
        # מיפוי רמות ה-ELO לרמות של Stockfish
        self.skill_map = {200: 0, 400: 2, 600: 4, 800: 6, 1000: 8}

    def get_best_move(self, board, elo_level, time_limit=0.2):
        """
        פונקציה זו מקבלת את מצב הלוח ואת רמת הקושי, ומחזירה את המהלך הטוב ביותר.
        """
        skill_level = self.skill_map.get(elo_level, 2)  # ברירת מחדל: 2

        try:
            # פתיחה וסגירה של המנוע עבור המהלך
            with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
                engine.configure({"Skill Level": skill_level})
                result = engine.play(board, chess.engine.Limit(time=time_limit))
                return result.move
        except Exception as e:
            print(f"Engine Error: {e}")
            return None

    # --- הכנה לשלבים הבאים של האפליקציה ---

    def get_evaluation(self, board, time_limit=0.1):
        """
        פונקציה עתידית: מחזירה הערכת מצב (יתרון ללבן או לשחור)
        שימושי כדי להראות לשחקן 'מדד כוח' או להבין אם הוא עשה טעות קריטית.
        """
        try:
            with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
                info = engine.analyse(board, chess.engine.Limit(time=time_limit))
                return info["score"].white()
        except Exception:
            return None

    def get_hint(self, board):
        """
        פונקציה עתידית: מחזירה רמז לשחקן (המהלך המומלץ עבורו).
        """
        return self.get_best_move(board, elo_level=2000)  # רמז תמיד מבוסס על רמה גבוהה
