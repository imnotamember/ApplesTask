import glob
import random
from psychopy import visual, monitors


def create_window(fullscreen=True, size=(1920, 1080), units='deg', screen=0):
    if units == 'deg':
        mon = monitors.Monitor('default', 44, 40)
        mon.setSizePix(size)
    window = visual.Window(size=size, fullscr=fullscreen, units=units, allowGUI=False, monitor=mon, screen=screen,
                           waitBlanking=True)
    return window


def create_fixation_screen(window):
    return visual.TextStim(win=window, text="+", pos=[0, 0], rgb='black')


def create_instructions_screen(window, instructions, wrapWidth=30, units='deg'):
    return visual.TextStim(win=window, text=instructions, wrapWidth=wrapWidth)


def create_stim_screens(window, number_of_target_stim):
    all_stim = sorted(glob.glob('fractal_stimuli/*.png'))
    random.shuffle(all_stim)
    stim_list = []
    for i in xrange(1, number_of_target_stim + 1):
        for j in xrange(number_of_target_stim):
            stim_file = all_stim.pop()
            stim_list.append(visual.ImageStim(win=window, image=stim_file, units='deg'))
    for i in xrange(len(all_stim)):
        stim_file = all_stim.pop()
        stim_list.append(visual.ImageStim(win=window, image=stim_file, units='deg'))
    return stim_list


def create_circle(window, location=(0, 0), size=1):
    circle = visual.Circle(window, pos=location, radius=size, fillColor='black', lineColor='black')
    return circle
