# Copyright (c) RedFantom 2017
# For license see LICENSE
from ttkwidgets import ScrolledFrame
from tests import BaseWidgetTest
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class TestVerticalScrollFrame(BaseWidgetTest):
    def test_vertical_scroll_frame_init(self):
        frame = ScrolledFrame(self.window)
        frame.pack()
        self.window.update()

    def test_scrollframe_scroll(self):
        frame = ScrolledFrame(self.window)
        frame._mouse_wheel(self.ScrollEvent())

    def test_scrollframe_configure(self):
        frame = ScrolledFrame(self.window)
        frame.resize_canvas(200, 200)

    def test_scrollframe_configure_interior(self):
        frame = ScrolledFrame(self.window)
        label = tk.Label(frame, text="Great label")
        label.grid()

    class ScrollEvent(object):
        delta = 100
