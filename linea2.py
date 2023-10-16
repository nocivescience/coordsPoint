from manim import *
class MyLinesAgain(Scene):
    CONFIG={
        "line_config":{
            "stroke_width":1.6,
            "stroke_color":ORANGE
        }
    }
    def construct(self):
        x_value=ValueTracker(0)
        fx=lambda x: x.get_value()**2/2
        gx=lambda x: 200*np.cos(x.get_value())
        fx_value=ValueTracker(fx(x_value))
        gx_value=ValueTracker(gx(x_value))
        x_mins=[-10,-100,-1000]
        x_maxs=[10,100,1000]
        factors=[2,20,200]
        v_trackers=[x_value,fx_value,gx_value]
        my_lines=VGroup()
        for x_min,x_max,factor,v_tracker in zip(x_mins,x_maxs,factors,v_trackers):
            my_line=self.get_my_line(x_min=x_min,x_max=x_max+1,\
                factor=list(range(x_min,x_max,factor)),v_tracker=v_tracker,**self.CONFIG['line_config'])
            my_number=self.my_numbers(my_line[0],x_min,x_max,factor)
            my_line.add(my_number)
            my_value=self.my_count(v_tracker,my_line[1])
            my_lines.add(my_line,my_value)
        my_lines.arrange(DOWN,buff=.25)
        self.play(LaggedStartMap(FadeIn,my_lines),run_time=1)
        self.wait()
        time=0
        while time<5:
            my_time=np.random.random()
            if my_time<0.4:
                my_time=0.4
            time+=my_time
            position_1=np.random.random()*x_maxs[0]
            position_2=fx(ValueTracker(position_1))
            position_3=gx(ValueTracker(position_1))
            self.play(x_value.animate.set_value(position_1), 
                fx_value.animate.set_value(position_2),
                gx_value.animate.set_value(position_3),
                run_time=my_time)
        self.wait()
    def get_my_line(self,x_min,x_max,factor,v_tracker,**kwargs_line):
        my_line=NumberLine(x_range=[x_min, x_max,5], unit_size=10,numbers_with_elongated_ticks=factor,**kwargs_line)
        my_line.set_width(config['frame_width']-1)
        my_tip=Arrow().rotate(PI/2)
        my_tip.stretch_to_fit_width(0.08)
        my_tip.stretch_to_fit_height(0.8)
        my_tip.add_updater(lambda m: m.next_to(my_line.number_to_point(v_tracker.get_value()),UP,buff=0))
        return VGroup(my_line,my_tip)
    def my_numbers(self,line,x_min,x_max,factor):
        numbers=VGroup()
        for x in range(x_min,x_max+1,factor):
            number=MathTex(f"{x}").scale(0.5)
            number.next_to(line.number_to_point(x),DOWN,buff=0.4)
            numbers.add(number)
        return numbers
    def my_count(self,v_tracker,tip):
        my_value=DecimalNumber(v_tracker.get_value())
        my_value.add_updater(lambda t: t.set_value(v_tracker.get_value()))
        my_value.add_updater(lambda t: t.next_to(tip,UP,buff=0.2))
        my_value.scale(0.6)
        my_value.set_color(BLUE)
        return my_value