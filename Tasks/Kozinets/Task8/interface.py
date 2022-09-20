import bl


def main_flow():
	exit = False
	while exit != True:
		data = bl.represent_category()
		filtered_data = []
		while exit != True:
			if filtered_data:
				new_filtered_data = bl.represent_catalog(filtered_data,bl.cart)
				if new_filtered_data == 'back': break
				elif new_filtered_data == 'go to cart':
					bl.cart = bl.go_to_cart(bl.cart)
					if bl.cart == 'exit':
						exit = True
						break
					continue
			else:
				new_filtered_data = bl.represent_catalog(data,bl.cart)
				if new_filtered_data == 'back': break
				elif new_filtered_data == 'go to cart':
					bl.cart = bl.go_to_cart(bl.cart)
					if bl.cart == 'exit':
						exit = True
						break
					continue
			filtered_data = new_filtered_data

main_flow()