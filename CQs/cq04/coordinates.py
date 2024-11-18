def get_coords(xs: str, ys: str) -> None:
    """ "creating a new function get coords"""
    xs_idx: int = 0
    """xs starts at 0"""
    ys_idx: int = 0
    """ys starts at 0"""
    while xs_idx < len(xs):
        ys_idx: int = 0
    while ys_idx < len(ys):
        print("(" + xs[xs_idx] + "," + ys[ys_idx] + ")")
        ys_idx += 1
    return None


"""CQ04 - learning to import"""

__author__ = "730668125"
