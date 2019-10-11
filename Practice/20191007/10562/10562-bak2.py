#!/usr/bin/env python3
class Node:
    def __init__(self, name, ind):
        self._name = name
        self._ind = ind
        self._is_single = False
        self._has_children = False
        self._children_range = None
        self._children = []

    def get_string(self):
        return '{0}({1})'.format(self._name, ''.join([c.get_string() for c in self._children]))

    @property
    def name(self):
        return self._name

    @property
    def ind(self):
        return self._ind

    @property
    def is_single(self):
        return self._is_single

    @is_single.setter
    def is_single(self, val):
        self._is_single = val

    @property
    def has_children(self):
        return self._has_children

    @has_children.setter
    def has_children(self, val):
        self._has_children = val

    @property
    def children_range(self):
        return self._children_range

    @children_range.setter
    def children_range(self, val):
        self._children_range = val

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, val):
        self._children = val


def parse_letter_row(row, global_pad=0):
    letters = [char for char in row if char not in ' \t\n\r\f\v']
    # print(letters == row.split(), letters, row.split())     # DEBUG
    nodes = []
    # INFO: Find indices
    pad = 0
    tmp_row = row
    for l in letters:
        ind = tmp_row.index(l) + pad
        nodes.append(Node(l, ind+global_pad))
        pad = ind + 1
        tmp_row = row[pad:]
    return nodes


def parse_tree(tree):
    parent, link, span, children = tree[:4]
    # INFO: Parse parent row
    parent_nodes = parse_letter_row(parent)
    # INFO: Parse link row, check if each parent has children
    for pnode in parent_nodes:
        if pnode.ind >= len(link):
            break
        if link[pnode.ind] == '|':
            pnode.has_children = True
            if pnode.ind == len(link) - 1:
                continue
            pnode.is_single = link[pnode.ind+1] == '|'
    # INFO: Parse span row into sections
    span_sect = []
    in_span = False
    for i in range(len(span)):
        if span[i] == '-':
            if not in_span:
                in_span = True
                start = i
        else:
            if in_span:
                in_span = False
                span_sect.append((start, i))
    if in_span:
        span_sect.append((start, i))
    # INFO: Check which parent each section corresponds to
    ipnode = 0
    while span_sect:
        sect = span_sect[0]
        sect_range = range(*sect)
        while ipnode < len(parent_nodes):
            pnode = parent_nodes[ipnode]
            ipnode += 1
            if not pnode.has_children:
                continue
            if pnode.is_single:
                pnode.children = (sect[0], sect[0]+1)
                del span_sect[0]
                span_sect.insert(0, (sect[0]+1, sect[1]))
                break
            pnode.children_range = sect
            del span_sect[0]
            break
    # INFO: Check which children each parent corresponds to
    for pnode in parent_nodes:
        if not pnode.has_children:
            continue
        start, end = pnode.children_range
        children_sect = children[start:end]
        pnode.children = parse_letter_row(children_sect, start)
    # INFO: If only 4 rows left, return
    if len(tree) < 5:
        return parent_nodes
    # INFO: Else, parse next 4 rows
    children_nodes = parse_tree(tree[3:])
    # INFO: Link children nodes by index
    for pnode in parent_nodes:
        if not pnode.has_children:
            continue
        children_indices = [c.ind for c in pnode.children]
        i = 0
        new_children = []
        while i < len(children_nodes) and children_indices:
            cnode = children_nodes[i]
            if cnode.ind not in children_indices:
                i += 1
                continue
            new_children.append(cnode)
            del children_nodes[i]
            children_indices.remove(cnode.ind)
        pnode.children = new_children
    return parent_nodes


def main():
    t = int(input())
    # INFO: For each case
    for _ in range(t):
        # print()     # DEBUG
        # INFO: Read till '#'
        tree = []
        line = input()
        while line.strip() != '#':
            tree.append(line)
            line = input()
        if not tree:
            print('()')
            continue
        if len(tree) == 1:
            print('({})'.format(''.join(['{}()'.format(char) for char in [
                  char for char in tree[0] if char not in ' \t\n\r\f\v']])))
            continue
        # INFO: Parse tree
        nodes = parse_tree(tree)
        # print(nodes)    # DEBUG
        print('({})'.format(''.join([c.get_string() for c in nodes])))


if __name__ == '__main__':
    main()
