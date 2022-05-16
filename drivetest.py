vexcode_brain_precision = 0
vexcode_console_precision = 0
vexcode_controller_1_precision = 0
myVariable = 0
counter = 0

def when_started1():
    global myVariable, counter, vexcode_brain_precision, vexcode_console_precision, vexcode_controller_1_precision
    brain.screen.print("Drive motorgroup by 90 degrees")
    drivetrain.drive_for(FORWARD, 600, MM, wait=True)
    wait(1.5, SECONDS)
    brain.screen.print(motor_group_4.position(DEGREES), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
    drivetrain.turn_for(RIGHT, 90, DEGREES, wait=True)
    wait(1.5, SECONDS)
    brain.screen.print(motor_group_4.position(DEGREES), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
    drivetrain.drive_for(FORWARD, 600, MM, wait=True)
    wait(1.5, SECONDS)
    # stop project not currently supported

# Calibrate the Drivetrain
calibrate_drivetrain()

when_started1()
