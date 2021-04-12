# LP2
Language Processing 2 Authorship Verification Task

This is the GitHub repository for the best authorship verification model ever made.

## About the data:

I have written a bit about the data and made a script which tinkers with it. You can look at this if you find it useful. Damn, this is some nerdy shit and might be useless to you ;-)

We have two files (for now):

* `data/pan20-authorship-verification-training-small-truth.jsonl`
* `data/pan20-authorship-verification-training-small.jsonl`

They are not included in this repository, due to size. [Download here](https://absalon.ku.dk/courses/41573/files/folder/project?).

Each line in the JSON files is a dictionary, consisting of two documents. Here is their format:

```
small-truth.jsonl:
	id	- str, the ID for the entry.
	fandoms	- list/str, what two fanfic universes are the documents?
	pair	- list/str, the actual text of the two documents.

small.jsonl:
	id	- str, the ID of the entry.
	same	- bool, is the author of the two documents the same?
	authors	- list/str, the author IDs. 
```