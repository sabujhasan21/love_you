# love_gift_burst.py
import tkinter as tk
import random
import math

# ---------- CONFIG ----------
NUM_PETALS = 50
TYPE_SPEED = 50  # ms per character
SCREEN_DURATION = 3000  # ms per message

# ---------- HEART PETALS ----------
class HeartPetal:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.x = random.uniform(0, self.width)
        self.y = random.uniform(-self.height, -10)
        self.size = random.uniform(6, 12)
        self.speed = random.uniform(1.0, 2.5)
        self.swing = random.uniform(20, 80)
        self.phase = random.uniform(0, 2*math.pi)
        self.phase_speed = random.uniform(0.01, 0.04)
        self.scale = self.size/10
        self.id = self.create_heart()

    def create_heart(self):
        points = []
        for t in range(0,360,12):
            rad = math.radians(t)
            x = 16*math.sin(rad)**3
            y = 13*math.cos(rad) -5*math.cos(2*rad)-2*math.cos(3*rad)-math.cos(4*rad)
            points.append(self.x + x*self.scale)
            points.append(self.y - y*self.scale)
        return self.canvas.create_polygon(points, outline="#ff4d6d", fill="", width=2)

    def update(self):
        self.phase += self.phase_speed
        dx = math.sin(self.phase)*(self.swing*0.02)
        self.x += dx
        self.y += self.speed
        points=[]
        for t in range(0,360,12):
            rad = math.radians(t)
            x = 16*math.sin(rad)**3
            y = 13*math.cos(rad) -5*math.cos(2*rad)-2*math.cos(3*rad)-math.cos(4*rad)
            points.append(self.x + x*self.scale)
            points.append(self.y - y*self.scale)
        self.canvas.coords(self.id,*points)
        if self.y>self.height+40:
            self.canvas.delete(self.id)
            self.reset()

# ---------- HEART EXPLOSION ----------
class HeartExplosion:
    def __init__(self, canvas, x, y, count=20):
        self.canvas = canvas
        self.particles=[]
        for _ in range(count):
            angle = random.uniform(0,2*math.pi)
            speed = random.uniform(2,5)
            dx = math.cos(angle)*speed
            dy = math.sin(angle)*speed
            size = random.uniform(6,12)
            p = {'x':x,'y':y,'dx':dx,'dy':dy,'size':size,'id':self.canvas.create_oval(x,x+size,y,y+size, fill="#ff4d6d", outline="")}
            self.particles.append(p)

    def update(self):
        for p in self.particles:
            p['x'] += p['dx']
            p['y'] += p['dy']
            p['size'] *=0.95
            self.canvas.coords(p['id'], p['x'],p['y'],p['x']+p['size'],p['y']+p['size'])

# ---------- TYPEWRITER TEXT ----------
class TypewriterText:
    def __init__(self, canvas, x, y, font, messages, callback=None):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.font = font
        self.messages = messages
        self.index = 0
        self.char_index = 0
        self.text_id = self.canvas.create_text(x, y, text="", font=self.font, fill="#ffe6f2", justify="center")
        self.callback = callback
        self.next_message()

    def next_message(self):
        if self.index >= len(self.messages):
            if self.callback:
                self.callback()  # call last interface
            return
        self.char_index = 0
        self.current_msg = self.messages[self.index]
        self.index += 1
        self.type_next_char()

    def type_next_char(self):
        if self.char_index <= len(self.current_msg):
            self.canvas.itemconfig(self.text_id, text=self.current_msg[:self.char_index])
            self.char_index += 1
            self.canvas.after(TYPE_SPEED, self.type_next_char)
        else:
            self.canvas.after(SCREEN_DURATION, self.next_message)

# ---------- MAIN APP ----------
class LoveApp:
    def __init__(self, root):
        self.root = root
        root.title("❤️ Love Gift Animation ❤️")
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        root.geometry(f"{self.width}x{self.height}")
        root.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#1a0f1f")
        self.canvas.pack()

        # Petals & explosions
        self.petals = [HeartPetal(self.canvas,self.width,self.height) for _ in range(NUM_PETALS)]
        self.explosions = []

        # Gift box as 💝 emoji in white
        self.gift_id = self.canvas.create_text(self.width//2, self.height//2, text="💝", font=("Arial", 120), fill="white")
        # Text below gift
        self.instruction_id = self.canvas.create_text(self.width//2, self.height//2+100, text="Open the box", font=("Georgia",28,"italic"), fill="#ffe6f2")
        self.canvas.tag_bind(self.gift_id, "<Button-1>", self.open_gift)

        self.animate()
        self.root.after(5000,self.create_explosion)

    def open_gift(self, event=None):
        # Remove gift & instruction
        self.canvas.delete(self.gift_id)
        self.canvas.delete(self.instruction_id)
        # Heart explosion like gift burst
        for _ in range(5):
            self.explosions.append(HeartExplosion(self.canvas, self.width//2, self.height//2, count=20))
        # Start typewriter messages
        self.messages = [
            "My heart smiles whenever I think of you.",
            "You are the sweetest part of my life.",
            "Every moment with you feels like magic.",
            "You make my ordinary days feel special.",
            "Your love is the reason I believe in happiness.",
            "You are my peace, my joy, my everything.",
            "My world feels complete because of you.",
            "And lastly..."
        ]
        self.text = TypewriterText(self.canvas,self.width//2,self.height//2,("Georgia",36,"bold"),
                                   self.messages,self.show_final_interface)

    def show_final_interface(self):
        # Clear canvas except background
        self.canvas.delete("all")
        self.canvas.configure(bg="#1a0f1f")
        # Petals & explosions continue
        self.petals = [HeartPetal(self.canvas,self.width,self.height) for _ in range(NUM_PETALS)]
        self.explosions = []
        # Fade-in "I love you, Sona"
        self.final_text_id = self.canvas.create_text(self.width//2,self.height//2,
                                                     text="I love you, Sona ❤️",
                                                     font=("Georgia",72,"bold"),
                                                     fill="#ff4d6d", state='hidden')
        self.alpha = 0
        self.fade_in_final_text()

    def fade_in_final_text(self):
        self.alpha += 5
        if self.alpha>255:
            self.alpha = 255
        color = f"#{self.alpha:02x}4d6d"
        self.canvas.itemconfig(self.final_text_id, fill=color, state='normal')
        if self.alpha<255:
            self.canvas.after(50, self.fade_in_final_text)

    def create_explosion(self):
        x = random.randint(self.width//3, 2*self.width//3)
        y = random.randint(self.height//3, 2*self.height//3)
        self.explosions.append(HeartExplosion(self.canvas,x,y))
        self.root.after(4000, self.create_explosion)

    def animate(self):
        for p in self.petals:
            p.update()
        for e in self.explosions:
            e.update()
        self.root.after(30,self.animate)

root = tk.Tk()
LoveApp(root)
root.mainloop()
