import arcade
import game_constants as gc

class MainMenu(arcade.View):
    def on_show_view(self):
        self.window.background_color = arcade.color.CHARTREUSE

    def on_draw(self):
        self.clear()
        title = arcade.Text("MENU", gc.SCREEN_WIDTH/2, gc.SCREEN_HEIGHT/1.5,
                    arcade.color.WHITE_SMOKE, 50, bold=True,
                    anchor_x="center")
        start = arcade.Text("Jouer", gc.SCREEN_WIDTH/2, gc.SCREEN_HEIGHT/3,
                    arcade.color.WHITE_SMOKE, 25, bold=True,
                    anchor_x="center")
        title.draw()
        start.draw()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.window.show_view(PauseMenu())


class PauseMenu(arcade.View):
    def on_show_view(self):
        self.window.background_color = arcade.color.BLEU_DE_FRANCE

    def on_draw(self):
        self.clear()
        pause = arcade.Text("Pause", gc.SCREEN_WIDTH/2, gc.SCREEN_HEIGHT/2,
                    arcade.color.WHITE_SMOKE, 75, bold=True,
                    anchor_x="center", anchor_y="center")
        unpause = arcade.Text("Continuer", gc.SCREEN_WIDTH/2, gc.SCREEN_HEIGHT/3,
                    arcade.color.WHITE_SMOKE, 25, bold=True,
                    anchor_x="center")
        pause.draw()
        unpause.draw()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.window.show_view(MainMenu())
joe = arcade.Window(gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT, "123")
joe.show_view(MainMenu())
arcade.run()