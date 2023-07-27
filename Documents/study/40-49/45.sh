sort output45.txt | uniq --count | sort --numeric-sort --reverse > "すべて.txt"

grep '^行う\s' output45.txt | sort | uniq --count | sort --numeric-sort --reverse > "行う.txt"

grep '^なる\s' output45.txt | sort | uniq --count | sort --numeric-sort --reverse > "なる.txt"

grep '^与える\s' output45.txt | sort | uniq --count | sort --numeric-sort --reverse > "与える.txt"

