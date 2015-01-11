__author__ = 'Allen'
from Tkinter import *
import time, math


class DrunkVisualize:

    def __init__(self, field, delay = 0.2):
        "Initializes a visualization with the specified parameters."
        # Number of seconds to pause after each frame
        self.delay = delay
        self.field = field
        self.edges = field.getEdges()
        width, height = self.findDimensions(self.edges)

        self.max_dim = max(width, height)
        self.width = width
        self.height = height
        self.drunks = [drunk for drunk in field.drunks] # drunks in field is a dict

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(width, height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        # Draw gray squares for locations moved to
        self.tiles = {}
        for i in range(width):
            for j in range(height):
                x1, y1 = self._map_coords(i, j)
                x2, y2 = self._map_coords(i + 1, j + 1)
                self.tiles[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                             fill = "gray")

        # Draw gridlines
        for i in range(width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(width, i)
            self.w.create_line(x1, y1, x2, y2)

        # Draw some status text
        self.drunks = None
        self.text = self.w.create_text(25, 0, anchor=NW,
                                       text=self._status_string(0, 0))
        self.time = 0
        self.master.update()


    def _draw_drunk(self, position, direction):
        "Returns a polygon representing a drunk with the specified parameters."
        x, y = position
        d1 = direction + 165
        d2 = direction - 165
        x1, y1 = self._map_coords(x, y)
        x2, y2 = self._map_coords(x + 0.6 * math.sin(math.radians(d1)),
                                  y + 0.6 * math.cos(math.radians(d1)))
        x3, y3 = self._map_coords(x + 0.6 * math.sin(math.radians(d2)),
                                  y + 0.6 * math.cos(math.radians(d2)))
        return self.w.create_polygon([x1, y1, x2, y2, x3, y3], fill="red")


    def update(self, field, drunks):
        "Redraws the visualization with the specified room and robot state."
        # Removes a gray square for any tiles have been cleaned.
        # for i in range(self.width):
        #     for j in range(self.height):
        #         if room.isTileCleaned(i, j):
        #             self.w.delete(self.tiles[(i, j)])
        # Delete all existing robots.
        if self.drunks:
            for drunk in self.drunks:
                self.w.delete(drunk)
                self.master.update_idletasks()
        # Draw new robots
        self.drunks = []
        for drunk in field.getDrunks():
            x, y = drunk.getLocation()
            x1, y1 = self._map_coords(x - 0.08, y - 0.08)
            x2, y2 = self._map_coords(x + 0.08, y + 0.08)
            self.drunks.append(self.w.create_oval(x1, y1, x2, y2,
                                                  fill = "black"))
            self.drunks.append(self._draw_drunk((x, y), drunk.getDirection()))

        # Update text
        # self.w.delete(self.text)
        self.w.delete(self.text)
        self.time += 1
        self.text = self.w.create_text(
            25, 0, anchor=NW,
            text=self._status_string(self.time, field.getEdgeHitCount()))
        self.master.update()
        time.sleep(self.delay)

    def _status_string(self, time, num_edges_hit):
        "Returns an appropriate status string to print."
        return "Time: %04d; %d Edges hit" % \
            (time, num_edges_hit)

    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

    def findDimensions(self, edges):
        width = abs(edges[1] - edges[0])
        height = abs(edges[3] - edges[2])

        return width, height

    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()