# makefun-news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/verrysimatupang99/makefun-news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/verrysimatupang99/makefun-news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

**Sum up 27 November's world news in one image** — a make.fun bounty entry
([news-image-20261127](https://make.fun/bounty/news-image-20261127), $100, ends 2026-11-29 00:00 UTC).

One poster for Friday 27 November 2026, with the day named in big type
across the top. The lead story is the night's fuel-tanker disaster in
Cairo: a tanker overturned on the capital's Ring Road and caught fire,
killing 31 people and wounding 21 as the blaze engulfed 27 vehicles, with
the driver arrested. Below it, three more stories from the day: Russia
hitting two foreign grain ships carrying more than 100,000 tonnes of grain
near Ukraine's Black Sea ports of Odesa, alongside missile strikes on a
Kyiv shopping centre that wounded seven; Yemen's Houthis attacking Saudi
Aramco's Ras Tanura and Jazan refineries, killing one worker and pushing
Brent crude toward $95; and President Trump demanding a probe into the GDP
figures released before the midterm elections, calling them "fake". The
bottom lines add the Bogor gold-mine flood toll rising to 13 dead with 13
still trapped, UK net migration falling to 77,000 — its lowest since 1997
— Guinea-Bissau delaying its elections to 2028, and oil nearing $95 as
Gulf shipping faces new risks. The scenes are AI-drawn editorial pictures;
every word is set in clean type on top, so the date and each story stay
readable at a glance.

## Sources

Every story on the poster was checked against reporting published on
26–27 November 2026 before it was drawn: the Cairo tanker fire (Reuters,
26 Nov), the Russian strikes on grain ships and Kyiv (Reuters, 26 Nov),
the Houthi attacks on Saudi refineries (Reuters, 26 Nov), Trump's GDP
data probe demand (Reuters, 26 Nov), the Bogor mine toll (Reuters,
26 Nov), UK net migration (Reuters, 26 Nov) and Guinea-Bissau's delayed
elections (Reuters, 26 Nov). Nothing on the poster is invented.

## Running it

```shell
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

`main.py` (Python 3.13, standard library only) writes `entry.png` into
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` when that is set). The picture
is 1024×1024 and 343,704 bytes — JPEG bytes under the `entry.png` name, which
the bounty rules allow. Nothing is fetched from the
network and nothing varies between runs: two runs produce identical bytes.

## How the poster was made

A build script in the working directory lays the poster out with Pillow —
masthead, headline band, panel captions and the two footer lines — from two
generated scenes: a night view of Cairo's Ring Road after the tanker fire
for the hero, and one wide triptych split into the grain-ship, refinery
and Capitol panels. The scene files stay next to that script, not in
this repo. The poster is stored as JPEG bytes under the `entry.png` name
because the full PNG came to 1,196,381 bytes, just over the 1 MiB cap; the
JPEG is 343,704 bytes at the same 1024×1024.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
