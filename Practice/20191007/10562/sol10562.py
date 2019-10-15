#!/usr/bin/env python3
__author__ = 'Lemuel Li, Patrick Feany, and Jonathan Sohrabi'


class Node:
    '''You know... A node

    Attributes:
        name     (str)         Single-character name for the node
        ind      (int)         Index of the node within the letter row
        children (List[Node])  Child nodes
    '''

    def __init__(self, name, ind):
        self.name = name
        self.ind = ind
        self.children = []

    def gen_str(self):
        '''Generate string for the node

        Returns:
            (str)  The string of interest
        '''
        return '{0}({1})'.format(
            self.name,
            ''.join([child.gen_str() for child in self.children]))


class Link:
    '''Links between parents and children

    Attributes:
        start (int)        Start index (inclusive)
        end   (int)        End index (exclusive)
        link  (List[int])  List of indices for links
    '''

    def __init__(self, start, end, link):
        self.start = start
        self.end = end
        self.link = link


def parse_letter_row(row):
    '''Parse a row of letters

    Args:
        row (str)  A row of letters
    Returns:
        (List[Node])  List of nodes in such row
    '''
    return [Node(row[i], i)
            for i in range(len(row))
            if row[i] not in ' \t\n\r\f\v#']


def get_links(span, link):
    '''Parse links w/ spans

    Args:
        span (str)  Hyphen row of span
        link (str)  V-line row of link
    Returns:
        (List[Link])  List of links
    '''
    # Basically, iterate through the span row
    in_span = False
    i_start = 0
    i_links = []
    links = []
    for i in range(len(span)):
        if span[i] == '-':
            if not in_span:
                # Start of a new span
                in_span = True
                i_start = i
                i_links = []
            if i < len(link) and link[i] == '|':
                # Link above
                i_links.append(i)
        elif in_span:
            # End of a span
            in_span = False
            links.append(Link(i_start, i, i_links))
    # Check if there's an EOL span
    if in_span:
        links.append(Link(i_start, len(span), i_links))
    return links


def assign_links(nodes, links, parent):
    '''Get children for each link and assign them to parents

    Args:
        nodes  (List[Node])  List of nodes of the children
        links  (List[Link])  List of links
        parent (str)         Letter row of parent
    Returns:
        (List[Node])  New list of nodes (of parents, with children linked)
    '''
    # Parse parent row
    parents = parse_letter_row(parent)
    for link in links:
        # Find children in range
        children = []
        i = 0
        while i < len(nodes):
            if nodes[i].ind < link.start:
                i += 1
            elif nodes[i].ind >= link.end:
                break
            else:
                children.append(nodes[i])
                del nodes[i]
        # Add children to parent
        max_link = max(link.link)
        for parent in parents:
            if parent.ind > max_link:
                break
            if parent.ind in link.link:
                parent.children = children
    return parents


def parse_level(nodes, span, link, parent):
    '''Parse each 4-row level and link to the lower level of nodes

    Args:
        nodes    (List[Node])  List of nodes of the children
        span     (str)         Hyphen row of span
        link     (str)         V-line row of link
        parent   (str)         Letter row of parent
    Returns:
        (List[Node])  New list of nodes (of parents, with children linked)
    '''
    # Get link positions
    links = get_links(span, link)
    # For each link, get its children and assign it to a node
    nodes = assign_links(nodes, links, parent)
    return nodes


def undraw_the_trees(inv_tree):
    '''Main function for tree parsing

    Args:
        inv_tree (List[str])  Raw tree, inverted
    Returns:
        (str)  Parsed string for inputted raw tree
    '''
    # Check tree at least has 1 line
    if not inv_tree:
        return '()'
    # Parse last row
    nodes = parse_letter_row(inv_tree[0])
    del inv_tree[0]
    # Parse every 3 rows in groups of 4
    while inv_tree:
        group, inv_tree = inv_tree[:3], inv_tree[3:]
        nodes = parse_level(nodes, *group)
    # Get nodes into string
    string = '({})'.format(''.join([node.gen_str() for node in nodes]))
    return string


def main():
    '''Main interface
    '''
    # Iterate through each test
    t = int(input())  # Number of test cases
    for _ in range(t):
        # Collect input until '#'
        tree = []
        i = input()
        while i.strip() != '#':
            tree.append(i.rstrip())
            i = input()
        # Process input and print result
        result = undraw_the_trees(tree[::-1])   # Note inverted tree
        print(result)


if __name__ == '__main__':
    main()
