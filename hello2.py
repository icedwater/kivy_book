#! /usr/bin/env python

"""
Subclassing example from the first chapter.
"""
from kivy.app import App

class WeatherApp(App):
    """
    Still does nothing, as shown in the book. But it will retrieve its layout
    from the attached weather.kv file. Pylint complains because App has 45/20
    public methods, but what can we do?
    """
    pass

if __name__ == "__main__":
    WeatherApp().run()
