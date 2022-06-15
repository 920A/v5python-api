_C=False
_B=True
_A=None
class Enum:0
class PercentUnits(Enum):PCT=0
class AnalogUnits(Enum):PCT=PercentUnits.PCT;RANGE_8BIT=1;RANGE_10BIT=2;RANGE_12BIT=3;MV=4
class AxisType(Enum):XAXIS=1;YAXIS=2;ZAXIS=3
class BrakeType(Enum):COAST=0;BRAKE=1;HOLD=2;UNDEFINED=3
class ControllerType(Enum):PRIMARY=0;PARTNER=1
class CurrentUnits(Enum):AMP=0
class DetectionMode(Enum):OBJECT_DETECT=0;MIXED_DETECT=1;LINE_DETECT=2;TEST=3
class DirectionType(Enum):FWD=0;REV=1;UNDEFINED=2
class DistanceUnits(Enum):MM=1;IN=1;CM=2
class Eyes(Enum):BLACK_LEFT=1;BLACK_DOWN=2;BLACK_RESTING=3;BLACK_RIGHT=4;BLACK_STRAIGHT=5;BLUE_ANGRY=6;BLUE_RESTING=7;BLUE_RESTING_L=8;BLUE_RESTING_R=9;BLUE_SAD=10;BLUE_SQUINTING=11;GREEN_DOWN=12;GREEN_LEFT=13;GREEN_RESTING=14;GREEN_RIGHT=15;GREEN_UP=16;PURPLE_DOWN=17;PURPLE_LEFT=18;PURPLE_RESTING=19;PURPLE_RIGHT=20;PURPLE_UP=21
class Font(Enum):MONO_20=0;MONO_30=1;MONO_40=2;MONO_60=3;PROP_20=4;PROP_30=5;PROP_40=6;PROP_60=7;MONO_15=8;MONO_12=9;CHINESE_16=240
class GearSetting(Enum):RATIO36_1=0;RATIO18_1=1;RATIO6_1=2
class LedMode(Enum):AUTOMATIC=0;MANUAL=1
class LedState(Enum):OFF=0;ON=1
class OrientationType(Enum):ROLL=0;PITCH=1;YAW=2
class Ports(Enum):PORT1=0;PORT2=1;PORT3=2;PORT4=3;PORT5=4;PORT6=5;PORT7=6;PORT8=7;PORT9=8;PORT10=9;PORT11=10;PORT12=11;PORT13=12;PORT14=13;PORT15=14;PORT16=15;PORT17=16;PORT18=17;PORT19=18;PORT20=19;PORT21=20;PORT22=21
class PowerUnits(Enum):WATT=0
class RotationUnits(Enum):DEG=0;REV=1;RAW=99
class SizeType(Enum):NONE=0;SMALL=1;MEDIUM=2;LARGE=3
class TemperatureUnits(Enum):CELSIUS=0;FAHRENHEIT=1;PCT=255
class TimeUnits(Enum):SEC=0;MSEC=1
class TorqueUnits(Enum):NM=0;IN_LB=1
class TurnType(Enum):LEFT=0;RIGHT=1
class V5DeviceType(Enum):NO_SENSOR=0;MOTOR=2;LED=3;ABS_ENC=4;BUMPER=5;IMU=6;RANGE=7;RADIO=8;TETHER=9;BRAIN=10;VISION=11;ADI=12;GYRO=70;SONAR=71;GENERIC=128;GENERIC_SERIAL=129;UNDEFINED=255
class VelocityUnits(Enum):PCT=PercentUnits.PCT;RPM=1;DPS=2
class VoltageUnits(Enum):VOLT=0;MV=1
class WhiteBalanceMode(Enum):AUTOMATIC=0;START=1;MANUAL=2
class WifiMode(Enum):OFF=0;ON=1
class Device:
	def __init__(self,index=_A):0
	@staticmethod
	def type():0
	@staticmethod
	def installed():0
	@staticmethod
	def value():0
class BrainBattery:
	def __init__(self,parent):0
	@staticmethod
	def capacity(percentUnits=PercentUnits.PCT):0
	@staticmethod
	def temperature(temperatureUnits=TemperatureUnits.CELSIUS):0
	@staticmethod
	def voltage(voltageUnits=VoltageUnits.VOLT):0
	@staticmethod
	def current(currentUnits=CurrentUnits.AMP):0
class BrainLcd:
	def __init__(self,parent):0
	@staticmethod
	def set_cursor(row,column):0
	@staticmethod
	def set_font(font):0
	@staticmethod
	def set_pen_width(width):0
	@staticmethod
	def set_origin(x,y):0
	@staticmethod
	def column():0
	@staticmethod
	def row():0
	@staticmethod
	def set_pen_color(color):0
	@staticmethod
	def set_pen_color_hue(color):0
	@staticmethod
	def set_fill_color(color):0
	@staticmethod
	def set_fill_color_hue(color):0
	@staticmethod
	def get_string_width(text):0
	@staticmethod
	def get_string_height(text):0
	@staticmethod
	def print_(text,new_line=_B):0
	@staticmethod
	def print_line(number,text):0
	@staticmethod
	def print_at(x,y,opaque,text):0
	@staticmethod
	def clear_screen(color=_A):0
	@staticmethod
	def clear_screen_hue(hue):0
	@staticmethod
	def clear_line(number=_A,color=_A):0
	@staticmethod
	def clear_line_hue(number,hue):0
	@staticmethod
	def new_line():0
	@staticmethod
	def draw_pixel(x,y):0
	@staticmethod
	def draw_line(x1,y1,x2,y2):0
	@staticmethod
	def draw_rectangle(x,y,width,height,color=_A):0
	@staticmethod
	def draw_rectangle_hue(x,y,width,height,hue):0
	@staticmethod
	def draw_circle(x,y,radius,color=_A):0
	@staticmethod
	def draw_circle_hue(x,y,radius,hue):0
	@staticmethod
	def draw_image_from_buffer(buffer,x=0,y=0):0
	@staticmethod
	def draw_image_from_buffer_raw(buffer,x,y,width,height):0
	@staticmethod
	def draw_image_from_file(filename,x=0,y=0):0
	@staticmethod
	def draw_eyes(eyes):0
	@staticmethod
	def x_position():0
	@staticmethod
	def y_position():0
	@staticmethod
	def pressing():0
	@staticmethod
	def render(vsync_wait=_B):0
class BrainSDCard:
	def __init__(self,parent):0
	@staticmethod
	def is_inserted():0
	@staticmethod
	def filesize(filename):0
	@staticmethod
	def loadfile(filename,buffer):0
	@staticmethod
	def load_to_bytearray(filename,size=_A):0
	@staticmethod
	def load_to_string(filename,size=_A):0
	@staticmethod
	def savefile(filename,buffer):0
	@staticmethod
	def appendfile(filename,buffer):0
class Serial:
	def __init__(self,parent):0
	@staticmethod
	def write(data,null_terminate_string=_B):0
	@staticmethod
	def read(buffer):0
	@staticmethod
	def has_data():0
class Timer:
	def __init__(self):0
	@staticmethod
	def time(timeUnits=TimeUnits.SEC):0
	@staticmethod
	def clear():0
	@staticmethod
	def system():0
class TriportPort:
	def __init__(self,id,parent):0
class Triport(Device):a=TriportPort;b=TriportPort;c=TriportPort;d=TriportPort;e=TriportPort;f=TriportPort;g=TriportPort;h=TriportPort;port=TriportPort
class TriDevice:0
class Accelerometer(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value(analogUnits=AnalogUnits.PCT):0
class AnalogIn(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value(analogUnits=AnalogUnits.PCT):0
class Bitmap:
	def __init__(self,width,height,pixel_data=_A):0
	@staticmethod
	def from_png(png_data):0
	@staticmethod
	def from_png_file(filename):0
class Brain(Device):screen=BrainLcd;battery=BrainBattery;three_wire_port=Triport;timer=Timer;sdcard=BrainSDCard;serial=Serial
class Bumper(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value():0
	@staticmethod
	def pressing():0
class Color:
	def __init__(self,color_value):0
	@staticmethod
	def set_rgb(r,g,b):0
	@staticmethod
	def set_value(color_value):0
	@staticmethod
	def set_hsv(hue,saturation,value):0
	@staticmethod
	def set_web(web_color_str):0
	@staticmethod
	def value():0
	@staticmethod
	def is_transparent():0
	@staticmethod
	def from_rgb(r,g,b):0
	@staticmethod
	def from_hsv(h,s,v):0
	@staticmethod
	def from_web(web_color_str):0
class Competition:
	def __init__(self):0
	@staticmethod
	def is_enabled():0
	@staticmethod
	def is_driver_control():0
	@staticmethod
	def is_autonomous():0
	@staticmethod
	def is_competition_switch():0
	@staticmethod
	def is_field_control():0
	@staticmethod
	def autonomous(f):0
	@staticmethod
	def drivercontrol(f):0
class Controller(Device):
	def __init__(self,controllerType=ControllerType.PRIMARY):0
	@staticmethod
	def rumble(rumblePattern):0
	@staticmethod
	def set_deadband(deadband,percentUnits=PercentUnits.PCT):0
	@staticmethod
	def deadband(percentUnits=PercentUnits.PCT):0
	buttonL1=_A;buttonL2=_A;buttonR1=_A;buttonR2=_A
class ControllerAxis:
	def __init__(self,parent,id):0
	@staticmethod
	def value():0
	@staticmethod
	def position(percentUnits=PercentUnits.PCT):0
class ControllerButton:
	def __init__(self,parent,id):0
	@staticmethod
	def pressing():0
class ControllerLcd:
	def __init__(self,parent):0
	@staticmethod
	def set_cursor(row,col):0
	@staticmethod
	def print_(text,new_line=_B):0
	@staticmethod
	def clear_screen():0
	@staticmethod
	def clear_line(number=_A):0
	@staticmethod
	def new_line():0
class Devices:
	def __init__(self):0
	@staticmethod
	def get(index):0
	@staticmethod
	def type(index):0
	@staticmethod
	def number():0
	@staticmethod
	def number_of(type):0
class DigitalIn(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value():0
	@staticmethod
	def is_set():0
class DigitalOut(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value():0
	@staticmethod
	def set(is_set):0
	@staticmethod
	def is_set():0
class Distance(Device):
	@staticmethod
	def object_distance(distanceUnits=DistanceUnits.MM):0
	@staticmethod
	def object_size():0
	@staticmethod
	def object_raw_size():0
	@staticmethod
	def object_velocity():0
	@staticmethod
	def is_object_detected():0
class Encoder(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value():0
	@staticmethod
	def reset_rotation():0
	@staticmethod
	def set_rotation(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def rotation(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def velocity(velocityUnits=VelocityUnits.PCT):0
class Gyro(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def start_calibration(value=0):0
	@staticmethod
	def is_calibrating():0
	@staticmethod
	def heading(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def rotation(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def set_heading(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def reset_heading():0
	@staticmethod
	def set_rotation(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def reset_rotation():0
class Inertial(Device):
	@staticmethod
	def start_calibration():0
	@staticmethod
	def is_calibrating():0
	@staticmethod
	def calibrate():0
	@staticmethod
	def reset_heading():0
	@staticmethod
	def reset_rotation():0
	@staticmethod
	def set_heading(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def set_rotation(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def angle(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def roll(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def pitch(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def yaw(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def orientation(orientationType,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def heading(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def rotation(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def gyro_rate(axisType,velocityUnits=VelocityUnits.RPM):0
	@staticmethod
	def acceleration(axisType):0
class Led(DigitalOut):
	@staticmethod
	def on():0
	@staticmethod
	def off():0
	@staticmethod
	def value():0
	@staticmethod
	def set(is_set):0
	@staticmethod
	def is_set():0
class Light(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value(analogUnits=AnalogUnits.PCT):0
class Limit(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value():0
	@staticmethod
	def pressing():0
class Line(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value(analogUnits=AnalogUnits.PCT):0
class Motor(Device):
	def __init__(self,index,gearSetting=GearSetting.RATIO18_1,reverse=_C):0
	@staticmethod
	def set_reversed(isReversed):0
	@staticmethod
	def set_velocity(velocity,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def set_stopping(brakeType):0
	@staticmethod
	def reset_rotation():0
	@staticmethod
	def set_rotation(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def set_timeout(time,timeUnits=TimeUnits.SEC):0
	@staticmethod
	def timeout(timeUnits=TimeUnits.SEC):0
	@staticmethod
	def did_timeout():0
	@staticmethod
	def spin(direction,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def spin_with_voltage(direction,voltage,voltageUnits=VoltageUnits.VOLT):0
	@staticmethod
	def spin_to(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def spin_to_position(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def spin_for(direction,rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def spin_for_time(direction,time,timeUnits=TimeUnits.SEC,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_spin_to(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_spin_to_position(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_spin_for(direction,rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def is_spinning():0
	@staticmethod
	def is_done():0
	@staticmethod
	def stop(brakeType=_A):0
	@staticmethod
	def set_max_torque(value,torqueUnits=TorqueUnits.NM):0
	@staticmethod
	def set_max_torque_percent(value,percentUnits=PercentUnits.PCT):0
	@staticmethod
	def set_max_torque_current(value,currentUnits=CurrentUnits.AMP):0
	@staticmethod
	def direction():0
	@staticmethod
	def rotation(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def velocity(velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def current(currentUnits=CurrentUnits.AMP):0
	@staticmethod
	def voltage(voltageUnits=VoltageUnits.VOLT):0
	@staticmethod
	def power(powerUnits=PowerUnits.WATT):0
	@staticmethod
	def torque(torqueUnits=TorqueUnits.NM):0
	@staticmethod
	def efficiency(percentUnits=PercentUnits.PCT):0
	@staticmethod
	def temperature(temperatureUnits=TemperatureUnits.CELSIUS):0
class Motor29(Device):
	def __init__(self,triport_port,reverse=_C):0
	@staticmethod
	def set_velocity(velocity,percentUnits=PercentUnits.PCT):0
	@staticmethod
	def set_reversed(is_reversed):0
	@staticmethod
	def spin(direction,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def stop():0
class MotorVictor(Device):
	def __init__(self,triport_port,reverse=_C):0
	@staticmethod
	def set_velocity(velocity,percentUnits=PercentUnits.PCT):0
	@staticmethod
	def set_reversed(is_reversed):0
	@staticmethod
	def spin(direction,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def stop():0
class Optical(Device):
	@staticmethod
	def hue():0
	@staticmethod
	def brightness(raw=_C):0
	@staticmethod
	def color():0
	@staticmethod
	def color_int():0
	@staticmethod
	def is_near_object():0
	@staticmethod
	def set_light(ledState):0
	@staticmethod
	def set_light_pct(intensity,percentUnits=PercentUnits.PCT):0
class Pneumatics(DigitalOut):
	@staticmethod
	def open():0
	@staticmethod
	def close():0
class Pot(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value(rotationUnits=RotationUnits.DEG):0
class PwmOut(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def set_state(value,percentUnits=PercentUnits.PCT):0
class Rotation(Device):
	def __init__(self,index,is_reverse=_C):0
	@staticmethod
	def set_reversed(is_reverse):0
	@staticmethod
	def angle(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def reset_position():0
	@staticmethod
	def set_position(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def position(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def velocity(velocityUnits=VelocityUnits.DPS):0
class Servo(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def set_position(value,rotationUnits=RotationUnits.DEG):0
class Sonar(TriDevice):
	def __init__(self,triport_port):0
	@staticmethod
	def value():0
	@staticmethod
	def distance(distanceUnits=DistanceUnits.MM):0
class Vision(Device):
	def __init__(self,index,brightness=_A,signatures=_A):0
	@staticmethod
	def take_snapshot(id_or_sig_or_code,count=_A):0
	@staticmethod
	def set_signature(signature):0
	@staticmethod
	def set_mode(mode):0
	@staticmethod
	def get_mode():0
	@staticmethod
	def set_brightness(value):0
	@staticmethod
	def get_brightness():0
	@staticmethod
	def set_white_balance_mode(mode):0
	@staticmethod
	def get_white_balance_mode():0
	@staticmethod
	def set_white_balance_values(color):0
	@staticmethod
	def get_white_balance_values():0
	@staticmethod
	def set_led_mode(mode):0
	@staticmethod
	def get_led_mode():0
	@staticmethod
	def set_led_brightness(percent):0
	@staticmethod
	def get_led_brightness():0
	@staticmethod
	def set_led_color(red,green,blue):0
	@staticmethod
	def get_led_color():0
	@staticmethod
	def set_wifi_mode(mode):0
	@staticmethod
	def get_wifi_mode():0
class VisionCode:
	def __init__(self,ids_or_signatures):0
class VisionObject:
	def __init__(self):0
	@staticmethod
	def flip_angle():0
	@staticmethod
	def clear():0
	id=_A;originX=_A;originY=_A;centerX=_A;centerY=_A;width=_A;height=_A;angle=_A;exists=_A
class VisionSignature:
	def __init__(self,id,uMin,uMax,uMean,vMin,vMax,vMean,range,type):0
def wait(time,timeUnits=TimeUnits.SEC):0
class DriveTrain:
	def __init__(self,left_motor,right_motor,wheel_travel=319.1764,track_width=292.1,distanceUnits=DistanceUnits.MM,gear_ratio=1.0):0
	@staticmethod
	def set_gear_ratio(gear_ratio):0
	@staticmethod
	def set_drive_velocity(velocity,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def set_turn_velocity(velocity,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def set_timeout(time,timeUnits=TimeUnits.SEC):0
	@staticmethod
	def timeout(timeUnits=TimeUnits.SEC):0
	@staticmethod
	def did_timeout():0
	@staticmethod
	def set_stopping(brakeType):0
	@staticmethod
	def drive(directionType,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def drive_for(directionType,distance,distanceUnits=DistanceUnits.MM,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def turn(turnType,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def turn_for(turnType,angle,angleUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def start_drive_for(directionType,distance,distanceUnits=DistanceUnits.MM,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_turn_for(turnType,angle,angleUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def arcade(drivePower,turnPower,percentUnit=PercentUnits.PCT):0
	@staticmethod
	def is_moving():0
	@staticmethod
	def is_done():0
	@staticmethod
	def stop(brakeType=_A):0
	@staticmethod
	def velocity(velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def current(currentUnits=CurrentUnits.AMP):0
	@staticmethod
	def power(powerUnits=PowerUnits.WATT):0
	@staticmethod
	def torque(torqueUnits=TorqueUnits.NM):0
	@staticmethod
	def efficiency(percentUnits=PercentUnits.PCT):0
	@staticmethod
	def temperature(percentUnits=PercentUnits.PCT):0
class MotorGroup:
	def __init__(self,motors):0
	@staticmethod
	def count():0
	@staticmethod
	def set_velocity(velocity,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def set_stopping(brakeType):0
	@staticmethod
	def reset_rotation():0
	@staticmethod
	def set_rotation(value,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def set_timeout(time,timeUnits=TimeUnits.SEC):0
	@staticmethod
	def spin(dir,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def spin_with_voltage(dir,voltage,voltageUnits=VoltageUnits.VOLT):0
	@staticmethod
	def spin_to(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def spin_to_position(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def spin_for(dir,rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def spin_for_time(dir,time,timeUnits=TimeUnits.SEC,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_spin_to(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_spin_to_position(rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_spin_for(dir,rotation,rotationUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def is_spinning():0
	@staticmethod
	def is_done():0
	@staticmethod
	def stop(brakeType=_A):0
	@staticmethod
	def set_max_torque(value,torqueUnits=TorqueUnits.NM):0
	@staticmethod
	def set_max_torque_percent(value):0
	@staticmethod
	def set_max_torque_current(value):0
	@staticmethod
	def direction():0
	@staticmethod
	def rotation(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def velocity(velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def current():0
	@staticmethod
	def power(powerUnits=PowerUnits.WATT):0
	@staticmethod
	def torque(torqueUnits=TorqueUnits.NM):0
	@staticmethod
	def efficiency(percentUnits=PercentUnits.PCT):0
	@staticmethod
	def temperature(temperatureUnits=TemperatureUnits.CELSIUS):0
class SmartDrive(DriveTrain):
	def __init__(self,left_motor,right_motor,gyro,wheel_travel=319.1764,track_width=292.1,distanceUnits=DistanceUnits.MM,gear_ratio=1.0):0
	@staticmethod
	def set_turn_threshold(t):0
	@staticmethod
	def turn_to_heading(angle,angleUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def turn_to_rotation(angle,angleUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT,waitForCompletion=_B):0
	@staticmethod
	def start_turn_to_heading(angle,angleUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def start_turn_to_rotation(angle,angleUnits=RotationUnits.DEG,velocity=_A,velocityUnits=VelocityUnits.PCT):0
	@staticmethod
	def set_heading(angle,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def heading(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def set_rotation(angle,rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def rotation(rotationUnits=RotationUnits.DEG):0
	@staticmethod
	def is_turning():0
SYSTEM_DISPLAY_WIDTH=480
SYSTEM_DISPLAY_HEIGHT=272
STATUS_BAR_HEIGHT=32
DEGREES=RotationUnits.DEG
TURNS=RotationUnits.REV
PERCENT=PercentUnits.PCT
SECONDS=TimeUnits.SEC
INCHES=DistanceUnits.IN
MM=DistanceUnits.MM
FORWARD=DirectionType.FWD
REVERSE=DirectionType.REV
LEFT=TurnType.LEFT
RIGHT=TurnType.RIGHT
XAXIS=AxisType.XAXIS
YAXIS=AxisType.YAXIS
ZAXIS=AxisType.ZAXIS
ROLL=OrientationType.ROLL
PITCH=OrientationType.PITCH
YAW=OrientationType.YAW
MONO_M=Font.MONO_20
MONO_L=Font.MONO_30
MONO_XL=Font.MONO_40
MONO_XXL=Font.MONO_60
MONO_S=Font.MONO_15
MONO_XS=Font.MONO_12
PROP_M=Font.PROP_20
PROP_L=Font.PROP_30
PROP_XL=Font.PROP_40
PROP_XXL=Font.PROP_60
PRIMARY=ControllerType.PRIMARY
PARTNER=ControllerType.PARTNER
RUMBLE_LONG='----'
RUMBLE_SHORT='....'
RUMBLE_PULSE='-.-.'
