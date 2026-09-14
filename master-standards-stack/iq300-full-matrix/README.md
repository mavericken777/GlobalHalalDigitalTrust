# IQ300 - Full Clause-to-Control Intelligence Layer

This package upgrades the Master Standards Stack into a machine-oriented regulatory control model.

Primary clause-level source corpus:
- MS 2400-1:2019 - Transportation
- MS 2400-2:2019 - Warehousing
- MS 2400-3:2019 - Retailing

Supporting source corpus:
- supplied halal audit training PDF
- supplied halal awareness PDF
- supplied JAKIM/Malaysian Standards compendia

The three uploaded MS 2400 PDFs yield 613 unique numbered requirement objects across clauses 4-8, including nested clauses such as 4.3.4.1.1 and 7.5.3.4.

Canonical IQ300 path:

`Clause -> Control Objective -> HCP -> Evidence -> Audit Test -> Finding -> Corrective Action -> Re-verification -> Authority Gate -> Trust State`

Important boundary: the supplied sector-standard compendia do not contain the complete licensed numbered subclause text for every sector standard. IQ300 therefore does not fabricate missing subclauses. Those standards are preserved as family-level controls plus an explicit source-gap register until licensed official text is available for final objectization.

Machine-readable assets in this folder are designed for ingestion by a compliance knowledge graph, rules engine, audit application or digital-twin service.
