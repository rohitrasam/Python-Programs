def pizza(size, *toppings, **details):
    print(f"Ordered {size} sized pizza with {toppings}")
    print(f"{details}")
pizza("medium", "pepperoni", "jalapenenos", delivery=True, tip=10)