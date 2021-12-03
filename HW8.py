import matplotlib.pyplot as plt
import sqlite3
import unittest
import os

# Your name:
# The name(s) of anyone you worked with:


##############################################################################
# [Part 1]
##############################################################################
# Complete the get_restaurant_dict(..) function that accepts the filename of the database 
# as a parameter, and returns a dictionary with the number of restaurants with a price of 2 (“$$”) for each category. 
# The keys should be the category names and the values should be the number of restaurants with a price level of 2. 
# The dictionary should look like:
# Expected output
# 
# {'Farmers Market': 1, 'Salad': 2, 'Bakeries': 1, 'Pubs': 2, 'Delis': 2, 'Pizza': 8, 'Sandwiches': 1, 'Beer, Wine & Spirits': 2, 'Breweries': 1, 'Sports Bars': 1, 'American (Traditional)': 1, 'Italian': 1, 'Beer Bar': 1}
# Hints: Use WHERE clause.
#
# Your function must pass all the unit tests to get full credit.
###############################################################################

def  get_restaurant_dict(db_filename):

    pass

###############################################################################
# [Part 2]
###############################################################################
# Complete the function barchart_restaurants_and_price(..), which takes in a dictionary created by the function in Part 2, 
# and uses matplotlib functions to draw a bar chart with restaurant categories on the x axis, 
# and the number of restaurants with a price level of 2 in that category on the y axis. 
# The chart must have appropriate axis labels and a title.
# Sort the X axis alphabetically from left-to-right. 
# Finally, this function should sort the dictionary items alphabetically and return the resulting list of tuples.
# Submit an image file of your bar chart to Canvas, along with your
# repository link.
###############################################################################

def barchart_restaurants_and_price(cat_dict):
    pass

##############################################################################
# [Extra Credit]
##############################################################################
# One way to analyze restaurant data is to understand how dense it is for a specific category in one zip area. 
# For example, the pizza category has 2 restaurants at 48104, and 5 at 48106. 
# In this case, pizza is more dense at 48106 than 48104. 
# The more restaurants with the same category in one zip area, the more competition there would be. 
# 
# Complete function maximum_density_by_category(..) to plot a barchart. 
# The x axis will be the restaurant category. The y axis will be the number of restaurants at their most densely located zip. 
# Sort the x axis in alphabetically descending order from left-to-right. 
# The chart must have appropriate axis labels and a title.
#
# Submit an image file of your chart to Canvas.
# Finally, this function should return a dictionary where the keys are restaurant categories. 
# The values should be a nested dictionary, where the keys are zip code and values are the number of restaurants for that zip code and corresponding category.
##############################################################################


def maximum_density_by_category(db_filename):

    pass

# #############################################################################
#                        DO NOT MODIFY THE TEST CASES                         #
#                                                                             #
# Don't forget to uncomment the one for the extra credit if you are           #
# attempting it.                                                              #
# #############################################################################

class TestHW8(unittest.TestCase):

    maximum_density_by_category("Restaurants.db")

    def test_get_restaurant_dict(self):
        category_dict =  get_restaurant_dict('Restaurants.db')
        answer_dict = {
            'American (Traditional)': 1,
            'Bakeries': 1,
            'Beer Bar': 1,
            'Beer, Wine & Spirits': 2,
            'Breweries': 1,
            'Delis': 2,
            'Farmers Market': 1,
            'Italian': 1,
            'Pizza': 8,
            'Pubs': 2,
            'Salad': 2,
            'Sandwiches': 1,
            'Sports Bars': 1
        }
        self.assertEqual(type(category_dict), dict)
        self.assertEqual(len(category_dict), 13)
        self.assertDictEqual(category_dict, answer_dict)

    def test_barchart_restaurants_and_price(self):
        print(
            """
            Passing this test case does NOT guarentee you full points.
            You MUST check your image against the expected output.
            """
        )
        sorted_data = barchart_restaurants_and_price(get_restaurant_dict(
            'Restaurants.db')
        )
        answer_data = [
            ('American (Traditional)', 1),
            ('Bakeries', 1),
            ('Beer Bar', 1),
            ('Beer, Wine & Spirits', 2),
            ('Breweries', 1),
            ('Delis', 2),
            ('Farmers Market', 1),
            ('Italian', 1),
            ('Pizza', 8),
            ('Pubs', 2),
            ('Salad', 2),
            ('Sandwiches', 1),
            ('Sports Bars', 1)
        ]

        self.assertEqual(type(sorted_data), list)
        self.assertEqual(type(sorted_data[0]), tuple)
        self.assertEqual(len(sorted_data), 13)
        self.assertEqual(sorted_data, answer_data)


    # UNCOMMENT THIS IF YOU ARE ATTEMPTING THE EXTRA CREDIT
    # ######################################################
    # def test_maximum_density_by_category(self):
    #     print(
    #         """
    #         Passing this test case does NOT guarentee you full points.
    #         You MUST check your image against the expected output.
    #         """
    #     )
    #     density_dict = maximum_density_by_category('Restaurants.db')
    #     answer_dict = 
    #         {'Bakeries': {'48197': 1, '48108': 1}, 
    #           'Farmers Market': {'48103': 1}, 
    #           'Salad': {'48104': 2}, 
    #           'Smokehouse': {'48103': 1}, 
    #           'Italian': {'48104': 5}, 
    #           'Pubs': {'48103': 1, '48104': 2}, 
    #           'Delis': {'48104': 2}, 
    #           'Pizza': {'48103': 2, '48198': 3, '48104': 9, '48108': 3, '48111': 1, '48197': 2}, 
    #           'Tapas Bars': {'48104': 1}, 
    #           'Vegan': {'48104': 1}, 
    #           'Sandwiches': {'48104': 1}, 
    #           'Beer, Wine & Spirits': {'48113':2}, 
    #           'American (New)': {'48104': 1}, 
    #           'Breweries': {'48130': 1, '48104': 3}, 
    #           'Sports Bars': {'48176': 1}, 
    #           'American (Traditional)': {'48104': 1}, 
    #           'Chicken Wings': {'48130': 1}, 
    #           'Beer Bar': {'48103': 1}}
    #     self.assertEqual(type(density_dict), dict)
    #     self.assertEqual(len(density_dict), 18)
    #     self.assertDictEqual(density_dict, answer_dict)


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
