import tkinter as tk


# It is either pack-pack or grid-gird
# But inside a packed frame you can use grid

def calc(a=0, b=0):
    
    ans = tk.Label(frame, text=f"Answer={a+b}")
    ans.grid(row=2)

root = tk.Tk()
root.title('Calculator')

frame = tk.LabelFrame(root, text='Add 2 nums', padx=50, pady=50)
frame.pack(padx=10, pady=10)


inp1 = tk.Text(frame, height=2, widt=10)
inp2 = tk.Text(frame, height=2, widt=10)
inp1.grid(row=0, column=0)
inp2.grid(row=0, column=1)

b2 = tk.Button(frame, text="Calculate", command=lambda: calc(float(inp1.get(1.0, "end-1c")), float(inp2.get(1.0, "end-1c"))))
b2.grid(row=1)


root.mainloop()
