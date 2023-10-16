from manim import *
class SeveralMesures(Scene):
    CONFIG={
        "line_style":{
            "stroke_width":2,
            "stroke_color":ORANGE
        }
    }
    def construct(self):
        lines=VGroup()
        x_mins=[0,0,0]
        x_maxs=[10,100,1000]
        values=[]
        for t in x_maxs:
            value=np.random.uniform(0,t)
            values.append(value)
        factors=[1,10,100]
        for x_min,x_max,factor in zip(x_mins,x_maxs,factors):
            line=self.my_line(x_min,x_max,factor,**self.CONFIG['line_style'])
            number=self.my_numbers(line,factor)
            line.add(number)
            lines.add(line)
        lines.center()
        lines.arrange(DOWN,buff=0.6)
        
        self.play(Create(lines))
        self.my_tracker(lines,values)
        self.wait()
    def my_numbers(self,lines,factor):
        for line in lines:
            x_min=line.x_min
            x_max=line.x_max
            numbers=VGroup()
            for x in np.arange(x_min,x_max+1,factor):
                number=MathTex(f"{x}").scale(0.5)
                number.next_to(line.number_to_point(x),DOWN,buff=.3)
                numbers.add(number)
            return numbers

    def my_line(self,x_min,x_max,factor,**kwargs_line):
        my_line=NumberLine(x_range= [x_min, x_max], numbers_with_elongated_ticks=\
            list(range(x_min,x_max+1,factor)),**kwargs_line)
        my_line.stretch_to_fit_width(config['frame_width']-1)
        return my_line
    
    def my_tracker(self,lines,values):
        for t in range(len(values)):
            x_value=ValueTracker(values[t])
        fx=lambda x:x_value.get_value()*np.random.random()**2+.2
        fx_value=ValueTracker(fx(x_value))
        gx= lambda y: (fx_value.get_value()+fx(fx_value.get_value()))/2
        gx_value=ValueTracker(gx(x_value))
        my_tips=VGroup()
        for t,m in zip([x_value,fx_value,gx_value],[0,1,2]):  
            my_tip=Arrow(color=YELLOW_B).rotate(PI/2)
            my_tip.stretch_to_fit_width(.08)
            my_tip.stretch_to_fit_height(1)  
            my_tip.add_updater(lambda h: h.next_to(lines[m].number_to_point(t.get_value()),UP,buff=0))
            my_tips.add(my_tip)
        self.play(FadeIn(my_tips))
        time=0
        while time<3:
            my_time=np.random.random()
            if my_time<.5:
                my_time=0.5
            postions=np.random.random()
            time+=my_time
            self.play(x_value.animate.set_value(postions),run_time=my_time)

    #    for line, factor,value in zip(lines, factors, values):
    #        time=0
    #        x_value=ValueTracker(value)
    #        my_tip=ArrowTip().rotate(PI/2)
    #        my_tip.set_width(0.08,{"stretch":True})
    #        my_tip.set_height(0.8,{"stretch":True})
    #        my_tip.add_updater(lambda t: t.next_to(line.number_to_point(x_value.get_value()),UP,buff=0))
    #        self.play(FadeIn(my_tip))
    #        line.add(my_tip)
    #        while time<2:
    #            my_time=np.random.random()
    #            if my_time<0.5:
    #                my_time=0.5
    #            time+=my_time
    #            position=np.random.random()*factor
    #            self.play(*it.chain(*[(ValueTracker(value).set_value,position) for value in values]),run_time=my_time)
