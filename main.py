def showDate():
    global zero, theMonth, theDay
    zero = 0
    if DS3231.month() < 10:
        tm.showbit(zero, 0)
        tm.showbit(DS3231.month(), 1)
    else:
        theMonth = convert_to_text(DS3231.month())
        tm.showbit(parse_float(theMonth.char_at(0)), 0)
        tm.showbit(parse_float(theMonth.char_at(1)), 1)
    if DS3231.day() < 10:
        tm.showbit(zero, 2)
        tm.showbit(DS3231.day(), 3)
    else:
        theDay = convert_to_text(DS3231.day())
        tm.showbit(parse_float(theDay.char_at(0)), 2)
        tm.showbit(parse_float(theDay.char_at(1)), 3)
def showTime():
    global timeString
    timeString = DS3231.time_string()
    tm.showbit(parse_float(timeString.char_at(0)), 0)
    tm.showbit(parse_float(timeString.char_at(1)), 1)
    tm.showbit(parse_float(timeString.char_at(3)), 2)
    tm.showbit(parse_float(timeString.char_at(4)), 3)
    tm.show_dp(5, True)
    basic.pause(500)
    tm.show_dp(5, False)
    basic.pause(500)

def on_button_pressed_a():
    basic.show_string("" + str((DS3231.temperature())))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    # After you load this code to set the time you need to delete this block.
    setTime()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def setTime():
    DS3231.set_date(2, 29, 12, 2020)
    DS3231.set_time(11, 7, 30)
timeString = ""
theDay = ""
theMonth = ""
zero = 0
tm: TM1637.TM1637LEDs = None
tm = TM1637.create(DigitalPin.P0, DigitalPin.P1, 7, 4)

def on_forever():
    if input.button_is_pressed(Button.B):
        showDate()
    else:
        showTime()
basic.forever(on_forever)
