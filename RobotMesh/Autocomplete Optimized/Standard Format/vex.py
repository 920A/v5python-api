class Enum:
    pass


class PercentUnits(Enum):
    PCT = 0


class AnalogUnits(Enum):
    PCT = PercentUnits.PCT
    RANGE_8BIT = 1
    RANGE_10BIT = 2
    RANGE_12BIT = 3
    MV = 4


class AxisType(Enum):
    XAXIS = 1
    YAXIS = 2
    ZAXIS = 3


class BrakeType(Enum):
    COAST = 0
    BRAKE = 1
    HOLD = 2
    UNDEFINED = 3


class ControllerType(Enum):
    PRIMARY = 0
    PARTNER = 1


class CurrentUnits(Enum):
    AMP = 0


class DetectionMode(Enum):
    OBJECT_DETECT = 0
    MIXED_DETECT = 1
    LINE_DETECT = 2
    TEST = 3


class DirectionType(Enum):
    FWD = 0
    REV = 1
    UNDEFINED = 2


class DistanceUnits(Enum):
    MM = 1
    IN = 1
    CM = 2


class Eyes(Enum):
    BLACK_LEFT = 1
    BLACK_DOWN = 2
    BLACK_RESTING = 3
    BLACK_RIGHT = 4
    BLACK_STRAIGHT = 5
    BLUE_ANGRY = 6
    BLUE_RESTING = 7
    BLUE_RESTING_L = 8
    BLUE_RESTING_R = 9
    BLUE_SAD = 10
    BLUE_SQUINTING = 11
    GREEN_DOWN = 12
    GREEN_LEFT = 13
    GREEN_RESTING = 14
    GREEN_RIGHT = 15
    GREEN_UP = 16
    PURPLE_DOWN = 17
    PURPLE_LEFT = 18
    PURPLE_RESTING = 19
    PURPLE_RIGHT = 20
    PURPLE_UP = 21


class Font(Enum):
    MONO_20 = 0
    MONO_30 = 1
    MONO_40 = 2
    MONO_60 = 3
    PROP_20 = 4
    PROP_30 = 5
    PROP_40 = 6
    PROP_60 = 7
    MONO_15 = 8
    MONO_12 = 9
    CHINESE_16 = 0xf0


class GearSetting(Enum):
    RATIO36_1 = 0
    RATIO18_1 = 1
    RATIO6_1 = 2


class LedMode(Enum):
    AUTOMATIC = 0
    MANUAL = 1


class LedState(Enum):
    OFF = 0
    ON = 1


class OrientationType(Enum):
    ROLL = 0
    PITCH = 1
    YAW = 2


class Ports(Enum):
    PORT1 = 0
    PORT2 = 1
    PORT3 = 2
    PORT4 = 3
    PORT5 = 4
    PORT6 = 5
    PORT7 = 6
    PORT8 = 7
    PORT9 = 8
    PORT10 = 9
    PORT11 = 10
    PORT12 = 11
    PORT13 = 12
    PORT14 = 13
    PORT15 = 14
    PORT16 = 15
    PORT17 = 16
    PORT18 = 17
    PORT19 = 18
    PORT20 = 19
    PORT21 = 20
    PORT22 = 21


class PowerUnits(Enum):
    WATT = 0


class RotationUnits(Enum):
    DEG = 0
    REV = 1
    RAW = 99


class SizeType(Enum):
    NONE = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class TemperatureUnits(Enum):
    CELSIUS = 0
    FAHRENHEIT = 1
    PCT = 0xFF


class TimeUnits(Enum):
    SEC = 0
    MSEC = 1


class TorqueUnits(Enum):
    NM = 0
    IN_LB = 1


class TurnType(Enum):
    LEFT = 0
    RIGHT = 1


class V5DeviceType(Enum):
    NO_SENSOR = 0
    MOTOR = 2
    LED = 3
    ABS_ENC = 4
    BUMPER = 5
    IMU = 6
    RANGE = 7
    RADIO = 8
    TETHER = 9
    BRAIN = 10
    VISION = 11
    ADI = 12
    GYRO = 0x46
    SONAR = 0x47
    GENERIC = 128
    GENERIC_SERIAL = 129
    UNDEFINED = 255


class VelocityUnits(Enum):
    PCT = PercentUnits.PCT
    RPM = 1
    DPS = 2


class VoltageUnits(Enum):
    VOLT = 0
    MV = 1


class WhiteBalanceMode(Enum):
    AUTOMATIC = 0
    START = 1
    MANUAL = 2


class WifiMode(Enum):
    OFF = 0
    ON = 1


class Device:
    def __init__(self, index=None):
        pass

    @staticmethod
    def type():
        pass

    @staticmethod
    def installed():
        pass

    @staticmethod
    def value():
        pass


class BrainBattery:
    def __init__(self, parent):
        pass

    @staticmethod
    def capacity(percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def temperature(temperatureUnits=TemperatureUnits.CELSIUS):
        pass

    @staticmethod
    def voltage(voltageUnits=VoltageUnits.VOLT):
        pass

    @staticmethod
    def current(currentUnits=CurrentUnits.AMP):
        pass


class BrainLcd:
    def __init__(self, parent):
        pass

    @staticmethod
    def set_cursor(row, column):
        pass

    @staticmethod
    def set_font(font):
        pass

    @staticmethod
    def set_pen_width(width):
        pass

    @staticmethod
    def set_origin(x, y):
        pass

    @staticmethod
    def column():
        pass

    @staticmethod
    def row():
        pass

    @staticmethod
    def set_pen_color(color):
        pass

    @staticmethod
    def set_pen_color_hue(color):
        pass

    @staticmethod
    def set_fill_color(color):
        pass

    @staticmethod
    def set_fill_color_hue(color):
        pass

    @staticmethod
    def get_string_width(text):
        pass

    @staticmethod
    def get_string_height(text):
        pass

    @staticmethod
    def print_(text, new_line=True):
        pass

    @staticmethod
    def print_line(number, text):
        pass

    @staticmethod
    def print_at(x, y, opaque, text):
        pass

    @staticmethod
    def clear_screen(color=None):
        pass

    @staticmethod
    def clear_screen_hue(hue):
        pass

    @staticmethod
    def clear_line(number=None, color=None):
        pass

    @staticmethod
    def clear_line_hue(number, hue):
        pass

    @staticmethod
    def new_line():
        pass

    @staticmethod
    def draw_pixel(x, y):
        pass

    @staticmethod
    def draw_line(x1, y1, x2, y2):
        pass

    @staticmethod
    def draw_rectangle(x, y, width, height, color=None):
        pass

    @staticmethod
    def draw_rectangle_hue(x, y, width, height, hue):
        pass

    @staticmethod
    def draw_circle(x, y, radius, color=None):
        pass

    @staticmethod
    def draw_circle_hue(x, y, radius, hue):
        pass

    @staticmethod
    def draw_image_from_buffer(buffer, x=0, y=0):
        pass

    @staticmethod
    def draw_image_from_buffer_raw(buffer, x, y, width, height):
        pass

    @staticmethod
    def draw_image_from_file(filename, x=0, y=0):
        pass

    @staticmethod
    def draw_eyes(eyes):
        pass

    @staticmethod
    def x_position():
        pass

    @staticmethod
    def y_position():
        pass

    @staticmethod
    def pressing():
        pass

    @staticmethod
    def render(vsync_wait=True):
        pass


class BrainSDCard:
    def __init__(self, parent):
        pass

    @staticmethod
    def is_inserted():
        pass

    @staticmethod
    def filesize(filename):
        pass

    @staticmethod
    def loadfile(filename, buffer):
        pass

    @staticmethod
    def load_to_bytearray(filename, size=None):
        pass

    @staticmethod
    def load_to_string(filename, size=None):
        pass

    @staticmethod
    def savefile(filename, buffer):
        pass

    @staticmethod
    def appendfile(filename, buffer):
        pass


class Serial:
    def __init__(self, parent):
        pass

    @staticmethod
    def write(data, null_terminate_string=True):
        pass

    @staticmethod
    def read(buffer):
        pass

    @staticmethod
    def has_data():
        pass


class Timer:
    def __init__(self):
        pass

    @staticmethod
    def time(timeUnits=TimeUnits.SEC):
        pass

    @staticmethod
    def clear():
        pass

    @staticmethod
    def system():
        pass


class TriportPort:
    def __init__(self, id, parent):
        pass


class Triport(Device):
    a = TriportPort
    b = TriportPort
    c = TriportPort
    d = TriportPort
    e = TriportPort
    f = TriportPort
    g = TriportPort
    h = TriportPort
    port = TriportPort


class TriDevice:
    pass


class Accelerometer(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value(analogUnits=AnalogUnits.PCT):
        pass


class AnalogIn(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value(analogUnits=AnalogUnits.PCT):
        pass


class Bitmap:
    def __init__(self, width, height, pixel_data=None):
        pass

    @staticmethod
    def from_png(png_data):
        pass

    @staticmethod
    def from_png_file(filename):
        pass


class Brain(Device):
    screen = BrainLcd
    battery = BrainBattery
    three_wire_port = Triport
    timer = Timer
    sdcard = BrainSDCard
    serial = Serial


class Bumper(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def pressing():
        pass


class Color:
    def __init__(self, color_value):
        pass

    @staticmethod
    def set_rgb(r, g, b):
        pass

    @staticmethod
    def set_value(color_value):
        pass

    @staticmethod
    def set_hsv(hue, saturation, value):
        pass

    @staticmethod
    def set_web(web_color_str):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def is_transparent():
        pass

    @staticmethod
    def from_rgb(r, g, b):
        pass

    @staticmethod
    def from_hsv(h, s, v):
        pass

    @staticmethod
    def from_web(web_color_str):
        pass


class Competition:
    def __init__(self):
        pass

    @staticmethod
    def is_enabled():
        pass

    @staticmethod
    def is_driver_control():
        pass

    @staticmethod
    def is_autonomous():
        pass

    @staticmethod
    def is_competition_switch():
        pass

    @staticmethod
    def is_field_control():
        pass

    @staticmethod
    def autonomous(f):
        pass

    @staticmethod
    def drivercontrol(f):
        pass


class Controller(Device):
    def __init__(self, controllerType=ControllerType.PRIMARY):
        pass

    @staticmethod
    def rumble(rumblePattern):
        pass

    @staticmethod
    def set_deadband(deadband, percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def deadband(percentUnits=PercentUnits.PCT):
        pass

    buttonL1 = None
    buttonL2 = None
    buttonR1 = None
    buttonR2 = None


class ControllerAxis:
    def __init__(self, parent, id):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def position(percentUnits=PercentUnits.PCT):
        pass


class ControllerButton:
    def __init__(self, parent, id):
        pass

    @staticmethod
    def pressing():
        pass


class ControllerLcd:
    def __init__(self, parent):
        pass

    @staticmethod
    def set_cursor(row, col):
        pass

    @staticmethod
    def print_(text, new_line=True):
        pass

    @staticmethod
    def clear_screen():
        pass

    @staticmethod
    def clear_line(number=None):
        pass

    @staticmethod
    def new_line():
        pass


class Devices:
    def __init__(self):
        pass

    @staticmethod
    def get(index):
        pass

    @staticmethod
    def type(index):
        pass

    @staticmethod
    def number():
        pass

    @staticmethod
    def number_of(type):
        pass


class DigitalIn(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def is_set():
        pass


class DigitalOut(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def set(is_set):
        pass

    @staticmethod
    def is_set():
        pass


class Distance(Device):
    @staticmethod
    def object_distance(distanceUnits=DistanceUnits.MM):
        pass

    @staticmethod
    def object_size():
        pass

    @staticmethod
    def object_raw_size():
        pass

    @staticmethod
    def object_velocity():
        pass

    @staticmethod
    def is_object_detected():
        pass


class Encoder(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def reset_rotation():
        pass

    @staticmethod
    def set_rotation(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def velocity(velocityUnits=VelocityUnits.PCT):
        pass


class Gyro(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def start_calibration(value=0):
        pass

    @staticmethod
    def is_calibrating():
        pass

    @staticmethod
    def heading(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def set_heading(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def reset_heading():
        pass

    @staticmethod
    def set_rotation(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def reset_rotation():
        pass


class Inertial(Device):
    @staticmethod
    def start_calibration():
        pass

    @staticmethod
    def is_calibrating():
        pass

    @staticmethod
    def calibrate():
        pass

    @staticmethod
    def reset_heading():
        pass

    @staticmethod
    def reset_rotation():
        pass

    @staticmethod
    def set_heading(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def set_rotation(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def angle(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def roll(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def pitch(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def yaw(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def orientation(orientationType, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def heading(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def gyro_rate(axisType, velocityUnits=VelocityUnits.RPM):
        pass

    @staticmethod
    def acceleration(axisType):
        pass


class Led(DigitalOut):
    @staticmethod
    def on():
        pass

    @staticmethod
    def off():
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def set(is_set):
        pass

    @staticmethod
    def is_set():
        pass


class Light(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value(analogUnits=AnalogUnits.PCT):
        pass


class Limit(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def pressing():
        pass


class Line(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value(analogUnits=AnalogUnits.PCT):
        pass


class Motor(Device):
    def __init__(self, index, gearSetting=GearSetting.RATIO18_1, reverse=False):
        pass

    @staticmethod
    def set_reversed(isReversed):
        pass

    @staticmethod
    def set_velocity(velocity, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def set_stopping(brakeType):
        pass

    @staticmethod
    def reset_rotation():
        pass

    @staticmethod
    def set_rotation(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def set_timeout(time, timeUnits=TimeUnits.SEC):
        pass

    @staticmethod
    def timeout(timeUnits=TimeUnits.SEC):
        pass

    @staticmethod
    def did_timeout():
        pass

    @staticmethod
    def spin(direction, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def spin_with_voltage(direction, voltage, voltageUnits=VoltageUnits.VOLT):
        pass

    @staticmethod
    def spin_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def spin_to_position(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def spin_for(direction, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def spin_for_time(direction, time, timeUnits=TimeUnits.SEC, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_spin_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_spin_to_position(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_spin_for(direction, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def is_spinning():
        pass

    @staticmethod
    def is_done():
        pass

    @staticmethod
    def stop(brakeType=None):
        pass

    @staticmethod
    def set_max_torque(value, torqueUnits=TorqueUnits.NM):
        pass

    @staticmethod
    def set_max_torque_percent(value, percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def set_max_torque_current(value, currentUnits=CurrentUnits.AMP):
        pass

    @staticmethod
    def direction():
        pass

    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def velocity(velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def current(currentUnits=CurrentUnits.AMP):
        pass

    @staticmethod
    def voltage(voltageUnits=VoltageUnits.VOLT):
        pass

    @staticmethod
    def power(powerUnits=PowerUnits.WATT):
        pass

    @staticmethod
    def torque(torqueUnits=TorqueUnits.NM):
        pass

    @staticmethod
    def efficiency(percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def temperature(temperatureUnits=TemperatureUnits.CELSIUS):
        pass


class Motor29(Device):
    def __init__(self, triport_port, reverse=False):
        pass

    @staticmethod
    def set_velocity(velocity, percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def set_reversed(is_reversed):
        pass

    @staticmethod
    def spin(direction, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def stop():
        pass


class MotorVictor(Device):
    def __init__(self, triport_port, reverse=False):
        pass

    @staticmethod
    def set_velocity(velocity, percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def set_reversed(is_reversed):
        pass

    @staticmethod
    def spin(direction, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def stop():
        pass


class Optical(Device):
    @staticmethod
    def hue():
        pass

    @staticmethod
    def brightness(raw=False):
        pass

    @staticmethod
    def color():
        pass

    @staticmethod
    def color_int():
        pass

    @staticmethod
    def is_near_object():
        pass

    @staticmethod
    def set_light(ledState):
        pass

    @staticmethod
    def set_light_pct(intensity, percentUnits=PercentUnits.PCT):
        pass


class Pneumatics(DigitalOut):
    @staticmethod
    def open():
        pass

    @staticmethod
    def close():
        pass


class Pot(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value(rotationUnits=RotationUnits.DEG):
        pass


class PwmOut(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def set_state(value, percentUnits=PercentUnits.PCT):
        pass


class Rotation(Device):
    def __init__(self, index, is_reverse=False):
        pass

    @staticmethod
    def set_reversed(is_reverse):
        pass

    @staticmethod
    def angle(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def reset_position():
        pass

    @staticmethod
    def set_position(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def position(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def velocity(velocityUnits=VelocityUnits.DPS):
        pass


class Servo(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def set_position(value, rotationUnits=RotationUnits.DEG):
        pass


class Sonar(TriDevice):
    def __init__(self, triport_port):
        pass

    @staticmethod
    def value():
        pass

    @staticmethod
    def distance(distanceUnits=DistanceUnits.MM):
        pass


class Vision(Device):
    def __init__(self, index, brightness=None, signatures=None):
        pass

    @staticmethod
    def take_snapshot(id_or_sig_or_code, count=None):
        pass

    @staticmethod
    def set_signature(signature):
        pass

    @staticmethod
    def set_mode(mode):
        pass

    @staticmethod
    def get_mode():
        pass

    @staticmethod
    def set_brightness(value):
        pass

    @staticmethod
    def get_brightness():
        pass

    @staticmethod
    def set_white_balance_mode(mode):
        pass

    @staticmethod
    def get_white_balance_mode():
        pass

    @staticmethod
    def set_white_balance_values(color):
        pass

    @staticmethod
    def get_white_balance_values():
        pass

    @staticmethod
    def set_led_mode(mode):
        pass

    @staticmethod
    def get_led_mode():
        pass

    @staticmethod
    def set_led_brightness(percent):
        pass

    @staticmethod
    def get_led_brightness():
        pass

    @staticmethod
    def set_led_color(red, green, blue):
        pass

    @staticmethod
    def get_led_color():
        pass

    @staticmethod
    def set_wifi_mode(mode):
        pass

    @staticmethod
    def get_wifi_mode():
        pass


class VisionCode:
    def __init__(self, ids_or_signatures):
        pass


class VisionObject:
    def __init__(self):
        pass

    @staticmethod
    def flip_angle():
        pass

    @staticmethod
    def clear():
        pass

    id = None
    originX = None
    originY = None
    centerX = None
    centerY = None
    width = None
    height = None
    angle = None
    exists = None


class VisionSignature:
    def __init__(self, id, uMin, uMax, uMean, vMin, vMax, vMean, range, type):
        pass


def wait(time, timeUnits=TimeUnits.SEC):
    pass


class DriveTrain:
    def __init__(self, left_motor, right_motor, wheel_travel=319.1764, track_width=292.1, distanceUnits=DistanceUnits.MM, gear_ratio=1.0):
        pass

    @staticmethod
    def set_gear_ratio(gear_ratio):
        pass

    @staticmethod
    def set_drive_velocity(velocity, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def set_turn_velocity(velocity, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def set_timeout(time, timeUnits=TimeUnits.SEC):
        pass

    @staticmethod
    def timeout(timeUnits=TimeUnits.SEC):
        pass

    @staticmethod
    def did_timeout():
        pass

    @staticmethod
    def set_stopping(brakeType):
        pass

    @staticmethod
    def drive(directionType, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def drive_for(directionType, distance, distanceUnits=DistanceUnits.MM, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def turn(turnType, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def turn_for(turnType, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def start_drive_for(directionType, distance, distanceUnits=DistanceUnits.MM, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_turn_for(turnType, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def arcade(drivePower, turnPower, percentUnit=PercentUnits.PCT):
        pass

    @staticmethod
    def is_moving():
        pass

    @staticmethod
    def is_done():
        pass

    @staticmethod
    def stop(brakeType=None):
        pass

    @staticmethod
    def velocity(velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def current(currentUnits=CurrentUnits.AMP):
        pass

    @staticmethod
    def power(powerUnits=PowerUnits.WATT):
        pass

    @staticmethod
    def torque(torqueUnits=TorqueUnits.NM):
        pass

    @staticmethod
    def efficiency(percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def temperature(percentUnits=PercentUnits.PCT):
        pass


class MotorGroup:
    def __init__(self, motors):
        pass

    @staticmethod
    def count():
        pass

    @staticmethod
    def set_velocity(velocity, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def set_stopping(brakeType):
        pass

    @staticmethod
    def reset_rotation():
        pass

    @staticmethod
    def set_rotation(value, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def set_timeout(time, timeUnits=TimeUnits.SEC):
        pass

    @staticmethod
    def spin(dir, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def spin_with_voltage(dir, voltage, voltageUnits=VoltageUnits.VOLT):
        pass

    @staticmethod
    def spin_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def spin_to_position(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def spin_for(dir, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def spin_for_time(dir, time, timeUnits=TimeUnits.SEC, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_spin_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_spin_to_position(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_spin_for(dir, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def is_spinning():
        pass

    @staticmethod
    def is_done():
        pass

    @staticmethod
    def stop(brakeType=None):
        pass

    @staticmethod
    def set_max_torque(value, torqueUnits=TorqueUnits.NM):
        pass

    @staticmethod
    def set_max_torque_percent(value):
        pass

    @staticmethod
    def set_max_torque_current(value):
        pass

    @staticmethod
    def direction():
        pass

    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def velocity(velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def current():
        pass

    @staticmethod
    def power(powerUnits=PowerUnits.WATT):
        pass

    @staticmethod
    def torque(torqueUnits=TorqueUnits.NM):
        pass

    @staticmethod
    def efficiency(percentUnits=PercentUnits.PCT):
        pass

    @staticmethod
    def temperature(temperatureUnits=TemperatureUnits.CELSIUS):
        pass


class SmartDrive(DriveTrain):
    def __init__(self, left_motor, right_motor, gyro, wheel_travel=319.1764, track_width=292.1, distanceUnits=DistanceUnits.MM, gear_ratio=1.0):
        pass

    @staticmethod
    def set_turn_threshold(t):
        pass

    @staticmethod
    def turn_to_heading(angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def turn_to_rotation(angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    @staticmethod
    def start_turn_to_heading(angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def start_turn_to_rotation(angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def set_heading(angle, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def heading(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def set_rotation(angle, rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        pass

    @staticmethod
    def is_turning():
        pass


SYSTEM_DISPLAY_WIDTH = 480
SYSTEM_DISPLAY_HEIGHT = 272
STATUS_BAR_HEIGHT = 32
DEGREES = RotationUnits.DEG
TURNS = RotationUnits.REV
PERCENT = PercentUnits.PCT
SECONDS = TimeUnits.SEC
INCHES = DistanceUnits.IN
MM = DistanceUnits.MM
FORWARD = DirectionType.FWD
REVERSE = DirectionType.REV
LEFT = TurnType.LEFT
RIGHT = TurnType.RIGHT
XAXIS = AxisType.XAXIS
YAXIS = AxisType.YAXIS
ZAXIS = AxisType.ZAXIS
ROLL = OrientationType.ROLL
PITCH = OrientationType.PITCH
YAW = OrientationType.YAW
MONO_M = Font.MONO_20
MONO_L = Font.MONO_30
MONO_XL = Font.MONO_40
MONO_XXL = Font.MONO_60
MONO_S = Font.MONO_15
MONO_XS = Font.MONO_12
PROP_M = Font.PROP_20
PROP_L = Font.PROP_30
PROP_XL = Font.PROP_40
PROP_XXL = Font.PROP_60
PRIMARY = ControllerType.PRIMARY
PARTNER = ControllerType.PARTNER
RUMBLE_LONG = "----"
RUMBLE_SHORT = "...."
RUMBLE_PULSE = "-.-."
