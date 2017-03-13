import _screens
import _task

win = _screens.create_window(fullscreen=True, size=(800, 600), screen=1)
circle_shape = _screens.create_circle(win, size=4)
rect_shape = _screens.create_rectangle(win, width=10, height=5)
fixation = _screens.create_fixation_screen(win, size=5)
instructions = "In this task you will be playing a ball catching game.\n\n" \
               "You control a basket with your button-pad.\n" \
               "You can move the basket left by pressing '1',\n" \
               "and right by pressing '4'.\n\n" \
               "A ball will be falling down the screen.\n" \
               "Your task is to catch the ball with your basket.\n" \
               "Try to work as quickly and accurately as possible.\n\n" \
               "Press '3' when you're ready to begin 10 practice trials."
instructions_screen = _screens.create_instructions_screen(win, instructions, text_size=3, wrap_width=90)

_task.task(win, None, task_name='Apples', fixation=fixation, data_file_name=None, inst_screen=instructions_screen,
           stim_1=circle_shape, stim_2=rect_shape)
