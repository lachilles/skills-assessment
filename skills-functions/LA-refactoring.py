
price = raw_input("What is the price of the item?")
price = float(price)
state = raw_input("What state are you in?")

def item_cost(state, tax):

	""" Calculates item cost by adding tax """

	if state == "CA":
		tax = .07
	else:
		pass

	total = price + (tax * price)
	print total

item_cost(state, .05)

name = raw_input("What is your name? ")
title = raw_input("What is your title? ")


def title_name(title, name):
	"""Prints name and title"""
	if title == '':
		print "Engineer" + " " + name 
	else:
		print title + " " + name

title_name(title, name)