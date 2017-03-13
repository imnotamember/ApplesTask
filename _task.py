from psychopy import core, event
from psychopy.iohub import launchHubServer, EventConstants
import _data
import random

io = launchHubServer(experiment_code='key_evts', psychopy_monitor_name='default')
keyboard = io.devices.keyboard


def task(win, exp_info, task_name, fixation, data_file_name=None, inst_screen=None, stim_1=None, stim_2=None):
    trial_clock = core.Clock()
    t_clock = core.Clock()
    isi = core.StaticPeriod(60, win)
    possible_responses = 0
    number_of_correct_responses = 0
    accuracy = 0
    if inst_screen:
        inst_screen.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    for trial in xrange(10):
        # Prepare variables for each trial from the stimuli list
        # Show Fixation for .5 seconds
        fixation.draw()
        win.callOnFlip(t_clock.reset)
        win.callOnFlip(isi.start, .5)
        win.flip()
        fixation.draw()
        isi.complete()

        trial_rt = toj_presentation(win=win, clock=trial_clock, stim_1=stim_1, stim_2=stim_2)
        # resp, resp_time, possible_responses = key_logger(trial_clock, possible_responses)

        if data_file_name:
            _data.write_data(data_file_name,
                             (exp_info['Participant'],
                              trial+1,
                              task_name,
                              resp,
                              accuracy,
                              trial_rt,
                              resp_time,
                              t_clock.getTime(),
                              )
                             )


def toj_presentation(win, clock, stim_1, stim_2, fix=None):
    trial_continue = True
    basket_location = [0, -40]
    circle_start_location = random.randint(-45, 45)
    circle_location = [circle_start_location, 40]
    increment = 0
    while trial_continue:
        if fix:
            fix.draw()
        for event_k in keyboard.getEvents():
            if event_k.type == EventConstants.KEYBOARD_PRESS:
                print event_k.key
                if event_k.key in ['lshift', 'z']:
                    increment = -0.5
                elif event_k.key in ['rshift', 'slash', '/']:
                    increment = 0.5
                elif event_k.key in ['escape', 'esc']:
                    quit()
            if event_k.type == EventConstants.KEYBOARD_RELEASE:
                # the key is no longer being pressed, so stop changing the size:
                increment = 0
        basket_location[0] += increment
        if basket_location[0] > 45:
            basket_location[0] = 45
        if basket_location[0] < -45:
            basket_location[0] = -45
        circle_location[1] -= .5
        if circle_location[1] < -40:
            trial_continue = False
            #if circle_location[0] > (basket_location[0] - 5) and circle_location[0] < (basket_location[0] + 5):
            if stim_2.contains(stim_1.pos):
                print 'Basket!'
            else:
                print "missed."
        stim_1.pos = tuple(circle_location)
        stim_1.draw()
        stim_2.pos = tuple(basket_location)
        stim_2.draw()
        win.flip()
        trial_surplus = clock.getTime()
        clock.reset()
    return trial_surplus


def key_logger(trial_clock, correct_buttons, possible_trials, correct_tally):
    trial_rt = event.getKeys(timeStamped=trial_clock)
    correct = 0
    response = 'None'
    response_time = 'None'
    if trial_rt:
        response = trial_rt[0][0]
        response_time = trial_rt[0][1]
        if correct_buttons is 'None':
            correct = 'NA'
        else:
            if response in ['escape', 'esc']:
                quit()
            elif response in correct_buttons:
                correct = 1
            correct_tally += correct
            possible_trials += 1
    return response, response_time, correct, possible_trials, correct_tally


def instructions_screen(win, inst_screen):
    inst_screen.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
