import config

class Player:
    def __init__(self):
        self.x = config.PLAYER_START_X
        self.y = config.PLAYER_START_Y
        self.radius = config.PLAYER_RADIUS

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        self.handle_wall_collision()

    def move_to_position(self, x, y):
        self.x = x
        self.y = y
        
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
        self.x = config.BALL_START_X
        self.y = config.BALL_START_Y
        self.speed_x = 0
        self.speed_y = 0
        self.radius = config.BALL_RADIUS
    
    def apply_ressistance(self):
        self.speed_x *= config.BALL_RESISTANCE
        self.speed_y *= config.BALL_RESISTANCE

    def move(self):
        goal = self.handle_wall_collision()
        if goal == -1:
            self.x += self.speed_x
            self.y += self.speed_y
            self.apply_ressistance()
        else:
            self.x = config.BALL_START_X
            self.y = config.BALL_START_Y
            self.speed_x = 0
            self.speed_y = 0
        return goal

    def handle_wall_collision(self):
        goal = -1
        if self.x < self.radius:
            self.x = self.radius
            self.speed_x *= -1
            if self.y > config.GOAL_SIZE[0] and self.y < config.GOAL_SIZE[1]:
                goal = 1
        if self.y < self.radius:
            self.y = self.radius
            self.speed_y *= -1
        if self.x > config.WIDTH - self.radius:
            self.x = config.WIDTH - self.radius
            self.speed_x *= -1
            if self.y > config.GOAL_SIZE[0] and self.y < config.GOAL_SIZE[1]:
                goal = 0
        if self.y > config.HEIGHT - self.radius:
            self.y = config.HEIGHT - self.radius
            self.speed_y *= -1
        return goal

class GameEngine:
    def __init__(self):
        self.ball = Ball()
        self.player = Player()
        self.points = [0, 0]

    def handle_collision(self):
        distance_squared = (self.player.x-self.ball.x)**2 + (self.player.y-self.ball.y)**2
        if distance_squared <= (self.player.radius + self.ball.radius)**2: 
            self.ball.speed_x += (self.ball.x - self.player.x) / pow(distance_squared, 0.5)
            self.ball.speed_y += (self.ball.y - self.player.y) / pow(distance_squared, 0.5)  

    #updating the state of the game
    def game_loop(self, move_x, move_y):
        goal = self.ball.move()
        if goal != -1:
            self.points[goal] += 1
            self.player.move_to_position(config.PLAYER_START_X, config.PLAYER_START_Y)
        self.player.move(move_x, move_y)
        self.handle_collision()
        return self.player, self.ball, self.points

    