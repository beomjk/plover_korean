# Steno Order

Each key in this system is written as follows, in this order. (This order may differ from the one used on actual CAS machines.)

1. `1-`
2. `2-`
3. `3-`
4. `4-`
5. `5-`
6. `ㅎ-`
7. `ㅁ-`
8. `ㄱ-`
9. `ㅈ-`
10. `ㄴ-`
11. `ㄷ-`
12. `ㅇ-`
13. `ㅅ-`
14. `ㅂ-`
15. `ㄹ-`
16. `ㅗ-`
17. `ㅏ-`
18. `ㅜ-`
19. `-*`
20. `-ㅓ`
21. `-ㅣ`
22. `-6`
23. `-7`
24. `-8`
25. `-9`
26. `-0`
27. `-ㅎ`
28. `-ㅇ`
29. `-ㄹ`
30. `-ㄱ`
31. `-ㄷ`
32. `-ㅂ`
33. `-ㄴ`
34. `-ㅅ`
35. `-ㅈ`
36. `-ㅁ`

This order, called the steno order, gives a clear and consistent way to write strokes in dictionary entries and when talking with others. When a stroke has several keys, they must be written in this order for it to work. Unlike in English stenography, the order of the keys within each hand does not necessarily match the order of the letters in the output, but writing them in steno order is still required for Plover to read the stroke correctly.

Notice that keys on the left side of the layout *end* with a hyphen, and keys on the right side *start* with one. When you write several keys from the same side, their hyphens merge into one: at the end of the group for the left side, and at the start for the right side. For example, instead of `ㅎ-ㅈ-` you write `ㅎㅈ-`. If a stroke uses only left-side keys, the hyphen is usually dropped (`ㅎㅈ`); if it uses only right-side keys, the hyphen stays (`-ㅎㅈ`). Pressing several keys together is called a chord or a stroke.

The hyphens also disappear when the stroke includes one of the six middle keys, since a middle key already separates the two sides. For example, instead of `ㅎ--ㅓ-ㄱ` you write `ㅎㅓㄱ`. Without a middle key, a single hyphen stays between the sides: instead of `ㅎ--ㄱ` you write `ㅎ-ㄱ`.

Following these rules, the whole steno order can be written as: `12345ㅎㅁㄱㅈㄴㄷㅇㅅㅂㄹㅗㅏㅜ*ㅓㅣ67890ㅎㅇㄹㄱㄷㅂㄴㅅㅈㅁ`.

To write several strokes in a row, put a `/` between them. For example, `ㅎㅓ` followed by `ㅎㅏ` is written `ㅎㅓ/ㅎㅏ`. Combining multiple chords together like this can also be referred to as a stroke.
