import math
import random
import numpy as np
import copy
from statistics import mode
from mysklearn.mypytable import MyPyTable

def separate(data, header, classLabel):
    """ separates the X set from the y set based on classLabel
        Args:
            data(list of list): all the data
            header(list of str): labels for each column
            classLabel(str): label for the chosen class
        Returns:
            data(list of list): all of the X data
            classList(list of obj): all of the y values
    """
    classList = []
    index = header.index(classLabel)
    for row in data:
        classList.append(row[index])
        del row[index]
    return data, classList

def calculateLeastSquares(xCol, yCol, printer):
    """calculates the leastsquares line approximation
        Args:
            xCol (column of floats): values to compute as x values
            yCol (column of floats): values to compute as y values
        Returns:
            m (float): slope of approximate line
            b (float): y-int of approximate line
            r (float): the correlation coefficient
            cov (float): the covariance
    """
    x_mean = sum(xCol)/len(xCol)
    y_mean = sum(yCol)/len(yCol)
    
    num = sum([(xCol[i] - x_mean)*(yCol[i] - y_mean) for i in range(len(xCol))])
    
    m = num / sum([(xCol[i] - x_mean)**2 for i in range(len(xCol))])
    b = y_mean - m * x_mean 
    
    
    r = num / math.sqrt(sum([((xCol[i] - x_mean)**2)for i in range(len(xCol))])*sum([((yCol[i] - y_mean)**2) for i in range(len(xCol))]))
            
    cov = num / len(xCol)
    if printer:    
        print("y = " + str(m) + "x + " + str(b))
        print("Correlation Coefficient: " + str(r))
        print("Covariance: " + str(cov))
    
    return m,b,r,cov

def nestedListToList(nested):
    """flattens a list
        Args:
            nested (list of a list of obj): could be anything
        Returns:
            flattened list
    """
    return [ii for lis in nested for ii in lis]

def compute_bootstrapped_sample(table):
    n = len(table)
    sample = []
    for _ in range(n):
        rand_index = random.randrange(0, n)
        sample.append(table[rand_index])
    return sample

def random_stratified_split(X, y, test_size = 1/3):
    X_test = []
    X_train = []

    y_test = []
    y_train = []
    group_names, group_subtables= group_by(X, y)
    for ii, table in enumerate(group_subtables):
        split_index = math.ceil(len(table) * test_size)
        X_test.append(table[:split_index])
        for jj in range(len(table[:split_index])):
            y_test.append(group_names[ii])
        X_train.append(table[split_index:])
        for jj in range(len(table[split_index:])):
            y_train.append(group_names[ii])

    
    return nestedListToList(X_train), nestedListToList(X_test), y_train, y_test

def group_by(xVals, yVals):
    """collects all xVals by their yVals
        Args:
            xVals (list of obj): attributes
            yVals (list of obj): class names for xVals [parallel to xVals]
        Returns:
            group_names (list of obj): titles of class
            group_subtables (list of list of obj): 
    """
    group_names = list(set(yVals))
    group_subtables = [[] for _ in group_names]
    
    # algorithm: walk through each row and assign it to the appropriate
    # subtable based on its group_by_col_name value
    for ii, identifier in enumerate(yVals):
        group_by_value = identifier
        # which subtable to put this row in?
        group_index = group_names.index(group_by_value)
        group_subtables[group_index].append(copy.deepcopy(xVals[ii]))
    return group_names, group_subtables

def compute_euclidean_distance(v1, v2):
    """checks for equal length and the computer euclidean distance
        Args:
            v1 (float): another number
            v2 (float): a number
        Returns:
            dist (float): distance between v1 and v2
    """
    assert len(v1) == len(v2)    
    if isinstance(v1[0], str) or isinstance(v2[0],str):
        if v1 == v2:
            return 0
        else:
            return 1
    else:
        return np.sqrt(sum([(v1[i] - v2[i]) ** 2 for i in range(len(v1))]))

def findMostFrequent(v1):
    """returns the mode of input
    """
    return mode(v1)

def normalize(arr):
    """normalizes an entire array
        Args:
            arr (list of float): values to normalize
        Returns:
            normalized list
    """
    minimum = min(arr)
    arr = [item - minimum for item in arr]
    maximum = max(arr)
    return [item/maximum for item in arr]

def get_DOE_ranking(mpg):
    #Just some bins...
    if mpg <= 13.0:
        return 1
    elif mpg > 13.0 and mpg < 15.0:
        return 2
    elif mpg >= 15.0 and mpg < 17.0:
        return 3
    elif mpg >= 17.0 and mpg < 20.0:
        return 4
    elif mpg >= 20.0 and mpg < 24.0:
        return 5
    elif mpg >= 24.0 and mpg < 27.0:
        return 6
    elif mpg >=27.0 and mpg < 31.0:
        return 7
    elif mpg >=31.0 and mpg < 37.0:
        return 8
    elif mpg >=37.0 and mpg < 45.0:
        return 9
    else:
        return 10

def getNHTSAsizes(weight):
    # more bins
    if weight <= 1999:
        return 1
    elif weight >= 2000 and weight < 2500:
        return 2
    elif weight >= 2500 and weight < 3000:
        return 3
    elif weight >= 3000 and weight < 3500:
        return 4
    elif weight >= 3500:
        return 5

def recurse_tree(header, tree, class_name, attributes, holder):
    info_type = tree[0]
    if info_type == "Attribute":
        if holder != "IF ":
            holder += " AND "
        if attributes is None:
            holder += tree[1]
        else:
            index = header.index(tree[1])
            holder += attributes[index]

        for i in range(2, len(tree)):
            value_list = tree[i]
            temp = holder + " == " + str(value_list[1]) + " "
            recurse_tree(header, value_list[2], class_name, attributes, temp)
    else:
        print(holder + "THEN " + class_name + " == " + str(tree[1]) + "\n")

def select_attribute(instances, available_attributes, original):
    entropyNews =  []
    for index in available_attributes:
        entropyNews.append(compute_entropy(instances, available_attributes, original.index(index)))
    return available_attributes[entropyNews.index(min(entropyNews))]

def compute_entropy(instances, available_attributes, index):
    mypy = MyPyTable(available_attributes, instances)
    classes = mypy.get_column(-1)
    attributes = mypy.get_column(index)
    temp = set(attributes)
    __, tables = group_by(attributes, classes)
    totals = []
    sub_entropies = []
    # get the class counts here
    for jj, element in enumerate(temp):
        totals.append(attributes.count(element))
        # parallel array of counts of each att for each class
        arr = []
        for table in tables:
            arr.append(table.count(element))
        su = 0
        for kk in arr:
            if kk <= 0:
                pass
            else:
                su -= kk/totals[jj]*math.log2(kk/totals[jj])
        su *= totals[jj]/len(attributes)
        sub_entropies.append(su)
    return sum(sub_entropies)


def all_same_class(instances):
    # assumption: instances is not empty and class label is at index -1
    first_label = instances[0][-1]
    for instance in instances:
        if instance[-1] != first_label:
            return False 
    return True # if we get here, all instance labels matched the first label

def compute_partition_stats(partition):
    arr = [instance[-1] for instance in partition]
    majority = mode(arr)
    count = arr.count(majority)
    total = len(partition)
    return [majority, count, total]