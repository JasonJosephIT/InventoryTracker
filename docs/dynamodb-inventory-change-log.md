DynamoDB Table Design: inventory_change_log

Table Name

inventory_change_log

Purpose

Tracks all inventory modifications received through the POS system, including standalone items. This table serves as an immutable event log and supports future analytics, forecasting, and auditing use cases. Detected combos are handled by a separate function and stored in a different table.

Primary Keys

Partition Key: location (String)

Sort Key: transaction_id (String, unique identifier per event)

Rationale: This allows efficient querying of all inventory changes at a specific location with precise traceability using transaction IDs.

Secondary Indexes

Global Secondary Index (GSI): product_id-index

Partition Key: product_id

Sort Key: timestamp

Use Case: Enables product-based tracking and filtering across all stores and time windows.

Table Attributes

Attribute

Type

Description

product_id

String

SKU being tracked (e.g., P2154, S201)

base_product_id

String

Shared product reference for combo logic

category

String

Product type (pants, jacket, shirt, tie)

change

Number

Quantity change (positive or negative)

location

String

Store or warehouse identifier

timestamp

String

ISO 8601 formatted timestamp

source

String

Origin of event (POS, batch, etc.)

combo

Boolean

Whether the item is part of a detected bundle

combo_id

String

Unique ID for bundled jacket+pants pair

transaction_id

String

Unique transaction identifier used as sort key

Capacity Mode

On-Demand (Pay-per-request)

Workload is expected to have spiky traffic from retail POS systems. On-demand provides flexibility without provisioning capacity upfront.

TTL (Time to Live)

Not enabled initially. Data retention will be handled manually or through archival pipeline.

Well-Architected Considerations

Pillar

Alignment

Reliability

Primary and GSI keys enable quick recovery of historical logs

Operational Excellence

Clean, normalized event log format aids observability

Security

IAM roles restrict write access to Lambda only

Cost Optimization

On-demand mode for write-bursty workloads

Performance

Efficient access patterns aligned with query types

Sustainability

Table optimized for high-throughput, event-driven workloads

