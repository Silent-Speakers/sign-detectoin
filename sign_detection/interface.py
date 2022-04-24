import tkinter as tk
import tkinter.font as tkFont
from  sign_detection import SignDetection

class App:
    def __init__(self, root):
        #setting title
        root.title("Finger Spaek")
        #setting window size
        width=787
        height=514
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_524=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#6882b6"
        GLabel_524["justify"] = "center"
        GLabel_524["text"] = "FingerSpeak"
        GLabel_524.place(x=310,y=0,width=159,height=51)

        GMessage_251=tk.Message(root)
        GMessage_251["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_251["font"] = ft
        GMessage_251["fg"] = "#393d49"
        GMessage_251["justify"] = "center"
        GMessage_251["text"] = ""
        GMessage_251.place(x=210,y=100,width=175,height=192)

        GButton_67=tk.Button(root)
        GButton_67["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_67["font"] = ft
        GButton_67["fg"] = "#6882b6"
        GButton_67["justify"] = "center"
        GButton_67["text"] = "Listen to the word"
        GButton_67.place(x=240,y=200,width=126,height=30)
        GButton_67["command"] = self.GButton_67_command

        GButton_116=tk.Button(root)
        GButton_116["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_116["font"] = ft
        GButton_116["fg"] = "#6882b6"
        GButton_116["justify"] = "center"
        GButton_116["text"] = "practice"
        GButton_116.place(x=270,y=240,width=70,height=25)
        GButton_116["command"] = self.GButton_116_command

        GLabel_291=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_291["font"] = ft
        GLabel_291["fg"] = "#6882b6"
        GLabel_291["justify"] = "center"
        GLabel_291["text"] = "NICE"
        GLabel_291.place(x=230,y=110,width=138,height=49)

        GMessage_899=tk.Message(root)
        GMessage_899["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_899["font"] = ft
        GMessage_899["fg"] = "#333333"
        GMessage_899["justify"] = "center"
        GMessage_899["text"] = ""
        GMessage_899.place(x=410,y=100,width=175,height=192)

        GButton_42=tk.Button(root)
        GButton_42["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_42["font"] = ft
        GButton_42["fg"] = "#6882b6"
        GButton_42["justify"] = "center"
        GButton_42["text"] = "practice"
        GButton_42.place(x=460,y=240,width=70,height=25)
        GButton_42["command"] = self.GButton_42_command

        GButton_771=tk.Button(root)
        GButton_771["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_771["font"] = ft
        GButton_771["fg"] = "#6882b6"
        GButton_771["justify"] = "center"
        GButton_771["text"] = "Listen to the word"
        GButton_771.place(x=440,y=200,width=118,height=30)
        GButton_771["command"] = self.GButton_771_command

        GLabel_587=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_587["font"] = ft
        GLabel_587["fg"] = "#6882b6"
        GLabel_587["justify"] = "center"
        GLabel_587["text"] = "YELLOW"
        GLabel_587.place(x=430,y=110,width=138,height=49)

        GMessage_723=tk.Message(root)
        GMessage_723["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_723["font"] = ft
        GMessage_723["fg"] = "#393d49"
        GMessage_723["justify"] = "center"
        GMessage_723["text"] = ""
        GMessage_723.place(x=600,y=100,width=175,height=192)

        GButton_779=tk.Button(root)
        GButton_779["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#6882b6"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "Listen to the word"
        GButton_779.place(x=620,y=200,width=132,height=30)
        GButton_779["command"] = self.GButton_779_command

        GButton_642=tk.Button(root)
        GButton_642["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_642["font"] = ft
        GButton_642["fg"] = "#6882b6"
        GButton_642["justify"] = "center"
        GButton_642["text"] = "practice"
        GButton_642.place(x=650,y=240,width=70,height=25)
        GButton_642["command"] = self.GButton_642_command

        GLabel_579=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_579["font"] = ft
        GLabel_579["fg"] = "#6882b6"
        GLabel_579["justify"] = "center"
        GLabel_579["text"] = "I LOVE YOU"
        GLabel_579.place(x=620,y=110,width=144,height=49)

        GLabel_187=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_187["font"] = ft
        GLabel_187["fg"] = "#333333"
        GLabel_187["justify"] = "center"
        GLabel_187["text"] = "YES"
        GLabel_187.place(x=30,y=340,width=138,height=58)

        GMessage_794=tk.Message(root)
        GMessage_794["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_794["font"] = ft
        GMessage_794["fg"] = "#333333"
        GMessage_794["justify"] = "center"
        GMessage_794["text"] = ""
        GMessage_794.place(x=210,y=300,width=175,height=192)

        GButton_442=tk.Button(root)
        GButton_442["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_442["font"] = ft
        GButton_442["fg"] = "#6882b6"
        GButton_442["justify"] = "center"
        GButton_442["text"] = "Listen to the word"
        GButton_442.place(x=240,y=390,width=125,height=31)
        GButton_442["command"] = self.GButton_442_command

        GButton_500=tk.Button(root)
        GButton_500["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_500["font"] = ft
        GButton_500["fg"] = "#6882b6"
        GButton_500["justify"] = "center"
        GButton_500["text"] = "practice"
        GButton_500.place(x=270,y=430,width=70,height=25)
        GButton_500["command"] = self.GButton_500_command

        GLabel_347=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_347["font"] = ft
        GLabel_347["fg"] = "#6882b6"
        GLabel_347["justify"] = "center"
        GLabel_347["text"] = "NO"
        GLabel_347.place(x=230,y=310,width=138,height=49)

        GMessage_491=tk.Message(root)
        GMessage_491["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_491["font"] = ft
        GMessage_491["fg"] = "#333333"
        GMessage_491["justify"] = "center"
        GMessage_491["text"] = ""
        GMessage_491.place(x=410,y=300,width=175,height=192)

        GButton_499=tk.Button(root)
        GButton_499["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#6882b6"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "Listen to the word"
        GButton_499.place(x=430,y=390,width=135,height=32)
        GButton_499["command"] = self.GButton_499_command

        GButton_267=tk.Button(root)
        GButton_267["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_267["font"] = ft
        GButton_267["fg"] = "#6882b6"
        GButton_267["justify"] = "center"
        GButton_267["text"] = "practice"
        GButton_267.place(x=460,y=430,width=70,height=25)
        GButton_267["command"] = self.GButton_267_command

        GLabel_746=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_746["font"] = ft
        GLabel_746["fg"] = "#6882b6"
        GLabel_746["justify"] = "center"
        GLabel_746["text"] = "GREEN"
        GLabel_746.place(x=430,y=310,width=138,height=49)

        GMessage_163=tk.Message(root)
        GMessage_163["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_163["font"] = ft
        GMessage_163["fg"] = "#a7a3a3"
        GMessage_163["justify"] = "center"
        GMessage_163["text"] = ""
        GMessage_163.place(x=20,y=100,width=175,height=192)

        GLabel_986=tk.Label(root)
        GLabel_986["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_986["font"] = ft
        GLabel_986["fg"] = "#333333"
        GLabel_986["justify"] = "center"
        GLabel_986["text"] = ""
        GLabel_986.place(x=20,y=300,width=175,height=192)

        GButton_459=tk.Button(root)
        GButton_459["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_459["font"] = ft
        GButton_459["fg"] = "#6882b6"
        GButton_459["justify"] = "center"
        GButton_459["text"] = "Listen to the word"
        GButton_459.place(x=40,y=390,width=132,height=30)
        GButton_459["command"] = self.GButton_459_command

        GButton_154=tk.Button(root)
        GButton_154["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_154["font"] = ft
        GButton_154["fg"] = "#6882b6"
        GButton_154["justify"] = "center"
        GButton_154["text"] = "practice"
        GButton_154.place(x=70,y=430,width=70,height=25)
        GButton_154["command"] = self.GButton_154_command

        GLabel_483=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_483["font"] = ft
        GLabel_483["fg"] = "#6882b6"
        GLabel_483["justify"] = "center"
        GLabel_483["text"] = "YES"
        GLabel_483.place(x=40,y=310,width=138,height=49)

        GLabel_250=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_250["font"] = ft
        GLabel_250["fg"] = "#6882b6"
        GLabel_250["justify"] = "center"
        GLabel_250["text"] = "HELLO"
        GLabel_250.place(x=40,y=110,width=138,height=49)

        GButton_282=tk.Button(root)
        GButton_282["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_282["font"] = ft
        GButton_282["fg"] = "#6882b6"
        GButton_282["justify"] = "center"
        GButton_282["text"] = "Listen to the word"
        GButton_282.place(x=40,y=200,width=132,height=30)
        GButton_282["command"] = self.GButton_282_command

        GButton_754=tk.Button(root)
        GButton_754["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_754["font"] = ft
        GButton_754["fg"] = "#6882b6"
        GButton_754["justify"] = "center"
        GButton_754["text"] = "practice"
        GButton_754.place(x=70,y=240,width=70,height=25)
        GButton_754["command"] = self.GButton_754_command

        GMessage_506=tk.Message(root)
        GMessage_506["bg"] = "#316684"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_506["font"] = ft
        GMessage_506["fg"] = "#333333"
        GMessage_506["justify"] = "center"
        GMessage_506["text"] = ""
        GMessage_506.place(x=600,y=300,width=175,height=192)

        GButton_506=tk.Button(root)
        GButton_506["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_506["font"] = ft
        GButton_506["fg"] = "#6882b6"
        GButton_506["justify"] = "center"
        GButton_506["text"] = "Listen to the word"
        GButton_506.place(x=620,y=390,width=138,height=32)
        GButton_506["command"] = self.GButton_506_command

        GButton_969=tk.Button(root)
        GButton_969["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_969["font"] = ft
        GButton_969["fg"] = "#6882b6"
        GButton_969["justify"] = "center"
        GButton_969["text"] = "practice"
        GButton_969.place(x=650,y=430,width=70,height=25)
        GButton_969["command"] = self.GButton_969_command

        GLabel_314=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_314["font"] = ft
        GLabel_314["fg"] = "#6882b6"
        GLabel_314["justify"] = "center"
        GLabel_314["text"] = "PURPLE"
        GLabel_314.place(x=620,y=310,width=138,height=49)

        GLabel_449=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_449["font"] = ft
        GLabel_449["fg"] = "#6882b6"
        GLabel_449["justify"] = "center"
        GLabel_449["text"] = "Start  Translating your words by choosing a Card"
        GLabel_449.place(x=130,y=50,width=538,height=40)

    def GButton_67_command(self):
        SignDetection().voice_output("NICE")


    def GButton_116_command(self):
        SignDetection().hand_detection()


    def GButton_42_command(self):
        SignDetection().hand_detection()


    def GButton_771_command(self):
        SignDetection().voice_output("YELLOW")


    def GButton_779_command(self):
        SignDetection().voice_output("I LOVE YOU")


    def GButton_642_command(self):
        SignDetection().hand_detection()


    def GButton_442_command(self):
        SignDetection().voice_output("NO")


    def GButton_500_command(self):
        SignDetection().hand_detection()



    def GButton_499_command(self):
        SignDetection().voice_output("GREEN")


    def GButton_267_command(self):
        SignDetection().hand_detection()


    def GButton_459_command(self):
        SignDetection().voice_output("YES")


    def GButton_154_command(self):
        SignDetection().hand_detection()


    def GButton_282_command(self):
        SignDetection().voice_output("HELLO")


    def GButton_754_command(self):
        SignDetection().hand_detection()



    def GButton_506_command(self):
        SignDetection().voice_output("PURPLE")


    def GButton_969_command(self):
        SignDetection().hand_detection()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()