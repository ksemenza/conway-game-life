import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
simplegui.Frame._hide_status = True
simplegui.Frame._keep_timers = True



WIDTH = 500
HEIGHT = 500
SCALE = 20.0
pX = 0
pY = 0

# Define classes

class LifeGame:
    def __init__(self):
        self.cells = {}
        self.generation = 0

    def addCell(self, x, y):
        'add cell to life_game'
        self.cells[(x,y)] = True

    def getCells(self):
        'return list of cell coordinates'
        return self.cells.keys()

    def toggle(self, x, y):
        if (x in self.cells and y in self.cells[x]):
            del self.cells[(x,y)]
        else:
            self.cells[(x,y)] = True

    def countNeighbor(self, x, y):
        count = 0
        for nx in [x - 1, x, x + 1]:
            for ny in [y - 1, y, y + 1]:
                if ((x != nx or y != ny) and (nx,ny) in self.cells):
                    count += 1
                    # Greater than three is always bad
                    if (count > 3):
                        return count
        return count

    def getGeneration(self):
        return self.generation

    def getCellCount(self):
        return len(self.cells)


    def regenerate(self):
        newCells = {}
        tested = {}
        # Loop through cells
        for cell in self.cells.keys():
            cx = cell[0]
            cy = cell[1]
            # Loop through cell and neighbor
            for x in (cx - 1, cx, cx + 1):
                for y in (cy - 1, cy, cy + 1):
                    # Only test each cell once
                    if ( not (x,y) in tested ):
                        tested[(x,y)] = True
                        # Count neighbor of cell and neighbor
                        count = self.countNeighbor(x, y)
                        if ( ( count == 3 ) or
                            (( count == 2 ) and (x,y) in self.cells ) ):
                            newCells[(x,y)] = True
        self.cells = newCells
        self.generation += 1

# Define global variables (program state)
scale = SCALE
px = pX
py = pY
life_game = None
gen_label = None
cnt_label = None
timer = None
prev_position = [-1, -1]

# Defined helper functions

def clear():
    global life_game
    life_game = LifeGame()

def reset():
    global life_game, scale
    clear()
    scale = SCALE
    px = pX
    py = pY

# Grid Center
    x = WIDTH // scale // 2
    y = HEIGHT // scale // 2

    life_game.addCell(x, y - 1)
    life_game.addCell(x + 1, y - 1)
    life_game.addCell(x - 1, y)
    life_game.addCell(x, y)
    life_game.addCell(x, y + 1)
    

# Define Bee Hive function
def beeHive():
    global life_game, scale
    clear()
    scale = SCALE
    px = pX
    py = pY
    x = WIDTH // scale // 2
    y = HEIGHT // scale // 2
    life_game.addCell(x, y + 1)
    life_game.addCell(x, y - 1)
    life_game.addCell(x - 2, y)
    life_game.addCell(x + 1, y)
    life_game.addCell(x - 1, y -1)
    life_game.addCell(x -1, y +1)
# Define Blinker function

def blinker():
    global life_game, scale
    clear()
    scale = SCALE
    px = pX
    py = pY
    x = WIDTH // scale // 2
    y = HEIGHT // scale // 2
    life_game.addCell(x, y + 1)
    life_game.addCell(x, y - 1)
    life_game.addCell(x , y)
    
    
def beacon():
    global life_game, scale
    clear()
    scale = SCALE
    px = pX
    py = pY
    x = WIDTH // scale // 2
    y = HEIGHT // scale // 2
    life_game.addCell(x - 1, y)
    life_game.addCell(x - 1, y + 1)
    life_game.addCell(x - 2, y)
    life_game.addCell(x - 2, y + 1)
    life_game.addCell(x, y - 1)
    life_game.addCell(x, y - 2)
    life_game.addCell(x + 1 , y - 1)
    life_game.addCell(x + 1 , y - 2)


# Define event handler functions

def timer_handler():
    global life_game
    life_game.regenerate()


def start_handler():
    timer.start()

def stop_handler():
    timer.stop()

def clear_handler():
    timer.stop()
    clear()

def reset_handler():
    timer.stop()
    reset()
    
def beeHive_handler():
    timer.stop()
    beeHive()
    
def blinker_handler():
    timer.stop()
    blinker()
def beacon_handler():
    timer.stop()
    beacon()


# Translate mouse position to cell and toggle it
def mouse_handler(position):
    global prev_position
    x = position[0] // scale + px
    y = position[1] // scale + px
    if ( x != prev_position[0] or y != prev_position[1] ):
        life_game.toggle(x, y)
        prev_position = [x, y]

# Handler to draw on canvas
def draw(canvas):
    # Draw grid
    for y in range(int(HEIGHT / scale)):  
        canvas.draw_line((0, y * scale), (WIDTH, y * scale), 1, "purple")
    for x in range(int(WIDTH / scale)):  
        canvas.draw_line((x * scale, 0), (x * scale, HEIGHT), 1, "purple")
    # Loop through cells
    for cell in life_game.getCells():
        x = cell[0] - px
        y = cell[1] - py
        if ( x >= 0 and x * scale < WIDTH and y >=0 and y * scale < HEIGHT):
            canvas.draw_polygon([[x * scale + 1, y * scale + 1],
                             [x * scale + 1, (y + 1) * scale - 1],
                             [(x + 1) * scale - 1, (y + 1) * scale - 1],
                             [(x + 1) * scale - 1, y * scale + 1]
                             ], 1, "green", "green")
    # Update labels
    gen_label.set_text("Generation: "+str(life_game.getGeneration()))
    cnt_label.set_text("Living Cells: "+str(life_game.getCellCount()))

# Create a frame
frame = simplegui.create_frame("Guin Dev Present Conway's Game of Life", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Register event handlers
gen_label = frame.add_label("")
cnt_label = frame.add_label("")
frame.add_button("BeeHive", beeHive_handler)
frame.add_button("Blinker", blinker_handler)
frame.add_button("Beacon", beacon_handler)
frame.add_label("")
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)
frame.add_button("Clear", clear_handler)
frame.add_label("")
frame.set_mousedrag_handler(mouse_handler)

# Initialize
reset()

# Start frame and timers 
#TODO change timer to include user input values
timer = simplegui.create_timer(100, timer_handler)
frame.start()
