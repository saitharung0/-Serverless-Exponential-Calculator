# Exponential-calculator-webapp
A serverless web application that computes any base number raised to any exponent. Hosted on AWS Amplify, this app uses AWS Lambda to perform calculations, stores results in DynamoDB, and utilizes API Gateway for HTTP requests to trigger the computation.

Features
Calculate base-exponent results with high precision.
Store computation results in a DynamoDB table.
Seamless API integration using API Gateway.
Fully serverless architecture.

Technologies Used
AWS Amplify: Hosting the web application.
AWS Lambda: Python-based function to perform the calculations.
AWS API Gateway: Enables HTTP requests from the web app to Lambda.
AWS DynamoDB: Stores computation results for future use.

Architecture
Provide a simple architecture diagram (you can use tools like draw.io or Lucidchart):
User sends input (base and exponent) via the web app.
API Gateway processes the HTTP request.
API Gateway triggers the Lambda function.
Lambda performs the computation and writes the result to DynamoDB.
The response is sent back to the user via API Gateway.
