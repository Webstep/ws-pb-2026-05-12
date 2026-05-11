# Lyse Tele - case for ice

## Problemstilling

Du får en liste med samtaledata (CDRs - Call Detail Records). Hver post inneholder følgende felter:

- `Caller`: Telefonnummeret som initierer samtalen.
- `Receiver`: Telefonnummeret som mottar samtalen.
- `StartTime`: Starttidspunktet for samtalen (ISO 8601-format).
- `Duration`: Varigheten av samtalen i sekunder.

Du må prosessere disse postene og svare på følgende:

- Identifiser de 3 mest aktive ringerne (basert på antall samtaler).
- Total varighet av samtaler gjort til nummeret som har hatt flest utgående samtaler.
- Beregn det totale antallet unike telefonnumre som er involvert i datasettet.

## Eksempeldata (`cdrs.json`)

```json
[
	{
		"Caller": "12345678",
		"Receiver": "09876543",
		"StartTime": "2024-11-27T10:00:00Z",
		"Duration": 120
	},
	{
		"Caller": "12345678",
		"Receiver": "11223344",
		"StartTime": "2024-11-27T10:05:00Z",
		"Duration": 60
	},
	{
		"Caller": "09876543",
		"Receiver": "12345678",
		"StartTime": "2024-11-27T10:10:00Z",
		"Duration": 180
	},
	{
		"Caller": "11223344",
		"Receiver": "12345678",
		"StartTime": "2024-11-27T10:20:00Z",
		"Duration": 30
	},
	{
		"Caller": "12345678",
		"Receiver": "44556677",
		"StartTime": "2024-11-27T10:30:00Z",
		"Duration": 90
	}
]
```

## Forventet resultat

```text
Top 3 Most Active Callers:
12345678: 3 calls
09876543: 1 calls
11223344: 1 calls

Total Duration of Calls to 12345678: 210 seconds
Total Unique Phone Numbers: 4
```

## Leveranse

- Legg løsningen på GitHub som er kjørbar med en eksempelfil.
- Send linken senest dagen før intervjuet.
- Ta med laptop for å kunne kjore en demo av løsningen.

## Ekstra oppgave

Nå ønsker vi å skille på om samtalen er innenlands eller utenlands.

- Innenlandssamtaler koster 1 ore per sekund.
- Utenlandssamtaler koster 3 ore per sekund.

Hvilke 3 telefonnumre har pådratt seg mest kostnader?

Fremgangsmåte for å løse denne:

1. Parse en liste med CDRs.
2. Bestem om en samtale er internasjonal.
3. Beregn kostnad basert på samtaletype (internasjonal/nasjonal).
4. Summer kostnader per `Caller`.
5. Finn de 3 numrene med hoyest kostnad.
