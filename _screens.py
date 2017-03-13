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


def create_fixation_screen(window, size=1):
    return visual.TextStim(win=window, text="+", pos=[0, 0], rgb='black', height=size, units='deg')


def create_instructions_screen(window, instructions, wrap_width=30, units='deg', text_size=1):
    return visual.TextStim(win=window, text=instructions, wrapWidth=wrap_width, units=units, height=text_size)


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
    circle = visual.Circle(window, pos=location, radius=size, fillColor='black', lineColor='black', contrast=-.5)
    return circle


def create_rectangle(window, location=(0, 0), width=1, height=1):
    rectangle = visual.Rect(window, pos=location, width=width, height=height, fillColor='black', lineColor='black')
    return rectangle
