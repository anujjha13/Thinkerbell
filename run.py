import random

class GameMap:
    def __init__(self, grid_size, num_carrots, num_holes):
        self.grid_size = grid_size
        self.num_carrots = num_carrots
        self.num_holes = num_holes
        self.grid = [['-' for _ in range(grid_size)] for _ in range(grid_size)]
        self.rabbit_x, self.rabbit_y = None, None
        self.carrot_x, self.carrot_y = None, None
        self.hole_x, self.hole_y = None, None
        self.rabbit_has_carrot = False
        self.bothatsame=False
        self.both_x, self.both_y= None,None
        self.gameover=False
        self.generate_map()

    def generate_map(self):
        # Place Rabbit at a random position
        self.rabbit_x, self.rabbit_y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
        self.grid[self.rabbit_x][self.rabbit_y] = 'r'

        # Place Carrots randomly
        for _ in range(self.num_carrots):
            self.carrot_x, self.carrot_y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            while self.grid[self.carrot_x][self.carrot_y] != '-':
                self.carrot_x, self.carrot_y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.grid[self.carrot_x][self.carrot_y] = 'c'

        # Place Rabbit Holes randomly
        for _ in range(self.num_holes):
            self.hole_x, self.hole_y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            while self.grid[self.hole_x][self.hole_y] != '-':
                self.hole_x, self.hole_y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            self.grid[self.hole_x][self.hole_y] = 'O'

    def display_map(self):
        for row in self.grid:
            print(' '.join(row))

    
    def move_rabbit_left(self):
        if self.rabbit_y > 0 and self.grid[self.rabbit_x][self.rabbit_y - 1] != 'c' and self.grid[self.rabbit_x][self.rabbit_y - 1] != 'O' :
            self.grid[self.rabbit_x][self.rabbit_y], self.grid[self.rabbit_x][self.rabbit_y - 1] = self.grid[self.rabbit_x][self.rabbit_y - 1], self.grid[self.rabbit_x][self.rabbit_y]
            self.rabbit_y -=1
        elif self.rabbit_y > 0 and self.grid[self.rabbit_x][self.rabbit_y - 1] == 'c':
            self.both_x=self.rabbit_x
            self.both_y=self.rabbit_y - 1
            self.bothatsame=True
        elif self.rabbit_y > 0 and self.grid[self.rabbit_x][self.rabbit_y - 1] == 'O':
            self.jump_x=self.rabbit_x 
            self.jump_y=self.rabbit_y - 2
            self.jump=True


    def move_rabbit_right(self):
        if self.rabbit_y < self.grid_size - 1 and self.grid[self.rabbit_x][self.rabbit_y + 1] != 'c' and self.grid[self.rabbit_x][self.rabbit_y + 1] != 'O' :
            self.grid[self.rabbit_x][self.rabbit_y], self.grid[self.rabbit_x][self.rabbit_y + 1] = self.grid[self.rabbit_x][self.rabbit_y + 1], self.grid[self.rabbit_x][self.rabbit_y]
            self.rabbit_y += 1
        elif self.rabbit_y < self.grid_size - 1 and self.grid[self.rabbit_x][self.rabbit_y + 1] == 'c':
            self.both_x=self.rabbit_x 
            self.both_y=self.rabbit_y + 1
            self.bothatsame=True
        elif self.rabbit_y < self.grid_size - 1 and self.grid[self.rabbit_x][self.rabbit_y + 1] == 'O':
            self.jump_x=self.rabbit_x 
            self.jump_y=self.rabbit_y + 2
            self.jump=True


    def move_rabbit_up(self):
        if self.rabbit_x > 0 and self.grid[self.rabbit_x - 1][self.rabbit_y] != 'c' and self.grid[self.rabbit_x - 1][self.rabbit_y] != 'O':
            self.grid[self.rabbit_x][self.rabbit_y], self.grid[self.rabbit_x - 1][self.rabbit_y] = self.grid[self.rabbit_x - 1][self.rabbit_y], self.grid[self.rabbit_x][self.rabbit_y]
            self.rabbit_x -=1
        elif self.rabbit_x > 0 and self.grid[self.rabbit_x - 1][self.rabbit_y] == 'c':
            self.both_x=self.rabbit_x - 1
            self.both_y=self.rabbit_y
            self.bothatsame=True
        elif self.rabbit_x > 0 and self.grid[self.rabbit_x - 1][self.rabbit_y] == 'O':
            self.jump_x=self.rabbit_x - 2
            self.jump_y=self.rabbit_y
            self.jump=True
        
        

    def move_rabbit_down(self):
        if self.rabbit_x < self.grid_size - 1 and self.grid[self.rabbit_x + 1][self.rabbit_y] != 'c'  and self.grid[self.rabbit_x + 1][self.rabbit_y] != 'O':
            self.grid[self.rabbit_x][self.rabbit_y], self.grid[self.rabbit_x + 1][self.rabbit_y] = self.grid[self.rabbit_x + 1][self.rabbit_y], self.grid[self.rabbit_x][self.rabbit_y]
            self.rabbit_x += 1
        elif self.rabbit_x < self.grid_size - 1 and self.grid[self.rabbit_x + 1][self.rabbit_y] == 'c':
            self.both_x=self.rabbit_x + 1
            self.both_y=self.rabbit_y
            self.bothatsame=True
        elif self.rabbit_x < self.grid_size - 1 and self.grid[self.rabbit_x + 1][self.rabbit_y] == 'O':
            self.jump_x=self.rabbit_x + 2
            self.jump_y=self.rabbit_y
            self.jump=True
     


    def pick_carrot(self):
        if self.bothatsame:
             if self.grid[self.both_x][self.both_y] == 'c':
                self.grid[self.both_x][self.both_y] = 'R'
                self.grid[self.rabbit_x][self.rabbit_y] ='-'
                self.rabbit_x=self.both_x
                self.rabbit_y=self.both_y
                self.rabbit_has_carrot = True
                self.bothatsame = False
        elif self.rabbit_has_carrot:
            if  0 <= self.rabbit_x-1< self.grid_size and self.grid[self.rabbit_x-1][self.rabbit_y]=='O' :
                self.grid[self.rabbit_x-1][self.rabbit_y]='r'
                self.gameover=True
                print("Congratulations!!! Game Over")

            elif  0 <= self.rabbit_x+1< self.grid_size and self.grid[self.rabbit_x+1][self.rabbit_y]=='O' :
                self.grid[self.rabbit_x+1][self.rabbit_y]='r'
                self.gameover=True
                print("Congratulations!!! Game Over")

            elif  0 <= self.rabbit_y-1< self.grid_size and self.grid[self.rabbit_x][self.rabbit_y-1]=='O' :
                self.grid[self.rabbit_x][self.rabbit_y-1]='r'
                self.gameover=True
                print("Congratulations!!! Game Over")

            elif  0 <= self.rabbit_y+1< self.grid_size and self.grid[self.rabbit_x][self.rabbit_y+1]=='O' :
                self.grid[self.rabbit_x][self.rabbit_y+1]='r'
                self.gameover=True
                print("Congratulations!!! Game Over")
                

    def jump_hole(self):
        if self.jump and 0 <= self.jump_x < self.grid_size and 0 <= self.jump_y < self.grid_size :
            self.grid[self.rabbit_x][self.rabbit_y], self.grid[self.jump_x][self.jump_y] = self.grid[self.jump_x][self.jump_y], self.grid[self.rabbit_x][self.rabbit_y]
            self.rabbit_x=self.jump_x
            self.rabbit_y=self.jump_y
            self.jump=False
    
    

def main():
    grid_size = int(input("Enter grid size: "))
    
    while True:
        num_carrots = int(input("Enter number of carrots (greater than 1): "))
        if num_carrots > 1:
            break
        else:
            print("Please enter a number greater than 1 for carrots.")
    
    while True:
        num_holes = int(input("Enter number of rabbit holes (greater than 1): "))
        if num_holes > 1:
            break
        else:
            print("Please enter a number greater than 1 for rabbit holes.")

    game_map = GameMap(grid_size, num_carrots, num_holes)

    while True and not game_map.gameover:
        game_map.display_map()
        print("Controls: 'a' (left), 'd' (right), 'w' (up), 's' (down), 'p' (pick carrot), 'j' (jump hole), 'q' (quit)")
        action = input("Enter your move: ").lower()


        if action == 'q':
            break
        elif action == 'a':
            game_map.move_rabbit_left()
        elif action == 'd':
            game_map.move_rabbit_right()
        elif action == 'w':
            game_map.move_rabbit_up()
        elif action == 's':
            game_map.move_rabbit_down()
        elif action == 'p':
            game_map.pick_carrot()
        elif action == 'j':
            game_map.jump_hole()

if __name__ == "__main__":
    main()
