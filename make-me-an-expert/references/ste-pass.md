# STE and unslop pass

Run this pass on **every generated pack** and **every teaching reply**. Do not skip it.

`ste-writing` and `unslop` are always-on. They do not count toward the compose cap of 4.

## When

1. After you write pack Markdown (`MISSION.md`, `SOURCES.md`, `kb/`, `course/book.md`, `watchlist.md`, `supplements/`).
2. Before you render the PDF.
3. After each gap-fill append. Then re-render the PDF.
4. Before you send a teaching reply to the user.

Do not run this pass on:

- `STATE.md` YAML keys and values (machine state)
- Code fences, file paths, CLI commands, skill IDs
- Quoted resume phrases (keep `make me an expert — continue` as written)

## Step 1. Load `ste-writing`

Read `ste-writing/SKILL.md`. Use **STE-flavored** for notes, the coursebook, and teaching prose. Use **strict** for numbered procedures in the coursebook.

Rewrite pack prose in place:

- One name for one thing
- Short common words
- Active voice
- One instruction per sentence
- No semicolons
- No em dashes in new prose
- No contractions
- American spelling
- No marketing adjectives

Do not rewrite code, identifiers, or command syntax.

## Step 2. Run `unslop`

Read `unslop/SKILL.md`. For each generated Markdown file in the list above, run:

```bash
unslop --stdin --deterministic < "$FILE" > "$FILE.unslop" && mv "$FILE.unslop" "$FILE"
```

If `unslop` is missing, install with `pipx install unslop` or `uv tool install unslop`. Then run the command.

Use `--deterministic`. Do not use the LLM mode of `unslop`.

After `unslop`, read the file. Restore any broken code fence, table, or path.

## Step 3. Restore STE after `unslop`

`unslop` often inserts contractions. Expand them. Write "do not", "is not", "cannot", "will not". Do not keep "don't", "isn't", "can't".

Keep quoted resume phrases as written, including `make me an expert — continue`.

Then send or render.

## Teaching replies

Write the reply in STE. Pipe the reply through `unslop --stdin --deterministic`. Expand contractions. Send only the cleaned text.

## PDF

Render `course/book.md` only after this pass. The PDF must match the STE and unslop output.
