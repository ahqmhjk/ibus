import dbus.service
from ibus.common import \
	IBUS_ENGINE_IFACE

class IEngine (dbus.service.Object):
	# define method decorator.
	method = lambda **args: \
		dbus.service.method (dbus_interface = IBUS_ENGINE_IFACE, \
							 **args)

	# define signal decorator.
	signal = lambda **args: \
		dbus.service.signal (dbus_interface = IBUS_ENGINE_IFACE, \
							 **args)

	# define async method decorator.
	async_method = lambda **args: \
		dbus.service.method (dbus_interface = IBUS_ENGINE_IFACE, \
							 async_callbacks = ("reply_cb", "error_cb"), \
							 **args)

	@method (in_signature = "ubu", out_signature = "b")
	def ProcessKeyEvent (self, keyval, is_press, state):
		pass

	@method (in_signature = "iiii")
	def SetCursorLocation (self, x, y, w, h): pass

	@method ()
	def FocusIn (self): pass

	@method ()
	def FocusOut (self): pass

	@method ()
	def Reset (self): pass

	@method (in_signature = "b")
	def SetEnable (self, enable): pass

	@method (in_signature = "s")
	def TriggerProperty (self, property): pass

	@method ()
	def Destroy (self): pass

	@signal (signature="s")
	def CommitString (self, text): pass

	@signal (signature="ubu")
	def ForwardKeyEvent (self, keyval, is_press, state): pass

	@signal (signature="saaii")
	def PreeditChanged (self, text, attrs, cursor_pos): pass

	# below signals are optional. The engine could create and maintain panel by self.
	@signal (signature="v")
	def UpdateProperties (self, properties): pass

	@signal (signature="sv")
	def AuxStringChanged (self, text, attrs): pass

	@signal (signature="v")
	def UpdateLookupTable (self, lookup_table): pass

	@signal ()
	def ShowLookupTable (self): pass

	@signal ()
	def HideLookupTable (self): pass

