import os

from .helpers import fastq as fq
from .helpers import bio_files as bf

def filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    """
    Filters FASTQ reads by GC content, length and mean quality.
    Filtered reads are saved to a FASTQ file in the 'filtered' directory.

    Args:
        input_fastq: Path to the input FASTQ file.
        output_fastq: Name of the output FASTQ file.
        gc_bounds: Minimum and maximum GC percentages, or an upper bound.
        length_bounds: Minimum and maximum read lengths, or an upper bound.
        quality_threshold: Minimum acceptable mean quality score.

    Returns:
        Path to the filtered FASTQ file.
    """
    os.makedirs("filtered", exist_ok=True)

    output_filename = os.path.basename(output_fastq)
    output_path = os.path.join("filtered", output_filename)

    with open(input_fastq, "r") as input_file:
        with open(output_path, "w") as output_file:

            while True:
                header = input_file.readline()

                if header == "":
                    break

                sequence = input_file.readline()
                separator = input_file.readline()
                quality = input_file.readline()

                if sequence == "" or separator == "" or quality == "":
                    raise ValueError("Incomplete FASTQ record")

                header = header.rstrip("\r\n")
                sequence = sequence.rstrip("\r\n")
                separator = separator.rstrip("\r\n")
                quality = quality.rstrip("\r\n")

                if len(sequence) != len(quality):
                    raise ValueError(
                        "Sequence and quality lengths do not match"
                    )

                gc_passed = fq.check_gc_bounds(sequence, gc_bounds)
                length_passed = fq.check_length_bounds(
                    sequence, length_bounds
                )
                quality_passed = fq.check_quality_threshold(
                    quality, quality_threshold
                )

                if gc_passed and length_passed and quality_passed:
                    output_file.write(
                        f"{header}\n{sequence}\n{separator}\n{quality}\n"
                    )
    print ("Results are saved in"), output_path
    return output_path


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta):
    """
    Converts a multiline FASTA file into a file with one line per sequence.

    Args:
        input_fasta: Path to the input FASTA file.
        output_fasta: Path to the output FASTA file.

    Returns:
        Path to the output FASTA file.
    """
    with open(input_fasta, "r") as input_file:
        with open(output_fasta, "w") as output_file:

            header = None
            sequence = ""

            for line in input_file:
                line = bf.remove_line_ending(line)

                if line == "":
                    continue

                if bf.is_fasta_header(line):

                    if header is not None:
                        output_file.write(sequence + "\n")

                    header = line
                    output_file.write(header + "\n")
                    sequence = ""

                else:
                    if header is None:
                        raise ValueError(
                            "FASTA sequence found before the first header"
                        )

                    sequence = sequence + line

            if header is not None:
                output_file.write(sequence + "\n")

    print ("Results are saved in"), output_fasta
    return output_fasta
