import ctypes
import pygame as pg
import OpenGL.GL as gl
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader

class App:

    def __init__(self) -> None:
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        gl.glClearColor(0.1, 0.2, 0.2, 1)   # declaring which color to show on the screen
        self.shader = self.createShader("shaders/001_vert.shader", "shaders/001_frag.shader")
        self.triangle = Triangle()
        # gl.glUseProgram(self.shader)
        self.mainloop()

    def createShader(self, vertexFilePath, fragFilePath):

        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragFilePath, 'r') as f:
            frag_src = f.readlines()
        print(frag_src)

        shader = compileProgram(compileShader(vertex_src, gl.GL_VERTEX_SHADER), compileShader(frag_src, gl.GL_FRAGMENT_SHADER))
        return shader

    def mainloop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                
            # refresh screen
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        
            gl.glUseProgram(self.shader)
            gl.glBindVertexArray(self.triangle.vao) # binds vertex array of the index saved in self.triangle.vao variable 
            gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.triangle.vertex_count) # looks in the variable we have bound and takes the data and draws our triangle

            self.clock.tick(60)
            pg.display.flip()
            
        self.quit()
    
    def quit(self):
        self.triangle.destroy()
        gl.glDeleteProgram(self.shader)
        pg.quit()


class Triangle:

    def __init__(self) -> None:

        #  x, y, z, r, g, b
        self.vertices = np.array((
            -0.5, -0.5, 0.0, 0.25, 0.5, 1.0,
            0.5, -0.5, 0.0, 0.5, 1.0, 0.25,
            0.0, 0.5, 0.0, 1.0, 0.25, 0.5,
        ), dtype=np.float32)    # set to 32 bit float IMP!!

        self.vertex_count = 3

        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)
        # our vao has our vbo tied up in it, always bind vao before vbo
        self.vbo = gl.glGenBuffers(1)   # tell opengl to generate 1 buffer for us and the int index is stored in self.vbo, probably index 0
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo) # we bind the buffer, when we talk about GL_ARRAY_BUFFER we are talking about self.vbo array
                        # where to load,    how many bytes we sent, data to load in, how we plan to use the data we loaded
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, gl.GL_STATIC_DRAW) # func used to ship self.vertices to our graphics card

        """ can access these attribs in shaders through layout (location=0) in ....."""
        gl.glEnableVertexAttribArray(0) # 1st we enable the attribute, 
        # here attribute 0 is position, how many points in each attribute , dtype, normalized?, stride(how may bytes) to get to next position(6 X 4bytes = 24), offset i.e the starting position of the position attribute
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(0))   # then we describe how it is laid out in the vbo
        gl.glEnableVertexAttribArray(1)
        # attribute 1 is color, how many points in each attribute, dtype, normalized?, stride(how may bytes) to get to next color(6 X 4bytes = 24), offset i.e the starting position of the color attribute
        gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        gl.glDeleteVertexArrays(1, (self.vao,))
        gl.glDeleteBuffers(1, (self.vbo,))

if __name__ == '__main__':
    app = App()