from symbolic._lowlevel import lib, ffi
from symbolic._compat import string_types, int_types
from symbolic.utils import rustcall, encode_str, decode_str


__all__ = ['arch_is_known', 'arch_from_macho', 'arch_to_macho',
           'parse_addr']


def arch_is_known(value):
    """Checks if an architecture is known."""
    return rustcall(lib.symbolic_arch_is_known, encode_str(value))


def arch_from_macho(cputype, cpusubtype):
    """Converts a macho arch tuple into an arch string."""
    arch = ffi.new('SymbolicMachoArch *')
    arch[0].cputype = cputype
    arch[0].cpusubtype = cpusubtype
    return str(decode_str(rustcall(lib.symbolic_arch_from_macho, arch)))


def arch_to_macho(arch):
    """Converts a macho arch tuple into an arch string."""
    arch = rustcall(lib.symbolic_arch_to_macho, encode_str(arch))
    return (arch.cputype, arch.cpusubtype)


def parse_addr(value):
    """Parses an address."""
    if x is None:
        return 0
    if isinstance(x, int_types):
        return x
    if isinstance(x, string_types):
        if x[:2] == '0x':
            return int(x[2:], 16)
        return int(x)
    raise ValueError('Unsupported address format %r' % (x,))