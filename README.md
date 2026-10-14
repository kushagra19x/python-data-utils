# python-data-utils

A lightweight, zero-dependency reference library of hand-crafted Python data manipulation utilities, file parsers, and schema restructuring helpers. This repository contains modular functions for raw file processing, delimiter extraction, string sanitization, and converting unstructured text streams into native Python data structures.

---

## Overview

High-level libraries often abstract basic data ingestion behind opaque single-line functions. Understanding the underlying file handles, character streams, memory buffers, and collection schemas is essential for writing robust software and building custom data pipelines.

This repository serves as a practical, dependency-free reference for foundational data-wrangling tasks implemented entirely with the Python Standard Library:
* Reading, streaming, and stripping raw text files safely.
* Parsing delimited tabular files (CSV, TSV, custom separators).
* Normalizing headers, trimming whitespace, and casting data types dynamically.
* Handling missing or corrupt records through explicit fallbacks.
* Structuring raw data into native formats, such as Record Lists (`list[dict]`), Nested Tables (`list[list]`), or Columnar Dictionaries (`dict[str, list]`).

---
