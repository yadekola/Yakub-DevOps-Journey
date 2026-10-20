"""A tiny HTML web app returned by an AWS Lambda Function URL."""


def lambda_handler(event, context):
    """Return a web page as an HTTP response."""
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Tech365 Lambda App</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 720px; margin: 12vh auto; padding: 0 1.5rem; color: #172033; }
    main { padding: 2rem; border-radius: 1rem; background: #f0f5ff; }
    h1 { color: #174ea6; }
  </style>
</head>
<body>
  <main>
    <h1>Hello from AWS Lambda!</h1>
    <p>This web page is being served by a Python function running without a server to manage.</p>
    <p>Built with Terraform for Tech365.</p>
  </main>
</body>
</html>"""

    return {
        "statusCode": 200,
        "headers": {"content-type": "text/html; charset=utf-8"},
        "body": html,
    }
