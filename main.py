while True: 
     print("Light level:" + input.light_level()) 
     if input.light_level() > 20: 
         light.set_all(light.rgb(255,215,0))
     else: light.clear()