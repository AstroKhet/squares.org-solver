# Squares Solver

Solver for the word puzzle game [Squares](https://squares.org/).

## How to Use

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/squares-solver.git
cd squares-solver
```

2. **Set the board you want to solve**  
   In `solver.py`, update the variable `flattened_board` with your 4x4 board.  
   For example, the board:

```
A S X E
R T G B
O P T E
A M N V
```

would be represented as:

```python
flattened_board = "ASXERTGBOPTEAMNV"
```

3. **Run the solver:**

```bash
python solver.py
```

4. **Check the results**  
   - Found words are grouped by length.  
   - Try them all out! (Disclaimer: some words may not be recognized if they aren’t also in squares.org's dictionary.)

## Credits

Squares Solver uses this [word list](https://github.com/dwyl/english-words/blob/master/words.txt).
