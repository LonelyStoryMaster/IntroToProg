#(1): Prompt for four weights. Add all weights to a list. Output list.
def get_weights():
    weights = []
    for i in range(4):
        weight = float(input("Enter weight %d:\n" % (i + 1)))
        weights.append(weight)
    print("Weights:", weights)
    return weights

def print_weights(weight_list):

    #(2): Output average of weights.
    #(3): Output max weight from list.
    avg_weight = sum(weight_list) / len(weight_list)
    max_weight = max(weight_list)
    print("\nAverage weight: %0.2f\nMax weight: %0.2f" % (avg_weight, max_weight))

    #(4): Prompt the user for a list index and output that weight in pounds and kilograms.
    usr_index = int(input("\nEnter a list index (1 - 4):"))
    sel_lbs_weight = weight_list[usr_index - 1]
    sel_kilo_weight = weight_list[usr_index - 1] / 2.2
    print("\nWeight in pounds: %0.2f\nWeight in kilograms: %0.2f" % (sel_lbs_weight, sel_kilo_weight))

    #(5): Sort the list and output it.
    print("\nSorted list:", sorted(weight_list))

if __name__ == '__main__':
    print_weights(get_weights())
