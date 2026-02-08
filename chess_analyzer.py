#!/usr/bin/env python3
"""
Chess Analyzer - A simple chess position analyzer
Imported from Verdent project concepts
"""

class ChessBoard:
    """Represents a chess board and handles game logic"""
    
    def __init__(self):
        """Initialize an empty chess board"""
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.setup_initial_position()
    
    def setup_initial_position(self):
        """Set up the standard chess starting position"""
        # Black pieces
        pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i, piece in enumerate(pieces):
            self.board[0][i] = piece.lower()  # Black pieces (lowercase)
        for i in range(8):
            self.board[1][i] = 'p'  # Black pawns
        
        # White pieces
        for i, piece in enumerate(pieces):
            self.board[7][i] = piece  # White pieces (uppercase)
        for i in range(8):
            self.board[6][i] = 'P'  # White pawns
    
    def display(self):
        """Display the chess board"""
        print("\n  a b c d e f g h")
        print("  ---------------")
        for i, row in enumerate(self.board):
            print(f"{8-i}|{' '.join(row)}|")
        print("  ---------------")
    
    def get_piece(self, row, col):
        """Get piece at given position"""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def set_piece(self, row, col, piece):
        """Set piece at given position"""
        if 0 <= row < 8 and 0 <= col < 8:
            self.board[row][col] = piece
            return True
        return False


class ChessAnalyzer:
    """Analyzes chess positions and suggests moves"""
    
    def __init__(self):
        """Initialize the analyzer"""
        self.board = ChessBoard()
    
    def count_material(self):
        """Count material for both sides"""
        piece_values = {
            'P': 1, 'p': 1,
            'N': 3, 'n': 3,
            'B': 3, 'b': 3,
            'R': 5, 'r': 5,
            'Q': 9, 'q': 9,
            'K': 0, 'k': 0
        }
        
        white_material = 0
        black_material = 0
        
        for row in self.board.board:
            for piece in row:
                if piece != ' ':
                    if piece.isupper():
                        white_material += piece_values.get(piece, 0)
                    else:
                        black_material += piece_values.get(piece, 0)
        
        return white_material, black_material
    
    def analyze_position(self):
        """Analyze current position"""
        white_material, black_material = self.count_material()
        
        print("\n=== Position Analysis ===")
        print(f"White material: {white_material}")
        print(f"Black material: {black_material}")
        
        if white_material > black_material:
            print(f"White is ahead by {white_material - black_material} points")
        elif black_material > white_material:
            print(f"Black is ahead by {black_material - white_material} points")
        else:
            print("Material is equal")
    
    def display_board(self):
        """Display the current board position"""
        self.board.display()


def main():
    """Main entry point"""
    print("Chess Analyzer - Verdent Project")
    print("=" * 40)
    
    analyzer = ChessAnalyzer()
    analyzer.display_board()
    analyzer.analyze_position()


if __name__ == "__main__":
    main()
