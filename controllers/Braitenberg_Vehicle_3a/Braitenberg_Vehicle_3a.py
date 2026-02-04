from controller import Robot

TIMESTEP = 64
MAX_SPEED = 10

def run_robot(robot):
    motors = []
    wheels = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
    
    light_sensors = []
    light_sensor_names = ['ls_left', 'ls_right']
    
    for wheel in wheels:
        motor = robot.getDevice(wheel)
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
        motors.append(motor)

    for light_sensor_name in light_sensor_names:
        ls = robot.getDevice(light_sensor_name)
        ls.enable(TIMESTEP)
        light_sensors.append(ls)
        
    
    while robot.step(TIMESTEP) != -1:
        left_light_val = light_sensors[0].getValue() / 100
        right_light_val = light_sensors[1].getValue() / 100
         
        left_speed = MAX_SPEED - left_light_val
        right_speed = MAX_SPEED - right_light_val
        
        motors[0].setVelocity(left_speed)
        motors[2].setVelocity(left_speed)
        
        motors[1].setVelocity(right_speed)
        motors[3].setVelocity(right_speed)
    

if __name__ == '__main__':
    robot = Robot()
    run_robot(robot)
