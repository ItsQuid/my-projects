# Isaiah Garcia
# COP 2500C 0R06
# November 11th 2025
# Program 10 Thanksgiving menu
# I pushed to Github  yay



def get_guest_preferences(num_guests):
    
    #  Collects the name and three favorite dishes for a given number of guests.
    # Stores dishes in a list.
    
    preferences = {}

    for i in range(num_guests):
        guest_num = i + 1
        
        # Ask for the guest's name
        name = input("What is guest #" + str(guest_num) + "’s name?\n")

        # Ask for their three dishes
        print("What are " + name + "’s three favorite dishes?")
        
        dishes_list = []
        for j in range(3):
            # Read the dish and convert to lowercase
            dish = input().lower()
            dishes_list.append(dish)  # appends the list

        preferences[name] = dishes_list

    return preferences

def get_common_dishes(guest_data):
    
    # Finds the common dishes from a dictionary of guest preference lists.
    
    
    common_list = []
    is_first_guest = True # Checks for first guesst

    for current_guest_list in guest_data.values():
        
        if is_first_guest:
            
            for dish in current_guest_list:
                if dish not in common_list:
                    common_list.append(dish)
            
            
            is_first_guest = False
        else:
            
            new_common_list = []
            
            for dish in common_list:
                # Check if the dish from our common list
                # is also in the current guest's list.
                if dish in current_guest_list:
                    new_common_list.append(dish)
            
            # The new, smaller list becomes the common_list
            # for the next round of checks.
            common_list = new_common_list
    
    return common_list

def print_menu(common_dishes):
    
    # Prints the final Thanksgiving menu
    
    print("\nThis Thanksgiving, we will have:")

    # Use sort to sort the list
    common_dishes.sort()
    
    
    for dish in common_dishes:

        print(dish.title())

def main():
    
    # Main function to run the Thanksgiving menu planner.
    
    # Get the number of guests
    num_guests = int(input("How many guests are coming for Thanksgiving?\n"))

    # Get preferences from all guests
    all_preferences = get_guest_preferences(num_guests)

    # Find the common dishes
    common = get_common_dishes(all_preferences)

    # Print the final menu
    print_menu(common)


main()
