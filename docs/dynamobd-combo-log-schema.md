DynamoDB Table Design: combo_log

Table Name

combo_log

Purpose

Stores all successfully detected suit combos (jacket + pants) that have been validated and paired by a separate Lambda function. This table is optimized for analytics, reporting, and integrity audits of combo detections across stores and time ranges.

Primary Keys

Partition Key: combo_id (String)

Sort Key: timestamp (String, ISO 8601 format)

Rationale: Each combo has a unique identifier (e.g., J2345-P2345) where jacket and pants have matching base_product_id. timestamp supports time-range analysis.

Table Attributes

Attribute

Type

Description

combo_id

String

Unique ID for combo, e.g. J2345-P2345 (jacket and pants share the same base_product_id)

jacket_id

String

SKU of the jacket in the combo

pants_id

String

SKU of the pants in the combo

base_product_id

String

Shared identifier used to match jacket/pants (must match for valid combo)

location

String

Store where the combo was sold

timestamp

String

ISO 8601 formatted timestamp

quantity

Number

Number of combos detected (default: 1)

source

String

Source system (e.g., POS)

Capacity Mode

On-Demand (Pay-per-request)

Combo detection is relatively rare and event-based. On-demand eliminates the need for capacity planning.

TTL (Time to Live)

Not enabled initially. Data should be retained for business reporting unless otherwise defined.

Well-Architected Considerations

Pillar

Alignment

Reliability

Dedicated table ensures durability of detection events

Operational Excellence

Easy to analyze trends in suit sales

Security

IAM-controlled writes from Lambda only

Cost Optimization

Rare writes = ideal for on-demand billing

Performance

Keys support time-series + audit-based access

Sustainability

Lightweight design ensures minimal resource consumption
