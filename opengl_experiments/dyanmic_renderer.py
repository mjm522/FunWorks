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


class DynamicRendering():

    def __init__(self):
        self._width = 640
        self._height = 480
        self._objects_to_draw = []
        self._window = 0
        self._windowX = 200
        self._windowY = 200    

    def updateObjectList(self, new_object):
        print "Added new object!"
        self._objects_to_draw.append(new_object)

    def keyPressed(self, *args):

        #if the escape key is pressed, new object is added to the drawing list.
        if args[0] == '\033':
            pos  = np.hstack([np.random.rand(2)*10, -6])
            ori  = np.random.rand(3)
            size = np.random.rand(3)*2
            col  = abs(np.random.rand(3))
            self.updateObjectList(CubeObj(pos, ori, size, col))

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
                elif obj == 'arrow':
                    self.drawArrow()
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