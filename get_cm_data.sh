#!/bin/bash
URL_PREF="http://www.criminalmindsfanwiki.com/page/Season+";
URL_POST="+Quotes";
SEASONS=14;
let i=1;
function ee(){
    #echo $* >&2;
    eval $*;
}
while [ $i -lt $(($SEASONS+1)) ]; do {
    URL="${URL_PREF}${i}${URL_POST}";
    ee mkdir -p out/;
    CMD="{ w3m -cols 2000 -dump $URL | grep -E '^Episode' -A 10000 | grep -E '^\[INS' -B10000 | grep -vE '^Episode' | grep -vE '^\[INS' | grep -v 'Back to:' | sed -r 's/[\"“”]+/\"/g' | sed -E '/^$/d' | sed -r 's/^[0-9]+x[0-9]+,?\s*\"[^\"]+\"\s+//g' | grep -v '^[(][0-9] *quot' | sed -r 's/^\s+//g' | sed -r 's/\s{3,}/\",\"/g' | sed -r 's/\"\"/\"/g' | while read l; do echo \$l'\"'; done; }"
    ee "$CMD" > out/$i.txt;
    let i++;
}; done;
./print_table.py out/*.txt
