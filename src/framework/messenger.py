import libtcodpy as libtcod
import textwrap

class Messenger:
    def __init__(self, max_height, max_width):
        self.messages = []
        self.max_width = max_width
        self.max_height = max_height

    def send(self, msg, color = libtcod.white):
        msg_lines = textwrap.wrap(msg, self.max_width)
        
        for line in msg_lines:
            if len(self.messages) == self.max_height:
                del self.messages[0]

            self.messages.append((line, color))
    
