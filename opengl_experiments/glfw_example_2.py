import ctypes

import numpy
from OpenGL.GL import *
from OpenGL.GL import shaders
import glfw

VERTEX_SHADER = """
#version 330

layout (location=0) in vec4 position;
layout (location=1) in vec4 color;

smooth out vec4 theColor;

void main()
{
    gl_Position = position;
    theColor = color;
}
"""

FRAGMENT_SHADER = """
#version 330

smooth in vec4 theColor;
out vec4 outputColor;

void main()
{
    outputColor = theColor;
}
"""

shaderProgram = None
VAO = None

def initialize():
    global VERTEX_SHADER
    global FRAGMENT_SHADER
    global shaderProgram
    global VAO
    # compile shaders and program
    vertexShader = shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fragmentShader = shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)

    # triangle position and color
    vertexData = numpy.array([0.0, 0.5, 0.0, 1.0,
                            0.5, -0.366, 0.0, 1.0,
                            -0.5, -0.366, 0.0, 1.0,
                            1.0, 0.0, 0.0, 1.0,
                            0.0, 1.0, 0.0, 1.0,
                            0.0, 0.0, 1.0, 1.0, ],
                            dtype=numpy.float32)

    # create VAO
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # create VBO
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertexData.nbytes, vertexData, GL_STATIC_DRAW)

    # enable array and set up data
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 0, None)
    # the last parameter is a pointer
    # python donot have pointer, have to using ctypes
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(48))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

def render():
    global shaderProgram
    global VAO
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # active shader program
    glUseProgram(shaderProgram)

    glBindVertexArray(VAO)

    # draw triangle
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glBindVertexArray(0)
    glUseProgram(0)

    glfw.SwapBuffers()

def main():
    # init glfw
    glfw.init()

    # make a window
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    # glfw.window_hint(glfw.OPENGL_VERSION_MAJOR, 3)
    # glfw.window_hint(glfw.OPENGL_VERSION_MINOR, 3)

    glfw.create_window(640, 480, 8, 8, 8, 8, 0, 0, glfw.window)

    initialize()

    while True:#glfw.GetWindowParam(glfw.OPENED):
        render()

    glfw.Terminate()

if __name__ == '__main__':
    main()