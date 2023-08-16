import tkinter as tk


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Blue Circle on Green Background")
    
    # Set the window size
    window_width = 800
    window_height = 800
    root.geometry(f"{window_width}x{window_height}")
    
    # Create a canvas to draw on
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="green")
    canvas.pack()
    
    # Calculate circle position and dimensions
    circle_radius = 10
    circle_center_x = window_width // 2
    circle_center_y = window_height // 2
    
    # Draw the blue circle
    circle = canvas.create_oval(
        circle_center_x - circle_radius,
        circle_center_y - circle_radius,
        circle_center_x + circle_radius,
        circle_center_y + circle_radius,
        fill="blue"
    )
    
    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()

# import tkinter as tk

# root = tk.Tk()
# root.title("Circle Movement Game")

# canvas = tk.Canvas(root, width= 800, height= 600)
# canvas.pack()

# circle_radius = 20
# canvas_width = canvas.winfo_reqwidth()
# canvas_height = canvas.winfo_reqheight()

# circle_x = canvas_width // 2  # starting coordinates for x/y
# circle_y = canvas_height // 2

# circle = canvas.create_oval(
#     circle_x - circle_radius, circle_y - circle_radius,
#     circle_x + circle_radius, circle_y + circle_radius,
#     fill="red"
# )

# def move_circle(event):
#     global circle_x, circle_y
#     circle_x = event.x
#     circle_y = event.y
#     canvas.coords(circle, circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius)

# canvas.bind("<Button-1>", move_circle)

# root.mainloop()