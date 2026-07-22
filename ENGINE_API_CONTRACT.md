# Backgammon Coach v2.0 Engine API Contract

## Principle

Engine decides. Coach teaches.

The PWA sends the current position and every legal complete turn to an HTTPS analysis endpoint. The endpoint must rank those candidates using GNU Backgammon and identify itself as `GNU Backgammon`.

## Health

`GET /health`

```json
{"status":"ok","engine":"GNU Backgammon","version":"1.08.x"}
```

## Analyze

`POST /analyze`

The request contains:

- `protocol`
- complete board state
- dice and turn
- every legal candidate with stable index, notation, and checker steps

The response must contain:

```json
{
  "engine": "GNU Backgammon",
  "version": "1.08.x",
  "rankings": [
    {
      "rank": 1,
      "index": 4,
      "notation": "13/8 6/5",
      "equity": 0.123,
      "error": 0,
      "explanation": "Optional engine-grounded note"
    }
  ]
}
```

## Safety rule

The app rejects responses that do not identify the engine as GNU Backgammon. It never silently substitutes the local heuristic while displaying a grandmaster label.

## Deployment

The endpoint must use HTTPS and permit requests from the PWA origin. GNU Backgammon licensing and source-distribution obligations must be reviewed before distributing a combined or derivative service.
