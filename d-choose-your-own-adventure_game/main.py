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

def data_logic(l):
    '''
    data handling for the health and inventory in the game
    it can be : 
    : param l=[ "health" , "action" , amount  ]
    OR can be
    : param l=[ "inventory" , "action" ,  amount  , "type" ]
    
    l[0] : str : health or inventory
    l[1] : str : add or reduce
    l[2] : int : amount to be added or reduced
    l[3] : str : (only when l[0] is inventory) : type of utility
    '''
    data_type = l[0]
    action = l[1]
    amount = l[2]

    if data_type == "health" : 
        
        if action == "add" : 
            pass
        
        elif action == "reduce" :
            pass
        
        pass
    
    elif data_type == "inventory" : 
        utility_type = l[3]

        if action == "add" : 
            pass
        
        elif action == "reduce" :
            pass
        
        pass

def database(request):
    '''
    Storing the data of health and items in inventory in a form of dict
    
    : param request : health or inventory
    '''
    data = {"health":10,
            "inventory":{
                "water":10
            }
    }

    return data.get(request , {})

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
                    ["inventory", "add", "silver", 3],
                    ["inventory", "reduce", "water", 5]
                ],
                "r": [
                    ["inventory","sin","add",5],
                    ["inventory", "reduce", "water", 5]
                ]
            }
        },
    }

    return story_tree.get(location, {})

def ui(location,choice_num):
    '''
    location :                      choices made : 
    health :                        inventory : {item number}        

    Text : 

    Condition : 

    Enter input : Right, left, x for inventory
    '''
    current_location = location
    choice_number = choice_num
    health = database("health")
    inventory = database("inventory")

    while True:

        # create variables to print

        print(f'''

    Location : {current_location}{'':>20} Choices Made : {choice_number}

    Health : [{"■"*health}{' '*(10-health)}]{'':>14} Inventory : press x 

            ''')

        node = story(current_location)

        if not node:
            print("No scene found for : ", current_location)
    



def game():

    current_location = "main"

    ui(current_location,)    
    pass

if __name__ == "__main__":

    clear()
    
    game()