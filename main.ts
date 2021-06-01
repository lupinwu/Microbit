basic.showIcon(IconNames.Duck)
basic.pause(1000)
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . #
        . . . # #
        . . . . #
        . . . . #
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . # #
        . . # # #
        . . . # #
        . . . # #
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . # # .
        . # # # .
        . . # # #
        . . # # #
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . # # .
        . # # # .
        . . # # #
        . . # # #
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . # # . .
        # # # . .
        . # # # #
        . # # # .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        # # . . .
        # # . . .
        # # # # .
        # # # . .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        # . . . .
        # . . . .
        # # # . .
        # # . . .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # . . .
        # . . . .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
