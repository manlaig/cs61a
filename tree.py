def tree(val, child=[]):
    return [val] + child

def print_tree(tree, indent = 0):
    print(" " * indent + str(tree[0]))
    for b in tree[1:]:
        print_tree(b, indent=indent+5)

def get_leaves(tree):
    if len(tree) == 1:
        return tree
    
    leaves = []
    for b in tree[1:]:
        leaves += get_leaves(b)
    return leaves

def fib_tree(fib_num):
    if fib_num <= 2:
        return tree(max(0, fib_num-1))
    left, right = fib_tree(fib_num-1), fib_tree(fib_num-2)
    return tree(left[0] + right[0], [left, right])

def count_leaves(tree):
    if len(tree) == 1:
        return 1
    return sum([count_leaves(b) for b in tree[1:]])

def apply_to_leaves(t, func):
    if len(t) == 1:
        t[0] = func(t[0])
    else:
        for b in t[1:]:
            apply_to_leaves(b, func)

def new_tree_from_func(t, func):
    if len(t) == 1:
        return tree(func(t[0]))
    return tree(func(t[0]), [new_tree_from_func(b, func) for b in t[1:]])

#t = tree(5, [tree(1), tree(2,[tree(3)])])
t = fib_tree(3)
print_tree(t)

leaves = get_leaves(t)
print("leaves:", leaves)

print("# of leaves in each branch of root:", [count_leaves(b) for b in t[1:]])
print("total # of leaves:", count_leaves(t))

new_t = new_tree_from_func(t, lambda x : x*10)
print("\nafter new tree:")
print_tree(new_t)

apply_to_leaves(t, lambda x : x*10)
print("after applying function:", get_leaves(t))
print(t)
