♟️ TMC - TeachMeChess
Bridging the Gap Between Engine Analysis and Human Strategy.

TMC is an AI-powered chess educational tool developed to transform the way players interact with chess engines. Instead of just showing the "best" move, TMC is designed to eventually explain the logic behind the board, helping players improve their tactical vision.

🌟 The Story Behind TMC
This project was born out of a personal journey during a challenging period in Israel. Amidst the uncertainty of the war, I decided to channel my energy into two passions: Information Systems Engineering and Chess.

I realized that while engines like Stockfish are incredibly powerful, they speak in "numbers" and "evaluations," not in "concepts." TMC was created to pass the time productively, sharpen my software development skills (Python & Streamlit), and eventually build a "coach" that speaks like a human, not a machine.

🚀 Current Capabilities
Dynamic Stockfish Integration: Play against Stockfish with a customizable ELO slider (200 to 1000 ELO), mapping skill levels directly to the engine's internal logic.

Streamlit Interactive UI: A clean, wide-layout web interface featuring a dynamic board rendered with chessboardjs.

Smart Game Management:

Move History (PGN): Automatic generation of PGN records with a built-in download feature for post-game analysis.

State Persistence: Using Streamlit's session_state to ensure the game doesn't reset on UI interactions.

Move Validation: Full integration with the python-chess library to handle legal moves, checkmates, and draws.

Undo & Reset: Built-in controls to backtrack moves or start a fresh match instantly.

🛠️ Tech Stack
Python (Core Logic)

Streamlit (Web Framework & State Management)

Stockfish 16.1 (UCI Chess Engine)

python-chess (Move validation & PGN handling)

JavaScript (chessboardjs) - For high-quality board rendering via Streamlit Components.

🗺️ Roadmap: The "Coach" Evolution
TMC is currently a Work In Progress (WIP). The next milestones include:

Explainable AI (XAI): Utilizing engine evaluations to provide text-based hints (e.g., "This move creates a fork between the King and Rook").

Evaluation Bar: A visual representation of who is winning based on Stockfish's analysis.

Move Comparison: Showing the user their move vs. the engine's suggested move with a "loss in centipawns" explanation.

⚙️ Setup & Installation
Clone the repo.

Install dependencies: pip install streamlit chess.

Download the Stockfish binary and update the STOCKFISH_PATH in main.py.

Run the app: streamlit run main.py.
