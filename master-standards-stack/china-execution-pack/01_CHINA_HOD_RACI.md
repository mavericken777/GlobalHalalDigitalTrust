# 01 — China HOD Department-by-Department RACI

## Purpose

Create a concrete institutional interface for each Chinese counterpart domain. The exact named counterpart must be confirmed against the formal itinerary and meeting mandate; this matrix is deliberately written by **function/interface**, not as a claim that every listed institution is the designated project authority.

## RACI legend

- **R — Responsible:** performs the work.
- **A — Accountable:** owns the outcome/decision.
- **C — Consulted:** provides required subject-matter input.
- **I — Informed:** receives controlled status information.

## Master interface matrix

| Interface domain | Candidate China counterpart function | AHTE engagement | R | A | C | I | Required meeting output |
|---|---|---|---|---|---|---|---|
| National standardisation | SAC / relevant technical committee | Standards architecture, crosswalk, terminology, digital representation | Technical standards team | Designated standards owner | AHTE standards architect, JAKIM/JSM interface | Programme office | Standard crosswalk workstream + terminology register |
| Market regulation | SAMR / relevant local market-regulation authority | Product safety, traceability, quality, inspection, certification/recognition interfaces | Relevant regulatory team | Designated regulatory owner | AHTE compliance team, industry operators | Programme office | Regulatory interface map + traceability integration route |
| Food safety | Food-safety authority functions | Food production/traceability/import-export controls | Factory/regulatory operators | Competent food-safety authority for scope | AHTE food control team, laboratory | Logistics, importer | Food safety data and inspection interface |
| Customs | GACC / relevant customs port | Export/import declaration, cargo identity, inspection, release/hold | Port/customs operators | Customs authority for transaction | AHTE border gateway, logistics | Manufacturer, importer | Border trust-packet specification + inspection workflow |
| Commerce / trade | MOFCOM / relevant trade bureau | Foreign trade, trade corridor, bilateral coordination | Trade programme team | Designated commerce owner | AHTE trade/legal, importer/exporter | Other HODs | Trade-corridor workplan + counterpart liaison mechanism |
| Data / cyberspace governance | CAC / relevant provincial cyber administration | Cross-border data, personal information, important-data assessment | China data governance team | Data controller/operator for applicable data | Legal, security, AHTE architecture | Programme office | Data classification + transfer decision framework |
| Digital industry | MIIT / relevant industrial digitisation authority | Factory digitisation, industrial data, platform interoperability | Factory IT/OT team | Industrial programme owner | AHTE integration team, MES/ERP vendors | Trade/regulatory HODs | Factory integration reference architecture |
| Accreditation / conformity | CNCA / accredited conformity ecosystem where applicable | Conformity-assessment and laboratory interfaces | CAB/lab team | Relevant accreditation/conformity authority | AHTE assurance, GCC destination authority | Programme office | Recognition / evidence interoperability plan |
| Local implementation | Provincial / municipal departments | Pilot site activation and local coordination | Local implementation team | Local programme owner | Factory, logistics, AHTE | National counterparts | Pilot site approvals and local operating contacts |
| Industrial manufacturing | Manufacturer/HQ operations | Product selection, process control, HCP implementation | Factory management | Manufacturer executive sponsor | AHTE deployment, auditor, lab | Logistics/importer | Site activation package + product roster |
| Logistics | Sinotrans / China Merchants logistics interface or appointed operator | Container, seal, custody, transport telemetry, export handover | Carrier operations | Carrier account owner | AHTE logistics, customs | Manufacturer/importer | Custody-event API + seal protocol |
| Laboratory | Qualified laboratory network | Sampling, method control, results, chain of custody | Lab personnel | Lab technical director | AHTE analytical team, authority | Manufacturer | Method registry + sample chain + result schema |
| Cybersecurity | Security/CISO function of each participating entity | Identity, key management, device security, monitoring, incident response | Security engineering | Entity security owner | AHTE security architect | Programme office | Security baseline + incident playbook |

## Decision package for each HOD meeting

Every HOD engagement must end with seven explicit objects:

1. `INTERFACE_OWNER` — named responsible office/team.
2. `MANDATE_SCOPE` — what the interface may decide or coordinate.
3. `DATA_SCOPE` — datasets and classifications involved.
4. `TECH_SCOPE` — APIs, devices, systems and protocols.
5. `PILOT_ACTION` — one concrete deliverable inside the first pilot.
6. `ACCEPTANCE_TEST` — objective pass/fail criteria.
7. `ESCALATION_ROUTE` — next authority level for unresolved issues.

## HOD meeting sequence

```text
1. Institutional mandate
      ↓
2. Current operating process
      ↓
3. Physical assets and control points
      ↓
4. Existing information systems
      ↓
5. Data classifications
      ↓
6. Cross-border interfaces
      ↓
7. Required standards / specifications
      ↓
8. Pilot deliverable
      ↓
9. Acceptance criteria
      ↓
10. Scale pathway
```

## Minimum questions by function

### Standardisation
- Which Chinese standards apply to each pilot product/process?
- Which are mandatory versus recommended/contractual?
- What is the authoritative source and effective date?
- How is the standard represented digitally?
- Which Chinese and international terminology must be normalised?

### Market / food regulation
- Which traceability obligations apply to the selected products?
- Which production, inspection and recall records are required?
- Which data are reportable and through which systems?
- Which events must be generated in near real time?

### Customs
- Which data elements can be embedded in the electronic border packet?
- What physical inspection events need to bind to the digital object?
- Which seal/container identifiers are authoritative?
- What constitutes a mismatch or inspection hold?

### Data governance
- What data classes exist in the pilot?
- Which data remain domestic?
- Which data may cross-border without personal information or important data?
- Which cross-border mechanism is required for regulated data?
- Who owns the transfer assessment and approvals?

### Industrial digitisation
- Which MES/ERP/QMS/WMS/LIMS systems exist?
- Which integration method is supported: API, message bus, file gateway, edge connector?
- What is the authoritative batch/lot source?
- How are machine timestamps and event integrity established?

### Laboratory
- Which methods and matrices are validated?
- Who controls method versions?
- How are samples sealed and transferred?
- How is the lab result associated with product/batch and authority case?

## Governance model

The programme office maintains the master interface register, but each interface owner remains accountable for the source system and authoritative business meaning of its own data. AHTE records provenance, mappings and event relationships without silently changing source semantics.

China's Standardization Law places unified administration of standardisation with the State Council's standardisation administration department while assigning relevant sector responsibilities to competent authorities; it also recognises standards at national, sector, local, association and enterprise levels. citeturn356679search1 SAMR's official responsibilities include product quality safety, traceability, food-safety supervision, standardisation, inspection/testing and certification/recognition supervision. citeturn748828search1 MOFCOM's official mission includes foreign trade, import/export policy and bilateral/multilateral economic and trade cooperation. citeturn356679search2

## RACI for Shipment 001

| Work package | China manufacturer | Lab | Logistics | Customs/port | AHTE | Malaysia authority interface | GCC importer/authority |
|---|---|---|---|---|---|---|---|
| Product selection | A/R | C | I | I | R | C | C |
| Material dossier | A/R | C | I | I | R | C | C |
| Factory onboarding | R | C | I | I | A/R | C | I |
| Audit execution | C | C | I | I | R | A/C | I |
| Lab evidence | C | A/R | I | I | R | C | C |
| Batch/lot binding | A/R | C | I | I | R | C | C |
| Container/seal | C | I | A/R | C | R | I | C |
| Export packet | R | C | R | A/C | R | I | C |
| Border inspection | I | I | C | A/R | R | I | C |
| GCC import admission | I | I | C | C | R | I | A/R |
| Destination release | I | C | C | C | R | I | A/R |
| Incident / recall | A/R | C | R | C | R | C | A/R |

## Principle

Each institutional interface must become executable in the software and in the physical operation. A signed meeting minute alone is not an integration: the result must become a registry object, workflow, API contract, event type, owner and acceptance test.
