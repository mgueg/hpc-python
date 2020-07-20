import numpy as np
cimport numpy as cnp
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
@cython.profile(True)
# 21 sec with
#def evolve(cnp.ndarray u_previous, double a, double dt, double dx2, double dy2):
# !!! 0.040 with !!!
def evolve(cnp.ndarray[cnp.double_t, ndim=2] u_previous, double a, double dt, double dx2, double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """
    cdef cnp.ndarray[cnp.double_t, ndim=2] u
    cdef int n = u_previous.shape[0]
    cdef int m = u_previous.shape[1]

    cdef int i
    cdef int j
    u = np.empty((n, m), dtype=float)
    # Multiplication is more efficient than division
    cdef double dx2inv = 1. / dx2
    cdef double dy2inv = 1. / dy2
    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) * dx2inv + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) * dy2inv )
    u_previous[:] = u[:]
    return u

def iterate(field, field0, a, dx, dy, timesteps, image_interval):
    """Run fixed number of time steps of heat equation"""

    dx2 = dx**2
    dy2 = dy**2

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    for m in range(1, timesteps+1):
        field = evolve(field0, a, dt, dx2, dy2)


