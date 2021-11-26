# 6. Jelenleg pontosan 14 óra van. Beállítunk egy ébresztoórát úgy, hogy 51 órával kés ˝ obb csörögjön. Hány órakor fog az ébresztoóra megszólalni? (Segítség: Ha túlzottan vonz a lehet őség, hogy az ujjaidon számold ki, akkor 51 helyett dolgozz 5100-zal.)
most = 14
eltelt = 51
maradek = (most+eltelt)%24
napok = (most+eltelt)//24
print(napok,maradek)