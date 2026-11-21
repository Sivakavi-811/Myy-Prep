"""
DSA - Strings 06: Run-Length Encoding and Decoding

Problem:
    Compress a string by replacing each run of identical characters with the
    character followed by the run length ("aaabcc" -> "a3b1c2"), and decode
    such a string back. Assume the input contains no digits.

Approach / Intuition:
    Encode: scan with two pointers - `i` marks the run start, `j` advances
    while characters match; emit s[i] + str(j - i), then jump i to j.
    Decode: read a character, then accumulate all following digits as a
    (possibly multi-digit) count, e.g. "a12" -> 12 a's.
    Build output with a list + join to keep it linear (string += in a loop
    can be quadratic).

Complexity:
    Time:  O(n) for both
    Space: O(n) for the output
"""


def rle_encode(s: str) -> str:
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(f"{s[i]}{j - i}")
        i = j
    return "".join(out)


def rle_decode(s: str) -> str:
    out, i = [], 0
    while i < len(s):
        ch = s[i]
        i += 1
        count = 0
        while i < len(s) and s[i].isdigit():
            count = count * 10 + int(s[i])
            i += 1
        out.append(ch * count)
    return "".join(out)


if __name__ == "__main__":
    assert rle_encode("aaabcc") == "a3b1c2"
    assert rle_encode("wwwwaaadexxxxxx") == "w4a3d1e1x6"
    assert rle_encode("") == ""
    assert rle_encode("a" * 12) == "a12"

    for original in ("aaabcc", "wwwwaaadexxxxxx", "", "a" * 12, "abc"):
        assert rle_decode(rle_encode(original)) == original
    print("All test cases passed!")
