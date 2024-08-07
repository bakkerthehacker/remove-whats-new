# remove-whats-new
Script to patch steam css files removing the What's New section

# features

- Written in python, runs on all OSes
- No 3rd party libs needed
- Looks for common steam locations
- Can be run from anywhere
- Also removes What's New section from Big Picture mode
- Flexible to any changes in css file names or css class names (random chars that change sometimes)
- Preserves CRLF line endings on non-windows OSes to ensure the same file size

# non-features

- Doesn't open or close steam for you
- Doesn't detect any changes or look for any updates

# other similar scripts

- [ChunkPatcher](https://github.com/zero318/BegoneWhatsNew/issues/10#issuecomment-1859056116) (windows only)
- [SteamWhatsNewYeeter](https://github.com/MateusAuri/SteamWhatsNewYeeter) (windows only, bash also available in fork)
- ~~[BegoneWhatsNew](https://github.com/zero318/BegoneWhatsNew) OG theme repo~~ No longer working
- ~~[Kopert Instructions](https://old.reddit.com/r/Steam/comments/10r753g/whats_new_section_came_back/j6v0ye5/)~~ No longer working
- [xtcrefugee Instructions](https://old.reddit.com/r/Steam/comments/1cmqsbc/removing_whats_new_add_shelf_and_left_column_in/)

# todo

- test on steam deck
- test on MacOS/Windows instead of guessing path globs
