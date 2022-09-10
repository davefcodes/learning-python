# Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):  # the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")

make_pizza('16', 'pepperoni')
make_pizza('12', 'mushrooms', 'green peppers', 'extra cheese')