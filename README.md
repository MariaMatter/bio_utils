# Bioinformatics Utilities

This repository offers a collection of Python utilities for processing biological sequence files.

## Structure

```text
.
├── main.py
├── helpers/
│   ├── fastq.py
│   └── bio_files.py
└── README.md
```

- `main.py` — contains the two main utility functions.
- `helpers/fastq.py` — contains helper functions for FASTQ files filtering.
- `helpers/bio_files.py` — contains helper functions for FASTA file processing.

## Functions

### 1. FASTQ Filtering

**Function:** `filter_fastq()`

Filters FASTQ reads based on GC content, sequence length, and mean quality score.
A read is retained only if it satisfies all three filtering criteria.

**Parameters:**

| Parameter | Description | Default |
|---|---|---|
| `input_fastq` | Path to the input FASTQ file. | Required |
| `output_fastq` | Name of the output FASTQ file. | Required |
| `gc_bounds` | Minimum and maximum GC content percentages, or an upper bound. | `(0, 100)` |
| `length_bounds` | Minimum and maximum sequence lengths, or an upper bound. | `(0, 2**32)` |
| `quality_threshold` | Minimum acceptable mean quality score. | `0` |

The filtered FASTQ file is saved in the `filtered/` directory, which is created automatically in working directory if it does not exist.

**Example:**

```python
from main import filter_fastq 

filter_fastq(
    input_fastq="reads.fastq",
    output_fastq="filtered_reads.fastq",
    gc_bounds=(30, 70),
    length_bounds=(50, 300),
    quality_threshold=20
)

print(output_path)
```

This example retains reads with GC content between 30% and 70%, lengths between 50 and 300 nucleotides, and mean quality scores of at least 20.

### 2. Multiline FASTA Conversion

**Function:** `convert_multiline_fasta_to_oneline()`

Converts a multiline FASTA file into a format where each sequence is on a single line. Sequence headers remain on separate lines before them.

**Parameters:**

| Parameter | Description |
|---|---|
| `input_fasta` | Path to the input FASTA file. |
| `output_fasta` | Path to the output FASTA file. |

**Example:**

```python
from main import convert_multiline_fasta_to_oneline

output_path = convert_multiline_fasta_to_oneline(
    input_fasta="input.fasta",
    output_fasta="output.fasta"
)

print(output_path)
```
## Before start

Clone the repository using Git:

```bash
git clone <https://github.com/MariaMatter/bio_utils>
cd <bio_utils>
```
Alternatively, download the repository as a ZIP archive from GitHub and extract it.

### Import the utilities

The main utility functions are defined in `main.py`. If your Python script is located in the repository root, import the functions as follows:

```python
from main import filter_fastq, convert_multiline_fasta_to_oneline
```

You can then call the functions directly. The helper modules required by these utilities are located in the `helpers/` directory and are included in the repository.


