import os

from helpers import fastq as fq

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
