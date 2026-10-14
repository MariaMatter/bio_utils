
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
        return ValueError("The length of a nucleotide sequence must be not zero")

    gc_percent = gc_count / len(sequence) * 100

    return gc_percent

def calculate_mean_quality(quality):
    """
    Calculates the mean Phred score of a read.

    Args:
        A string with quality scores from fastq file.

    Returns:
        Mean quality score.
    """
    quality_sum = 0

    for symbol in quality:
        quality_score = ord(symbol) - 33
        quality_sum = quality_sum + quality_score

    if len(quality) == 0:
        return ValueError("The length of a quality sequence must be not zero")

    mean_quality = quality_sum / len(quality)

    return mean_quality

def check_gc_bounds(sequence, gc_bounds):
    """
    Checks whether GC content is within the specified bounds.

    Args:
        sequence: A nucleotide sequence.
        gc_bounds: A number of an upper GC bound or a tuple, containig minimum and maximum GC bounds. 
        Example of gc_bounds input as tuple - (40,60).

    Returns:
        True if GC content is lower one bound input or within bounds and False if not.
    """
    gc_percent = calculate_gc(sequence)

    if isinstance(gc_bounds, (int, float)):
        return gc_percent <= gc_bounds

    elif len(gc_bounds) == 2:
        return gc_bounds[0] <= gc_percent <= gc_bounds[1]

    else:
        raise ValueError("gc_bounds must be a number or a pair of numbers")


