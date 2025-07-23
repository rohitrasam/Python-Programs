import OpenGL.GL as gl
from OpenGL.GL.shaders import compileProgram, compileShader, ShaderProgram
import pygame as pg
import numpy as np
import ctypes
import math


WIDTH, HEIGHT = 720, 720

class App:

    def __init__(self) -> None:
        
        pg.init()
        pg.display.set_mode((WIDTH, HEIGHT), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        # gl.glClearColor(0.1, 0.2, 0.9, 1.0)
        self.fps = 60
        self.shader = self.createShader("D:/Python Programs/opengl/shaders/shading2.shader")
        self.screen = Screen()
        gl.glUseProgram(self.shader)
        self.run()

    def run(self) -> None:
        counter = 0
        running = True

        while running:


            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    running = False

            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            
            gl.glUseProgram(self.shader)

            self.clock.tick(self.fps)
            timeLoc = gl.glGetUniformLocation(self.shader, "time")
            gl.glUniform1f(timeLoc, counter)
            resolutionLoc = gl.glGetUniformLocation(self.shader, "u_resolution")
            gl.glUniform2f(resolutionLoc, WIDTH, HEIGHT)

            counter += 0.01

            gl.glBindVertexArray(self.screen.vao)
            gl.glDrawElements(gl.GL_TRIANGLES, len(self.screen.indices), gl.GL_UNSIGNED_INT, None)


            pg.display.flip()

        self.quit()

    def createShader(self, shaderPath: str) -> ShaderProgram:

        with open(shaderPath, 'r') as f:
            shaderSource = f.readlines()
        
        shaders = {}
        for line in shaderSource:
            if line.startswith("#shader"):
                if line.endswith("vertex\n"):
                    shaderType = "vertex"
                    shaders[shaderType] = []
                else:
                    shaderType = "frag"
                    shaders[shaderType] = []
            else:
                shaders[shaderType].append(line)

        program = compileProgram(compileShader(shaders["vertex"], gl.GL_VERTEX_SHADER), compileShader(shaders["frag"], gl.GL_FRAGMENT_SHADER))
        return program


    def quit(self) -> None:
        gl.glDeleteProgram(self.shader)
        self.screen.destroy()
        pg.quit()



class Screen:

    def __init__(self) -> None:
        
        # self.vertices = np.array([
        #     -0.5,  0.5, 0, 1.0, 0.1, 0.5,
        #      0.5,  0.5, 0, 0.1, 1.0, 0.5,
        #      0.5, -0.5, 0, 0.1, 0.5, 1.0,
        #     -0.5, -0.5, 0, 0.5, 1.0, 0.1,
        # ], dtype=np.float32)

        self.vertices = np.array([
            -1,  1, 0, 1.0, 0.1, 1,
             1,  1, 0, 0.1, 1.0, 1,
             1, -1, 0, 0.1, 1, 1.0,
            -1, -1, 0, 0.5, 1.0, 0.1,
        ], dtype=np.float32)

        self.vertex_count = 4
        
        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)

        self.vbo = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, gl.GL_STATIC_DRAW)

        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(0)
        
        gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(12))
        gl.glEnableVertexAttribArray(1)

        self.ebo = gl.glGenBuffers(1)
        self.indices = np.array([
            0, 1, 2,
            0, 3, 2
        ], dtype=np.uint)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, gl.GL_STATIC_DRAW)


    def destroy(self):
        gl.glDeleteVertexArrays(1, (self.vao,))
        gl.glDeleteBuffers(2, (self.vbo, self.ebo))


if __name__ == '__main__':
    app = App()