class Dialog:
    # Interface
    # Creator class that declares the factory method
    def create_button(self):
        pass

    def render(self):
        pass


# Concrete creators override the factory method.
class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()


class Button:
    # Interface
    # Declares the operations that all concrete products must implement
    def render(self):
        pass

    def on_click(self, f):
        pass


class WindowsButton(Button):
    def render(self):
        pass

    def on_click(self, f):
        pass


class HTMLButton(Button):
    def render(self):
        pass

    def on_click(self, f):
        pass
