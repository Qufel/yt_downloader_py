import eel

eel.init('gui')

@eel.expose
def App():
    print('App is running...')

App()

eel.start('index.html', size=(300,200))