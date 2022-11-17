def print_models(unprinted_design, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model {current_design}.")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Print info about printed designs."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
