from manim import *
import itertools as it
class Pentagono(RegularPolygon):
    def __init__(self, n=6, **kwargs):
        RegularPolygon.__init__(self, n=5, **kwargs)
        self.set_color(DARK_GRAY)
        self.set_stroke(width=6)
        self.scale(3)
class TimeWidthValues(Scene):
    configuracion={
        'offset_t': 0,
        'colors': [RED, GREEN, BLUE, YELLOW, PURPLE],
        'aleatorio': np.random.random(),
    }
    def construct(self):
        pentagonos= VGroup()
        for i in range(20):
            comienzo=0
            pentagono=Pentagono()
            pentagono.comienzo=comienzo
            direction=[UP, DOWN, LEFT, RIGHT]
            pentagono.direction=direction[i%4]
            pentagonos.add(pentagono)
        pentagonos.arrange_in_grid(buff=1, cols=5, rows=4).set_height(6)
        self.play(
            LaggedStartMap(
                DrawBorderThenFill, pentagonos,
                lag_ratio=0.1,
                run_time=5,
            )
        )
        pentagonos_copy=pentagonos.copy()
        self.play(
            LaggedStartMap(
                ShowPassingFlash, pentagonos_copy.set(color=RED),
            ),
            rate_func=there_and_back,
            run_time=7,
        )
        for pentagono in pentagonos:
            pentagono.generate_target()
            pentagono.target.set_width(0)
        self.play(
            LaggedStartMap(
                Rotating, pentagonos,
            )
        ),
        for pentagono in pentagonos:
            pentagono.generate_target()
            pentagono.target.set_height(0)
            pentagono.add_updater(self.update_pentagono)
        self.wait(6)
        for pentagono in pentagonos:
            pentagono.clear_updaters()
        def function_color(mob):
            mob.set_color(np.random.choice(self.configuracion['colors']))
        self.play(
            *[UpdateFromFunc(pentagono, function_color) for pentagono in pentagonos],
        )
        self.wait()
        for pentagono in pentagonos:
            pentagono.add_updater(self.update_direction)
        self.wait(6)
    def update_pentagono(self, pentagono, dt):
        pentagono.comienzo += dt
        pentagono.rotate(pentagono.comienzo * 0.01)
        return pentagono
    def update_direction(self, pentagono, dt):
        pentagono.direction += dt*np.array([0,0,0])
        pentagono.move_to(pentagono.direction * 0.01+pentagono.get_center())
        return pentagono