import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry('500x500')
root.title('Image')
# root.iconbitmap('C:\\Program Files\\Google\\Chrome\\Applicationicon\\Instagram.ico')
root.resizable(False, False)
# img = ImageTk.PhotoImage(Image.open("F:\\Pictures\\rasmoi xudam\\20220915_172327.jpg"))
# label = tk.Label(root, text='Image', image=img, font=('Times New Roman', 20, 'bold'),)
p = tk.PhotoImage(file='F:\\Pictures\\rasmoi xudam\\20220915_172327.jpg',)
a = Image.open("F:\\Pictures\\foto\\NDV_UZ_Objects (3).jpg")
#label.pack()
root.mainloop()


