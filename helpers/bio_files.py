def is_fasta_header(line):
    """
    Checks whether a line is a FASTA header.

    Args:
        line: A line from a FASTA file.

    Returns:
        True if the line starts with '>', otherwise False.
    """
    return line.startswith(">")


def remove_line_ending(line):
    """
    Removes newline characters from the end of a line.

    Args:
        line: A string read from a file.

    Returns:
        The line without its ending newline characters.
    """
    return line.rstrip("\r\n")