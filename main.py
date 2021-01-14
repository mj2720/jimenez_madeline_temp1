while True: 
     
     if input.sound_level() > 110:
        light.set_all(color.rgb(128,0,128))
     else:
        Sounds.SIREN