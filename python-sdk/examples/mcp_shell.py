import os
import sys
import json
import requests


def main() -> None:
    url = os.environ.get("MCP_SERVER_URL")
    if not url:
        print("Set MCP_SERVER_URL to the running MCP server endpoint", file=sys.stderr)
        sys.exit(1)

    payload = {
        "messages": [
            {"id": "1", "role": "user", "content": "hello"}
        ]
    }

    with requests.post(url, json=payload, stream=True, headers={"Accept": "text/event-stream"}) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
            except json.JSONDecodeError:
                print(line.decode("utf-8"))
                continue
            print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()

