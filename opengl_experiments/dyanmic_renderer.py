import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import numpy as np


class CubeObj():

    def __init__(self, pos=None, ori=None, size=None, col=None):

        if pos is None:
            self._pos = [0,0,-6.]
        else:
            self._pos = pos

        if ori is None:
            self._ori = [0,0,0]
        else:
            self._ori = ori

        if size is None:
            self._size = [1,1,1]
        else:
            self._size = size

        if col is None:
            self._col = [0.5,0.5,0.5, 1]
        else:
            self._col = col

class ArrowObj():

    def __init__(self, pos=None, ori=None, length=None, col=None):

        if pos is None:
            self._pos = [0,0,-6.]
        else:
            self._pos = pos

        if ori is None:
            self._ori = [0,0,0]
        else:
            self._ori = ori

        if length is None:
            self._length = 2.
        else:
            self._length = length

        if col is None:
            self._col = [0.5,0.5,0.5, 1]
        else:
            self._col = col


class DynamicRendering():

    def __init__(self, width=640, height=480, posX=200, posY=200):
        self._width   = width
        self._height  = height
        self._objects_to_draw = []
        self._window  = 0
        self._windowX = posX
        self._windowY = posY   

    def updateObjectList(self, new_object):
        print "Added new object!"
        self._objects_to_draw.append(new_object)

    def keyPressed(self, *args):

        #if the escape key is pressed, new object is added to the drawing list.
        if args[0] == '\033':
            pos  = np.hstack([np.random.rand(2)*3, -6])
            ori  = np.random.rand(3)
            size = np.random.rand(3)*6
            col  = abs(np.random.rand(3))
            self.updateObjectList(CubeObj(pos, ori, size, col))
        elif(args[0] == 'a'):
            pos    = np.hstack([np.random.rand(2)*4, -6])
            ori    = np.random.rand(3)
            length = abs(np.random.rand(1))*5
            col    = abs(np.random.rand(3))
            self.updateObjectList(ArrowObj(pos, ori, length, col))

    def drawArrow(self, arrow):

        gl.glLoadIdentity()

        gl.glTranslatef(arrow._pos[0], arrow._pos[1], arrow._pos[2])

        gl.glRotatef(arrow._ori[0],1.0,0.0,0.0)
        gl.glRotatef(arrow._ori[1],0.0,1.0,0.0)
        gl.glRotatef(arrow._ori[2],0.0,0.0,1.0)

        gl.glColor3f(arrow._col[0],arrow._col[1],arrow._col[2])

        # gl.glBegin(gl.GL_QUADS)

        quadObj=glu.gluNewQuadric()
        glu.gluCylinder(quadObj, 0.25, 0.25, arrow._length, 32, 16)

        gl.glTranslatef(0, 0, arrow._length)

        quadObj=glu.gluNewQuadric()
        glu.gluCylinder(quadObj, 0.45, 0., 4, 32, 16)

        # gl.glEnd()

        arrow._ori[0] +=  - 0.30
        arrow._ori[2] +=  - 0.30

    def drawCube(self, cube):

        gl.glLoadIdentity()

        gl.glTranslatef(cube._pos[0], cube._pos[1],cube._pos[2])

        gl.glScalef(cube._size[0],cube._size[1],cube._size[0])
 
        gl.glRotatef(cube._ori[0],1.0,0.0,0.0)
        gl.glRotatef(cube._ori[1],0.0,1.0,0.0)
        gl.glRotatef(cube._ori[2],0.0,0.0,1.0)

        gl.glColor3f(cube._col[0],cube._col[1],cube._col[2])
 
        # Draw Cube (multiple quads)
        gl.glBegin(gl.GL_QUADS)
 
        # gl.glColor3f(0.0,1.0,0.0)
        gl.glVertex3f( 1.0, 1.0,-1.0)
        gl.glVertex3f(-1.0, 1.0,-1.0)
        gl.glVertex3f(-1.0, 1.0, 1.0)
        gl.glVertex3f( 1.0, 1.0, 1.0) 
 
        # gl.glColor3f(1.0,0.0,0.0)
        gl.glVertex3f( 1.0,-1.0, 1.0)
        gl.glVertex3f(-1.0,-1.0, 1.0)
        gl.glVertex3f(-1.0,-1.0,-1.0)
        gl.glVertex3f( 1.0,-1.0,-1.0) 
 
        # gl.glColor3f(0.0,1.0,0.0)
        gl.glVertex3f( 1.0, 1.0, 1.0)
        gl.glVertex3f(-1.0, 1.0, 1.0)
        gl.glVertex3f(-1.0,-1.0, 1.0)
        gl.glVertex3f( 1.0,-1.0, 1.0)
 
        # gl.glColor3f(1.0,1.0,0.0)
        gl.glVertex3f( 1.0,-1.0,-1.0)
        gl.glVertex3f(-1.0,-1.0,-1.0)
        gl.glVertex3f(-1.0, 1.0,-1.0)
        gl.glVertex3f( 1.0, 1.0,-1.0)
 
        # gl.glColor3f(0.0,0.0,1.0)
        gl.glVertex3f(-1.0, 1.0, 1.0) 
        gl.glVertex3f(-1.0, 1.0,-1.0)
        gl.glVertex3f(-1.0,-1.0,-1.0) 
        gl.glVertex3f(-1.0,-1.0, 1.0) 
 
        # gl.glColor3f(1.0,0.0,1.0)
        gl.glVertex3f( 1.0, 1.0,-1.0) 
        gl.glVertex3f( 1.0, 1.0, 1.0)
        gl.glVertex3f( 1.0,-1.0, 1.0)
        gl.glVertex3f( 1.0,-1.0,-1.0)

        gl.glEnd()

        cube._ori[0] +=  - 0.30
        cube._ori[2] +=  - 0.30

    def drawGLScene(self):
        
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        if self._objects_to_draw:

            for obj in self._objects_to_draw:
                if isinstance(obj, CubeObj):
                    self.drawCube(obj)
                elif isinstance(obj, ArrowObj):
                    self.drawArrow(obj)
        else:

            print "The drawing object list empty, can't draw without a single object!"

        glut.glutSwapBuffers()

    def startRenderer(self):
        glut.glutInit()
        glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE | glut.GLUT_DEPTH)
        glut.glutInitWindowSize(self._width, self._height)
        glut.glutInitWindowPosition(self._windowX,self._windowY)

        self._window = glut.glutCreateWindow('Dynamic addition of objects')
 
        glut.glutDisplayFunc(self.drawGLScene)
        glut.glutIdleFunc(self.drawGLScene)
        glut.glutKeyboardFunc(self.keyPressed)

        gl.glClearColor(0.0, 0.0, 0.0, 0.0)
        gl.glClearDepth(1.0) 
        gl.glDepthFunc(gl.GL_LESS)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glShadeModel(gl.GL_SMOOTH)   
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        glu.gluPerspective(45.0, float(self._width)/float(self._height), 0.1, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        
        glut.glutMainLoop()


def main():
    dynrender = DynamicRendering()
    cube = CubeObj()
    dynrender._objects_to_draw.append(cube)
    dynrender.startRenderer()



if __name__ == '__main__':
    main()