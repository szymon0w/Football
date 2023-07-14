import config

class Player:
    def __init__(self):
        self.x = 350
        self.y = 400
        self.radius = 100

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        self.handle_wall_collision()
    
    def handle_wall_collision(self):
        if self.x < self.radius:
            self.x = self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.x > config.WIDTH - self.radius:
            self.x = config.WIDTH - self.radius
        if self.y > config.HEIGHT - self.radius:
            self.y = config.HEIGHT - self.radius

class Ball:
    def __init__(self):
        self.x = 350
        self.y = 200
        self.speed_x = 0
        self.speed_y = 0
        self.radius = 30
    
    def apply_ressistance(self):
        self.speed_x *= 0.98
        self.speed_y *= 0.98

    def move(self):
        self.handle_wall_collision()
        self.x += self.speed_x
        self.y += self.speed_y
        self.apply_ressistance()

    def handle_wall_collision(self):
        if self.x < self.radius:
            self.x = self.radius
            self.speed_x *= -1
        if self.y < self.radius:
            self.y = self.radius
            self.speed_y *= -1
        if self.x > config.WIDTH - self.radius:
            self.x = config.WIDTH - self.radius
            self.speed_x *= -1
        if self.y > config.HEIGHT - self.radius:
            self.y = config.HEIGHT - self.radius
            self.speed_y *= -1


class GameEngine:
    def __init__(self):
        self.ball = Ball()
        self.player = Player()

    def handle_collision(self):
        distance_squared = (self.player.x-self.ball.x)**2 + (self.player.y-self.ball.y)**2
        if distance_squared <= (self.player.radius + self.ball.radius)**2: 
            self.ball.speed_x += (self.ball.x - self.player.x) / pow(distance_squared, 0.5)
            self.ball.speed_y += (self.ball.y - self.player.y) / pow(distance_squared, 0.5)  

    #updating the state of the game
    def game_loop(self, move_x, move_y):
        self.ball.move()
        self.player.move(move_x, move_y)
        self.handle_collision()
        return self.player, self.ball

    