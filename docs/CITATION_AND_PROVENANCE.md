# Citation, provenance and reproducibility policy

## Cite both the collection and the original scientific source

If you use this repository, please cite **EVRP Benchmark Datasets** and cite the original dataset release and the primary paper that introduced the benchmark/problem variant. Citing this repository does not replace the original dataset or paper citation.

### Copy-ready citation for this repository

**APA 7**

> Prasad, A. (2026). *EVRP Benchmark Datasets* (Version 0.3.0) [Data set]. GitHub. https://github.com/anuxlab/evrp_benchmark_datasets

**IEEE**

> A. Prasad, “EVRP Benchmark Datasets,” version 0.3.0, GitHub repository, 2026. [Online]. Available: https://github.com/anuxlab/evrp_benchmark_datasets. [Accessed: Nov. 2, 2026].

**BibTeX**

```bibtex
@misc{prasad2026evrpbenchmarkdatasets,
  author       = {Prasad, Anurag},
  title        = {{EVRP Benchmark Datasets}},
  year         = {2026},
  version      = {0.3.0},
  howpublished = {GitHub repository},
  url          = {https://github.com/anuxlab/evrp_benchmark_datasets},
  note         = {Accessed: 2026-11-02}
}
```

**Chicago**

> Prasad, Anurag. 2026. *EVRP Benchmark Datasets*. Version 0.3.0. GitHub. https://github.com/anuxlab/evrp_benchmark_datasets.

For a later archival release, cite its Zenodo DOI instead of (or in addition to) the moving GitHub URL.

## Instance-level citation chain

Every benchmark instance must resolve through:

`instance -> dataset release -> source version/DOI or commit -> primary paper -> licence`

For derived instances, also cite the parent benchmark and the paper defining the transformation. Preserve the original filename and identify the transformation explicitly.

Examples:

- Schneider E-VRPTW: cite Schneider, Stenger & Goeke (2014) and the exact Mendeley Data version used.
- EVRP-NL-C: cite Montoya et al. (2017) for the 120-instance base family and Froger et al. (2022) for capacitated-station variants.
- Two-echelon EVRP: cite the formulation paper and the expanded dataset release separately.
- Gradient-aware derivatives: cite the gradient dataset/paper and the parent benchmark if derived from Schneider instances.

## Copy-ready experiment citation statement

> The benchmark instances were obtained from the *EVRP Benchmark Datasets* collection (Prasad, 2026). For each experiment, we additionally cite the original dataset release and primary publication identified in the instance-level provenance metadata. Dataset versions, source checksums, transformations and validation reports are recorded with the experiment artifacts.

Replace the generic statement with the exact dataset-specific references in the final paper.

## Never conflate

1. A **source collection** is a dataset landing page or repository.
2. A **release** is a versioned publication/archive/commit.
3. An **instance** is one problem file.
4. A **variant** is a defined mathematical problem extension.
5. A **derived instance** is created by a documented transformation.
6. A **local snapshot** is the exact archive/files stored or cached here.
7. A **catalogued source** is not necessarily downloaded.
8. A **locally integrated dataset** has actual files, licence review, checksums, parser support and validation evidence.

For DIMACS, for example, report 120 base instances plus 240 charger-capacity variants, not 360 unrelated base instances.

## Required provenance metadata

- dataset ID, title, release/version and landing page
- dataset DOI and paper DOI(s)
- source file name, retrieval timestamp, SHA-256
- licence and redistribution decision
- original parameter units and source definitions
- parent instance and transformation metadata (if derived)
- parser/schema version and validation status
- exact GitHub Actions run and report artifact

## Licence and redistribution

A public URL does not imply permission to mirror files. Keep external sources as download instructions when redistribution rights are absent or unclear. Do not commit non-commercial data for commercial reuse without checking the licence. Always retain original attribution and licence notices.
