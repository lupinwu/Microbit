basic.show_icon(IconNames.DUCK)
basic.pause(1000)

def on_forever():
    basic.show_leds("""
        . . . . .
        . . . . #
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . #
        . . . # #
        . . . . #
        . . . . #
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . # #
        . . # # #
        . . . # #
        . . . # #
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . # # .
        . # # # .
        . . # # #
        . . # # #
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . # # .
        . # # # .
        . . # # #
        . . # # #
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . # # . .
        # # # . .
        . # # # #
        . # # # .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        # # . . .
        # # . . .
        # # # # .
        # # # . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        # . . . .
        # . . . .
        # # # . .
        # # . . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # . . .
        # . . . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
