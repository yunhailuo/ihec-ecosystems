# IHEC Data Hub Sample schema Schema

```

```

The IHEC Data Hub Sample schema covers all metadata requested by IHEC Metadata Standards, as specified here:
https://github.com/IHEC/ihec-metadata/blob/master/specs/Ihec_metadata_specification.md

| Abstract            | Extensible | Status       | Identifiable | Custom Properties | Additional Properties | Defined In                                         |
| ------------------- | ---------- | ------------ | ------------ | ----------------- | --------------------- | -------------------------------------------------- |
| Can be instantiated | Yes        | Experimental | No           | Forbidden         | Permitted             | [sample.json.schema.json](sample.json.schema.json) |

# IHEC Data Hub Sample schema Definitions

| Property                                                              | Type     | Group                                |
| --------------------------------------------------------------------- | -------- | ------------------------------------ |
| [batch](#batch)                                                       | `string` | `#/definitions/cell_line`            |
| [cell_type](#cell_type)                                               | `string` | `#/definitions/primary_cell_culture` |
| [collection_method](#collection_method)                               | `string` | `#/definitions/primary_tissue`       |
| [culture_conditions](#culture_conditions)                             | `string` | `#/definitions/primary_cell_culture` |
| [differentiation_method](#differentiation_method)                     | `string` | `#/definitions/cell_line`            |
| [differentiation_stage](#differentiation_stage)                       | `string` | `#/definitions/cell_line`            |
| [donor_age](#donor_age)                                               | complex  | `#/definitions/donor`                |
| [donor_age_unit](#donor_age_unit)                                     | `enum`   | `#/definitions/donor`                |
| [donor_ethnicity](#donor_ethnicity)                                   | `string` | `#/definitions/donor`                |
| [donor_health_status](#donor_health_status)                           | `string` | `#/definitions/donor`                |
| [donor_health_status_ontology_uri](#donor_health_status_ontology_uri) | `string` | `#/definitions/donor`                |
| [donor_id](#donor_id)                                                 | `string` | `#/definitions/donor`                |
| [donor_life_stage](#donor_life_stage)                                 | `enum`   | `#/definitions/donor`                |
| [donor_sex](#donor_sex)                                               | `enum`   | `#/definitions/donor`                |
| [line](#line)                                                         | `string` | `#/definitions/cell_line`            |
| [lineage](#lineage)                                                   | `string` | `#/definitions/cell_line`            |
| [markers](#markers)                                                   | `string` | `#/definitions/primary_cell_culture` |
| [medium](#medium)                                                     | `string` | `#/definitions/cell_line`            |
| [origin_sample](#origin_sample)                                       | `string` | `#/definitions/primary_cell_culture` |
| [origin_sample_ontology_uri](#origin_sample_ontology_uri)             | `string` | `#/definitions/primary_cell_culture` |
| [passage](#passage)                                                   | `string` | `#/definitions/cell_line`            |
| [passage_if_expanded](#passage_if_expanded)                           | `string` | `#/definitions/primary_cell_culture` |
| [sex](#sex)                                                           | `enum`   | `#/definitions/cell_line`            |
| [tissue_depot](#tissue_depot)                                         | `string` | `#/definitions/primary_tissue`       |
| [tissue_type](#tissue_type)                                           | `string` | `#/definitions/primary_tissue`       |

## batch

The batch from which the cell line is derived. Primarily applicable to initial H1 cell line batches. NA if not
applicable.

`batch`

- is optional
- type: `string`
- defined in this schema

### batch Type

`string`

## cell_type

`cell_type`

- is **required**
- type: `string`
- defined in this schema

### cell_type Type

`string`

## collection_method

The protocol for collecting the primary tissue.

`collection_method`

- is optional
- type: `string`
- defined in this schema

### collection_method Type

`string`

## culture_conditions

The conditions under which the primary cell was cultured.

`culture_conditions`

- is **required**
- type: `string`
- defined in this schema

### culture_conditions Type

`string`

## differentiation_method

The protocol used to differentiation the cell line.

`differentiation_method`

- is optional
- type: `string`
- defined in this schema

### differentiation_method Type

`string`

## differentiation_stage

The stage in cell differentiation to which the cell line belongs.

`differentiation_stage`

- is **required**
- type: `string`
- defined in this schema

### differentiation_stage Type

`string`

## donor_age

The age of the donor that provided the cells/tissues. NA if not available. If over 90 years enter as 90+. If entering a
range of ages use the format “{age}-{age}”.

`donor_age`

- is **required**
- type: complex
- defined in this schema

### donor_age Type

**One** of the following _conditions_ need to be fulfilled.

#### Condition 1

`number`

#### Condition 2

`string`

#### Condition 3

`string`

All instances must conform to this regular expression (test examples
[here](https://regexr.com/?expression=%5E%5Cd%2B-%5Cd%2B%24)):

```regex
^\d+-\d+$
```

## donor_age_unit

`donor_age_unit`

- is **required**
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#donor_age_unit-known-values).

### donor_age_unit Known Values

| Value   | Description |
| ------- | ----------- |
| `year`  |             |
| `month` |             |
| `week`  |             |
| `day`   |             |

## donor_ethnicity

The ethnicity of the donor that provided the primary cell. NA if not available. If dealing with small/vulnerable
populations consider identifiability issues.

`donor_ethnicity`

- is **required**
- type: `string`
- defined in this schema

### donor_ethnicity Type

`string`

## donor_health_status

The health status of the donor that provided the primary cell. NA if not available.

`donor_health_status`

- is **required**
- type: `string`
- defined in this schema

### donor_health_status Type

`string`

## donor_health_status_ontology_uri

(Ontology: NCIM) Links to the health status of the donor that provided the primary cell. The NCImetathesaurus term
C0277545 'Disease type AND/OR category unknown' should be used for unknown diseases. For samples without any known
disease, use the NCImetathesaurus term C0549184 'None'. Phenotypes associated with the disease should be submitted as
DISEASE_ONTOLOGY_URIs (if available) or in the free form DISEASE attribute. If dealing with a rare disease, please
consider identifiability issues.

`donor_health_status_ontology_uri`

- is optional
- type: `string`
- defined in this schema

### donor_health_status_ontology_uri Type

`string`

## donor_id

An identifying designation for the donor that provided the cells/tissues.

`donor_id`

- is **required**
- type: `string`
- defined in this schema

### donor_id Type

`string`

## donor_life_stage

`donor_life_stage`

- is optional
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#donor_life_stage-known-values).

### donor_life_stage Known Values

| Value       | Description |
| ----------- | ----------- |
| `fetal`     |             |
| `newborn`   |             |
| `child`     |             |
| `adult`     |             |
| `unknown`   |             |
| `embryonic` |             |
| `postnatal` |             |

## donor_sex

'Male', 'Female', 'Unknown', or 'Mixed' for pooled samples.

`donor_sex`

- is **required**
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#donor_sex-known-values).

### donor_sex Known Values

| Value     | Description |
| --------- | ----------- |
| `Male`    |             |
| `Female`  |             |
| `Unknown` |             |
| `Mixed`   |             |

## line

The name of the cell line.

`line`

- is **required**
- type: `string`
- defined in this schema

### line Type

`string`

## lineage

The developmental lineage to which the cell line belongs.

`lineage`

- is **required**
- type: `string`
- defined in this schema

### lineage Type

`string`

## markers

Markers used to isolate and identify the cell type.

`markers`

- is optional
- type: `string`
- defined in this schema

### markers Type

`string`

## medium

The medium in which the cell line has been grown.

`medium`

- is **required**
- type: `string`
- defined in this schema

### medium Type

`string`

## origin_sample

Description of the origin tissue from which sample was extracted.

`origin_sample`

- is optional
- type: `string`
- defined in this schema

### origin_sample Type

`string`

## origin_sample_ontology_uri

(Ontology: UBERON) links to the tissue from which sample was extracted.

`origin_sample_ontology_uri`

- is optional
- type: `string`
- defined in this schema

### origin_sample_ontology_uri Type

`string`

## passage

The number of times the cell line has been re-plated and allowed to grow back to confluency or to some maximum density
if using suspension cultures.

`passage`

- is optional
- type: `string`
- defined in this schema

### passage Type

`string`

## passage_if_expanded

If the primary cell culture has been expanded, the number of times the primary cell culture has been re-plated and
allowed to grow back to confluency or to some maximum density if using suspension cultures. NA if no expansion.

`passage_if_expanded`

- is optional
- type: `string`
- defined in this schema

### passage_if_expanded Type

`string`

## sex

'Male', 'Female', 'Unknown', or 'Mixed' for pooled samples.

`sex`

- is **required**
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#sex-known-values).

### sex Known Values

| Value     | Description |
| --------- | ----------- |
| `Male`    |             |
| `Female`  |             |
| `Unknown` |             |
| `Mixed`   |             |

## tissue_depot

Details about the anatomical location from which the primary tissue was collected.

`tissue_depot`

- is **required**
- type: `string`
- defined in this schema

### tissue_depot Type

`string`

## tissue_type

The type of tissue.

`tissue_type`

- is **required**
- type: `string`
- defined in this schema

### tissue_type Type

`string`

# IHEC Data Hub Sample schema Properties

| Property                                      | Type     | Required     | Nullable | Defined by                                 |
| --------------------------------------------- | -------- | ------------ | -------- | ------------------------------------------ |
| [biomaterial_provider](#biomaterial_provider) | `string` | Optional     | No       | IHEC Data Hub Sample schema (this schema)  |
| [biomaterial_type](#biomaterial_type)         | `enum`   | **Required** | No       | IHEC Data Hub Sample schema (this schema)  |
| [disease](#disease)                           | `string` | **Required** | No       | IHEC Data Hub Sample schema (this schema)  |
| [disease_ontology_uri](#disease_ontology_uri) | `string` | **Required** | No       | IHEC Data Hub Sample schema (this schema)  |
| [sample_ontology_uri](#sample_ontology_uri)   | `string` | **Required** | No       | IHEC Data Hub Sample schema (this schema)  |
| [treatment](#treatment)                       | `string` | Optional     | No       | IHEC Data Hub Sample schema (this schema)  |
| `*`                                           | any      | Additional   | Yes      | this schema _allows_ additional properties |

## biomaterial_provider

The name of the company, laboratory or person that provided the biological material.

`biomaterial_provider`

- is optional
- type: `string`
- defined in this schema

### biomaterial_provider Type

`string`

## biomaterial_type

`biomaterial_type`

- is **required**
- type: `enum`
- defined in this schema

The value of this property **must** be equal to one of the [known values below](#biomaterial_type-known-values).

### biomaterial_type Known Values

| Value                  | Description |
| ---------------------- | ----------- |
| `Cell Line`            |             |
| `Primary Cell`         |             |
| `Primary Cell Culture` |             |
| `Primary Tissue`       |             |

## disease

Free form field for more specific sample disease information. This property reflects the disease for this particular
sample, not for the donor health condition. If dealing with a rare disease consider identifiability issues.

`disease`

- is **required**
- type: `string`
- defined in this schema

### disease Type

`string`

## disease_ontology_uri

(Ontology: NCIM) links to sample disease ontology information. This property reflects the disease for this particular
sample, not for the donor health condition. The NCImetathesaurus term C0277545 “Disease type AND/OR category unknown”
should be used for unknown diseases. Phenotypes associated with the disease should be submitted as
DISEASE_ONTOLOGY_URIs (if available) or in the free form DISEASE attribute. For samples without any known disease, use
the NCImetathesaurus C0549184 term 'None'. If dealing with a rare disease consider identifiability issues.

`disease_ontology_uri`

- is **required**
- type: `string`
- defined in this schema

### disease_ontology_uri Type

`string`

## sample_ontology_uri

(Ontology: EFO) links to sample ontology information.

`sample_ontology_uri`

- is **required**
- type: `string`
- defined in this schema

### sample_ontology_uri Type

`string`

## treatment

Any artificial modification (differentiation, activation, genome editing, etc).

`treatment`

- is optional
- type: `string`
- defined in this schema

### treatment Type

`string`

**Any** following _options_ needs to be fulfilled.

#### Option 1

- []() – `file:../schemas/json/sample.json#/definitions/cell_line`

#### Option 2

- []() – `file:../schemas/json/sample.json#/definitions/primary_cell`

#### Option 3

- []() – `file:../schemas/json/sample.json#/definitions/primary_cell_culture`

#### Option 4

- []() – `file:../schemas/json/sample.json#/definitions/primary_tissue`
