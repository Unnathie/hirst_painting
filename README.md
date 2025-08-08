# 🎨 Hirst Spot Painting Generator – Python Turtle Magic  
Ever looked at Damien Hirst’s dot paintings and thought, *“I could make that… but with Python”*? Well, now you can. This project uses Python’s `turtle` graphics to generate a **Hirst-style spot painting** with 100 beautifully random dots.  
## ✨ Features  
- **Randomized colors** from a hand-picked palette extracted from a real image.  
- **10x10 grid** of colorful dots – change it if you want bigger or smaller paintings.  
- Built with Python’s friendly `turtle` module – no art degree required.  
- Fully customizable: dot size, spacing, and colors are all yours to tweak.  
## 🖌 How It Works  
1. **Color extraction (optional)** – Uses `colorgram.py` to grab colors from an image (already done for you with a preloaded list).  
2. **Turtle setup** – Hides the turtle, sets RGB mode, and moves to the starting corner.  
3. **Painting** – Loops through rows and columns, placing randomly chosen dots from the palette until your masterpiece is complete.  
## 🕹 How to Run It  
1. Clone the repo:  
   git clone https://github.com/Unnathie/hirst_painting.git  
   cd hirst_painting  
2. Install dependencies (only if you want to extract your own colors):  
   pip install colorgram.py  
3. Run the script:  
   python main.py  
4. Watch as your screen comes alive with a splash of colors.  
5. Click anywhere in the turtle window to close it when you’re done admiring your work.  
## 📸 Example Output  
Here’s the outcome: your exact painting will be unique every time:  
![Example Output](example.png)  
<img width="958" height="840" alt="image" src="https://github.com/user-attachments/assets/32e95002-8108-4c98-8f11-a0d0e6874721" />

## ⚙️ Customize Your Masterpiece  
- **Change grid size** → Edit the loop ranges in the code.  
- **Change dot size** → Modify `timmy.dot(20)` to your liking.  
- **Change spacing** → Adjust the distance in  `timmy.teleport(...)`.  
- **Use your own palette** → Uncomment the color extraction code at the top and point it to a new image.  
## 📦 Requirements  
- Python 3.x  
- `colorgram.py` (only needed for custom color extraction)  
## 🚀 Future Fun Ideas  
- Randomize grid size and dot size every run.  
- Add multiple palettes to choose from.  
- Save the finished artwork as an image file automatically.  
## 📜 License  
MIT License – Fork it, paint with it, and share the joy.  
