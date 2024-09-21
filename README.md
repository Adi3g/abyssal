# Abyssal

**Abyssal** is a Python library that parses LaTeX mathematical expressions and computes advanced mathematical operations such as limits, integrals, logarithmic functions, and more. Built to handle a wide range of mathematical expressions, Abyssal dives deep into the complexity of symbolic math, making it easy to perform both symbolic and numerical calculations.

## Features

- Parse LaTeX mathematical expressions.
- Compute:
  - Limits (e.g., \(\lim_{x \to 0} \frac{\sin{x}}{x}\))
  - Definite integrals (e.g., \(\int_{0}^{1} e^x \, dx\))
  - Logarithmic and trigonometric functions (e.g., \(\ln{x}\), \(\sin{x}\), \(\cos{x}\))
  - Complex expressions with nested functions and multiple operations.
- Built on top of powerful libraries like **SymPy** and **SciPy** for symbolic and numerical computation.

## Installation

You can install **Abyssal** using `pip`:

```bash
pip install abyssal
```

Alternatively, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/abyssal.git
cd abyssal
pip install -r requirements.txt
```

## Usage

### Basic Example: Calculating a Limit

Here’s an example of how to use **Abyssal** to calculate a limit.

**LaTeX Expression**:
\[
\lim_{x \to 0} \frac{\sin{x}}{x}
\]

```python
from abyssal.engine import MathEngine

# Create an instance of the MathEngine
engine = MathEngine()

# Define a LaTeX expression for calculating a limit
latex_expression = "\\lim_{x \\to 0} \\frac{\\sin{x}}{x}"

# No parameters needed for this calculation
params = {}

# Evaluate the LaTeX expression
result = engine.evaluate(latex_expression, params)

# Output the result
print(f"The result of '{latex_expression}' is: {result}")
```

**Expected Output**:
```
The result of '\lim_{x \to 0} \frac{\sin{x}}{x}' is: 1.0
```

---

### Example: Calculating a Definite Integral

**LaTeX Expression**:
\[
\int_{0}^{1} e^x \, dx
\]

```python
from abyssal.engine import MathEngine

# Create an instance of the MathEngine
engine = MathEngine()

# Define a LaTeX expression for a definite integral
latex_expression = "\\int_{0}^{1} e^x \, dx"

# No parameters are needed for this integral
params = {}

# Evaluate the LaTeX expression
result = engine.evaluate(latex_expression, params)

# Output the result
print(f"The result of '{latex_expression}' is: {result}")
```

**Expected Output**:
```
The result of '\int_{0}^{1} e^x \, dx' is: 1.718281828459045
```

---

### Example: Logarithmic and Trigonometric Functions

**LaTeX Expression**:
\[
\ln{(e^x \cdot \sin{x})} + \cos{\left( \frac{\pi}{4} \right)}
\]

```python
from abyssal.engine import MathEngine

# Create an instance of the MathEngine
engine = MathEngine()

# Define a LaTeX expression with logarithmic and trigonometric functions
latex_expression = "\\ln{(e^x \cdot \\sin{x})} + \\cos{\\left(\\frac{\\pi}{4}\\right)}"

# Provide a parameter for x
params = {'x': 1}

# Evaluate the LaTeX expression
result = engine.evaluate(latex_expression, params)

# Output the result
print(f"The result of '{latex_expression}' with x=1 is: {result}")
```

**Expected Output**:
```
The result of '\ln{(e^x \cdot \sin{x})} + \cos{\left( \frac{\pi}{4} \right)}' with x=1 is: 1.7871289893776849
```

---

### Example: Complex Nested Function with Trigonometric and Power Functions

**LaTeX Expression**:
\[
\sqrt{x^2 + y^2}
\]

```python
from abyssal.engine import MathEngine

# Create an instance of the MathEngine
engine = MathEngine()

# Define a LaTeX expression for calculating the square root of a sum of squares
latex_expression = "\\sqrt{x^2 + y^2}"

# Provide parameters for x and y
params = {'x': 3, 'y': 4}

# Evaluate the LaTeX expression
result = engine.evaluate(latex_expression, params)

# Output the result
print(f"The result of '{latex_expression}' with x=3 and y=4 is: {result}")
```

**Expected Output**:
```
The result of '\sqrt{x^2 + y^2}' with x=3 and y=4 is: 5.0
```

---

## How It Works

- **Parsing LaTeX:** Abyssal converts LaTeX mathematical expressions into an abstract syntax tree (AST) that it can process.
- **Symbolic and Numerical Computation:** Abyssal uses **SymPy** for symbolic math (e.g., calculating limits) and **SciPy** for numerical methods (e.g., definite integrals).

### Supported Operations:
- **Limits**: `\lim_{x \to a} f(x)`
- **Integrals**: `\int_{a}^{b} f(x) \, dx`
- **Logarithmic and Exponential Functions**: `\ln{x}`, `e^x`
- **Trigonometric Functions**: `\sin{x}`, `\cos{x}`, `\tan{x}`
- **Basic Arithmetic**: Addition, subtraction, multiplication, division, and powers.

## Requirements

- **Python 3.6+**
- **SymPy**
- **SciPy**

All dependencies can be installed via the provided `requirements.txt` file.

## Contributing

We welcome contributions! Here’s how you can contribute to **Abyssal**:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and add tests for the new feature or bug fix.
4. Push to your branch: `git push origin feature-branch`.
5. Submit a pull request.

### Running Tests

To run the test suite, use:

```bash
pytest
```

Make sure all tests pass before submitting a pull request.

## License

**Abyssal** is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
