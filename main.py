while True: 
     print("Light level:" + input.light_level()) 
     if input.light_level() > 20: 
         light.show_animation(light.rainbowAnimation, 5000) 
     else: light.clear()