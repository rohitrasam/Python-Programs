import moderngl as gl
import pygame as pg
# import numpy as np
from array import array

pg.init()

screen = pg.display.set_mode((600, 600), pg.OPENGL | pg.DOUBLEBUF)

clock = pg.time.Clock()

# img = pg.transform.scale2x(pg.image.load("Space shooter\data\imgs\space_background_pack\parallax-space-1.png"))
surf = pg.Surface((500, 500))

ctx = gl.create_context()
quad_buffer = ctx.buffer(data=array('f', [
   # x  , y  , u  , v 
    -1.0, 1.0, 0.0, 0.0,    # top left
    1.0, 1.0, 1.0, 0.0,     # top right
    -1.0, -1.0, 0.0, 1.0,   # bottom left
    1.0, -1.0, 1.0, 1.0,    # bottom right
]))

vert_shader = """
    #version 330 core

    in vec2 vert;
    in vec2 texCoord;
    out vec2 uvs;

    void main(){
        uvs = texCoord;
        gl_Position = vec4(vert, 0.0, 1.0);
    }
"""

frag_shader  = """
    #version 330 core
    
    uniform vec2 res;
    out vec4 f_color;

    float rectshape(vec2 pos, vec2 scale){
        scale = vec2(0.5)-scale*0.5;
        vec2 shaper = vec2(step(scale.x, pos.x), step(scale.y, pos.y));
        shaper *= vec2(step(scale.x, 1.0-pos.x), step(scale.y, 1.0-pos.y));
        return shaper.x * shaper.y;
    }


    void main(){
        vec2 pos = gl_FragCoord.xy / res;
        vec3 color = vec3(0.0);
        float rectangle = rectshape(pos, vec2(0.3, 0.5));
        color = vec3(rectangle);
        f_color = vec4(color.xy*0.2, color.z*0.5, 1.0);
    }


"""

""" resolution helps us with scaling """

# Circle
"""
    #version 330 core

    uniform vec2 res;

    float circleshape(vec2 position, float rad){
        return step(rad, length(position-vec2(0.5)));
    }
    
    void main(){
        vec2 position = gl_FragCoord.xy / res;
        vec3 color = vec3(0.0);
        float circle = circleshape(position, 0.2);
        color = vec3(circle);
        gl_FragColor = vec4(color, 1.0);    
    }   

"""

"""
    #version 330 core

    void main(){
        vec3 color = vec3(0.3, 0.4, 0.7);
        gl_FragColor = vec4(color, 0.5);
    }
"""

"""
    #version 330 core

    uniform sampler2D tex;
    uniform float time;
    
    in vec2 uvs;
    out vec4 f_color;

    void main(){
        vec2 sample_pos = vec2(uvs.x + cos(time*0.01), uvs.y+sin(time*0.01));
        vec3 color = texture(tex, sample_pos).rgb;
        f_color = vec4(0.0, color.gb, 1.0);
    }
"""

prog = ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)

# '2f 2f' = 'vert texCoord'
render_obj = ctx.vertex_array(prog, [(quad_buffer, '2f 2f', 'vert', 'texCoord')]) # should match `in` values in the vertex shader

# convert pygame surf to opengl texture
def surf_to_text(surf):
    tex = ctx.texture(surf.get_size(), 4)
    tex.filter = (gl.NEAREST, gl.NEAREST)
    tex.swizzle = 'RGBA'
    view = surf.get_view('2')
    print(view)
    tex.write(view)
    return tex

# time = 0
 
while True:

    screen.get_view()
    screen.fill("white")
    # screen.blit(img, pg.mouse.get_pos())
    surf.fill("white")
    screen.blit(surf, (50, 50))
    # time += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    frame_tex = surf_to_text(screen)
    frame_tex.use(0)
    # prog['tex'] = 0
    # prog['time'] = time
    prog['res'] = screen.get_size()
    render_obj.render(mode=gl.TRIANGLE_STRIP)

    pg.display.flip()
    frame_tex.release() # free/delete
    clock.tick(60)