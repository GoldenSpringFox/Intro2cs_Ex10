import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame(args.rounds, args.apples, args)
    gd.show_score(game.score)

    game.draw_board(gd)
    # END OF ROUND 0

    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)

        # UPDATE OBJECTS
        game.update_objects()
        
        # DRAW BOARD
        game.draw_board(gd)
        
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")