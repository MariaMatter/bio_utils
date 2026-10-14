
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
        return ValueError

    mean_quality = quality_sum / len(quality)

    return mean_quality


