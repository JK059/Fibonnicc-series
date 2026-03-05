def fibonacci_series(n):
    # Initializing the first two terms
    a, b = 0, 1
    series = []
    
    # Generate the series up to n terms
    for _ in range(n):
        series.append(a)
        # Update values: a becomes b, and b becomes the sum of both
        a, b = b, a + b
    return series

# Example: Get the first 10 terms
num_terms = 10
print(f"Fibonacci Series ({num_terms} terms):", fibonacci_series(num_terms))
