# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/wildechoes11-ops/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/wildechoes11-ops/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A program that writes one image summing up the world news of Saturday, 21 November 2026 — "The World in One Day". An entry for the make.fun bounty [“Sum up 21 November’s world news in one image”](https://make.fun/bounty/news-image-20261121).

The image is a newspaper-style infographic drawn with Pillow: a masthead
naming Saturday, 21 November 2026, and six stories reported that day —

- a magnitude 6.9 earthquake in Peru’s Andes, felt in Lima;
- Iran’s claim to have downed a 58th US MQ-9 drone over the Strait of Hormuz;
- the FBI’s probe into a suspected hack of its national crime database;
- KL Rahul becoming the first Indian opener with a Test hundred in every
  SENA country;
- Thinking Machines’ Inkling 2 Mini, a 26B-parameter AI model that runs on
  a laptop;
- OpenAI’s MedChemBench, with GPT-6.2 Astra scoring 84.5%.

Every story was checked against reporting dated 21 November 2026 before it
went on the image. The artwork is drawn from scratch (Pillow primitives);
no photos or copied artwork are used.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That copies `entry.png` to `out/entry.png`. The program uses only the
Python standard library, needs no network, and writes the same bytes on
every run.

## Files

- `entry.png` — the image (1024×1024 PNG)
- `main.py` — the entry program
- `LICENSE` — MIT

## Licence

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
