from scipy.spatial.distance import pdist, squareform
from particlebox import ParticleBox
from forces import gravitational_force, restoring_force

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from math import sin, cos, radians, sqrt
from random import uniform 

dt = 1. / 30 # 30fps

def initializer(box, rect, particles):
    def init():
        particles.set_data([], [])
        rect.set_edgecolor('none')
        return particles, rect
    return init 

flag = 50
collided = None
updown = None
target_y = uniform(-1.0, 1.0)

def animate(i):
    """perform animation step"""
    global box, rect, dt, ax, fig
    box.step(dt)

    ms = int(fig.dpi * 2 * box.size * fig.get_figwidth()
             / np.diff(ax.get_xbound())[0])
    
    # update pieces of the animation
    rect.set_edgecolor('k')
    particles.set_data(box.state[:, 0], box.state[:, 1])
    particles.set_markersize(ms)
    return particles, rect

def generate_animater(box, rect, dt, ax, fig, particles):
    def animate(i):
        global flag, collided, updown
        box.step(dt)

        ms = int(fig.dpi * 2 * box.size * fig.get_figwidth()
                / np.diff(ax.get_xbound())[0])

        # update pieces of the animation
        rect.set_edgecolor('k')
        particles.set_data(box.state[:, 0], box.state[:, 1])
        particles.set_markersize(ms)

        
        return particles, rect

    return animate



def check_collision(angle = 0, dt = dt,):
    global collided, target_y, updown 

    V = sqrt(21.25)
    angle = radians(angle)
    v_x, v_y = V*cos(angle), V*sin(angle)
    
    fig = plt.figure()

    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=True,)
    NUMBER_OF_PARTICLES = 50
    MEAN_VELOCITY = 1.0
    init_state = []
    box_size = 2
    particle_size = 0.04
    particle_mass = 1.0
    gravity = 10

    for i in range(NUMBER_OF_PARTICLES):
        # initial position 
        x_init, y_init = np.random.random(), np.random.random()
        
        x_init = 2 * box_size * (x_init - 0.5)
        y_init = 2 * box_size * (y_init - 0.5)
        
        # initial velocity
        v_dir_init = np.random.random()
        v_dir_init = 2 * np.pi * v_dir_init
        v_x_init = MEAN_VELOCITY * np.cos(v_dir_init)
        v_y_init = MEAN_VELOCITY * np.sin(v_dir_init)
        init_state.append([x_init, y_init, v_x_init, v_y_init])

    #init_state = -0.5 + np.random.random((NUMBER_OF_PARTICLES, 4))
    #init_state[:, :2] *= 3.9

    bounds = [-box_size, box_size, -box_size, box_size]

    box = ParticleBox(init_state, bounds, particle_size, particle_mass, gravity)

    # particles holds the locations of the particles
    particles, = ax.plot([], [], 'bo', ms=6)

    # rect is the box edge
    rect = plt.Rectangle(box.bounds[::2],
                        box.bounds[1] - box.bounds[0],
                        box.bounds[3] - box.bounds[2],
                        ec='none', lw=2, fc='none')
    ax.add_patch(rect)
    print(f'simulation for angle {angle}')

    # collided = False 
    
    try:
        ani = animation.FuncAnimation(fig, 
                            generate_animater(box, rect, dt, ax, fig, particles), 
                            frames=600,
                            interval=10, 
                            blit=True, 
                            init_func=initializer(box, rect, particles))
        plt.show()
    except StopIteration:
        pass 
    
    if collided is None:
        res = updown 
        updown = None 
        # print(res, updown)
        return res

    res = collided
    collided = None 
    updown = None 
    
    return res

#################################################
# if __name__ == '__main__':
#     from finder import manual_finder
    
#     print(manual_finder(check_collision))
#################################################    

if __name__ == '__main__':
    from finder import smart_finder
    check_collision(0.0)
    # print(smart_finder(check_collision, 0.0, 90.0))
    