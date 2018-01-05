# python3


def make_set(tree, i):
    tree[i] = {
        'index': i,
        'parent': i,
        'rank': 0
    }


def find(tree, i):
    while tree[i]['parent'] != i:
        i = tree[i]['parent']

    return tree[i]


def union(tree, i, j):
    i_id = find(tree, i)
    j_id = find(tree, j)
    if i_id == j_id:
        return
    if i_id['rank'] > j_id['rank']:
        j_id['parent'] = i_id['parent']
    else:
        i_id['parent'] = j_id['parent']
        if i_id['rank'] == j_id['rank']:
            j_id['rank'] += 1
