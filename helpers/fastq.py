
def calculate_gc(sequence):
    """
    Calculates G and C nucleotides percentage in a sequence.

    Args:
        A nucleotide sequence.

    Returns:
        GC content as a percentage.
    """
    gc_count = sequence.upper().count("G") + sequence.upper().count("C")

    if len(sequence) == 0:
        return ValueError

    gc_percent = gc_count / len(sequence) * 100

    return gc_percent

