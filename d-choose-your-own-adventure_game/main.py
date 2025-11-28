from utilities import clear , style , press_key , sleep

def valid_input():
    '''
    takes the different inputs but find the closest and return : r for right and l for left
    '''   
    while True:
        user = input("\n\nRIGHT or LEFT???\nEnter your choice : ").lower()
    # check if empty
        if not user:
            style("\nEmpty input...\nTry Again...",0.02)
            sleep(1)
            continue
    # check for inventory
        if user[0]=='x':
            if user == 'x' or user =='inventory':
                user = 'x'
                return user
            continue
    # check if its right
        if user[0]=='r':
            if user == 'r' or user =='rock':
                user = 'r'
                return user
            else:
                ask = input("Did you mean RIGHT ? (y/n) : ")
                if ask == 'y':
                    user = 'r'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
    # check if its left
        elif user[0]=='l':
            if user == 'l' or user =='left':
                user = 'l'
                return user
            else:
                ask = input("Did you mean LEFT ? (y/n) : ")
                if ask == 'y':
                    user = 'l'
                    return user
                else:
                    style("\nummm, we could not guess your input.\nTry Again...",0.02)
                    sleep(2)
    # if could not understand
        else:
            style("\nummm, we could not guess your input.\nTry Again...",0.02)
            sleep(2)

def inventory_logic(l):
    '''
    inventory stores different types of utilities that u find in the game and use them during gameplay
    
    :param l=[ type , action , amount ]
    
    l[0] : type : type of utilities
    l[1] : action : 0-reduce , 1-add
    l[2] : amount : amount to be added or reduced from the inventory 

    :return nothing just make changes in the list
    '''
    utility_type = l[0]
    action = l[1]
    amount = l[2]

    if action == 0 : # reduce from inventory
        pass

    elif action == 1 : # add in inventory
        pass

    pass

def health_logic(l):
    '''
    inventory stores different types of utilities that u find in the game and use them during gameplay
    
    :param l=[ action , amount ]
    
    l[0] : action : 0-reduce , 1-add
    l[1] : amount : amount to be added or reduced from the health 

    :return nothing just make changes in the list
    '''
    action = l[0]
    amount = l[1]

    if action == 0 : # reduce from inventory
        pass

    elif action == 1 : # add in inventory
        pass
    
    
    pass

def database():
    '''
    Storing the data of health and items in inventory in a form of dict
    '''
    data = {"health":100,
            "inventory":{
                "water":10
            }
    }

def story(location):
    """
    INPUT:
        location (str): the name of the current story scene

    OUTPUT:
        node (dict): a dictionary containing:
            - "text": description of the scene
            - "choices": possible user choices (mapping letters -> next locations)
            - "effects": effects tied to each choice (optional)
    """

    story_tree = {
        "main": {
            "text": "You stand at the Forest Gate...",
            "choices": {
                "l": "The Whispering River",
                "r": "The Forgotten Ruins",
                "x": "inventory"
            },
            # no effects here
        },

        "The Whispering River": {
            "text": "You reach a flowing river...",
            "choices": {
                "l": "Help the Stranger",
                "r": "Ignore the Stranger"
            },
            "effects": {
                "l": [
                    ["health", "reduce", 10],
                    ["inventory", "add", "silver", 3]
                ],
                "r": []
            }
        },
    }

    return story_tree.get(location, {})


    pass

def ui(location,choice_number,inventory):
    '''
    location :                      choices made : 
    inventory : {item number}       health : 

    Condition : 

    Enter input : Right, left, x for inventory
    '''
    
    
    pass


def game():

    
    
    pass

if __name__ == "__main__":

    clear()
    h = valid_input()
    print(h)