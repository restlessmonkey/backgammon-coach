# GNU Backgammon Service Integration

The iPhone PWA cannot execute the native GNU Backgammon desktop program directly. v2.0 therefore includes a strict HTTPS engine-adapter interface.

To activate verified grandmaster recommendations:

1. Deploy or connect an HTTPS service that evaluates the supplied legal candidates using GNU Backgammon.
2. Implement `ENGINE_API_CONTRACT.md`.
3. Enter the `/analyze` endpoint in the app.
4. Tap **Test engine connection**.
5. Keep **GNU Backgammon service — verified** selected.

Until that service is connected, v2.0 intentionally blocks grandmaster-labeled recommendations. The prior evaluator is still available as **Local teaching fallback — not grandmaster**.

No GNU Backgammon binary or neural-network weights are bundled in this ZIP.
