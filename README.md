# Math King Calculator 🧮

A comprehensive scientific calculator with **250+ mathematical functions** built in Python.

## Features

✨ **250+ Mathematical Functions** including:
- Basic arithmetic operations
- Trigonometric functions (sin, cos, tan, etc.)
- Hyperbolic functions
- Logarithmic and exponential functions
- Statistical functions
- Number theory functions
- Complex number operations
- Matrix operations
- Financial calculations
- And many more!

## Installation

```bash
git clone https://github.com/bio-computerinteranthusasum786/math-king-calculator.git
cd math-king-calculator
pip install -r requirements.txt
```

## Usage

### Interactive Calculator

```bash
python calculator.py
```

Then use commands like:
```
> add 5 3
8
> sin 1.5708
1.0
> factorial 5
120
> gcd 48 18
6
```

### Import as Library

```python
from calculator import MathKingCalculator

calc = MathKingCalculator()
result = calc.add(10, 5)
print(result)  # 15

result = calc.sin(3.14159/2)
print(result)  # ~1.0
```

## Function Categories

### 1. Basic Arithmetic (10 functions)
- add, subtract, multiply, divide, modulo, power, floor_divide, absolute, negate, sign

### 2. Trigonometric (24 functions)
- sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh
- degrees, radians, sin_degrees, cos_degrees, tan_degrees
- sec, csc, cot, asec, acsc, acot

### 3. Logarithmic & Exponential (12 functions)
- log, log10, log2, ln, exp, sqrt, cbrt, power, log_base, exp2, exp10

### 4. Number Theory (25 functions)
- factorial, fibonacci, gcd, lcm, is_prime, prime_factors, divisors
- is_perfect_square, is_perfect_cube, next_prime, prev_prime
- sum_of_divisors, euler_totient, mobius, is_palindrome
- digital_root, sum_of_digits, reverse_number, is_armstrong
- perfect_numbers, triangular_number, square_number, pentagonal_number
- catalan_number, bell_number, stirling_number

### 5. Statistical (20 functions)
- mean, median, mode, variance, std_dev, range, percentile, quartiles
- skewness, kurtosis, covariance, correlation, z_score, iqr
- min, max, sum, product, harmonic_mean, geometric_mean
- weighted_mean, cumulative_sum

### 6. Combinatorics (15 functions)
- factorial, combination, permutation, multicombination
- multinomial, derangement, stirling_first, stirling_second
- bell_number, catalan_number, partition, compositions
- set_partitions, necklaces, bracelets

### 7. Complex Numbers (18 functions)
- complex_add, complex_subtract, complex_multiply, complex_divide
- complex_conjugate, complex_magnitude, complex_angle, complex_power
- complex_sqrt, complex_exp, complex_log, complex_sin, complex_cos
- to_polar, to_rectangular, complex_reciprocal, complex_absolute

### 8. Matrix Operations (20 functions)
- matrix_add, matrix_subtract, matrix_multiply, matrix_transpose
- matrix_determinant, matrix_inverse, matrix_trace, matrix_rank
- matrix_eigenvalues, matrix_eigenvectors, matrix_norm, matrix_solve
- matrix_lu_decomposition, matrix_qr_decomposition, identity_matrix
- zero_matrix, ones_matrix, diagonal_matrix, matrix_from_list

### 9. Financial Mathematics (15 functions)
- compound_interest, simple_interest, present_value, future_value
- annuity, loan_payment, amortization, npv, irr, payback_period
- roi, break_even, margin, markup, effective_rate, apr_to_apy

### 10. Calculus (18 functions)
- derivative_numerical, integral_trapezoidal, integral_simpson
- limit_from_left, limit_from_right, taylor_series, taylor_polynomial
- fourier_coefficient, fourier_series, gradient, hessian
- laplacian, divergence, curl, jacobian, partial_derivative

### 11. Geometry (20 functions)
- circle_area, circle_circumference, circle_arc_length
- triangle_area, triangle_perimeter, triangle_height
- rectangle_area, rectangle_perimeter, polygon_area
- sphere_volume, sphere_surface_area, cylinder_volume
- cone_volume, pyramid_volume, cube_volume
- distance_2d, distance_3d, midpoint, angle_between_vectors

### 12. Random & Probability (18 functions)
- random_integer, random_float, random_choice, random_sample
- random_shuffle, binomial_coefficient, probability_poisson
- probability_normal, probability_exponential, probability_uniform
- random_normal, random_exponential, random_poisson, random_binomial
- cdf_normal, pdf_normal, inverse_normal, random_permutation

### 13. Rounding & Precision (12 functions)
- round_nearest, round_up, round_down, truncate, decimal_places
- significant_figures, round_to_nearest_even, round_to_multiple
- round_percentage, scale_number, normalize, denormalize

### 14. Miscellaneous (17 functions)
- gcd, lcm, is_even, is_odd, is_zero, is_positive, is_negative
- sign, clip, lerp, map_range, degrees_to_radians, radians_to_degrees
- bitwise_and, bitwise_or, bitwise_xor, count_bits, hamming_distance

## Requirements

- Python 3.7+
- NumPy
- SciPy

## Documentation

See [FUNCTIONS.md](FUNCTIONS.md) for detailed documentation of all 250+ functions.

## License

MIT License - feel free to use this in your projects!

## Author

Created by [@bio-computerinteranthusasum786](https://github.com/bio-computerinteranthusasum786)
