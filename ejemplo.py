from manim import *


class LineScreen(Scene):
    def construct(self):
        value_tracker = ValueTracker(0)
        line = NumberLine(
            x_range=[-10-1, 10+1, 2],
            unit_size=.5,
            include_numbers=True,
            include_tip=True,
            numbers_with_elongated_ticks=[-10, 2],
        )
        line.value_tracker = value_tracker
        integro = self.get_number(value_tracker)
        self.play(Create(line))
        dot = self.getting_dot(line)
        self.play(Create(dot))
        self.play(Write(integro))
        self.play(value_tracker.animate.set_value(10))
        self.wait()

    def getting_dot(self, line):
        return Dot(line.value_tracker.get_value()).add_updater(lambda m: m.move_to(line.number_to_point(line.value_tracker.get_value())))

    def get_number(self, valor):
        integro = DecimalNumber(valor.get_value())
        integro.add_updater(lambda m: m.set_value(
            valor.get_value()))
        integro.to_edge(UP)
        return integro
