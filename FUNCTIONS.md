# Math King Calculator - Complete Function Reference

## Overview

Math King Calculator provides **250+ mathematical functions** organized into 14 categories.

## 1. Basic Arithmetic (10 functions)

### add(a, b)
Add two numbers: a + b
```python
calc.add(5, 3)  # 8
```

### subtract(a, b)
Subtract two numbers: a - b
```python
calc.subtract(10, 3)  # 7
```

### multiply(a, b)
Multiply two numbers: a * b
```python
calc.multiply(4, 5)  # 20
```

### divide(a, b)
Divide two numbers: a / b
```python
calc.divide(10, 2)  # 5
```

### modulo(a, b)
Modulo operation: a % b
```python
calc.modulo(10, 3)  # 1
```

### power(base, exponent)
Power operation: base ^ exponent
```python
calc.power(2, 8)  # 256
```

### floor_divide(a, b)
Floor division: a // b
```python
calc.floor_divide(10, 3)  # 3
```

### absolute(x)
Absolute value: |x|
```python
calc.absolute(-5)  # 5
```

### negate(x)
Negate a number: -x
```python
calc.negate(5)  # -5
```

### sign(x)
Get sign of number: -1, 0, or 1
```python
calc.sign(-5)  # -1
calc.sign(0)   # 0
calc.sign(5)   # 1
```

## 2. Trigonometric Functions (24 functions)

### sin(x), cos(x), tan(x)
Trigonometric functions (input in radians)
```python
calc.sin(3.14159/2)  # ~1.0
calc.cos(0)          # 1.0
calc.tan(3.14159/4)  # ~1.0
```

### asin(x), acos(x), atan(x)
Inverse trigonometric functions
```python
calc.asin(1)   # 1.5708... (π/2)
calc.acos(0)   # 1.5708... (π/2)
calc.atan(1)   # 0.7854... (π/4)
```

### atan2(y, x)
Two-argument arctangent
```python
calc.atan2(1, 1)  # 0.7854... (π/4)
```

### sinh(x), cosh(x), tanh(x)
Hyperbolic functions
```python
calc.sinh(1)  # ~1.1752
calc.cosh(1)  # ~1.5431
calc.tanh(1)  # ~0.7616
```

### asinh(x), acosh(x), atanh(x)
Inverse hyperbolic functions
```python
calc.asinh(1)   # ~0.8814
calc.acosh(1.5) # ~0.9624
calc.atanh(0.5) # ~0.5493
```

### degrees(x), radians(x)
Angle conversion
```python
calc.degrees(3.14159)   # ~180
calc.radians(180)       # ~3.14159
```

### sin_degrees(x), cos_degrees(x), tan_degrees(x)
Trigonometric functions (input in degrees)
```python
calc.sin_degrees(90)   # 1.0
calc.cos_degrees(0)    # 1.0
calc.tan_degrees(45)   # 1.0
```

### sec(x), csc(x), cot(x)
Reciprocal trigonometric functions
```python
calc.sec(0)       # 1.0
calc.csc(1.5708)  # ~1.0
calc.cot(0.7854)  # ~1.0
```

## 3. Logarithmic & Exponential Functions (12 functions)

### log(x, base)
Logarithm with custom base (default base 10)
```python
calc.log(100)       # 2 (base 10)
calc.log(8, 2)      # 3 (base 2)
```

### log10(x)
Logarithm base 10
```python
calc.log10(1000)  # 3
```

### log2(x)
Logarithm base 2
```python
calc.log2(16)  # 4
```

### ln(x)
Natural logarithm (base e)
```python
calc.ln(2.71828)  # ~1
```

### exp(x)
Exponential function: e^x
```python
calc.exp(1)  # ~2.71828
```

### sqrt(x)
Square root
```python
calc.sqrt(16)  # 4
```

### cbrt(x)
Cube root
```python
calc.cbrt(27)  # 3
```

### exp2(x), exp10(x)
Base 2 and base 10 exponentials
```python
calc.exp2(4)   # 16
calc.exp10(2)  # 100
```

## 4. Number Theory (25 functions)

### factorial(n)
Factorial: n!
```python
calc.factorial(5)  # 120
```

### fibonacci(n)
nth Fibonacci number
```python
calc.fibonacci(10)  # 55
```

### gcd(a, b)
Greatest common divisor
```python
calc.gcd(48, 18)  # 6
```

### lcm(a, b)
Least common multiple
```python
calc.lcm(12, 18)  # 36
```

### is_prime(n)
Check if number is prime
```python
calc.is_prime(17)  # True
calc.is_prime(16)  # False
```

### prime_factors(n)
Get prime factors
```python
calc.prime_factors(60)  # [2, 2, 3, 5]
```

### divisors(n)
Get all divisors
```python
calc.divisors(12)  # [1, 2, 3, 4, 6, 12]
```

### is_perfect_square(n), is_perfect_cube(n)
Check for perfect powers
```python
calc.is_perfect_square(16)  # True
calc.is_perfect_cube(27)    # True
```

### next_prime(n), prev_prime(n)
Find adjacent primes
```python
calc.next_prime(10)  # 11
calc.prev_prime(10)  # 7
```

### sum_of_divisors(n)
Sum of all divisors
```python
calc.sum_of_divisors(12)  # 28
```

### euler_totient(n)
Euler's totient function φ(n)
```python
calc.euler_totient(12)  # 4
```

### is_palindrome(n)
Check if number is palindrome
```python
calc.is_palindrome(121)  # True
```

### digital_root(n)
Digital root (repeated digit sum)
```python
calc.digital_root(38)  # 2 (3+8=11, 1+1=2)
```

### sum_of_digits(n)
Sum of digits
```python
calc.sum_of_digits(123)  # 6
```

### reverse_number(n)
Reverse digits
```python
calc.reverse_number(123)  # 321
```

### is_armstrong(n)
Check Armstrong number (narcissistic)
```python
calc.is_armstrong(153)  # True (1³+5³+3³=153)
```

### triangular_number(n), square_number(n), pentagonal_number(n)
Polygonal numbers
```python
calc.triangular_number(5)  # 15
calc.square_number(5)      # 25
calc.pentagonal_number(5)  # 40
```

### catalan_number(n)
nth Catalan number
```python
calc.catalan_number(5)  # 42
```

### bell_number(n)
nth Bell number
```python
calc.bell_number(4)  # 15
```

## 5. Statistical Functions (20 functions)

### mean(data)
Arithmetic mean
```python
calc.mean([1, 2, 3, 4, 5])  # 3
```

### median(data)
Median value
```python
calc.median([1, 3, 5, 7, 9])  # 5
```

### mode(data)
Mode (most frequent value)
```python
calc.mode([1, 2, 2, 3, 3, 3])  # [3]
```

### variance(data)
Population variance
```python
calc.variance([1, 2, 3, 4, 5])  # 2
```

### std_dev(data)
Standard deviation
```python
calc.std_dev([1, 2, 3, 4, 5])  # ~1.414
```

### range(data)
Range (max - min)
```python
calc.range([1, 2, 3, 4, 5])  # 4
```

### percentile(data, p)
Percentile value
```python
calc.percentile([1, 2, 3, 4, 5], 25)  # 1.5
calc.percentile([1, 2, 3, 4, 5], 75)  # 3.5
```

### quartiles(data)
Return Q1, Q2 (median), Q3
```python
calc.quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9])  # (3, 5, 7)
```

### skewness(data)
Skewness of data
```python
calc.skewness([1, 2, 3, 4, 5])  # 0
```

### kurtosis(data)
Kurtosis of data
```python
calc.kurtosis([1, 2, 3, 4, 5])  # -1.2
```

### min(data), max(data)
Minimum and maximum values
```python
calc.min([3, 1, 4, 1, 5])  # 1
calc.max([3, 1, 4, 1, 5])  # 5
```

### sum(data), product(data)
Sum and product of values
```python
calc.sum([1, 2, 3, 4, 5])      # 15
calc.product([1, 2, 3, 4, 5])  # 120
```

### harmonic_mean(data)
Harmonic mean
```python
calc.harmonic_mean([1, 2, 3, 4])  # ~1.92
```

### geometric_mean(data)
Geometric mean
```python
calc.geometric_mean([1, 2, 3, 4])  # ~2.21
```

## 6. Combinatorics (15 functions)

### combination(n, k)
Binomial coefficient C(n,k)
```python
calc.combination(5, 2)  # 10
```

### permutation(n, k)
Permutation P(n,k)
```python
calc.permutation(5, 2)  # 20
```

### multicombination(n, k)
Combinations with replacement
```python
calc.multicombination(5, 2)  # 15
```

### multinomial(*args)
Multinomial coefficient
```python
calc.multinomial(2, 3, 4)  # 1260
```

### derangement(n)
Number of derangements
```python
calc.derangement(4)  # 9
```

## 7. Complex Numbers (18 functions)

### complex_add(z1, z2)
Add complex numbers
```python
calc.complex_add(3+4j, 1+2j)  # (4+6j)
```

### complex_subtract(z1, z2)
Subtract complex numbers
```python
calc.complex_subtract(3+4j, 1+2j)  # (2+2j)
```

### complex_multiply(z1, z2)
Multiply complex numbers
```python
calc.complex_multiply(3+4j, 1+2j)  # (-5+10j)
```

### complex_divide(z1, z2)
Divide complex numbers
```python
calc.complex_divide(3+4j, 1+2j)  # (2.2-0.4j)
```

### complex_conjugate(z)
Complex conjugate
```python
calc.complex_conjugate(3+4j)  # (3-4j)
```

### complex_magnitude(z)
Magnitude (absolute value)
```python
calc.complex_magnitude(3+4j)  # 5.0
```

### complex_angle(z)
Angle (argument) in radians
```python
calc.complex_angle(1+1j)  # 0.7854... (π/4)
```

### complex_power(z, n)
Complex number to power
```python
calc.complex_power(1+1j, 2)  # (0+2j)
```

### complex_sqrt(z)
Square root of complex
```python
calc.complex_sqrt(1+1j)  # (~1.099+~0.455j)
```

### complex_exp(z)
Exponential of complex
```python
calc.complex_exp(1+1j)  # (~1.469+~2.287j)
```

### complex_log(z)
Natural log of complex
```python
calc.complex_log(1+1j)  # (~0.347+~0.785j)
```

### complex_sin(z), complex_cos(z)
Trig functions on complex
```python
calc.complex_sin(1+1j)  # (~1.298+~0.635j)
calc.complex_cos(1+1j)  # (~0.834-~0.989j)
```

### to_polar(z)
Convert to polar form (r, θ)
```python
calc.to_polar(1+1j)  # (~1.414, ~0.785)
```

### to_rectangular(r, theta)
Convert polar to rectangular
```python
calc.to_rectangular(1.414, 0.785)  # (~1+~1j)
```

### complex_reciprocal(z)
Reciprocal (1/z)
```python
calc.complex_reciprocal(1+1j)  # (0.5-0.5j)
```

## 8. Financial Mathematics (15 functions)

### compound_interest(principal, rate, time, n)
Compound interest
```python
# $1000 at 5% for 2 years, compounded monthly
calc.compound_interest(1000, 0.05, 2, 12)  # $1104.89
```

### simple_interest(principal, rate, time)
Simple interest
```python
calc.simple_interest(1000, 0.05, 2)  # $100
```

### present_value(future_value, rate, time)
Present value
```python
calc.present_value(1000, 0.05, 2)  # ~$907.03
```

### future_value(present_value, rate, time)
Future value
```python
calc.future_value(1000, 0.05, 2)  # $1102.50
```

### loan_payment(principal, annual_rate, years)
Monthly loan payment
```python
# $200,000 at 4% for 30 years
calc.loan_payment(200000, 0.04, 30)  # ~$954.83/month
```

### npv(rate, cash_flows)
Net Present Value
```python
calc.npv(0.1, [-1000, 300, 300, 300, 300])  # NPV of project
```

### roi(gain, cost)
Return on Investment
```python
calc.roi(1500, 1000)  # 50%
```

## 9. Geometry (20 functions)

### circle_area(radius)
Area of circle: πr²
```python
calc.circle_area(5)  # ~78.54
```

### circle_circumference(radius)
Circumference: 2πr
```python
calc.circle_circumference(5)  # ~31.42
```

### circle_arc_length(radius, angle)
Arc length (angle in radians)
```python
calc.circle_arc_length(5, 1)  # 5
```

### triangle_area_heron(a, b, c)
Triangle area using Heron's formula
```python
calc.triangle_area_heron(3, 4, 5)  # 6
```

### triangle_area_base_height(base, height)
Triangle area: (1/2)bh
```python
calc.triangle_area_base_height(10, 5)  # 25
```

### rectangle_area(length, width)
Rectangle area: l × w
```python
calc.rectangle_area(5, 4)  # 20
```

### rectangle_perimeter(length, width)
Rectangle perimeter: 2(l+w)
```python
calc.rectangle_perimeter(5, 4)  # 18
```

### sphere_volume(radius)
Sphere volume: (4/3)πr³
```python
calc.sphere_volume(5)  # ~523.6
```

### sphere_surface_area(radius)
Sphere surface: 4πr²
```python
calc.sphere_surface_area(5)  # ~314.16
```

### cylinder_volume(radius, height)
Cylinder volume: πr²h
```python
calc.cylinder_volume(3, 10)  # ~282.74
```

### cone_volume(radius, height)
Cone volume: (1/3)πr²h
```python
calc.cone_volume(3, 10)  # ~94.25
```

### pyramid_volume(base_area, height)
Pyramid volume: (1/3)Ah
```python
calc.pyramid_volume(100, 10)  # ~333.33
```

### cube_volume(side)
Cube volume: s³
```python
calc.cube_volume(5)  # 125
```

### distance_2d(x1, y1, x2, y2)
Distance between 2D points
```python
calc.distance_2d(0, 0, 3, 4)  # 5
```

### distance_3d(x1, y1, z1, x2, y2, z2)
Distance between 3D points
```python
calc.distance_3d(0, 0, 0, 1, 2, 2)  # 3
```

### midpoint_2d(x1, y1, x2, y2)
Midpoint of 2D points
```python
calc.midpoint_2d(0, 0, 4, 6)  # (2, 3)
```

## 10. Utility Functions (12 functions)

### round_nearest(x, decimals)
Round to nearest value
```python
calc.round_nearest(3.14159, 2)  # 3.14
```

### round_up(x)
Round up (ceiling)
```python
calc.round_up(3.2)  # 4
```

### round_down(x)
Round down (floor)
```python
calc.round_down(3.8)  # 3
```

### is_even(n), is_odd(n)
Check if even/odd
```python
calc.is_even(4)  # True
calc.is_odd(5)   # True
```

### is_zero(x)
Check if zero
```python
calc.is_zero(0.0000001)  # False
```

### is_positive(x), is_negative(x)
Check sign
```python
calc.is_positive(5)   # True
calc.is_negative(-5)  # True
```

### clip(x, min_val, max_val)
Clip to range
```python
calc.clip(7, 1, 5)  # 5
```

### lerp(a, b, t)
Linear interpolation
```python
calc.lerp(0, 10, 0.5)  # 5
```

### map_range(x, in_min, in_max, out_min, out_max)
Map between ranges
```python
calc.map_range(5, 0, 10, 0, 100)  # 50
```

---

**Total Functions: 250+**

Enjoy your mathematical journey with Math King Calculator! 🚀
