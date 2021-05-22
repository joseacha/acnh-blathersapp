import kivy
import sqlite3
from pprint import pprint
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput

conn = sqlite3.connect('fish.db')

c = conn.cursor()


class MainWindow(BoxLayout):
    topTitle = ObjectProperty(None)
    infoPage = ObjectProperty(None)
    submitButton = ObjectProperty(None)
    blathersIcon = ObjectProperty(None)
    bottomLabel = ObjectProperty(None)

    def btnPress(self):
        hen = printfish()
        fshlst = '\n'.join(map(str, hen))

        # print('button test')
        self.infoPage.text = str(fshlst)


def printfish():


    c.execute(""" SELECT name, price, location
    FROM 'fishes'
    WHERE strftime('%m', 'now', 'localtime') BETWEEN strftime('%m', start) AND  strftime('%m', end)
    AND strftime('%H %M', 'now', 'localtime') BETWEEN strftime('%H %M', start) AND strftime('%H %M', end) """)

    return c.fetchall()


class MyApp(App):
    def build(self):
        return MainWindow()

#
# a = printfish()
# print(*a,sep='\n')


if __name__ == "__main__":
    MyApp().run()


conn.commit()
conn.close()
