import string
from random import choices

__all__ = ["gen_password"]


def gen_password(
    length: int = 12,
    lower: bool = True,
    upper: bool = True,
    digit: bool = True,
    special: bool = True,
) -> str:
    if length < 1 or not (lower or upper or digit or special):
        return ""

    mix = ""
    if lower:
        mix += string.ascii_lowercase
    if upper:
        mix += string.ascii_uppercase
    if digit:
        mix += string.digits
    if special:
        mix += """!"#$%&'()*+,-.:;<=>?@[]^_`{|}~"""
    return "".join(choices(mix, k=length))
