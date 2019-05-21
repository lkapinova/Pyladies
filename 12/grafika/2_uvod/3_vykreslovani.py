import pyglet

window = pyglet.window.Window(width=1000, height=700)

def tik(t):
    print(t)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    print(text)


pyglet.app.run()
