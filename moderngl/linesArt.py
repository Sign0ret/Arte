import moderngl
import numpy as np

from PIL import Image

ctx = moderngl.create_standalone_context()

prog = ctx.program(
    vertex_shader='''
        #version 330

        in vec2 in_vert;
        in vec3 in_color;

        out vec3 v_color;

        void main() {
            v_color = in_color;
            gl_Position = vec4(in_vert, 0.0, 1.0);
        }
    ''',
    fragment_shader='''
        #version 330

        in vec3 v_color;

        out vec3 f_color;

        void main() {
            f_color = v_color;
    
        }
    ''',
)

r = np.ones(50)
g = np.zeros(50)
b = np.zeros(50)

def line(x1, y1, x2, y2):
    """ creates a line based on the function received and the input values for x and y. """
    x = np.linspace(-x1,x1, 50)
    y = np.sin((x))
    z = np.cos((y)) 
    # x = np.linspace(x1, x2, 50)  # Adjust number of points as needed
    # y_positive = np.sqrt(5**2 - x**2)
    # y_negative = -np.sqrt(5**2 - x**2)
    # y = np.concatenate([y_positive, y_negative])
    # x = np.concatenate([x, x])

    vertices = np.dstack([z, y, r, g, b])
    vbo = ctx.buffer(vertices.astype('f4').tobytes())
    vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_color')
    fbo = ctx.simple_framebuffer((512, 512))
    fbo.use()
    fbo.clear(0.0, 0.0, 0.0, 1.0)
    vao.render(moderngl.LINE_STRIP)
    Image.frombytes('RGB', fbo.size, fbo.read(), 'raw', 'RGB', 0, -1).show()


def linesArtDrawing(n):
    x1 = 10
    y1 = 25
    x2 = 50
    y2 = 25
    for i in range(n):
        line(x1, y1, x2, y2)


linesArtDrawing(1)
