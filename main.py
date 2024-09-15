import tkinter as  tk


class Mianpage:
    def __init__(self, master:tk.Tk):
        self.root = master
        self.root.title('manpage')
        self.root.geometry('600x400')
        self.create_page()

    def create_page(self):
        self.about_frame = tk.Frame(self.root)
        tk.Label(self.about_frame, text='使用python制作').pack()
        tk.Label(self.about_frame, text='tkinter').pack()
        tk.Label(self.about_frame, text='最后一次更新日期2024-09-15，版本：1.0 DEV').pack()

        self.xkz_frame = tk.Frame(self.root)
        tk.Label(self.xkz_frame, text='许可证').pack()

        self.password_frame = tk.Frame(self.root)
        tk.Label(self.password_frame, text='密码').pack()

        self.tool_frame = tk.Frame(self.root)
        tk.Label(self.tool_frame, text='配置工具').pack()

        self.star_frame = tk.Frame(self.root)
        tk.Label(self.star_frame, text='查询').pack()

        menubar = tk.Menu(self.root)
        menubar.add_command(label='查询',command=self.show_star)
        menubar.add_command(label='工具',command=self.show_tool)
        menubar.add_command(label='密码',command=self.show_password)
        menubar.add_command(label='许可证',command=self.show_xkz)
        menubar.add_command(label='关于',command=self.show_about)
        self.root['menu'] = menubar

    def show_about(self):
        self.about_frame.pack()
        self.xkz_frame.pack_forget()
        self.password_frame.pack_forget()
        self.tool_frame.pack_forget()
        self.star_frame.pack_forget()

    def show_xkz(self):
        self.xkz_frame.pack()
        self.about_frame.pack_forget()
        self.password_frame.pack_forget()
        self.tool_frame.pack_forget()
        self.star_frame.pack_forget()

    def show_password(self):
        self.password_frame.pack()
        self.about_frame.pack_forget()
        self.xkz_frame.pack_forget()
        self.tool_frame.pack_forget()
        self.star_frame.pack_forget()

    def show_tool(self):
        self.tool_frame.pack()
        self.about_frame.pack_forget()
        self.xkz_frame.pack_forget()
        self.password_frame.pack_forget()
        self.star_frame.pack_forget()

    def show_star(self):
        self.star_frame.pack()
        self.about_frame.pack_forget()
        self.tool_frame.pack_forget()
        self.xkz_frame.pack_forget()
        self.password_frame.pack_forget()

if __name__ == '__main__':
    root = tk.Tk()
    Mianpage(root)
    root.mainloop()