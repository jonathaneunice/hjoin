# -*- coding: utf-8 -*-

def string_shape(s):
    """
    Return the height, width of a string, in lines/scharacters.
    h,w order chosen to be compatible with rows, columns standard of
    NumPy and and its shape method.
    """
    lines = s.splitlines()
    lengths = [len(l) for l in lines]
    return (len(lengths), max(lengths or [0]))


def hjoin(strings, sep=' '):
    """
    Horizontal join. Concatenates strings horizontally. Like
    join, but considers nth line of each string to be another column
    and concatenates it appropriately.
    """
    if not strings:
        return ''
    ncols = len(strings)
    slines = [s.splitlines() for s in strings]
    shapes = [string_shape(s) for s in strings]
    heights, widths = zip(*shapes)
    height = max(heights)
    lines = []
    for row_index in range(height):
        row = []
        for col_index in range(ncols):
            col_lines = slines[col_index]
            if row_index < heights[col_index]:
                cell = col_lines[row_index]
            else:
                cell = ''
            celljust = cell.ljust(widths[col_index])
            row.append(celljust)
        lines.append(sep.join(row))
    return '\n'.join(lines)
