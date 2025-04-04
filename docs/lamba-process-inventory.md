# Lambda Function Specification: Real-Time Inventory Processor

## Function Purpose
Defines the behavior of a Lambda function responsible for processing real-time inventory change events from a point-of-sale (POS) system. The function decodes product SKUs, validates input, detects suit combos, and stores transactional logs in DynamoDB.

## Function Name
`processInventoryChange`

## Trigger Source
- API Gateway (HTTP POST request)
- Future extension: EventBridge for batch processing or scheduled imports

## Input Payload Schema
Example payload:
```json
{
  "product_id": "P2154",
  "base_product_id": "54",
  "category": "pants",
  "change": -1,
  "location": "store-1",
  "timestamp": "2025-04-03T16:00:00Z",
  "source": "POS",
  "combo": true
}
```
Assumes the payload passes initial schema validation at the API Gateway level.

## Output Format
Example response:
```json
{
  "status": "success",
  "message": "Inventory change processed",
  "combo_detected": true,
  "combo_id": "J2345-P2154"
}
```
On error, the function should return:
```json
{
  "status": "error",
  "message": "Description of the error"
}
```

## Core Responsibilities
- Decode `product_id` using internal SKU logic
- Validate presence and correctness of required fields
- Apply business logic to detect suit combos
- Write the transaction to the DynamoDB table (`inventory_change_log`)
- Include `combo_id` for paired jacket and pants entries

## Integration Points
- DynamoDB table: `inventory_change_log`
- Future integrations: Amazon SNS or EventBridge for notifications and async workflows

## IAM Permissions Required
- `dynamodb:PutItem` on `inventory_change_log`
- Optional: `logs:PutLogEvents` for enhanced logging to CloudWatch

## Error Handling
- Log all invalid payloads to CloudWatch
- Return structured error responses via API Gateway mapping templates
- Future: Consider a Dead Letter Queue (DLQ) or EventBridge for retry logic on failed messages

## Logging and Observability
- Log incoming requests and SKU decoding results
- Log all detected suit combos with `combo_id`
- Use JSON structured logging for integration with CloudWatch Logs Insights

## AWS Well-Architected Framework Alignment

### Operational Excellence
- Includes structured logging and validation logic
- Supports agile development via schema-first design and small deployments

### Security
- Follows the principle of least privilege with minimal IAM permissions
- Input is validated before processing to prevent injection or logic abuse

### Reliability
- Validates data before writing to DynamoDB
- Design anticipates and plans for payload issues and malformed requests

### Performance Efficiency
- Lightweight, stateless execution model using AWS Lambda
- Efficient request-based processing avoids idle compute

### Cost Optimization
- Serverless architecture minimizes compute overhead and idle cost
- Supports efficient DynamoDB write usage

### Sustainability
- Uses AWS Lambda for on-demand execution, avoiding unnecessary infrastructure
- Promotes efficient resource utilization through streamlined processing

