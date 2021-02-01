from mathics_scanner.characters import replace_wl_with_plain_text as wl_to_unicode
from mathics_scanner.characters import replace_unicode_with_wl as unicode_to_wl
from util import yaml_data, json_data


def test_roundtrip():
    wl_to_unicode_dict = json_data["wl-to-unicode-dict"]
    unicode_to_wl_dict = json_data["unicode-to-wl-dict"]

    for k, v in yaml_data.items():
        if v["has-unicode-inverse"]:
            wl = v["wl-unicode"]
            assert (
                unicode_to_wl(wl_to_unicode(wl)) == wl
            ), f"key {k} unicode {uni}, {wl_to_unicode(uni)}"

            uni = v["unicode-equivalent"]
            if uni != wl:
                assert (
                    uni == wl_to_unicode_dict[wl]
                ), f"key {k} unicode {uni}, {wl_to_unicode[uni]}"

                assert (
                    uni in unicode_to_wl_dict
                ), f"key {k} has a non-trivial unicode inverse but isn't included in unicode-to-wl-dict"

                assert (
                    unicode_to_wl_dict[uni] == wl
                ), f"key {k} unicode {uni}, {wl_to_unicode[uni]}"

