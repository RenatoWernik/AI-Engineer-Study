unprinted_designs = ["phone case","anime toy","robot"]
completed_models = []

def print_designs(pendent_designs,completed_designs):
    while unprinted_designs:
        for model in unprinted_designs:
            current_design = unprinted_designs.pop()
            print(f"Printing {current_design}")
            completed_models.append(current_design)
    print(f"The current models have been printed: {', '.join(completed_models).title()}")

print_designs(unprinted_designs,completed_models)
