test = """hxbxwxba"""


def has_increasing_straight_letters(s: str) -> bool:
    # Iterate through the string checking for increasing sequences
    for i in range(len(s) - 2):
        if ord(s[i + 1]) == ord(s[i]) + 1 and ord(s[i + 2]) == ord(s[i]) + 2:
            return True
    return False


def test_has_increasing_straight_letters():
    assert has_increasing_straight_letters("abc") is True
    assert has_increasing_straight_letters("hijklmmn") is True
    assert has_increasing_straight_letters("abbceffg") is False
    assert has_increasing_straight_letters("abcdefg") is True


def has_iol(s: str) -> bool:
    for letter in "iol":
        if letter in s:
            return False

    return True


def has_two_non_overlapping_pairs(s: str) -> bool:
    pairs = {}

    for i in range(len(s) - 1):
        pair = s[i : i + 2]
        if pair[0] != pair[1]:
            continue

        # Check if the pair is already in the dictionary and if it's non-overlapping
        if pair in pairs:
            if i > pairs[pair] + 1:
                pairs[pair] = i
        else:
            pairs[pair] = i

    return len(pairs) >= 2


def test_has_two_non_overlapping_pairs():
    assert has_two_non_overlapping_pairs("aabb") is True
    assert has_two_non_overlapping_pairs("aaa") is False
    assert has_two_non_overlapping_pairs("abbceffg") is True
    assert has_two_non_overlapping_pairs("abbcegjk") is False


def next_letter(character: str) -> tuple[str, int]:
    carry = 0

    if character == "z":
        next_letter_ascii = ord("a")
        carry = 1
    else:
        next_letter_ascii = ord(character) + 1

    return chr(next_letter_ascii), carry


def next_password(letters: str) -> str:
    letters_list = []

    for letter in letters[::-1]:
        new_letter, carry = next_letter(letter)
        letters_list.append(new_letter)
        if carry == 0:
            break
    return letters[: len(letters) - len(letters_list)] + "".join(letters_list[::-1])


def test_next_password():
    assert next_password("abcd") == "abce"
    assert next_password("xyz") == "xza"
    assert next_password("az") == "ba"
    assert next_password("zz") == "aa"
    assert next_password("aaazz") == "aabaa"


def next_valid_password(current_pass: str) -> str:
    candidate = next_password(current_pass)
    while True:
        candidate = next_password(candidate)

        if all(
            f(candidate)
            for f in (has_iol, has_increasing_straight_letters, has_two_non_overlapping_pairs)
        ):
            return candidate
    return "Not found"


def test_next_valid_password() -> None:
    assert next_valid_password("abcdefgh") == "abcdffaa"
    assert next_valid_password("ghijklmn") == "ghjaabcc"


if __name__ == "__main__":
    print(next_valid_password("hxbxxyzz"))
