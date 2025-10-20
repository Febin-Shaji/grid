from ..grid import Grid

def test_grid_fill():
    """
    Test the fill method for the grid class.
    """

    # Intialise a 10x10 grid.
    g = Grid(10, 10)

    # Tally counter for the number of filled cells.
    n = 0

    # Let's check that the fill method works for all
    # cells in the grid. Probably overkill, but what the heck!

    # Loop over the width of the grid.
    for w in range(0, g.width()):

        # Loop over the height of the grid.
        for h in range(0, g.height()):

            # Increment the number of cells.
            n += 1

            # Fill the cell.
            g.fill(w, h)

            # Check that the number of filled cells is correct.
            assert g.nFilled() == n

            # Check that this cell is marked as filled.
            assert g.cell(w, h).occupied()

            # Try filling the cell again. (Not allowed!)
            g.fill(w, h)

            # Check that the number of filled cells is correct.
            assert g.nFilled() == n


def test_grid_empty():
    """
    Test the empty method for the grid class.
    """

    # Intialise a 10x10 grid.
    g = Grid(10, 10)

    # Let's check that the empty method works for all
    # cells in the grid. Probably overkill, but what the heck!

    # Loop over the width of the grid.
    for w in range(0, g.width()):

        # Loop over the height of the grid.
        for h in range(0, g.height()):

            # Fill the cell.
            g.fill(w, h)

            # Check that their is one filled cell.
            assert g.nFilled() == 1

            # Check that this cell is marked as filled.
            assert g.cell(w, h).occupied()

            # Empty the cell.
            g.empty(w, h)

            # Check that their are no filled cells.
            assert g.nFilled() == 0

            # Check that this cell is marked as empty.
            assert not g.cell(w, h).occupied()
