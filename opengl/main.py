import ctypes
import numpy as np
from sys import exit
import pygame as pg
import OpenGL.GL as gl

class App:

    def __init__(self) -> None:

        pg.init()
        pg.display.set_mode((1000, 720), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()

        # initialize opengl, 
        gl.glClearColor(0.0, 0.5, 0.8, 0.1)
        self.main()

    def main(self):

        running = True
        while running:
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    self.quit()
            
            # refresh screen
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            pg.display.flip() # or update() any will do

            self.clock.tick(60)

    def quit(self):
        pg.quit()
        exit()


class Triangle:
    
    def __init__(self) -> None:
        
        # x, y, z, r, g, b
        self.vertices = np.array([
                            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                            0.5, 0.5, 0.0, 0.0, 0.0, 1.0
                         ], dtype=np.float32)

        self.vertex_count = 3

        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)
        self.vbo = gl.glGenBuffers(1) # vertex buffer object
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, gl.GL_STATIC_DRAW)
        gl.glEnableVertexAttribArray(0) # attribute 0 is position
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(1) # attribute 1 is color
        gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        
        gl.glDeleteVertexArrays(1, (self.vao,))
        gl.glDeleteBuffers(1, (self.vbo,))


if __name__ == '__main__':
    app = App()
    app.main()

