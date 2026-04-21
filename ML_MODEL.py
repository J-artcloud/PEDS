# Train model and make predictions


from email.policy import strict


l1 = [2, 0, 1]
l2 = [1, 0, 3]

def dot_product(v1, v2):
    """ num1 = values in v1
        num2 = values in v2
    """
    sum = 0
    for num1, num2 in zip(v1, v2):
        sum += num1 * num2
    return sum

def train():
    pass

def predict():
    pass