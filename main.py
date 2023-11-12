from tkinter import *
from tkinter import filedialog, font, PhotoImage
from PIL import Image, ImageDraw, ImageFont, ImageTk



class Watermark:
    def __init__(self):
        self.image = None

        self.window = Tk()
        self.window.config(bg="#45474B")
        self.window.title("SealStream")

        # Get the screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set window size to screen size
        self.window.geometry(f"{screen_width}x{screen_height}")


        # Create a right bar
        right_bar = Frame(self.window, width=300, height=screen_height, bg="#454545")
        right_bar.pack(side='right', fill='y', expand=False)

        # Open the main image button.
        open_image_button = Button(right_bar, text="Open Image", fg="#FFF", bg="#45474B", width=29, height=2, command=self.open_main_image)
        open_image_button.pack(side="top", padx=5, pady=40)

        # Create an Entry widget
        text_font = font.Font(size=14)
        self.text_erea = Text(right_bar, width=21, height=3, font=text_font)
        self.text_erea.pack(side="top", padx=5)

        # Add text as watermark button.
        add_text_button = Button(right_bar, text="Add Text", fg="#FFF", bg="#45474B", width=29, height=2, command=self.add_text)
        add_text_button.pack(side="top", padx=5, pady=10) 

        # Select Logo button.
        select_logo_button = Button(right_bar, text="Select logo", fg="#FFF", bg="#45474B", width=29, height=2, command=self.add_logo)
        select_logo_button.pack(side="top", padx=5, pady=10)

        # Select Logo button.
        save_button = Button(right_bar, text="Save ", fg="#FFF", bg="#45474B", width=29, height=2, command=self.save_image)
        save_button.pack(side="top", padx=5, pady=10)

        # Create a label to display the image
        self.image_label = Label(self.window, bg="#45474B", width=1000, height=700)
        self.image_label.pack(side='left', padx=50, pady=10, fill='y')

        self.window.mainloop()


    def open_main_image(self):
        image_path = filedialog.askopenfilename()
        self.image = Image.open(image_path)

        self.add_image_to_window()

    def add_logo(self):
        logo_path = filedialog.askopenfilename()

        logo = Image.open(logo_path)
        logo = logo.resize((80, 80), Image.Resampling.LANCZOS)

        self.image.paste(logo, (0,0), logo)
        self.add_image_to_window()





    def add_text(self):
        text = self.text_erea.get("1.0", "end-1c")
        
        width, height = self.image.size
        draw = ImageDraw.Draw(self.image)

        font_size = int(width / 35)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)

        x, y = int(width/2), int(height/2)
        draw.text((x, y), text, font=font, fill="#FFF", stroke_width=3, stroke_fill="#222", anchor="ms")

        self.add_image_to_window()



    def save_image(self):
        saving_path = filedialog.asksaveasfilename(defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        self.image.save(saving_path)


    def add_image_to_window(self):
        self.lable_image = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.lable_image)
        self.image_label.image = self.lable_image

Watermark()