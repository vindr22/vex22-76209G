vexcode_brain_precision = 0
vexcode_console_precision = 0
vexcode_controller_1_precision = 0
myVariable = 0
counter = 0

def when_started1():
    global myVariable, counter, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    while True:
        brain.screen.print("This is my heading and my rotation")
        brain.screen.next_row()
        brain.screen.print(drivetrain.heading(), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.print(" degrees  ")
        brain.screen.next_row()
        brain.screen.print(drivetrain.rotation(), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.print(" degrees  ")
        brain.screen.next_row()
        counter = counter + 1
        brain.screen.print(counter, precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.next_row()
        wait(0.1, SECONDS)
        brain.screen.set_cursor(1, 1)
        wait(5, MSEC)
    # stop project not currently supported

# Calibrate the Drivetrain
calibrate_drivetrain()

when_started1()
