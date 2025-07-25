from vex import SECONDS, Brain, Color, FontType, wait

brain = Brain()


# Clear screen with black rectangle and display initial text
brain.screen.clear_screen()
brain.screen.set_fill_color("#000000")  # black
brain.screen.draw_rectangle(0, 0, 480, 240)

brain.screen.set_pen_color("#FFFFFF")  # white
brain.screen.print_at("Hello, there!", x=10, y=20)

brain.screen.set_pen_color(Color.BLUE)
brain.screen.print_at("Welcome!", x=10, y=40)

brain.screen.set_pen_color(Color.PURPLE)
brain.screen.print_at("Enjoy robotics!", x=10, y=60)
wait(6, SECONDS)

brain.screen.clear_screen()
brain.screen.set_pen_color(Color.WHITE)
brain.screen.print_at("Hello again!", x=10, y=20)
wait(6, SECONDS)

brain.screen.clear_screen()
img_filepath: str = "images/aix.png"

if brain.sdcard.exists(img_filepath):
    brain.screen.draw_image_from_file(img_filepath, 0, 0)
    wait(6, SECONDS)
else:
    brain.screen.set_font(FontType.MONO20)
    brain.screen.set_pen_color(Color.RED)
    brain.screen.print_at("Image not found at: ", img_filepath, x=50, y=100)
