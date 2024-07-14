#import jarvis wishme action
from jarvis_actions import wishme

#import jarvis gui
import jarvis_GUI


#start program
if __name__ == "__main__":
    #greet user
    wishme()

    #launch gui window
    app = jarvis_GUI.App()
    app.mainloop()
