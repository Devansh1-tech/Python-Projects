import webbrowser

while True:
    car_name = input("Enter the car name with model and year : ")
    if car_name.lower() in[]:
        break
    
    website = f"https://www.google.com/search?q=site:cars24.com + {car_name.replace(' ', '+')} "
    
    print(f"Opening Cars24 page for: {car_name}")
    webbrowser.open(website)