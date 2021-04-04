function showDate () {
    zero = 0
    if (DS3231.month() < 10) {
        tm.showbit(zero, 0)
        tm.showbit(DS3231.month(), 1)
    } else {
        theMonth = convertToText(DS3231.month())
        tm.showbit(parseFloat(theMonth.charAt(0)), 0)
        tm.showbit(parseFloat(theMonth.charAt(1)), 1)
    }
    if (DS3231.day() < 10) {
        tm.showbit(zero, 2)
        tm.showbit(DS3231.day(), 3)
    } else {
        theDay = convertToText(DS3231.day())
        tm.showbit(parseFloat(theDay.charAt(0)), 2)
        tm.showbit(parseFloat(theDay.charAt(1)), 3)
    }
}
function showTime () {
    timeString = DS3231.timeString()
    tm.showbit(parseFloat(timeString.charAt(0)), 0)
    tm.showbit(parseFloat(timeString.charAt(1)), 1)
    tm.showbit(parseFloat(timeString.charAt(3)), 2)
    tm.showbit(parseFloat(timeString.charAt(4)), 3)
    tm.showDP(5, true)
    basic.pause(500)
    tm.showDP(5, false)
    basic.pause(500)
}
input.onButtonPressed(Button.A, function () {
    basic.showString("" + DS3231.temperature())
})
input.onButtonPressed(Button.AB, function () {
    // After you load this code to set the time you need to delete this block.
    setTime()
})
function setTime () {
    DS3231.setDate(2, 29, 12, 2020)
    DS3231.setTime(11, 7, 30)
}
let timeString = ""
let theDay = ""
let theMonth = ""
let zero = 0
let tm: TM1637.TM1637LEDs = null
tm = TM1637.create(
DigitalPin.P0,
DigitalPin.P1,
7,
4
)
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        showDate()
    } else {
        showTime()
    }
})
