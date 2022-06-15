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

    def type(self):
        pass

    def installed(self):
        pass

    def value(self):
        pass


class BrainBattery:
    def __init__(self, parent):
        pass

    def capacity(self, percentUnits=PercentUnits.PCT):
        pass

    def temperature(self, temperatureUnits=TemperatureUnits.CELSIUS):
        pass

    def voltage(self, voltageUnits=VoltageUnits.VOLT):
        pass

    def current(self, currentUnits=CurrentUnits.AMP):
        pass


class BrainLcd:
    def __init__(self, parent):
        pass

    def set_cursor(self, row, column):
        pass

    def set_font(self, font):
        pass

    def set_pen_width(self, width):
        pass

    def set_origin(self, x, y):
        pass

    def column(self):
        pass

    def row(self):
        pass

    def set_pen_color(self, color):
        pass

    def set_pen_color_hue(self, color):
        pass

    def set_fill_color(self, color):
        pass

    def set_fill_color_hue(self, color):
        pass

    def get_string_width(self, text):
        pass

    def get_string_height(self, text):
        pass

    def print_(self, text, new_line=True):
        pass

    def print_line(self, number, text):
        pass

    def print_at(self, x, y, opaque, text):
        pass

    def clear_screen(self, color=None):
        pass

    def clear_screen_hue(self, hue):
        pass

    def clear_line(self, number=None, color=None):
        pass

    def clear_line_hue(self, number, hue):
        pass

    def new_line(self):
        pass

    def draw_pixel(self, x, y):
        pass

    def draw_line(self, x1, y1, x2, y2):
        pass

    def draw_rectangle(self, x, y, width, height, color=None):
        pass

    def draw_rectangle_hue(self, x, y, width, height, hue):
        pass

    def draw_circle(self, x, y, radius, color=None):
        pass

    def draw_circle_hue(self, x, y, radius, hue):
        pass

    def draw_image_from_buffer(self, buffer, x=0, y=0):
        pass

    def draw_image_from_buffer_raw(self, buffer, x, y, width, height):
        pass

    def draw_image_from_file(self, filename, x=0, y=0):
        pass

    def draw_eyes(self, eyes):
        pass

    def x_position(self):
        pass

    def y_position(self):
        pass

    def pressing(self):
        pass

    def render(self, vsync_wait=True):
        pass


class BrainSDCard:
    def __init__(self, parent):
        pass

    def is_inserted(self):
        pass

    def filesize(self, filename):
        pass

    def loadfile(self, filename, buffer):
        pass

    def load_to_bytearray(self, filename, size=None):
        pass

    def load_to_string(self, filename, size=None):
        pass

    def savefile(self, filename, buffer):
        pass

    def appendfile(self, filename, buffer):
        pass


class Serial:
    def __init__(self, parent):
        pass

    def write(self, data, null_terminate_string=True):
        pass

    def read(self, buffer):
        pass

    def has_data(self):
        pass


class Timer:
    def __init__(self):
        pass

    def time(self, timeUnits=TimeUnits.SEC):
        pass

    def clear(self):
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

    def value(self, analogUnits=AnalogUnits.PCT):
        pass


class AnalogIn(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self, analogUnits=AnalogUnits.PCT):
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

    def value(self):
        pass

    def pressing(self):
        pass


class Color:
    def __init__(self, color_value):
        pass

    def set_rgb(self, r, g, b):
        pass

    def set_value(self, color_value):
        pass

    def set_hsv(self, hue, saturation, value):
        pass

    def set_web(self, web_color_str):
        pass

    def value(self):
        pass

    def is_transparent(self):
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

    def is_enabled(self):
        pass

    def is_driver_control(self):
        pass

    def is_autonomous(self):
        pass

    def is_competition_switch(self):
        pass

    def is_field_control(self):
        pass

    def autonomous(self, f):
        pass

    def drivercontrol(self, f):
        pass


class Controller(Device):
    def __init__(self, controllerType=ControllerType.PRIMARY):
        pass

    def rumble(self, rumblePattern):
        pass

    def set_deadband(self, deadband, percentUnits=PercentUnits.PCT):
        pass

    def deadband(self, percentUnits=PercentUnits.PCT):
        pass

    buttonL1 = None  # Actual Values Differ
    buttonL2 = None
    buttonR1 = None
    buttonR2 = None


class ControllerAxis:
    def __init__(self, parent, id):
        pass

    def value(self):
        pass

    def position(self, percentUnits=PercentUnits.PCT):
        pass


class ControllerButton:
    def __init__(self, parent, id):
        pass

    def pressing(self):
        pass


class ControllerLcd:
    def __init__(self, parent):
        pass

    def set_cursor(self, row, col):
        pass

    def print_(self, text, new_line=True):
        pass

    def clear_screen(self):
        pass

    def clear_line(self, number=None):
        pass

    def new_line(self):
        pass


class Devices:
    def __init__(self):
        pass

    def get(self, index):
        pass

    def type(self, index):
        pass

    def number(self):
        pass

    def number_of(self, type):
        pass


class DigitalIn(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self):
        pass

    def is_set(self):
        pass


class DigitalOut(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self):
        pass

    def set(self, is_set):
        pass

    def is_set(self):
        pass


class Distance(Device):
    def object_distance(self, distanceUnits=DistanceUnits.MM):
        pass

    def object_size(self):
        pass

    def object_raw_size(self):
        pass

    def object_velocity(self):
        pass

    def is_object_detected(self):
        pass


class Encoder(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self):
        pass

    def reset_rotation(self):
        pass

    def set_rotation(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def rotation(self, rotationUnits=RotationUnits.DEG):
        pass

    def velocity(self, velocityUnits=VelocityUnits.PCT):
        pass


class Gyro(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self, rotationUnits=RotationUnits.DEG):
        pass

    def start_calibration(self, value=0):
        pass

    def is_calibrating(self):
        pass

    def heading(self, rotationUnits=RotationUnits.DEG):
        pass

    def rotation(self, rotationUnits=RotationUnits.DEG):
        pass

    def set_heading(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def reset_heading(self):
        pass

    def set_rotation(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def reset_rotation(self):
        pass


class Inertial(Device):
    def start_calibration(self):
        pass

    def is_calibrating(self):
        pass

    def calibrate(self):
        pass

    def reset_heading(self):
        pass

    def reset_rotation(self):
        pass

    def set_heading(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def set_rotation(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def angle(self, rotationUnits=RotationUnits.DEG):
        pass

    def roll(self, rotationUnits=RotationUnits.DEG):
        pass

    def pitch(self, rotationUnits=RotationUnits.DEG):
        pass

    def yaw(self, rotationUnits=RotationUnits.DEG):
        pass

    def orientation(self, orientationType, rotationUnits=RotationUnits.DEG):
        pass

    def heading(self, rotationUnits=RotationUnits.DEG):
        pass

    def rotation(self, rotationUnits=RotationUnits.DEG):
        pass

    def gyro_rate(self, axisType, velocityUnits=VelocityUnits.RPM):
        pass

    def acceleration(self, axisType):
        pass


class Led(DigitalOut):
    def on(self):
        pass

    def off(self):
        pass

    def value(self):
        pass

    def set(self, is_set):
        pass

    def is_set(self):
        pass


class Light(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self, analogUnits=AnalogUnits.PCT):
        pass


class Limit(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self):
        pass

    def pressing(self):
        pass


class Line(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self, analogUnits=AnalogUnits.PCT):
        pass


class Motor(Device):
    def __init__(self, index, gearSetting=GearSetting.RATIO18_1, reverse=False):
        pass

    def set_reversed(self, isReversed):
        pass

    def set_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        pass

    def set_stopping(self, brakeType):
        pass

    def reset_rotation(self):
        pass

    def set_rotation(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def set_timeout(self, time, timeUnits=TimeUnits.SEC):
        pass

    def timeout(self, timeUnits=TimeUnits.SEC):
        pass

    def did_timeout(self):
        pass

    def spin(self, direction, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def spin_with_voltage(self, direction, voltage, voltageUnits=VoltageUnits.VOLT):
        pass

    def spin_to(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def spin_to_position(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def spin_for(self, direction, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def spin_for_time(self, direction, time, timeUnits=TimeUnits.SEC, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_spin_to(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_spin_to_position(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_spin_for(self, direction, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def is_spinning(self):
        pass

    def is_done(self):
        pass

    def stop(self, brakeType=None):
        pass

    def set_max_torque(self, value, torqueUnits=TorqueUnits.NM):
        pass

    def set_max_torque_percent(self, value, percentUnits=PercentUnits.PCT):
        pass

    def set_max_torque_current(self, value, currentUnits=CurrentUnits.AMP):
        pass

    def direction(self):
        pass

    def rotation(self, rotationUnits=RotationUnits.DEG):
        pass

    def velocity(self, velocityUnits=VelocityUnits.PCT):
        pass

    def current(self, currentUnits=CurrentUnits.AMP):
        pass

    def voltage(self, voltageUnits=VoltageUnits.VOLT):
        pass

    def power(self, powerUnits=PowerUnits.WATT):
        pass

    def torque(self, torqueUnits=TorqueUnits.NM):
        pass

    def efficiency(self, percentUnits=PercentUnits.PCT):
        pass

    def temperature(self, temperatureUnits=TemperatureUnits.CELSIUS):
        pass


class Motor29(Device):
    def __init__(self, triport_port, reverse=False):
        pass

    def set_velocity(self, velocity, percentUnits=PercentUnits.PCT):
        pass

    def set_reversed(self, is_reversed):
        pass

    def spin(self, direction, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def stop(self):
        pass


class MotorVictor(Device):
    def __init__(self, triport_port, reverse=False):
        pass

    def set_velocity(self, velocity, percentUnits=PercentUnits.PCT):
        pass

    def set_reversed(self, is_reversed):
        pass

    def spin(self, direction, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def stop(self):
        pass


class Optical(Device):
    def hue(self):
        pass

    def brightness(self, raw=False):
        pass

    def color(self):
        pass

    def color_int(self):
        pass

    def is_near_object(self):
        pass

    def set_light(self, ledState):
        pass

    def set_light_pct(self, intensity, percentUnits=PercentUnits.PCT):
        pass


class Pneumatics(DigitalOut):
    def open(self):
        pass

    def close(self):
        pass


class Pot(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self, rotationUnits=RotationUnits.DEG):
        pass


class PwmOut(TriDevice):
    def __init__(self, triport_port):
        pass

    def set_state(self, value, percentUnits=PercentUnits.PCT):
        pass


class Rotation(Device):
    def __init__(self, index, is_reverse=False):
        pass

    def set_reversed(self, is_reverse):
        pass

    def angle(self, rotationUnits=RotationUnits.DEG):
        pass

    def reset_position(self):
        pass

    def set_position(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def position(self, rotationUnits=RotationUnits.DEG):
        pass

    def velocity(self, velocityUnits=VelocityUnits.DPS):
        pass


class Servo(TriDevice):
    def __init__(self, triport_port):
        pass

    def set_position(self, value, rotationUnits=RotationUnits.DEG):
        pass


class Sonar(TriDevice):
    def __init__(self, triport_port):
        pass

    def value(self):
        pass

    def distance(self, distanceUnits=DistanceUnits.MM):
        pass


class Vision(Device):
    def __init__(self, index, brightness=None, signatures=None):
        pass

    def take_snapshot(self, id_or_sig_or_code, count=None):
        pass

    def set_signature(self, signature):
        pass

    def set_mode(self, mode):
        pass

    def get_mode(self):
        pass

    def set_brightness(self, value):
        pass

    def get_brightness(self):
        pass

    def set_white_balance_mode(self, mode):
        pass

    def get_white_balance_mode(self):
        pass

    def set_white_balance_values(self, color):
        pass

    def get_white_balance_values(self):
        pass

    def set_led_mode(self, mode):
        pass

    def get_led_mode(self):
        pass

    def set_led_brightness(self, percent):
        pass

    def get_led_brightness(self):
        pass

    def set_led_color(self, red, green, blue):
        pass

    def get_led_color(self):
        pass

    def set_wifi_mode(self, mode):
        pass

    def get_wifi_mode(self):
        pass

class VisionCode:
    def __init__(self, ids_or_signatures):
        pass


class VisionObject:
    def __init__(self):
        pass

    def flip_angle(self):
        pass

    def clear(self):
        pass

    id = None  # Actual Values Differ
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

    def set_gear_ratio(self, gear_ratio):
        pass

    def set_drive_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        pass

    def set_turn_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        pass

    def set_timeout(self, time, timeUnits=TimeUnits.SEC):
        pass

    def timeout(self, timeUnits=TimeUnits.SEC):
        pass

    def did_timeout(self):
        pass

    def set_stopping(self, brakeType):
        pass

    def drive(self, directionType, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def drive_for(self, directionType, distance, distanceUnits=DistanceUnits.MM, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def turn(self, turnType, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def turn_for(self, turnType, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def start_drive_for(self, directionType, distance, distanceUnits=DistanceUnits.MM, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_turn_for(self, turnType, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def arcade(self, drivePower, turnPower, percentUnit=PercentUnits.PCT):
        pass

    def is_moving(self):
        pass

    def is_done(self):
        pass

    def stop(self, brakeType=None):
        pass

    def velocity(self, velocityUnits=VelocityUnits.PCT):
        pass

    def current(self, currentUnits=CurrentUnits.AMP):
        pass

    def power(self, powerUnits=PowerUnits.WATT):
        pass

    def torque(self, torqueUnits=TorqueUnits.NM):
        pass

    def efficiency(self, percentUnits=PercentUnits.PCT):
        pass

    def temperature(self, percentUnits=PercentUnits.PCT):
        pass


class MotorGroup:
    def __init__(self, motors):
        pass

    def count(self):
        pass

    def set_velocity(self, velocity, velocityUnits=VelocityUnits.PCT):
        pass

    def set_stopping(self, brakeType):
        pass

    def reset_rotation(self):
        pass

    def set_rotation(self, value, rotationUnits=RotationUnits.DEG):
        pass

    def set_timeout(self, time, timeUnits=TimeUnits.SEC):
        pass

    def spin(self, dir, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def spin_with_voltage(self, dir, voltage, voltageUnits=VoltageUnits.VOLT):
        pass

    def spin_to(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def spin_to_position(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def spin_for(self, dir, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def spin_for_time(self, dir, time, timeUnits=TimeUnits.SEC, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_spin_to(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_spin_to_position(self, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_spin_for(self, dir, rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def is_spinning(self):
        pass

    def is_done(self):
        pass

    def stop(self, brakeType=None):
        pass

    def set_max_torque(self, value, torqueUnits=TorqueUnits.NM):
        pass

    def set_max_torque_percent(self, value):
        pass

    def set_max_torque_current(self, value):
        pass

    def direction(self):
        pass

    def rotation(self, rotationUnits=RotationUnits.DEG):
        pass

    def velocity(self, velocityUnits=VelocityUnits.PCT):
        pass

    def current(self):
        pass

    def power(self, powerUnits=PowerUnits.WATT):
        pass

    def torque(self, torqueUnits=TorqueUnits.NM):
        pass

    def efficiency(self, percentUnits=PercentUnits.PCT):
        pass

    def temperature(self, temperatureUnits=TemperatureUnits.CELSIUS):
        pass


class SmartDrive(DriveTrain):
    def __init__(self, left_motor, right_motor, gyro, wheel_travel=319.1764, track_width=292.1, distanceUnits=DistanceUnits.MM, gear_ratio=1.0):
        pass

    def set_turn_threshold(self, t):
        pass

    def turn_to_heading(self, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def turn_to_rotation(self, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT, waitForCompletion=True):
        pass

    def start_turn_to_heading(self, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def start_turn_to_rotation(self, angle, angleUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    def set_heading(self, angle, rotationUnits=RotationUnits.DEG):
        pass

    def heading(self, rotationUnits=RotationUnits.DEG):
        pass

    def set_rotation(self, angle, rotationUnits=RotationUnits.DEG):
        pass

    def rotation(self, rotationUnits=RotationUnits.DEG):
        pass

    def is_turning(self):
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
