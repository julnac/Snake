from pygame.math import Vector2


class MediatorInterface:

    def init_position(self) -> Vector2:
        pass

    def notify(self, game_object, position):
        pass
