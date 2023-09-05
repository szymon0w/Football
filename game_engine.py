import config

class Player:
    def __init__(self, color, start_x = config.PLAYER_START_X):
        self.x = start_x
        self.y = config.PLAYER_START_Y
        self.radius = config.PLAYER_RADIUS
        self.color = color

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
    def __init__(self, instantBounce):
        self.ball = Ball()
        self.players = [Player(config.GREEN), Player(config.RED, config.WIDTH - config.PLAYER_START_X)]
        self.points = [0, 0]
        self.instantBounce = instantBounce

    def handle_collision(self, player):
        distance_squared = (player.x-self.ball.x)**2 + (player.y-self.ball.y)**2
        if distance_squared <= (player.radius + self.ball.radius)**2: 
            if not self.instantBounce:
                self.ball.speed_x += (self.ball.x - player.x) / pow(distance_squared, 0.5)
                self.ball.speed_y += (self.ball.y - player.y) / pow(distance_squared, 0.5) 
            else:
                self.ball.speed_x = ((self.ball.x - player.x) / pow(distance_squared, 0.5))*10
                self.ball.speed_y = ((self.ball.y - player.y) / pow(distance_squared, 0.5))*10  

    #updating the state of the game
    def game_loop(self, player_moves):
        goal = self.ball.move()
        if goal != -1:
            self.points[goal] += 1
            self.players[0].move_to_position(config.PLAYER_START_X, config.PLAYER_START_Y)
            self.players[1].move_to_position(config.WIDTH - config.PLAYER_START_X, config.PLAYER_START_Y)

        self.players[0].move(player_moves[0][0], player_moves[0][1])
        self.players[1].move(player_moves[1][0], player_moves[1][1])
        self.handle_collision(self.players[0])
        self.handle_collision(self.players[1])
        return self.players, self.ball, self.points

    