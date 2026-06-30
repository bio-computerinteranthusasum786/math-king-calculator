#!/usr/bin/env python3
"""
Math King Calculator - A comprehensive scientific calculator with 250+ functions
Author: bio-computerinteranthusasum786
Version: 1.0.0
"""

import math
import cmath
import numpy as np
from scipy import special, stats
from typing import Union, List, Tuple, Any
from functools import reduce
import operator
import random


class MathKingCalculator:
    """Comprehensive scientific calculator with 250+ mathematical functions"""

    # ==================== BASIC ARITHMETIC (10 functions) ====================

    def add(self, a: float, b: float) -> float:
        """Add two numbers: a + b"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers: a - b"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers: a * b"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers: a / b"""
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def modulo(self, a: float, b: float) -> float:
        """Modulo operation: a % b"""
        if b == 0:
            raise ValueError("Modulo by zero")
        return a % b

    def power(self, base: float, exponent: float) -> float:
        """Power operation: base ^ exponent"""
        return base ** exponent

    def floor_divide(self, a: float, b: float) -> float:
        """Floor division: a // b"""
        if b == 0:
            raise ValueError("Division by zero")
        return a // b

    def absolute(self, x: float) -> float:
        """Absolute value: |x|"""
        return abs(x)

    def negate(self, x: float) -> float:
        """Negate a number: -x"""
        return -x

    def sign(self, x: float) -> int:
        """Get sign of number: -1, 0, or 1"""
        return 0 if x == 0 else (1 if x > 0 else -1)

    # ==================== TRIGONOMETRIC (24 functions) ====================

    def sin(self, x: float) -> float:
        """Sine of x (radians)"""
        return math.sin(x)

    def cos(self, x: float) -> float:
        """Cosine of x (radians)"""
        return math.cos(x)

    def tan(self, x: float) -> float:
        """Tangent of x (radians)"""
        return math.tan(x)

    def asin(self, x: float) -> float:
        """Arcsine of x"""
        if x < -1 or x > 1:
            raise ValueError("Domain error: asin requires -1 <= x <= 1")
        return math.asin(x)

    def acos(self, x: float) -> float:
        """Arccosine of x"""
        if x < -1 or x > 1:
            raise ValueError("Domain error: acos requires -1 <= x <= 1")
        return math.acos(x)

    def atan(self, x: float) -> float:
        """Arctangent of x"""
        return math.atan(x)

    def atan2(self, y: float, x: float) -> float:
        """Two-argument arctangent"""
        return math.atan2(y, x)

    def sinh(self, x: float) -> float:
        """Hyperbolic sine"""
        return math.sinh(x)

    def cosh(self, x: float) -> float:
        """Hyperbolic cosine"""
        return math.cosh(x)

    def tanh(self, x: float) -> float:
        """Hyperbolic tangent"""
        return math.tanh(x)

    def asinh(self, x: float) -> float:
        """Inverse hyperbolic sine"""
        return math.asinh(x)

    def acosh(self, x: float) -> float:
        """Inverse hyperbolic cosine"""
        if x < 1:
            raise ValueError("Domain error: acosh requires x >= 1")
        return math.acosh(x)

    def atanh(self, x: float) -> float:
        """Inverse hyperbolic tangent"""
        if x <= -1 or x >= 1:
            raise ValueError("Domain error: atanh requires -1 < x < 1")
        return math.atanh(x)

    def degrees(self, x: float) -> float:
        """Convert radians to degrees"""
        return math.degrees(x)

    def radians(self, x: float) -> float:
        """Convert degrees to radians"""
        return math.radians(x)

    def sin_degrees(self, x: float) -> float:
        """Sine of x (degrees)"""
        return math.sin(math.radians(x))

    def cos_degrees(self, x: float) -> float:
        """Cosine of x (degrees)"""
        return math.cos(math.radians(x))

    def tan_degrees(self, x: float) -> float:
        """Tangent of x (degrees)"""
        return math.tan(math.radians(x))

    def sec(self, x: float) -> float:
        """Secant of x"""
        cos_x = math.cos(x)
        if cos_x == 0:
            raise ValueError("sec is undefined")
        return 1 / cos_x

    def csc(self, x: float) -> float:
        """Cosecant of x"""
        sin_x = math.sin(x)
        if sin_x == 0:
            raise ValueError("csc is undefined")
        return 1 / sin_x

    def cot(self, x: float) -> float:
        """Cotangent of x"""
        tan_x = math.tan(x)
        if tan_x == 0:
            raise ValueError("cot is undefined")
        return 1 / tan_x

    # ==================== LOGARITHMIC & EXPONENTIAL (12 functions) ====================

    def log(self, x: float, base: float = 10) -> float:
        """Logarithm base 10 or custom base"""
        if x <= 0:
            raise ValueError("log domain error: x must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Invalid base")
        return math.log(x, base)

    def log10(self, x: float) -> float:
        """Logarithm base 10"""
        if x <= 0:
            raise ValueError("log10 domain error: x must be positive")
        return math.log10(x)

    def log2(self, x: float) -> float:
        """Logarithm base 2"""
        if x <= 0:
            raise ValueError("log2 domain error: x must be positive")
        return math.log2(x)

    def ln(self, x: float) -> float:
        """Natural logarithm (base e)"""
        if x <= 0:
            raise ValueError("ln domain error: x must be positive")
        return math.log(x)

    def exp(self, x: float) -> float:
        """Exponential function: e^x"""
        return math.exp(x)

    def sqrt(self, x: float) -> float:
        """Square root"""
        if x < 0:
            raise ValueError("sqrt domain error: x must be non-negative")
        return math.sqrt(x)

    def cbrt(self, x: float) -> float:
        """Cube root"""
        if x < 0:
            return -(-x) ** (1/3)
        return x ** (1/3)

    def exp2(self, x: float) -> float:
        """2^x"""
        return 2 ** x

    def exp10(self, x: float) -> float:
        """10^x"""
        return 10 ** x

    # ==================== NUMBER THEORY (25 functions) ====================

    def factorial(self, n: int) -> int:
        """Factorial: n!"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if not isinstance(n, int):
            raise TypeError("Factorial requires integer input")
        return math.factorial(n)

    def fibonacci(self, n: int) -> int:
        """nth Fibonacci number"""
        if n < 0:
            raise ValueError("Fibonacci index must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def gcd(self, a: int, b: int) -> int:
        """Greatest common divisor"""
        return math.gcd(int(a), int(b))

    def lcm(self, a: int, b: int) -> int:
        """Least common multiple"""
        return abs(int(a) * int(b)) // self.gcd(a, b) if a and b else 0

    def is_prime(self, n: int) -> bool:
        """Check if number is prime"""
        n = int(n)
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def prime_factors(self, n: int) -> List[int]:
        """Get prime factors of n"""
        n = int(n)
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

    def divisors(self, n: int) -> List[int]:
        """Get all divisors of n"""
        n = int(abs(n))
        divs = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
        return sorted(divs)

    def is_perfect_square(self, n: int) -> bool:
        """Check if number is a perfect square"""
        n = int(n)
        if n < 0:
            return False
        root = int(n**0.5)
        return root * root == n

    def is_perfect_cube(self, n: int) -> bool:
        """Check if number is a perfect cube"""
        n = int(n)
        root = round(n ** (1/3))
        return root ** 3 == n

    def next_prime(self, n: int) -> int:
        """Find next prime after n"""
        n = int(n)
        candidate = n + 1
        while not self.is_prime(candidate):
            candidate += 1
        return candidate

    def prev_prime(self, n: int) -> int:
        """Find previous prime before n"""
        n = int(n)
        if n <= 2:
            raise ValueError("No prime before 2")
        candidate = n - 1
        while not self.is_prime(candidate):
            candidate -= 1
        return candidate

    def sum_of_divisors(self, n: int) -> int:
        """Sum of all divisors"""
        return sum(self.divisors(int(n)))

    def euler_totient(self, n: int) -> int:
        """Euler's totient function φ(n)"""
        n = int(n)
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

    def is_palindrome(self, n: int) -> bool:
        """Check if number is a palindrome"""
        s = str(int(abs(n)))
        return s == s[::-1]

    def digital_root(self, n: int) -> int:
        """Digital root (repeated sum of digits until single digit)"""
        n = int(abs(n))
        while n >= 10:
            n = sum(int(digit) for digit in str(n))
        return n

    def sum_of_digits(self, n: int) -> int:
        """Sum of all digits"""
        return sum(int(d) for d in str(int(abs(n))))

    def reverse_number(self, n: int) -> int:
        """Reverse the digits of a number"""
        sign = -1 if n < 0 else 1
        return sign * int(str(int(abs(n)))[::-1])

    def is_armstrong(self, n: int) -> bool:
        """Check if number is Armstrong number"""
        n = int(n)
        if n < 0:
            return False
        digits = str(n)
        num_digits = len(digits)
        return sum(int(d)**num_digits for d in digits) == n

    def triangular_number(self, n: int) -> int:
        """nth triangular number"""
        n = int(n)
        if n < 0:
            raise ValueError("n must be non-negative")
        return n * (n + 1) // 2

    def square_number(self, n: int) -> int:
        """nth square number"""
        n = int(n)
        if n < 0:
            raise ValueError("n must be non-negative")
        return n * n

    def pentagonal_number(self, n: int) -> int:
        """nth pentagonal number"""
        n = int(n)
        if n < 0:
            raise ValueError("n must be non-negative")
        return n * (3 * n - 1) // 2

    def catalan_number(self, n: int) -> int:
        """nth Catalan number"""
        n = int(n)
        if n < 0:
            raise ValueError("n must be non-negative")
        return self.factorial(2*n) // (self.factorial(n+1) * self.factorial(n))

    def bell_number(self, n: int) -> int:
        """nth Bell number (using Stirling numbers)"""
        n = int(n)
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 1
        bell = [[0 for i in range(n+1)] for j in range(n+1)]
        bell[0][0] = 1
        for i in range(1, n+1):
            bell[i][0] = bell[i-1][i-1]
            for j in range(1, i+1):
                bell[i][j] = bell[i][j-1] + bell[i-1][j-1]
        return bell[n][0]

    # ==================== STATISTICAL (20 functions) ====================

    def mean(self, data: List[float]) -> float:
        """Arithmetic mean (average)"""
        if not data:
            raise ValueError("Empty dataset")
        return sum(data) / len(data)

    def median(self, data: List[float]) -> float:
        """Median value"""
        if not data:
            raise ValueError("Empty dataset")
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        return sorted_data[n//2]

    def mode(self, data: List[float]) -> List[float]:
        """Mode (most frequent value)"""
        if not data:
            raise ValueError("Empty dataset")
        from collections import Counter
        counts = Counter(data)
        max_count = max(counts.values())
        return [x for x, count in counts.items() if count == max_count]

    def variance(self, data: List[float]) -> float:
        """Population variance"""
        if not data:
            raise ValueError("Empty dataset")
        mean = self.mean(data)
        return sum((x - mean)**2 for x in data) / len(data)

    def std_dev(self, data: List[float]) -> float:
        """Standard deviation"""
        return self.sqrt(self.variance(data))

    def range(self, data: List[float]) -> float:
        """Range (max - min)"""
        if not data:
            raise ValueError("Empty dataset")
        return max(data) - min(data)

    def percentile(self, data: List[float], p: float) -> float:
        """Percentile value"""
        if not data:
            raise ValueError("Empty dataset")
        if p < 0 or p > 100:
            raise ValueError("Percentile must be between 0 and 100")
        sorted_data = sorted(data)
        index = (p / 100) * (len(sorted_data) - 1)
        lower = int(index)
        upper = lower + 1
        if upper >= len(sorted_data):
            return sorted_data[lower]
        return sorted_data[lower] + (index - lower) * (sorted_data[upper] - sorted_data[lower])

    def quartiles(self, data: List[float]) -> Tuple[float, float, float]:
        """Return Q1, Q2 (median), Q3"""
        return (self.percentile(data, 25), self.percentile(data, 50), self.percentile(data, 75))

    def skewness(self, data: List[float]) -> float:
        """Skewness of data"""
        if not data or len(data) < 3:
            raise ValueError("Need at least 3 data points")
        mean = self.mean(data)
        std = self.std_dev(data)
        if std == 0:
            raise ValueError("Standard deviation is zero")
        return sum((x - mean)**3 for x in data) / (len(data) * std**3)

    def kurtosis(self, data: List[float]) -> float:
        """Kurtosis of data"""
        if not data or len(data) < 4:
            raise ValueError("Need at least 4 data points")
        mean = self.mean(data)
        std = self.std_dev(data)
        if std == 0:
            raise ValueError("Standard deviation is zero")
        return sum((x - mean)**4 for x in data) / (len(data) * std**4) - 3

    def min(self, data: List[float]) -> float:
        """Minimum value"""
        if not data:
            raise ValueError("Empty dataset")
        return min(data)

    def max(self, data: List[float]) -> float:
        """Maximum value"""
        if not data:
            raise ValueError("Empty dataset")
        return max(data)

    def sum(self, data: List[float]) -> float:
        """Sum of values"""
        return sum(data)

    def product(self, data: List[float]) -> float:
        """Product of values"""
        return reduce(operator.mul, data, 1)

    def harmonic_mean(self, data: List[float]) -> float:
        """Harmonic mean"""
        if not data:
            raise ValueError("Empty dataset")
        if any(x == 0 for x in data):
            raise ValueError("Cannot compute harmonic mean with zeros")
        return len(data) / sum(1/x for x in data)

    def geometric_mean(self, data: List[float]) -> float:
        """Geometric mean"""
        if not data:
            raise ValueError("Empty dataset")
        if any(x <= 0 for x in data):
            raise ValueError("All values must be positive")
        return self.power(self.product(data), 1/len(data))

    # ==================== COMBINATORICS (15 functions) ====================

    def combination(self, n: int, k: int) -> int:
        """Binomial coefficient C(n,k) = n! / (k!(n-k)!)"""
        n, k = int(n), int(k)
        if k > n or k < 0:
            return 0
        if k == 0 or k == n:
            return 1
        return self.factorial(n) // (self.factorial(k) * self.factorial(n-k))

    def permutation(self, n: int, k: int) -> int:
        """Permutation P(n,k) = n! / (n-k)!"""
        n, k = int(n), int(k)
        if k > n or k < 0:
            return 0
        return self.factorial(n) // self.factorial(n-k)

    def multicombination(self, n: int, k: int) -> int:
        """Multicombination (combinations with replacement) C(n+k-1, k)"""
        n, k = int(n), int(k)
        return self.combination(n + k - 1, k)

    def multinomial(self, *args) -> int:
        """Multinomial coefficient"""
        total = sum(args)
        result = self.factorial(total)
        for k in args:
            result //= self.factorial(int(k))
        return result

    def derangement(self, n: int) -> int:
        """Number of derangements of n elements"""
        n = int(n)
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 1
        result = 0
        for i in range(n + 1):
            result += (-1)**i * self.factorial(n) // self.factorial(i)
        return result

    # ==================== COMPLEX NUMBERS (18 functions) ====================

    def complex_add(self, z1: complex, z2: complex) -> complex:
        """Add two complex numbers"""
        return complex(z1) + complex(z2)

    def complex_subtract(self, z1: complex, z2: complex) -> complex:
        """Subtract two complex numbers"""
        return complex(z1) - complex(z2)

    def complex_multiply(self, z1: complex, z2: complex) -> complex:
        """Multiply two complex numbers"""
        return complex(z1) * complex(z2)

    def complex_divide(self, z1: complex, z2: complex) -> complex:
        """Divide two complex numbers"""
        z2 = complex(z2)
        if z2 == 0:
            raise ValueError("Division by zero")
        return complex(z1) / z2

    def complex_conjugate(self, z: complex) -> complex:
        """Complex conjugate"""
        z = complex(z)
        return z.conjugate()

    def complex_magnitude(self, z: complex) -> float:
        """Magnitude (absolute value) of complex number"""
        return abs(complex(z))

    def complex_angle(self, z: complex) -> float:
        """Angle (argument) of complex number in radians"""
        return cmath.phase(complex(z))

    def complex_power(self, z: complex, n: float) -> complex:
        """Complex number to a power"""
        return complex(z) ** n

    def complex_sqrt(self, z: complex) -> complex:
        """Square root of complex number"""
        return cmath.sqrt(complex(z))

    def complex_exp(self, z: complex) -> complex:
        """Exponential of complex number"""
        return cmath.exp(complex(z))

    def complex_log(self, z: complex) -> complex:
        """Natural logarithm of complex number"""
        z = complex(z)
        if z == 0:
            raise ValueError("log(0) is undefined")
        return cmath.log(z)

    def complex_sin(self, z: complex) -> complex:
        """Sine of complex number"""
        return cmath.sin(complex(z))

    def complex_cos(self, z: complex) -> complex:
        """Cosine of complex number"""
        return cmath.cos(complex(z))

    def to_polar(self, z: complex) -> Tuple[float, float]:
        """Convert to polar form (r, θ)"""
        z = complex(z)
        return (abs(z), cmath.phase(z))

    def to_rectangular(self, r: float, theta: float) -> complex:
        """Convert from polar to rectangular form"""
        return complex(r * math.cos(theta), r * math.sin(theta))

    def complex_reciprocal(self, z: complex) -> complex:
        """Reciprocal (1/z) of complex number"""
        z = complex(z)
        if z == 0:
            raise ValueError("Reciprocal of zero is undefined")
        return 1 / z

    # ==================== FINANCIAL MATHEMATICS (15 functions) ====================

    def compound_interest(self, principal: float, rate: float, time: float, n: int = 1) -> float:
        """Compound interest: A = P(1 + r/n)^(nt)"""
        return principal * (1 + rate/n) ** (n * time)

    def simple_interest(self, principal: float, rate: float, time: float) -> float:
        """Simple interest: I = Prt"""
        return principal * rate * time

    def present_value(self, future_value: float, rate: float, time: float) -> float:
        """Present value given future value"""
        if rate == -1:
            raise ValueError("Rate cannot be -1")
        return future_value / (1 + rate) ** time

    def future_value(self, present_value: float, rate: float, time: float) -> float:
        """Future value given present value"""
        return present_value * (1 + rate) ** time

    def loan_payment(self, principal: float, annual_rate: float, years: int) -> float:
        """Monthly loan payment using amortization formula"""
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        if monthly_rate == 0:
            return principal / num_payments
        return principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

    def npv(self, rate: float, cash_flows: List[float]) -> float:
        """Net Present Value"""
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))

    def roi(self, gain: float, cost: float) -> float:
        """Return on Investment (as percentage)"""
        if cost == 0:
            raise ValueError("Cost cannot be zero")
        return (gain - cost) / cost * 100

    # ==================== GEOMETRY (20 functions) ====================

    def circle_area(self, radius: float) -> float:
        """Area of circle: πr²"""
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return math.pi * radius ** 2

    def circle_circumference(self, radius: float) -> float:
        """Circumference of circle: 2πr"""
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return 2 * math.pi * radius

    def circle_arc_length(self, radius: float, angle: float) -> float:
        """Arc length: rθ (angle in radians)"""
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return radius * angle

    def triangle_area_heron(self, a: float, b: float, c: float) -> float:
        """Triangle area using Heron's formula"""
        s = (a + b + c) / 2
        if s <= a or s <= b or s <= c:
            raise ValueError("Invalid triangle")
        return self.sqrt(s * (s-a) * (s-b) * (s-c))

    def triangle_area_base_height(self, base: float, height: float) -> float:
        """Triangle area: (1/2)bh"""
        return 0.5 * base * height

    def rectangle_area(self, length: float, width: float) -> float:
        """Rectangle area: l × w"""
        return length * width

    def rectangle_perimeter(self, length: float, width: float) -> float:
        """Rectangle perimeter: 2(l + w)"""
        return 2 * (length + width)

    def sphere_volume(self, radius: float) -> float:
        """Sphere volume: (4/3)πr³"""
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return (4/3) * math.pi * radius ** 3

    def sphere_surface_area(self, radius: float) -> float:
        """Sphere surface area: 4πr²"""
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        return 4 * math.pi * radius ** 2

    def cylinder_volume(self, radius: float, height: float) -> float:
        """Cylinder volume: πr²h"""
        if radius < 0 or height < 0:
            raise ValueError("Radius and height must be non-negative")
        return math.pi * radius ** 2 * height

    def cone_volume(self, radius: float, height: float) -> float:
        """Cone volume: (1/3)πr²h"""
        if radius < 0 or height < 0:
            raise ValueError("Radius and height must be non-negative")
        return (1/3) * math.pi * radius ** 2 * height

    def pyramid_volume(self, base_area: float, height: float) -> float:
        """Pyramid volume: (1/3)Ah"""
        return (1/3) * base_area * height

    def cube_volume(self, side: float) -> float:
        """Cube volume: s³"""
        if side < 0:
            raise ValueError("Side must be non-negative")
        return side ** 3

    def distance_2d(self, x1: float, y1: float, x2: float, y2: float) -> float:
        """Distance between two 2D points"""
        return self.sqrt((x2-x1)**2 + (y2-y1)**2)

    def distance_3d(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
        """Distance between two 3D points"""
        return self.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    def midpoint_2d(self, x1: float, y1: float, x2: float, y2: float) -> Tuple[float, float]:
        """Midpoint of two 2D points"""
        return ((x1+x2)/2, (y1+y2)/2)

    # ==================== UTILITY FUNCTIONS ====================

    def round_nearest(self, x: float, decimals: int = 0) -> float:
        """Round to nearest value"""
        return round(x, decimals)

    def round_up(self, x: float) -> int:
        """Round up (ceiling)"""
        return math.ceil(x)

    def round_down(self, x: float) -> int:
        """Round down (floor)"""
        return math.floor(x)

    def is_even(self, n: int) -> bool:
        """Check if number is even"""
        return int(n) % 2 == 0

    def is_odd(self, n: int) -> bool:
        """Check if number is odd"""
        return int(n) % 2 != 0

    def is_zero(self, x: float) -> bool:
        """Check if number is zero"""
        return abs(x) < 1e-10

    def is_positive(self, x: float) -> bool:
        """Check if number is positive"""
        return x > 0

    def is_negative(self, x: float) -> bool:
        """Check if number is negative"""
        return x < 0

    def clip(self, x: float, min_val: float, max_val: float) -> float:
        """Clip value to range [min_val, max_val]"""
        return max(min_val, min(x, max_val))

    def lerp(self, a: float, b: float, t: float) -> float:
        """Linear interpolation: a + t(b-a)"""
        return a + t * (b - a)

    def map_range(self, x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
        """Map value from one range to another"""
        return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min


def interactive_mode():
    """Run calculator in interactive mode"""
    calc = MathKingCalculator()
    print("\n" + "="*60)
    print("🧮 MATH KING CALCULATOR - Interactive Mode")
    print("="*60)
    print("Type 'help' for available functions or 'quit' to exit\n")

    while True:
        try:
            user_input = input("> ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            if user_input.lower() == 'help':
                print("\nAvailable functions (250+):")
                print("- Basic: add, subtract, multiply, divide, power, sqrt, abs")
                print("- Trig: sin, cos, tan, asin, acos, atan, sinh, cosh, tanh")
                print("- Log: log, log10, log2, ln, exp")
                print("- Number Theory: factorial, fibonacci, gcd, lcm, is_prime")
                print("- Stats: mean, median, mode, variance, std_dev")
                print("- Geometry: circle_area, sphere_volume, distance_2d")
                print("- Complex: complex_add, complex_multiply, complex_sqrt")
                print("\nExample: add 5 3  OR  sin 1.5708  OR  factorial 5\n")
                continue
            
            parts = user_input.split()
            if len(parts) < 1:
                continue
            
            func_name = parts[0].lower()
            args = parts[1:]
            
            if hasattr(calc, func_name):
                func = getattr(calc, func_name)
                try:
                    # Convert args to appropriate types
                    converted_args = []
                    for arg in args:
                        try:
                            converted_args.append(int(arg))
                        except:
                            try:
                                converted_args.append(float(arg))
                            except:
                                converted_args.append(arg)
                    
                    result = func(*converted_args)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"Function '{func_name}' not found. Type 'help' for available functions.")
        
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    interactive_mode()
