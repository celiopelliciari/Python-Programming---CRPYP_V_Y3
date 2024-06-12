#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys


# // Command line parsing //
parser = argparse.ArgumentParser(description="Description here")
parser.add_argument(
    "-a", "--arg_a", help="Argument A", nargs=1, 
    type=ascii, default="", required=False
)
parser.add_argument(
    "-b", "--arg_b", help="Argument B", nargs=2, 
    type=float, default=0, required=False
)
parser.add_argument(
    "-c", "--arg_c", help="Argument C", 
    action="store_true", required=False
)
parser.add_argument(
    "-d", "--arg_d", help="Argument D", nargs="*", 
    type=int, default=[], required=False
)

args = parser.parse_args()  # Class: argparse.Namespace
print("-" * 40)
print("help message")
print("-" * 40)
print(parser.print_help())
print("-" * 40)
print(type(args))
print("-" * 40)
print("args.arg_a: ", args.arg_a)
print("args.arg_b: ", args.arg_b)
print("args.arg_c: ", args.arg_c)
print("args.arg_d: ", args.arg_d)

args = vars(args)  # Convert from 'argparse.Namespace' to dict
print("-" * 40)
print(type(args))
print("-" * 40)
print("args['arg_a']: ", args["arg_a"])
print("args['arg_b']: ", args["arg_b"])
print("args['arg_c']: ", args["arg_c"])
print("args['arg_d']: ", args["arg_d"])
print()
