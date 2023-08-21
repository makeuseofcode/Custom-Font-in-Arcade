import arcade

# Set up constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLUE = arcade.color.BLUE

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Simple Game Example")
        arcade.set_background_color(arcade.color.WHITE)

        # Initialize player position
        self.player_x = width // 2
        self.player_y = height // 2

    def on_draw(self):
        arcade.start_render()
        # Draw player as a circle
        arcade.draw_circle_filled(self.player_x, self.player_y, 30, BLUE)

    def on_key_press(self, key, modifiers):
        # Move player based on arrow key inputs
        if key == arcade.key.LEFT:
            self.player_x -= 10
        elif key == arcade.key.RIGHT:
            self.player_x += 10
        elif key == arcade.key.UP:
            self.player_y += 10
        elif key == arcade.key.DOWN:
            self.player_y -= 10

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
