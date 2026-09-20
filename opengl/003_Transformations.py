import ctypes
import pygame as pg
import OpenGL.GL as gl
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr

class Cube:

    def __init__(self, position, eulers) -> None:

        self.position = np.array(position, dtype=np.float32)
        self.eulers = np.array(eulers, dtype=np.float32)


class App:

    def __init__(self) -> None:
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        gl.glClearColor(0.1, 0.2, 0.2, 1)   # declaring which color to show on the screen
        gl.glEnable(gl.GL_BLEND)    # used for transparent bg texture
        gl.glEnable(gl.GL_DEPTH_TEST)    # check if objects are drawing in front of each other properly
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)  # used for transparent bg texture
        # self.shader = self.createShader("shaders/003_vert.shader", "shaders/003_frag.shader")
        self.shader = self.createShader("shaders/003_vert.shader", "shaders/003_frag.shader")
        gl.glUseProgram(self.shader)
        self.cube= Cube(position=[0, 0, -3], 
                        eulers=[0, 0, 0])
        
        self.cube_mesh = CubeMesh()
        self.alien_tex = Material("gfx/1.png")
        proj_trans = pyrr.matrix44.create_perspective_projection(
                                                            fovy=45, 
                                                            aspect=640/480, 
                                                            near=0.1,   # anything nearer than 0.1 units won't be drawn 
                                                            far=10, # anything farther than 10 units won't be drawn
                                                            dtype=np.float32
                                                        )
        print("line 39", proj_trans)
        gl.glUniform1i(gl.glGetUniformLocation(self.shader, "imageTexture"), 0) # sending in 1 int param value to our uniform location, also settin our sampler to 0(sampling texture 0; Material.use() 1st line)
                            # location of projection uniform matrix, no. of matrices sending to the shader, transpose?, matrix to send
        gl.glUniformMatrix4fv(gl.glGetUniformLocation(self.shader, "projection"), 1, gl.GL_FALSE, proj_trans)   # sending uniform in form of matrix

        self.modelMatrixLocation = gl.glGetUniformLocation(self.shader, "model")
        # gl.glUseProgram(self.shader)
        self.mainloop()

    def createShader(self, vertexFilePath, fragFilePath):

        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragFilePath, 'r') as f:
            frag_src = f.readlines()

        shader = compileProgram(compileShader(vertex_src, gl.GL_VERTEX_SHADER), compileShader(frag_src, gl.GL_FRAGMENT_SHADER))
        return shader

    def mainloop(self):
        running = True
        # gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # update cube
            # self.cube.eulers[0] += 0.5
            # if self.cube.eulers[0] > 360:
            #     self.cube.eulers[0] -= 360
            self.cube.eulers[2] += 0.5
            if self.cube.eulers[2] > 360:
                self.cube.eulers[2] -= 360
            # self.cube.eulers[1] += 0.5
            # if self.cube.eulers[1] > 360:
            #     self.cube.eulers[1] -= 360

            # refresh screen
            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # clear the depth buffer as well for every frame
        
            gl.glUseProgram(self.shader)
            self.alien_tex.use()

            model_transform = pyrr.matrix44.create_identity(dtype=np.float32)
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform, 
                m2=pyrr.matrix44.create_from_eulers(
                    eulers=self.cube.eulers * np.pi/180, 
                    dtype=np.float32
                    )
                )
            model_transform = pyrr.matrix44.multiply(
                m1=model_transform, 
                m2=pyrr.matrix44.create_from_translation(
                    vec=self.cube.position, 
                    dtype=np.float32
                    )
                )
            gl.glUniformMatrix4fv(self.modelMatrixLocation, 1, gl.GL_FALSE, model_transform)
            gl.glBindVertexArray(self.cube_mesh.vao) # binds vertex array of the index saved in self.triangle.vao variable 
            gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.cube_mesh.vertex_count) # looks in the variable we have bound and takes the data and draws our triangle

            self.clock.tick(60)
            pg.display.flip()
            
        self.quit()
    
    def quit(self):
        self.cube_mesh.destroy()
        self.alien_tex.destroy()
        gl.glDeleteProgram(self.shader)
        pg.quit()


class CubeMesh:

    def __init__(self) -> None:

        # 3 lines is one triangle 
        # 12 triangles needed to create one cube
        # 2 triangles to create one side of a cube, a cube has 6 sides
        #  x, y, z, s, t
        self.vertices = np.array([
            -0.5, -0.5, -0.5, 0, 0,
             0.5, -0.5, -0.5, 1, 0,
             0.5,  0.5, -0.5, 1, 1,

             0.5,  0.5, -0.5, 1, 1,
            -0.5,  0.5, -0.5, 0, 1,
            -0.5, -0.5, -0.5, 0, 0,

            -0.5, -0.5,  0.5, 0, 0,
             0.5, -0.5,  0.5, 1, 0,
             0.5,  0.5,  0.5, 1, 1,

             0.5,  0.5,  0.5, 1, 1,
            -0.5,  0.5,  0.5, 0, 1,
            -0.5, -0.5,  0.5, 0, 0,

            -0.5,  0.5,  0.5, 1, 0,
            -0.5,  0.5, -0.5, 1, 1,
            -0.5, -0.5, -0.5, 0, 1,

            -0.5, -0.5, -0.5, 0, 1,
            -0.5, -0.5,  0.5, 0, 0,
            -0.5,  0.5,  0.5, 1, 0,

             0.5,  0.5,  0.5, 1, 0,
             0.5,  0.5, -0.5, 1, 1,
             0.5, -0.5, -0.5, 0, 1,

             0.5, -0.5, -0.5, 0, 1,
             0.5, -0.5,  0.5, 0, 0,
             0.5,  0.5,  0.5, 1, 0,

            -0.5, -0.5, -0.5, 0, 1,
             0.5, -0.5, -0.5, 1, 1,
             0.5, -0.5,  0.5, 1, 0,

             0.5, -0.5,  0.5, 1, 0,
            -0.5, -0.5,  0.5, 0, 0,
            -0.5, -0.5, -0.5, 0, 1,

            -0.5,  0.5, -0.5, 0, 1,
             0.5,  0.5, -0.5, 1, 1,
             0.5,  0.5,  0.5, 1, 0,

             0.5,  0.5,  0.5, 1, 0,
            -0.5,  0.5,  0.5, 0, 0,
            -0.5,  0.5, -0.5, 0, 1
        ], dtype=np.float32)    # set to 32 bit float IMP!!

        self.vertex_count = self.vertices.shape[0] // 5 # 36 vertices in a cube

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
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 20, ctypes.c_void_p(0))   # then we describe how it is laid out in the vbo

        gl.glEnableVertexAttribArray(1)
        # attribute 1 is texture, how many points in each attribute, dtype, normalized?, stride(how may bytes) to get to next color(6 X 4bytes = 24), offset i.e the starting position of the color attribute
        gl.glVertexAttribPointer(1, 2, gl.GL_FLOAT, gl.GL_FALSE, 20, ctypes.c_void_p(12))

    def destroy(self):
        gl.glDeleteVertexArrays(1, (self.vao,))
        gl.glDeleteBuffers(1, (self.vbo,))


class Material:

    def __init__(self, filepath) -> None:
        self.texture = gl.glGenTextures(1)  # generate a texture for us, allocate space in memory, returns index of the space allocated
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)    # bind it as the current texture that we are going to be work with
                        
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)    # will repeat the texture
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)    # will repeat the texture
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)   
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
        image = pg.image.load(filepath).convert_alpha()
        image_width, image_height = image.get_size()
        image_data = pg.image.tobytes(image, 'RGBA')   # to make opengl understand the format of the image

                    # texture location that we are loading to, mipmap lvl, specify internal format the image data will be stored in, width, height, border_color, format we are loading in, data format, actual image data 
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, image_width, image_height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, image_data)
        gl.glGenerateMipmap(gl.GL_TEXTURE_2D)   # generate a mipmap of the image that is loaded in

    
    def use(self):
        gl.glActiveTexture(gl.GL_TEXTURE0)  # tell opengl that we are working with texture unit 0
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)    # bind texture into location 0

    def destroy(self):
        gl.glDeleteTextures(1, (self.texture,))


if __name__ == '__main__':
    app = App()