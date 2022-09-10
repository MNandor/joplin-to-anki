# Joplin To Anki

Script to create & update Anki notes based on content in Joplin notes.
`python`

## How it works

![graph](svg.svg)

In Joplin, and other Markdown editors, it's possible to create tables.

The following Markdown:
```markdown
|Country|Capital|
|-------|-------|
|Netherlands|Amsterdam|
|Germany|Berlin|
```

Would result in this table:

|Country|Capital|
|-------|-------|
|Netherlands|Amsterdam|
|Germany|Berlin|

The script scans Joplin notebooks for any such tables and exports them into a format that can be easily imported into Anki as notes.

## Setup

## About Tags

If your Joplin notebook has headings as seen below, they will automatically be added as nested tags.
```markdown
# Heading 1
## This is h2
x
```

In this case, notes created from the location of `x` would have the tag `heading-1::this-is-h2`.
You can find these notes in Anki by searching for either `heading-1` or `heading-1::this-is-h2`.
There is a bit of an edge case to be aware of here: if you're updating existing notes, the existing list of tags in Anki will be overwritten.
To get around this, any of these options work:

- disable updating existing notes when importing in Anki
- just don't set other tags for the notes inside Anki
- disable writing tags in this script by calling it `joplin-to-anki.py --no-heading-tags` **TODO**
- have a Tags column inside Joplin with the values you want to see in Anki

