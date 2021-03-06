"""
Author: RedFantom
License: GNU GPLv3
Source: This repository
"""
# Based on an idea by Nelson Brochado (https://www.github.com/nbro/tkinter-kit)
try:
    import Tkinter as tk
    import ttk
    import tkFont as font
except ImportError:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import font


class FontPropertiesFrame(ttk.Frame):
    """
    Simple frame with buttons for Bold, Italic and Undelrine font types
    """

    def __init__(self, master=None, callback=None, label=True, fontsize=11, **kwargs):
        """
        :param master: master widget
        :param callback: callback with argument (bool bold, bool italic, bool underline, bool overstrike)
        :param label: show a header label
        :param fontsize: size of the font on the buttons
        :param kwargs: keyword arguments passed on to Frame initializer
        """
        ttk.Frame.__init__(self, master, **kwargs)
        self._style = ttk.Style()
        self.__label = label
        self.__callback = callback
        self._header_label = ttk.Label(self, text="Font properties:")
        self._style.configure("Bold.Toolbutton", font=("default", fontsize, "bold"), anchor=tk.CENTER)
        self._style.configure("Italic.Toolbutton", font=("default", fontsize, "italic"), anchor=tk.CENTER)
        self._style.configure("Underline.Toolbutton", font=("default", fontsize, "underline"), anchor=tk.CENTER)
        self._style.configure("Overstrike.Toolbutton", font=("default", fontsize, "overstrike"), anchor=tk.CENTER)
        self._bold = tk.BooleanVar()
        self._italic = tk.BooleanVar()
        self._underline = tk.BooleanVar()
        self._overstrike = tk.BooleanVar()
        self._bold_button = ttk.Checkbutton(self, style="Bold.Toolbutton", text="B", width=2, command=self._on_click,
                                            variable=self._bold)
        self._italic_button = ttk.Checkbutton(self, style="Italic.Toolbutton", text="I", width=2,
                                              command=self._on_click, variable=self._italic)
        self._underline_button = ttk.Checkbutton(self, style="Underline.Toolbutton", text="U", width=2,
                                                 command=self._on_click, variable=self._underline)
        self._overstrike_button = ttk.Checkbutton(self, style="Overstrike.Toolbutton", text="O", width=2,
                                                  command=self._on_click, variable=self._overstrike)
        self._grid_widgets()

    def _grid_widgets(self):
        """
        Place the widgets in the correct positions
        :return: None
        """
        if self.__label:
            self._header_label.grid(row=0, column=1, columnspan=3, sticky="nw", padx=5, pady=(5, 0))
        self._bold_button.grid(row=1, column=1, sticky="nswe", padx=5, pady=2)
        self._italic_button.grid(row=1, column=2, sticky="nswe", padx=(0, 5), pady=2)
        self._underline_button.grid(row=1, column=3, sticky="nswe", padx=(0, 5), pady=2)
        self._overstrike_button.grid(row=1, column=4, sticky="nswe", padx=(0, 5), pady=2)

    def _on_click(self):
        """
        Handles clicks and calls callback
        :return: None
        """
        if callable(self.__callback):
            self.__callback((self.bold, self.italic, self.underline, self.overstrike))

    @property
    def bold(self):
        """
        :return: True if bold is selected
        """
        return self._bold.get()

    @property
    def italic(self):
        """
        :return: True if italic is selected
        """
        return self._italic.get()

    @property
    def underline(self):
        """
        :return: True if underline is selected
        """
        return self._underline.get()

    @property
    def overstrike(self):
        """
        :return: True if overstrike is selected
        """
        return self._overstrike.get()
