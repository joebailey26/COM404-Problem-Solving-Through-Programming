  # The available from currencies
  self.from_choices = [ "GBP", "Euros"]

  # A variable to track the currently selected option
  self.from _selected = StringVar()

  # The default value
  self.from_selected.set("GBP")

  # The from currency option menu
  self.from_optionmenu = OptionMenu(self, self.from_selected, *self.choices)
  self.from_optionmenu.pack(fill=X)
