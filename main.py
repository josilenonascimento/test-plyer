# coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from plyer import vibrator, battery, notification
from plyer.utils import platform


class RootWidget(BoxLayout):

	data = StringProperty("0")
	
	def __init__(self, **kwargs):
		super(RootWidget, self).__init__(**kwargs)
		self.data = str(platform)	

	def vibrate(self, *args):
		if platform == "android" or platform == "ios":
			vibrator.vibrate(2) # vibrate for 2 seconds
		else:
			self.data = "Vibrator not found"
	
	def notify(self, *args):
		notification.notify(title="My title", message="Hello, World!")

	def battery(self, *args):
		self.data = str(battery.status['percentage']) + "%"


class MyApp(App):
	...


if __name__ == "__main__":
	MyApp().run()

