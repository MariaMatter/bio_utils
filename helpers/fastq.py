
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
        raise ValueError("The length of a nucleotide sequence must be not zero")

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
        raise ValueError("The length of a quality sequence must be not zero")

    mean_quality = quality_sum / len(quality)

    return mean_quality

def check_gc_bounds(sequence, gc_bounds=(0, 100)):
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

def check_length_bounds(sequence, length_bounds=(0, 2**32)):
    """
    Checks whether sequence length is within the specified bounds.

    Args:
        sequence: A nucleotide sequence.
        length_bounds: A number of an upper sequence length bound or a tuple, 
        containig minimum and maximum sequence length bounds.

    Returns:
        True if sequence length is within bounds, otherwise False.
    """
    sequence_length = len(sequence)

    if isinstance(length_bounds, (int, float)):
        return sequence_length <= length_bounds

    elif len(length_bounds) == 2:
        return length_bounds[0] <= sequence_length <= length_bounds[1]

    else:
        raise ValueError("length_bounds must be a number or a pair of numbers")


def check_quality_threshold(quality, quality_threshold=0):
    """
    Checks whether mean read quality reaches the threshold.

    Args:
        quality: A string with quality scores.
        quality_threshold: Minimum acceptable mean quality.

    Returns:
        True if mean quality reaches the threshold, otherwise returns False.
    """
    mean_quality = calculate_mean_quality(quality)

    if mean_quality >= quality_threshold:
        return True
    else:
        return False


