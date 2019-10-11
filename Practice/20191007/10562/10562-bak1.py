#!/usr/bin/env python3
class Parent:
    def __init__(self, name, has_children, ind):
        self._name = name
        self._has_children = has_children
        self._ind = ind
        self._span = None
        self._children = []
        self._children_nodes = []

    def get_string(self):
        if not self._has_children:
            return '{}()'.format(self._name)
        return '{0}({1})'.format(self._name, ''.join([c.get_string() for c in self._children_nodes]))

    @property
    def name(self):
        return self._name

    @property
    def ind(self):
        return self._ind

    @property
    def has_children(self):
        return self._has_children

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, val):
        self._children = val

    @property
    def children_nodes(self):
        return self._children_nodes

    @children_nodes.setter
    def children_nodes(self, val):
        self._children_nodes = val

    # @property
    # def span(self):
    #     return self._span

    # @span.setter
    # def span(self, val):
    #     self._span = val


def get_name_and_indices(string, pad=0):
    nodes = [char for char in string if char not in ' \n']
    indices = []
    j = 0
    for i in range(len(string)):
        if j >= len(nodes):
            break
        if string[i] == nodes[j]:
            indices.append(i+pad)
            j += 1
    return (nodes, indices)


def parse_tree(tree):
    parent, relation, span, children = tree[:4]
    # Parse parent and relation
    parent_nodes, parent_indices = get_name_and_indices(parent)
    nodes = []
    print(parent, parent_indices)
    for ind in parent_indices:
        nodes.append(Parent(parent[ind], relation[ind] == '|', ind))
    # Parse span
    spans = []
    in_span = False
    for i in range(len(span)):
        char = span[i]
        if char == '-':
            if not in_span:
                in_span = True
                start = i
        else:
            if in_span:
                in_span = False
                spans.append((start, i))
    # Associate relations and children with span
    for x in spans:
        r = range(*x)
        for y in nodes:
            if y.ind in r:
                # y.span = x
                c = children[x[0]: x[1]]
                _, y.children = get_name_and_indices(c, x[0])
                break
    # Parse the next 4 lines
    # print(len(tree), nodes, [x.name for x in nodes],
    #       [x.children_nodes for x in nodes])
    if len(tree) < 5:
        return nodes
    cs = parse_tree(tree[3:])
    # print(cs, [x.name for x in cs])
    for x in nodes:
        if not x.has_children:
            continue
        cst = []
        for y in x.children:
            i = 0
            while i < len(cs):
                z = cs[i]
                if z.ind != y:
                    i += 1
                    continue
                cst.append(z)
                del cs[i]
        # print(cst)
        x.children_nodes = cst
    return nodes


def main():
    t = int(input())
    for _ in range(t):
        tree = []
        branch = input()
        while branch.strip() != '#':
            tree.append(branch)
            branch = input()
        node_tree = parse_tree(tree)
        print(''.join([c.get_string() for c in node_tree]))


if __name__ == '__main__':
    main()
