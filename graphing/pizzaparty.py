#!/usr/bin/env python3
"""TLG Learning | CWilliams
   MatPlot Pizza Party"""

import matplotlib.pyplot as plt

def main():
    """Run-time code"""

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Chicken', 'Cheese', 'Onions', 'Mushrooms'
    sizes = [30, 50, 10, 10]
    explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Clucks')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle

    plt.savefig("/home/student/mycode/pizzaparty.png")
    plt.savefig("/home/student/static/pizzaparty.png")

if __name__ == "__main__":
    main()
