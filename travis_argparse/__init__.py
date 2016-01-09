# -*- coding: utf-8 -*-
#
# This file is part of easydms.
# Copyright (c) 2015 Peter Kessen
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject
# to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import sys
import argparse


parser = argparse.ArgumentParser(prog="travis_argparse")
parser.set_defaults(cmd=None)


class SimpleCmdException(Exception):
    pass


class ExtendedSub1CmdException(Exception):
    pass


# ===========================================================================
# Top level arguments
# ===========================================================================
class VersionAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(VersionAction, self).__init__(
            option_strings, dest, help="print version and exit",
            nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('{0} {1}'.format(parser.prog, "0.0.0"))
        sys.exit()


parser.add_argument('--version', action=VersionAction)


subparsers = parser.add_subparsers()

# ===========================================================================
# simple
# ===========================================================================
simpleParser = subparsers.add_parser('simple')


def simpleCmd(args):
    raise SimpleCmdException()


simpleParser.set_defaults(cmd=simpleCmd)


# ===========================================================================
# extended
# ===========================================================================
extendedParser = subparsers.add_parser('extended')


def print_usage_extended(args):
    sys.exit(extendedParser.format_usage())


extendedParser.set_defaults(rawCmd=print_usage_extended)

extendedSubparsers = extendedParser.add_subparsers()

# =======================================================================
# extended sub1
# =======================================================================
extendedDumpParser = extendedSubparsers.add_parser('sub1')


def extendedSub1Cmd(args=None):
    raise ExtendedSub1CmdException()
extendedDumpParser.set_defaults(cmd=extendedSub1Cmd)


def main():
    args = parser.parse_args(sys.argv[1:])
    if args.cmd is not None:
        args.cmd(args)
