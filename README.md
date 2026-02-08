# Chess Analyzer

An interactive chess analyzer and gaming tool imported from the Verdent project.

## Features

- **Chess Board Representation**: Display and manage chess positions
- **Material Analysis**: Count and compare material for both sides
- **Position Evaluation**: Basic position analysis capabilities

## Installation

No external dependencies required. Simply clone the repository:

```bash
git clone https://github.com/israelfeldman-cpu/Chess_Analizer.git
cd Chess_Analizer
```

## Usage

Run the chess analyzer:

```bash
python3 chess_analyzer.py
```

## Project Structure

```
Chess_Analizer/
├── chess_analyzer.py   # Main chess analysis tool
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Components

### ChessBoard Class
Manages the chess board state and piece positions:
- `setup_initial_position()`: Sets up standard starting position
- `display()`: Shows the current board state
- `get_piece(row, col)`: Retrieves piece at position
- `set_piece(row, col, piece)`: Places piece at position

### ChessAnalyzer Class
Analyzes chess positions:
- `count_material()`: Calculates material count for both sides
- `analyze_position()`: Provides position evaluation
- `display_board()`: Displays the current position

## Piece Notation

- Uppercase letters represent White pieces: `P N B R Q K`
- Lowercase letters represent Black pieces: `p n b q k`
- Empty squares are represented by spaces

## Material Values

- Pawn (P/p): 1 point
- Knight (N/n): 3 points
- Bishop (B/b): 3 points
- Rook (R/r): 5 points
- Queen (Q/q): 9 points
- King (K/k): No point value (invaluable)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available under the MIT License.
