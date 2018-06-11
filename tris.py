import pygame

s_size = 300
line_size = 2

done = False

class TrisTable(object):
    def __init__(self, size = s_size):
        pygame.init()
        screen = pygame.display.set_mode((size, size))
        self.screen = screen
        self.size = int(size / 3)
        self.table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.table[0][0] = 1
        self.table[2][1] = -1 
        self.draw_table()

    def draw_table(self):
        self.screen.fill((0,0,0))
        print(self.table)
        for cnt in range(3):
            pygame.draw.line(self.screen, (255, 255, 255), 
                (0, (cnt + 1) * self.size), 
                (self.size * 3, (cnt + 1) * self.size))
            pygame.draw.line(self.screen, (255, 255, 255), 
                ((cnt + 1) * self.size, 0), 
                ((cnt + 1) * self.size, self.size * 3))
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == 1:
                    self.draw_tris_circle((i,j))
                elif self.table[i][j] == -1:
                    self.draw_tris_x((i,j))

    def draw_cicle(self, pos):
        self.draw_simbol(1, pos)

    def draw_x(self, pos):
        self.draw_simbol(-1, pos)

    def draw_simbol(self, simbol, pos):
        i,j = pos
        self.table[i][j] = simbol
        self.draw_table()

    def draw_tris_circle(self, pos):
        pos = (int(pos[0] * s_size/3 + s_size/6), int(pos[1] * s_size/3 + s_size/6))
        pygame.draw.circle(self.screen, (255, 0, 0), pos , int(s_size/10) )

    def draw_tris_x(self, pos):
        pos = (int(pos[0] * s_size/3 + s_size/6), int(pos[1] * s_size/3 + s_size/6))
        dist = int(s_size/10)
        pygame.draw.line(self.screen, (0, 255, 0), (pos[0] - dist, pos[1] - dist), (pos[0] + dist, pos[1] + dist) , int(s_size/40) )
        pygame.draw.line(self.screen, (0, 255, 0), (pos[0] - dist, pos[1] + dist), (pos[0] + dist, pos[1] - dist) , int(s_size/40) )

    def draw_tris_cursor(self, pos):
        self.draw_table()
        pos = (int(pos[0] * s_size/3 + s_size/6), int(pos[1] * s_size/3 + s_size/6))
        pygame.draw.circle(self.screen, (255, 255, 255), pos , int(s_size/30) )

tris_table = TrisTable()

current_pos = [0,0]
simbol = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_pos[0] = (current_pos[0] - 1) % 3
            if event.key == pygame.K_RIGHT:
                current_pos[0] = (current_pos[0] + 1) % 3
            if event.key == pygame.K_UP:
                current_pos[1] = (current_pos[1] - 1) % 3
            if event.key == pygame.K_DOWN:
                current_pos[1] = (current_pos[1] + 1) % 3
            if event.key == pygame.K_RETURN:
                tris_table.draw_simbol(simbol, current_pos)
                simbol *= -1
            tris_table.draw_tris_cursor(current_pos)
        if event.type == pygame.QUIT:
                done = True        
    pygame.display.flip()
