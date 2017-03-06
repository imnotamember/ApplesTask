import _screens, _task

win = _screens.create_window(fullscreen=True, size=(800, 600), screen=1)
circle_shape = _screens.create_circle(win)
fixation = _screens.create_fixation_screen(win)

'''
for i in xrange(10):
    for cSize in xrange(-1, -15, -1):
        circle_shape.pos = (0, cSize*.5)
        circle_shape.draw()
        win.flip()
'''

_task.task(win, None, task_name='Apples', fixation=fixation, data_file_name=None, inst_screen=None, stim_1=circle_shape)