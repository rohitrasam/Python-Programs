# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must me an odd number
c = '.'

# Top Cone
for i in range(thickness):
    d = (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
    print(d)

# Top Pillars
for i in range(thickness + 1):
    d = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
    print(d)

# Middle Belt
for i in range((thickness + 1) // 2):
    d = (c * thickness * 5).center(thickness * 6)
    print(d)

# Bottom Pillars
for i in range(thickness + 1):
    d = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
    print(d)

# Bottom Cone
for i in range(thickness):
    d = ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness *
                                                                                                            6)
    print(d)