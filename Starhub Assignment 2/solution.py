def program(n):
    
    if  n <= 1:
        raise ValueError('This function only accepts an integer greater than 1, in order to run.')
    
    import json
    
    counter_dict = {"Count of Star": 0,
                    "Count of Hub": 0,
                    "Count of StarHub": 0}
    
    for i in range(1, n + 1):
        if '2' in str(i) and '7' in str(i):
            counter_dict["Count of StarHub"] += 1
        elif '2' in str(i):
            counter_dict["Count of Star"] += 1
        elif '7' in str(i):
            counter_dict["Count of Hub"] += 1
        else:
            continue
    
    counter_json = json.dumps(counter_dict)
    
    print(counter_json)
    
    return(counter_json)

if __name__ == '__main__':
    
    msg = "Enter an integer greater than 1: "
    valid = False
    
    while not valid:
        n = input(msg)
        
        try:
            n = int(n)
            valid = True
            
        except ValueError:
            raise ValueError("Function only accepts an integer as input, in order to run")
    
    program(n)