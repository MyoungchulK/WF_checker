import numpy as np
from scipy.interpolate import Akima1DInterpolator

def interpolation_bin_width(int_dt=0.5): # bin width scale is ns

    return int_dt, int_dt/1e9, 1/(int_dt/1e9)

def time_pad_maker(p_dt, p_range = 1024, p_offset = -200):

    # make long pad that can contain all 16 antenna wf length in the same range
    t_pad = np.arange(-1*p_range/2 - p_offset, p_range/2 - p_offset, p_dt)

    return t_pad, len(t_pad), t_pad[0], t_pad[-1]

def TGraph_to_raw(graph):

    return np.frombuffer(graph.GetX(),dtype=float,count=-1), np.frombuffer(graph.GetY(),dtype=float,count=-1)

#Akima interpolation from python Akima1DInterpolator library
def akima_interp(raw_t, raw_v, dt):

    # set the initial time bin to x.0ns or x.5ns at the inside of the original range
    if raw_t[0] - int(raw_t[0]) > dt:
        int_ti = np.ceil(raw_t[0]) # if value is x.501...~x.999..., ceil to x+1.0
    elif raw_t[0] - int(raw_t[0]) < dt:
        int_ti = int(raw_t[0]) + dt # if value is x.001...~x.499..., ceil to x.5
    else:
        int_ti = raw_t[0] # if value is x.5 exact, leave it

    # set the final time bin to x.0ns or x.5ns at the inside of the original range
    if raw_t[-1] - int(raw_t[-1]) > dt:
        int_tf = int(raw_t[-1]) + dt # if value is x.501...~x.999..., floor to x.5
    elif raw_t[-1] - int(raw_t[-1]) < dt:
        int_tf = np.floor(raw_t[-1]) # # if value is x.001...~x.499..., ceil to x.0
    else:
        int_tf = raw_t[-1] # if value is x.5 exact, leave it

    # set time range by dt
    int_t = np.arange(int_ti, int_tf+dt, dt)

    # akima interpolation!
    akima = Akima1DInterpolator(raw_t, raw_v)
    del raw_t, raw_v

    return int_ti, int_tf, akima(int_t), len(int_t)


