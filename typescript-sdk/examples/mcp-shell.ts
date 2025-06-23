import { HttpAgent } from "../packages/client/src/agent";

async function main() {
  const url = process.env.MCP_SERVER_URL;
  if (!url) {
    console.error("Set MCP_SERVER_URL to the running Smithery server endpoint");
    process.exit(1);
  }

  const agent = new HttpAgent({ url });
  agent.messages = [
    { id: "1", role: "user", content: "hello" },
  ];

  for await (const event of agent.runAgent()) {
    console.log(event);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
