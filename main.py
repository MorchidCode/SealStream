from tkinter import *
from tkinter import filedialog, font, PhotoImage
from PIL import Image, ImageDraw, ImageFont, ImageTk

image = None

def open_main_image():
    global image, image_label
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)

    lable_image = ImageTk.PhotoImage(image)
    image_label.config(image=lable_image)
    image_label.image = lable_image

def add_logo():
    global image, image_label
    logo_path = filedialog.askopenfilename()

    logo = Image.open(logo_path)
    logo = logo.resize((80, 80), Image.Resampling.LANCZOS)

    image.paste(logo, (0,0), logo)

    lable_image = ImageTk.PhotoImage(image)
    image_label.config(image=lable_image)
    image_label.image = lable_image


def add_text():
    global image, image_label
    text = text_erea.get("1.0", "end-1c")
    
    width, height = image.size
    draw = ImageDraw.Draw(image)

    font_size = int(width / 35)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)

    x, y = int(width/2), int(height/2)
    draw.text((x, y), text, font=font, fill="#FFF", stroke_width=3, stroke_fill="#222", anchor="ms")

    lable_image = ImageTk.PhotoImage(image)
    image_label.config(image=lable_image)
    image_label.image = lable_image



def save_image():
    saving_path = filedialog.asksaveasfilename(defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
    image.save(saving_path)




window = Tk()
window.config(bg="#45474B")
window.title("SealStream")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set window size to screen size
window.geometry(f"{screen_width}x{screen_height}")


# Create a right bar
right_bar = Frame(window, width=300, height=screen_height, bg="#454545")
right_bar.pack(side='right', fill='y', expand=False)

# Open the main image button.
open_image_button = Button(right_bar, text="Open Image", fg="#FFF", bg="#45474B", width=29, height=2, command=open_main_image)
open_image_button.pack(side="top", padx=5, pady=40)

# Create an Entry widget
text_font = font.Font(size=14)
text_erea = Text(right_bar, width=21, height=3, font=text_font)
text_erea.pack(side="top", padx=5)

# Add text as watermark button.
add_text_button = Button(right_bar, text="Add Text", fg="#FFF", bg="#45474B", width=29, height=2, command=add_text)
add_text_button.pack(side="top", padx=5, pady=10) 

# Select Logo button.
select_logo_button = Button(right_bar, text="Select logo", fg="#FFF", bg="#45474B", width=29, height=2, command=add_logo)
select_logo_button.pack(side="top", padx=5, pady=10)

# Select Logo button.
save_button = Button(right_bar, text="Save ", fg="#FFF", bg="#45474B", width=29, height=2, command=save_image)
save_button.pack(side="top", padx=5, pady=10)

# Create a label to display the image
image_label = Label(window, bg="#45474B", width=1000, height=700)
image_label.pack(side='left', padx=50, pady=10, fill='y')

window.mainloop()