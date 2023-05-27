### Append DB
## Testing out how to make some basic storage engines
## One of the most basic ones is an append only db that appends entries to a file
## This works well with writes. The issue here is reads can take a while. This is also not space contious.
## Writes do not override. Reads simply get the latest entry. Overwrites simply add another entry.
## Some optimizations can be made with reads and space. To be explained.