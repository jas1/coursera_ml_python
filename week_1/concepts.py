# ------------------------------------------------
def hypothesis_function(input_params,strategy="lin_reg"):
    """
    hypotesis_function: to represent hypothesis. 
    its related to the specific slide:  trainig set > learning algorithm > hypothesis funciton
    it recives an input, and then output. 
    in this initial case will use univarated linear regression.
    to keep the "framework" just delegate the responsability of linear regression in another function.
    eventually this can have an strategy pattern on different algorithms.
    """

    output_value = None
  
    if strategy=='lin_reg' :
        output_value=first_example_univariated_linear_reg(input_params)
    elif strategy=='nn_1':
        output_value=nn_1(input_params)
    else:
        raise Exception("NOT VALID STRATEGY. {}".format(strategy))

    return(output_value)


def nn_1(input_params):
    raise Exception("NOT IMPLEMENTED")

def first_example_univariated_linear_reg(input_params):
    """
    univariated linear regression example.
    """
    output_value = ''
    thetha_1 = ''
    thetha_2 = ''
    x = input_params['x']

    output_value = thetha_1 + thetha_2 * x

    return(output_value)


def cost_function(train_set,strategy="sum_sqr_error"): 
    """
    this cost function is what we need to minimize
    """
    cost_function_return = None

    if strategy=='sum_sqr_error' :
        cost_function_return=sum_sqr_error(train_set)
    elif strategy=='other':
        cost_function_return=other_cost_function(train_set)
    else:
        raise Exception("NOT VALID STRATEGY. {}".format(strategy))

    return cost_function_return

# choose thetha_1 , thetha_2 that minimize the difference between Y and Y'
# N number of training examples. 
def sum_sqr_error(train_set):

    N_train_set_observations=len(train_set['x']) # range its not inclusive 
    index_range = range(0, N_train_set_observations,1)

    total_sum=0
    for index in index_range:
        current_sum=(hypothesis_function(train_set['x'][index]) - train_set['y'][index])**2
        total_sum=total_sum + current_sum

    ret = (1/(2 * N_train_set_observations )) * total_sum

    return(ret)

def other_cost_function(train_set):
    raise Exception("NOT IMPLEMENTED")