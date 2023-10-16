from manim import *


class MyScreen(Scene):
    CONFIG = {
        "largo": 3,
        "alto": 2,
        "t_offset": 0,
        "escala": .7,
        "graph_origin": 2*LEFT,
    }
    def construct(self):
        def update_graph(c, dt):
            rate = dt
            c.become(self.get_my_curve(self.CONFIG['t_offset']+rate))
            self.CONFIG['t_offset'] += rate

        def update_graph1(c, dt):
            rate = dt
            c.become(self.get_other_curve(self.CONFIG['t_offset']+rate))
            self.CONFIG['t_offset'] += rate

        def update_graph2(c, dt):
            rate = dt
            c.become(self.get_other_curve1(self.CONFIG['t_offset']+rate))
            self.CONFIG['t_offset'] += rate
        def update_graph3(c, dt):
            rate = dt
            c.become(self.get_other_curve2(self.CONFIG['t_offset']+rate))
            self.CONFIG['t_offset'] += rate
        c = self.get_my_curve(0)
        c1 = self.get_other_curve(0)
        c2 = self.get_other_curve1(0)
        c3 = self.get_other_curve2(0)
        cuadro = Rectangle(width=2*self.CONFIG['largo'], height=2 *
                           self.CONFIG['alto'], color=YELLOW)
        self.play(Create(c), FadeIn(cuadro), Create(c1), Write(c2), Write(c3))
        for C, U in zip([c, c1, c2, c3], [update_graph, update_graph1, update_graph2, update_graph3]):
            C.add_updater(U)
        self.wait(3)

    def get_my_curve(self, dt):
        my_curve = FunctionGraph(
            lambda x:
            (self.CONFIG['alto']-.1)*np.sin(3*x+dt),
            x_range=[-self.CONFIG['largo'], self.CONFIG['largo']],
            stroke_width=1.4,
            color=YELLOW_B
        )
        return my_curve

    def get_other_curve(self, dt):
        other_curve = FunctionGraph(
            lambda x:
            (self.CONFIG['alto']-.1)*np.cos(3*x+dt),
            x_range=[-self.CONFIG['largo'], self.CONFIG['largo']],
            stroke_width=1.4,
            color=YELLOW_B
        )
        return other_curve

    def get_other_curve1(self, dt):
        other_curve = FunctionGraph(
            lambda x:
            (self.CONFIG['alto']-.1)/2*(np.cos(3*x+dt)-np.sin(x+dt)),
            x_range=[-self.CONFIG['largo'], self.CONFIG['largo']],
            stroke_width=1.4,
            color=YELLOW_B
        )
        return other_curve
    
    def get_other_curve2(self, dt):
        other_curve = FunctionGraph(
            lambda x:
            (self.CONFIG['alto']-.1)/3*(np.cos(3*x+dt)-np.sin(x+dt)+ np.cos(2*x+dt)),
            x_range=[-self.CONFIG['largo'], self.CONFIG['largo']],
            stroke_width=1.4,
            color=YELLOW_B
        )
        return other_curve
    def making_number_c(self, funtion):
        pass 