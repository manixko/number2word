# 🔢 Number to Words Converter

This is a simple Python program that converts numbers into their English word representation.  
For example:
- `42` → `forty two`
- `317` → `three hundred and seventeen`

---

## 🚀 Features
- Converts numbers from **0 to 999** into words.
- Handles user input interactively.
- Displays helpful error messages for invalid inputs.
- Option to **exit** the program by typing `exit`.

---

## 📂 Project Structure
    project/
    |── src/
        │── constants.py # Stores word mappings for numbers
        │── number2word.py # Main program (converter logic and CLI)

---

## ▶️ How to Run
1. Clone this repository or download the files.
2. Make sure you have **Python 3** installed.
3. Run the program in your terminal:
   ```bash
   python src/number2word.py
    ```
4. Enter a number and see the output in words.
5. Type `exit` to quit.

---

## ⚠️ Limitations
- Only supports numbers from 0 to 999.
- Negative numbers are not supported.