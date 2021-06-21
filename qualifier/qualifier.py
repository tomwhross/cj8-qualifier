from typing import Any, List, Optional


def get_max_column_lengths(rows: List[List[Any]]) -> dict:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).

    :return: A dict of the maximum string length in each column
    """

    number_of_columns = len(rows[0])

    max_lengths = dict()

    # for i in range(0, number_of_columns):
    #     max_lengths[i] = 0
    #     for row in rows:
    #         word = row[i]
    #         if len(str(word)) > max_lengths[i]:
    #             max_lengths[i] = len(str(word))

    for index, row in enumerate(rows):
        max_lengths[index] = 0
        for word in row:
            if len(str(word)) > max_lengths[index]:
                max_lengths[index] = len(str(word))

    return max_lengths


def make_table(
    rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False
) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    PIPE = "│"
    DASH = "─"
    TOP_LEFT = "┌"
    TOP_CENTER = "┬"
    TOP_RIGHT = "┐"
    MID_LEFT = "├"
    MID_CENTER = "┼"
    MID_RIGHT = "┤"
    BOTTOM_LEFT = "└"
    BOTTOM_CENTER = "┴"
    BOTTOM_RIGHT = "┘"

    max_lengths = get_max_column_lengths(rows)
    print(max_lengths)

    number_of_columns = len(rows[0])

    for i in range(0, number_of_columns):
        foo = "| "
        for row in rows:
            print(row[i])
            print((max_lengths[i] - len(str(row[i]))))
            foo = f"{foo}{row[i]}{' ' * (max_lengths[i] - len(str(row[i])) + 1)}"
        foo = f"{foo} |"
        print(foo)
