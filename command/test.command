load std

set listA to []
set listB to []
set listC to []
set listD to []

set i to 0
while i < 10
    edit listA at end insert i+1
    edit listB at end insert i+3
    edit listC at end insert i+5
    set i to i+1

set alpha to ((0@listC)@listB)@listA
show ((0 em C) em B) em A: alpha
show itens de A:
execute showList listA

show soma de A:
set sum to 0
execute sum listA
apply to sum
show sum