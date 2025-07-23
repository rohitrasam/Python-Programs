from sys import exit
import pygame as pg

def findNorm(a, b):
    # (-y, x) is the vector perpendicular to vector (x, y) 
    norm_axis = (-(b[1] - a[1]), b[0] - a[0])   # axis normal to vector formed by points b - a
    return norm_axis

def dot(x, y):
    return x[0]*y[0] + x[1]*y[1]

def sat_collision(polyA, polyB):
    seprations = 0
    for point in range(len(polyA)):
        norm_vec = findNorm(polyA[point], polyA[(point+1)%len(polyA)])

        for points_b in polyB:
            minSep = 9999999999
            vec_b_a = (points_b[0] - polyA[point][0], points_b[1] - polyA[point][1])
            minSep = min(minSep, dot(vec_b_a, norm_vec))
            
        seprations = min(minSep, seprations)
    return seprations

if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((500, 500))
    clock = pg.Clock()
    
    poly1 = [(250, 50), (450, 250), (50, 250)]
    

    while True:

        poly2_mid = pg.mouse.get_pos()
        poly2 = [
                 (poly2_mid[0]+50, poly2_mid[1]-50),
                 (poly2_mid[0]+50, poly2_mid[1]+50),
                 (poly2_mid[0]-50, poly2_mid[1]+50),
                 ]
        
        display.fill((0, 0, 0))
        pg.draw.polygon(display, (255, 255, 255), poly1)
        pg.draw.polygon(display, (255, 150, 250), poly2)

        print(sat_collision(poly1, poly2), sat_collision(poly2, poly1))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
        pg.display.update()
        clock.tick(60)