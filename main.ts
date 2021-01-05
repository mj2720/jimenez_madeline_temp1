while (true) {
    console.log("Light level:" + input.lightLevel())
    if (input.lightLevel() > 20) {
        light.showAnimation(light.rainbowAnimation, 5000)
    } else {
        light.clear()
    }
    
}
