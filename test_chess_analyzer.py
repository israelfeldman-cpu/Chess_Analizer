#!/usr/bin/env python3
"""
Tests for Chess Analyzer
"""

import sys
sys.path.insert(0, '.')

from chess_analyzer import ChessBoard, ChessAnalyzer


def test_board_initialization():
    """Test that the board initializes correctly"""
    print("Testing board initialization...")
    board = ChessBoard()
    
    # Check that white pieces are in correct positions
    assert board.get_piece(7, 0) == 'R', "White rook should be at a1"
    assert board.get_piece(7, 4) == 'K', "White king should be at e1"
    assert board.get_piece(6, 0) == 'P', "White pawn should be at a2"
    
    # Check that black pieces are in correct positions
    assert board.get_piece(0, 0) == 'r', "Black rook should be at a8"
    assert board.get_piece(0, 4) == 'k', "Black king should be at e8"
    assert board.get_piece(1, 0) == 'p', "Black pawn should be at a7"
    
    # Check empty squares
    assert board.get_piece(3, 3) == ' ', "d5 should be empty"
    assert board.get_piece(4, 4) == ' ', "e4 should be empty"
    
    print("✓ Board initialization test passed")


def test_material_counting():
    """Test material counting"""
    print("Testing material counting...")
    analyzer = ChessAnalyzer()
    
    white_material, black_material = analyzer.count_material()
    
    # Initial position should have equal material
    assert white_material == 39, f"White should have 39 points, got {white_material}"
    assert black_material == 39, f"Black should have 39 points, got {black_material}"
    
    print("✓ Material counting test passed")


def test_piece_manipulation():
    """Test setting and getting pieces"""
    print("Testing piece manipulation...")
    board = ChessBoard()
    
    # Clear a square
    board.set_piece(6, 4, ' ')  # Remove white pawn from e2
    assert board.get_piece(6, 4) == ' ', "e2 should be empty"
    
    # Place a piece
    board.set_piece(4, 4, 'N')  # Place white knight on e4
    assert board.get_piece(4, 4) == 'N', "e4 should have white knight"
    
    print("✓ Piece manipulation test passed")


def test_material_after_exchange():
    """Test material counting after pieces are exchanged"""
    print("Testing material after exchange...")
    analyzer = ChessAnalyzer()
    
    # Remove a pawn from each side (simulate an exchange)
    analyzer.board.set_piece(6, 4, ' ')  # Remove white pawn
    analyzer.board.set_piece(1, 4, ' ')  # Remove black pawn
    
    white_material, black_material = analyzer.count_material()
    
    assert white_material == 38, f"White should have 38 points, got {white_material}"
    assert black_material == 38, f"Black should have 38 points, got {black_material}"
    
    print("✓ Material after exchange test passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("Running Chess Analyzer Tests")
    print("=" * 50)
    
    try:
        test_board_initialization()
        test_material_counting()
        test_piece_manipulation()
        test_material_after_exchange()
        
        print("=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
        return True
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
